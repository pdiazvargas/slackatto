import logging

from minik.core import Minik
from api import dynamo

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Minik()


@app.post("/events")
def post_event():
    payload = app.request.json_body
    request_type = payload.get("type")

    logger.info(f"request type: {request_type}")
    logger.info(payload)

    if request_type == "event_callback":
        request_type = payload.get("event", {}).get("type")

    return event_handlers_by_type.get(request_type, no_op)(payload)


def no_op(payload):
    return {"error": "Invalid request type received."}


def return_challenge(payload):
    return payload["challenge"]


def user_change_handler(payload):
    user = payload["event"]["user"]

    if user.get("deleted", False):
        dynamo.remove_user(user)
    else:
        dynamo.add_or_update_user(user)


event_handlers_by_type = {
    "url_verification": return_challenge,
    "user_change": user_change_handler,
}
