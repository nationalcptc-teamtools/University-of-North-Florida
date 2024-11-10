import os
import re
from concurrent.futures import ThreadPoolExecutor, wait
import botocore.exceptions
from boto3 import client
from botocore import UNSIGNED
from botocore.client import Config, BaseClient
from humanize import naturalsize
import args as argsmod
import awsaccount
from format import *


class File:

    def __init__(self, _client: BaseClient, bucket: str, file_info: dict) -> None:
        """
        Establishes key, bytes_size, size, last_modified, type, name, and is_readable on initialization.

        :param _client: S3 Client
        :param bucket: Name of target bucket
        :param file_info: Data of file
        """
        self.__client: BaseClient = _client
        self.__bucket: str = bucket
        self.__file_info: dict = file_info

        self.key: str = file_info['Key']
        self.bytes_size: int = file_info['Size']
        self.size: str = naturalsize(self.bytes_size) if self.bytes_size > 0 else ''
        self.last_modified: str = file_info['LastModified'].strftime("%b %d %Y")
        self.type: str = self.get_type()
        self.name: str = self.get_name()
        self.is_readable: str = ' ✓' if self.is_file_readable() else ''
        self.directory: str = self.__bucket + '/' + '/'.join(self.key.split('/')[:-1])

    def get_type(self) -> str:
        """
        Gets the type/extension of the file.

        :return: File type
        """
        file_name_parts = self.key.split('.')
        last_part = file_name_parts[-1]

        if len(file_name_parts) > 1:
            return last_part.lower()
        return 'dir' if last_part.endswith('/') else 'file'

    def get_name(self) -> str:
        """
        Gets the formatted version of a file including colorization and subdirectories.
        Used to print to the user when ls() is called.

        :return: Formatted file name
        """
        split_file = self.key.split('/')
        if len(split_file) > 1:
            split_file[0] = '[cyan]{}'.format(split_file[0])
            split_file[-1] = '[bold green]{}[/bold green]'.format(split_file[-1])
            return '/'.join(split_file)
        return '[bold green]{}[/bold green]'.format(split_file[0])

    def is_file_readable(self) -> bool:
        """
        Determines if a file is readable with the current permissions.

        :return: True if file is readable, False otherwise
        """
        try:
            self.__client.head_object(Bucket=self.__bucket, Key=self.key)
            return True
        except botocore.exceptions.ClientError:
            return False

    @property
    def printable_name(self) -> str:
        """
        Gets the name of the file, ignoring all subdirectories or stylization.
        Used for evaluation.

        :return:
        """
        split_file = self.key.replace(' ', '_').split('/')
        return split_file[-1] if len(split_file) > 1 else split_file[0]


###########################################
# ------------) Exceptions (-------------#
###########################################

def error_handler(func):
    """
    Handles errors for all functions that have the decorator assigned.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except botocore.exceptions.ClientError as e:
            response_code = e.response['Error']['Code']
            if response_code == 'NoSuchWebsiteConfiguration':
                Format.print_data('No Website Configured')
            elif response_code == 'AccessDenied' or response_code == 'MethodNotAllowed':
                Format.print_error('Access Denied', border=True)
            else:
                Format.print_error('\n' + e.response['Error']['Message'])
        except KeyboardInterrupt:
            pass

    return wrapper


###########################################
# -----------) AWS Commands (-------------#
###########################################

def bucket_exists(_client: BaseClient, bucket_name: str) -> bool:
    """
    Uses head_bucket to determine if a bucket exists or not.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    :return True if bucket exists, False otherwise
    """
    try:
        _client.head_bucket(Bucket=bucket_name)
        return True
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '403':
            return True
        else:
            return False


@error_handler
def list_object_versions(_client: BaseClient, bucket_name: str) -> None:
    """
    Execute list_object_versions on a specified bucket and prints the output.
    If a non-latest version of an object is found, it will attempt to call get_object()
    to get the contents.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    """
    response = _client.list_object_versions(Bucket=bucket_name)
    old_versions = [version for version in response['Versions'] if version['IsLatest'] is False]
    Format.print_info('Found {} non-latest versions'.format(len(old_versions)))

    for file in old_versions:
        Format.print_title2('{} ({})'.format(file['Key'], file['VersionId']))

        file_extension = file['Key'].split('.')[-1].lower()
        if file_extension not in BLACKLISTED_EXTENSIONS:
            Format.print_title3('get-object')
            get_object(_client, bucket_name, file['Key'], file['VersionId'])


@error_handler
def get_object(_client: BaseClient, bucket_name: str, key: str, version_id: str) -> None:
    """
    Execute get_object on a specified object in a bucket with a specific VersionId.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    :param key: Key of target file
    :param version_id: VersionId of target file
    """
    response = _client.get_object(Bucket=bucket_name, Key=key, VersionId=version_id)
    try:
        file_contents = response['Body'].read().decode('utf-8')
        if file_contents:
            Format.print_data(file_contents)
    except UnicodeDecodeError:
        pass


@error_handler
def get_bucket_acl(_client: BaseClient, bucket_name: str) -> None:
    """
    Execute get_bucket_acl on a specified bucket and prints the output.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    """
    response = _client.get_bucket_acl(Bucket=bucket_name)
    grants = response['Grants']

    for grant in grants:
        Format.print_data(grant)


@error_handler
def get_bucket_policy(_client: BaseClient, bucket_name: str) -> None:
    """
    Execute get_bucket_policy on a specified bucket and prints the output.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    """
    response = _client.get_bucket_policy(Bucket=bucket_name)
    parsed_policy = json.loads(response['Policy'])
    statements = parsed_policy['Statement']

    for statement in statements:
        Format.print_data(statement)


@error_handler
def get_bucket_tagging(_client: BaseClient, bucket_name: str) -> None:
    """
    Execute get_bucket_tagging on a specified bucket and prints the output.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    """
    response = _client.get_bucket_tagging(Bucket=bucket_name)
    tags = response['TagSet']

    for tag in tags:
        Format.print_data(tag)


@error_handler
def get_bucket_website(_client: BaseClient, bucket_name: str) -> None:
    """
    Execute get_bucket_website on a specified bucket and prints the output.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    """
    response = _client.get_bucket_website(Bucket=bucket_name)
    Format.print_data(response)


###########################################
# -------) ls + file download (----------#
###########################################

@error_handler
def ls(_client: BaseClient, bucket_name: str) -> None:
    """
    Execute list_objects_v2 on a specified bucket and prints objects in a readable format.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    """
    response = _client.list_objects_v2(Bucket=bucket_name)
    files = response['Contents']
    pool = ThreadPoolExecutor(max_workers=10)
    threads = []
    readable_files = []

    Format.print_info(f'Found {len(files)} objects in {bucket_name}')
    Format.print_file_headers()

    for file_data in files:
        t = pool.submit(File, _client, bucket_name, file_data)
        threads.append(t)

    wait(threads, return_when='ALL_COMPLETED')

    for t in threads:
        file = t.result()
        if file.is_readable:
            readable_files.append(file)
        Format.print_file(file)

    if readable_files:
        readable_dict = get_completions(readable_files)
        download(_client, bucket_name, readable_dict)


def get_completions(files: list[File]) -> dict:
    """
    Generate a dictionary for prompt auto-completions.

    :param files: List of File objects
    :return: Dictionary to be used for prompt auto-completion
    """
    completions = {'*': ''}

    # Add directories
    for file in files:
        directory = os.path.dirname(file.key)
        while directory:
            if directory not in completions.keys():
                completions[directory + '/*'] = ''
            directory = os.path.dirname(directory)

    # Add printable names
    for file in files:
        if file.printable_name:
            completions[file.printable_name] = file

    return completions


def download(_client: BaseClient, bucket_name: str, readable_dict: dict) -> None:
    """
    Parses user's input to determine what files should be downloaded if any.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    :param readable_dict: Dictionary to be used for prompt auto-completion
    """
    readable_file_objs = [file_obj for file_obj in readable_dict.values() if file_obj]
    user_input = download_prompt(list(readable_dict.keys()))
    to_download = []

    while user_input:

        # SOLO WILDCARD: download all files
        if '*' in user_input:
            to_download = readable_file_objs
            user_input.clear()

        # WILDCARD ANYWHERE IN ARG: download all files that match supplied pattern
        elif has_wildcard(user_input):
            arguments = [argument for argument in user_input if '*' in argument]

            for argument in arguments:
                pattern = re.compile(argument.replace('*', '.*'), re.IGNORECASE)
                any_match = False

                for file in readable_file_objs:
                    if re.search(pattern, file.key):
                        any_match = True
                        to_download.append(file)

                if not any_match:
                    Format.print_error(f'No files match the pattern "{argument}"')

                user_input.remove(argument)

        # INDIVIDUAL FILE: download specific file
        for file_printable in user_input:
            try:
                file = readable_dict[file_printable]
                to_download.append(file)
            except KeyError:
                Format.print_error(f"{file_printable} not found.", border=True)
                pass

        for file in to_download:
            if not directory_exists(file.directory):
                create_directory(file.directory)

            download_file(_client, bucket_name, file)

        user_input = download_prompt(list(readable_dict.keys()))


def directory_exists(directory_name: str) -> bool:
    """
    Check if a directory exists in the current directory.

    :param directory_name: The name of the directory to check
    :return: True if the directory exists, False otherwise
    """
    current_directory = os.getcwd()
    directory_path = os.path.join(current_directory, directory_name)
    return os.path.isdir(directory_path)


def create_directory(directory_name: str) -> str | None:
    """
    Create a directory in the current directory.

    :param directory_name: The name of the directory to create
    :return: The path of the created directory, None otherwise
    """
    current_directory = os.getcwd()
    directory_path = os.path.join(current_directory, directory_name)

    try:
        os.makedirs(directory_path)
        return directory_path
    except FileExistsError:
        return
    except PermissionError:
        Format.print_error('This program does not have the permissions to write a file here.')
        exit()


def download_file(_client: BaseClient, bucket_name: str, file: File) -> None:
    """
    Downloads a file from a specified S3 Bucket and supplies a progress bar.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    :param file: File object for the file that is to be downloaded
    """
    progress_bar = get_progress_bar()
    progress_bar.start()
    download_task = progress_bar.add_task(
        '{:<25}'.format(file.printable_name[:22] + "..." if len(file.printable_name) > 25 else file.printable_name),
        total=file.bytes_size)

    def progress_bar_callback(bytes_amount):
        progress_bar.update(download_task, advance=bytes_amount)

    out_file = f'{file.directory}/{file.printable_name}'
    _client.download_file(bucket_name, file.key, output_directory(out_file), Callback=progress_bar_callback)

    with progress_bar:
        while not progress_bar.finished:
            progress_bar.update(download_task)

    progress_bar.stop()


def output_directory(file_path: str) -> str:
    """
    Check if a directory exists in the current directory.

    :param file_path: The name of the directory to check
    :return: Output file path
    """
    current_directory = os.getcwd()
    directory_path = os.path.join(current_directory, file_path)
    return directory_path


def has_wildcard(arguments: list[str]) -> bool:
    """
    Determine if a list of user's arguments have at least one wildcard argument.

    :param arguments: List of user's arguments
    :return: True if wildcard is present, False otherwise
    """
    for argument in arguments:
        if '*' in argument:
            return True
    return False


###########################################
# ----------------) Main (----------------#
###########################################


def authenticated_account() -> awsaccount.AWSAccount | None:
    """
    Attempts to resolve an AWS account.

    :return: AWSAccount object if valid account, None otherwise
    """
    try:
        account = awsaccount.resolve_aws_account(
            args.profile,
            access_key=args.access_key,
            secret_key=args.secret_key,
            session_token=args.session_token,
            region=args.region,
        )
    except (awsaccount.AccountError, AttributeError):
        return

    return account


def enum(_client: BaseClient, bucket_name: str) -> None:
    """
    Runs all enumeration functions against a specified bucket.

    :param _client: S3 client
    :param bucket_name: Name of target bucket
    """
    functions = [
        (list_object_versions, 'list-object-versions'),
        (get_bucket_acl, 'get-bucket-acl'),
        (get_bucket_policy, 'get-bucket-policy'),
        (get_bucket_tagging, 'get-bucket-tagging'),
        (get_bucket_website, 'get-bucket-website'),
        (ls, 'ls')
    ]

    if args.ls:
        functions = [(ls, 'ls')]

    for func, title in functions:
        Format.print_title1(title)
        func(_client, bucket_name)


def main() -> None:
    bucket_name = args.bucket
    unauthenticated_client = client('s3', config=Config(signature_version=UNSIGNED))

    if bucket_exists(unauthenticated_client, bucket_name):
        if not args.no_anon:
            Format.print_title('Unauthenticated')
            enum(unauthenticated_client, bucket_name)

        auth_account = authenticated_account()
        if auth_account:
            Format.print_title(auth_account.name)
            enum(auth_account.session.client('s3'), bucket_name)

    else:
        Format.print_error('S3 bucket cannot be found')


if __name__ == '__main__':
    args = argsmod.parse_args()
    Format = Format(border=args.no_border)
    main()
