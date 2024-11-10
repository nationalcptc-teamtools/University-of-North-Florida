import boto3
from botocore.exceptions import ProfileNotFound, ClientError


def resolve_aws_account(
        profile,
        access_key=None,
        secret_key=None,
        session_token=None,
        region=None
):
    if access_key or secret_key or session_token:
        account = AWSAccount(access_key, secret_key, session_token, region)
    else:
        account = get_account_from_profile(profile)
        if region:
            account.region = region

    if not account.access_key:
        raise AccountError("No access key, please specify one")

    if not account.secret_key:
        raise AccountError("No secret key, please specify one")

    return account


def get_account_from_profile(profile):
    try:
        session = boto3.Session(profile_name=profile)
        creds = session.get_credentials()

        access_key = creds.access_key
        secret_key = creds.secret_key
        session_token = creds.token
        region = session.region_name
        return AWSAccount(access_key, secret_key, session_token, region)

    except ProfileNotFound:
        raise AccountError("Profile '{}' cannot be found".format(profile))


class AccountError(Exception):
    pass


class AWSAccount:

    def __init__(self, access_key, secret_key, session_token, region):
        self.access_key = access_key
        self.secret_key = secret_key
        self.session_token = session_token
        self.region = region
        self.session = self._create_session()
        self.name = self._get_name()

    def _create_session(self):
        session = boto3.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            aws_session_token=self.session_token,
            region_name=self.region
        )
        return session

    def _get_name(self):
        try:
            response = self.session.client("sts").get_caller_identity()
            arn = response["Arn"]
            return arn.split("/")[-1]
        except ClientError:
            return "Unknown"
