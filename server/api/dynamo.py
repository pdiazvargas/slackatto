import json
import boto3
import time

# _users_table = (
#     boto3.Session(profile_name="smart", region_name="us-east-2")
#     .resource("dynamodb")
#     .Table("slackatto-users")
# )
_users_table = boto3.resource("dynamodb").Table("slackatto-users")


def get_users():
    """
    Read all the users from the dynamo database.
    """
    response = _users_table.scan(Select="ALL_ATTRIBUTES")
    return [json.loads(record["user_obj"]) for record in response.get("Items", [])]


def add_or_update_user(user):
    """
    Given the information of a user as a json object, add the user to
    the dynamo database. The identifier of ther user will be it's unique id.
    """
    return _users_table.update_item(
        Key={"id": user["id"]},
        UpdateExpression="SET user_obj = :user_obj, username = :username",
        ExpressionAttributeValues={
            ":user_obj": json.dumps(user),
            ":username": user["name"],
        },
    )


def remove_user(user):
    """
    Delete a user from the dynamo database.
    """
    return _users_table.delete_item(Key={"id": user["id"]})

