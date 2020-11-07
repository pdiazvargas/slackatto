import logging

from minik.core import Minik
from api import dynamo

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Minik()


@app.post("/events")
def slack_event_handler():
    """
    Event handler responsible for taking care of the requests sent by slack.
    Different type of events include verification and user changes. User changes
    are persisted in a dynamo database.
    """
    payload = app.request.json_body
    request_type = payload.get("type")

    logger.info(f"request type: {request_type}")
    logger.info(payload)

    if request_type == "event_callback":
        request_type = payload.get("event", {}).get("type")

    return event_handlers_by_type.get(request_type, no_op)(payload)


@app.get("/users")
def get_users():
    """
    Endpoint used to retrieve the set of users in the dynamo database.
    """
    return dynamo.get_users()


def no_op(payload):
    """
    The base case in which the given request type is not valid.
    """
    return {"error": "Invalid request type received."}


def return_challenge(payload):
    """
    If the type of event is the slack challenge, return the value sent
    by their API. This response will complete the validation.
    """
    return payload["challenge"]


def user_change_handler(payload):
    """
    This handler will take care of managing user events. A user event
    can be defined a change in the profile of a given user, an addition
    of the user to the slack workspace or the removal/deactivate of a
    user from the workspace.
    """
    user = payload["event"]["user"]

    if user.get("deleted", False):
        dynamo.remove_user(user)
    else:
        dynamo.add_or_update_user(user)


# Keep track of the type of events supported and their respective handler.
# This approach allows us to update the event type, while keeping the same
# implementation. I.e. say that slack no longer sends a `url_verification`,
# but a `url_validation`. In this case, we would only need to update this
# mapping.
event_handlers_by_type = {
    "url_verification": return_challenge,
    "user_change": user_change_handler,
}
