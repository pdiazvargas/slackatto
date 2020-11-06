import json
import boto3
import time

# _users_table = (
#     boto3.Session(profile_name="smart", region_name="us-east-2")
#     .resource("dynamodb")
#     .Table("slackatto-users")
# )
_users_table = boto3.resource("dynamodb").Table("slackatto-users")


def add_or_update_user(user):
    return _users_table.update_item(
        Key={"id": user["id"]},
        UpdateExpression="SET user_obj = :user_obj, username = :username",
        ExpressionAttributeValues={
            ":user_obj": json.dumps(user),
            ":username": user["name"],
        },
    )


def remove_user(user):
    return _users_table.delete_item(Key={"id": user["id"]})

