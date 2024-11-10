import botocore.exceptions
from botocore.client import BaseClient
import args as argsmod
import awsaccount
from format import Format, header

all_groups = []


###########################################
# ---------------) General (--------------#
###########################################

def handle_client_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except botocore.exceptions.ClientError as e:
            response_code = e.response['Error']['Code']
            if response_code == 'AccessDenied' or response_code == 'MethodNotAllowed':
                Format.print_error(' Access Denied')
            else:
                Format.print_error('\n' + e.response['Error']['Message'])
        except KeyboardInterrupt:
            pass

    return wrapper


@handle_client_error
def get_policy(client: BaseClient, policy_arn: str):
    Format.print_title3("Get-Policy")

    resp = client.get_policy(PolicyArn=policy_arn)
    Format.print_data(resp["Policy"])
    get_policy_version(client, policy_arn, resp["Policy"]["DefaultVersionId"])


@handle_client_error
def get_policy_version(client: BaseClient, policy_arn: str, version_id: str):
    Format.print_title3("Get-Policy-Version")

    resp = client.get_policy_version(PolicyArn=policy_arn, VersionId=version_id)
    policies = resp["PolicyVersion"]["Document"]["Statement"]

    for policy in policies:
        Format.print_data(policy)


# Attached
@handle_client_error
def get_attached_policies(client: BaseClient, policy_type: str, name: str):
    client = client

    if policy_type == "user":
        resp = client.list_attached_user_policies(UserName=name)
    elif policy_type == "group":
        resp = client.list_attached_group_policies(GroupName=name)
    else:
        resp = client.list_attached_role_policies(RoleName=name)

    policies = resp.get("AttachedPolicies", [])
    num_policies = len(policies)
    Format.print_info(f"Found {num_policies} Attached {'Policy' if num_policies == 1 else 'Policies'}")

    for i, policy in enumerate(policies, 1):
        Format.print_title2(f"[{i}] {policy['PolicyName']} ({policy['PolicyArn']})")
        get_policy(client, policy["PolicyArn"])


# Inline
@handle_client_error
def get_inline_policies(client: BaseClient, policy_type: str, name: str):
    if policy_type == "user":
        resp = client.list_user_policies(UserName=name)
        policy_getter = get_user_policy
    elif policy_type == "group":
        resp = client.list_group_policies(GroupName=name)
        policy_getter = get_group_policy
    else:
        resp = client.list_role_policies(RoleName=name)
        policy_getter = get_role_policy

    policies = resp.get("PolicyNames", [])
    num_policies = len(policies)
    Format.print_info(f"Found {num_policies} Inline {'Policy' if num_policies == 1 else 'Policies'}")

    for i, policy_name in enumerate(policies, 1):
        Format.print_title2(f"[{i}] {policy_name}")
        policy_getter(client, name, policy_name)


###########################################
# ---------------) Users (----------------#
###########################################

def enum_user_policies(client: BaseClient, username: str):
    Format.print_title("User")

    Format.print_title1("Attached")
    get_attached_policies(client, "user", username)

    Format.print_title1("Inline")
    get_inline_policies(client, "user", username)


@handle_client_error
def get_user_policy(client: BaseClient, username: str, policy_name: str):
    Format.print_title3("Get-User-Policy")

    resp = client.get_user_policy(UserName=username, PolicyName=policy_name)
    policies = resp["PolicyDocument"]["Statement"]

    for policy in policies:
        Format.print_data(policy)


###########################################
# ---------------) Groups (---------------#
###########################################

@handle_client_error
def enum_groups_for_user(client: BaseClient, username: str):
    Format.print_title(f'"{username}" Group Memberships')

    resp = client.list_groups_for_user(UserName=username)
    groups = resp["Groups"]

    if groups:
        for group in groups:
            group_name = group["GroupName"]
            all_groups.append(group_name)
            Format.print_title1(f'{group_name} ({group["Arn"]})')
            get_attached_policies(client, "group", group_name)

            get_inline_policies(client, "group", group_name)


@handle_client_error
def enum_group_policies(client: BaseClient):
    Format.print_title("Other Groups")

    resp = client.list_groups()
    groups = resp["Groups"]

    for group in groups:
        group_name = group["GroupName"]
        if group_name not in all_groups:
            Format.print_title1(f'{group_name} ({group["Arn"]})')
            get_attached_policies(client, "group", group_name)

            get_inline_policies(client, "group", group_name)


@handle_client_error
def get_group_policy(client: BaseClient, group_name: str, policy_name: str):
    Format.print_title3("Get-Group-Policy")

    resp = client.get_group_policy(GroupName=group_name, PolicyName=policy_name)
    policies = resp["PolicyDocument"]["Statement"]

    for policy in policies:
        Format.print_data(policy)


###########################################
# ---------------) Roles (----------------#
###########################################

@handle_client_error
def enum_role_policies(client: BaseClient):
    Format.print_title("Roles")

    resp = client.list_roles()
    roles = resp["Roles"]

    for role in roles:
        role_name = role["RoleName"]
        if "AWSServiceRoleFor" not in role_name:
            Format.print_title1(role_name)
            Format.print_title3("Get-Role")
            Format.print_data(role)

            get_attached_policies(client, "role", role_name)
            get_inline_policies(client, "role", role_name)


@handle_client_error
def get_role_policy(client: BaseClient, role_name: str, policy_name: str):
    Format.print_title3("Get-Role-Policy")

    resp = client.get_role_policy(RoleName=role_name, PolicyName=policy_name)
    policies = resp["PolicyDocument"]["Statement"]

    for policy in policies:
        Format.print_data(policy)


###########################################
# ----------------) Main (----------------#
###########################################

def enum(account: awsaccount.AWSAccount):
    client = account.session.client("iam")
    username = account.name
    enum_user_policies(client, username)
    enum_groups_for_user(client, username)
    enum_group_policies(client)
    enum_role_policies(client)


def main():
    try:
        account = awsaccount.resolve_aws_account(
            args.profile,
            access_key=args.access_key,
            secret_key=args.secret_key,
            session_token=args.session_token,
            region=args.region,
        )
    except awsaccount.AccountError as e:
        Format.print_error(f"Error: {e}")
        return

    enum(account)


if __name__ == "__main__":
    header()
    args = argsmod.parse_args()
    Format = Format(border=args.no_border)
    main()
