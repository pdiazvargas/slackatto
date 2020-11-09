import json
from unittest.mock import MagicMock

from minik.status_codes import codes
from minik.utils import create_api_event
from api.lambda_handler import app

context = MagicMock()


def test_url_verification_request():
    """
    With a valid url verification event type, return
    the challenge provided.
    """
    event = create_api_event(
        "/events", body={"type": "url_verification", "challenge": "findme"}
    )

    response = app(event, context)

    assert response["statusCode"] == codes.ok
    assert response["body"] == '"findme"'


def test_url_verification_request_without_challenge():
    """
    If a url_verification request does not have a
    valid challenge, a bad request is returned
    """
    event = create_api_event("/events", body={"type": "url_verification"})

    response = app(event, context)

    assert response["statusCode"] == codes.bad_request


def test_invalid_event_type():

    event = create_api_event("/events", body={"type": "not_there"})

    response = app(event, context)

    assert response["statusCode"] == codes.bad_request


class TestUserEventAPI:
    """
    Validate that when slack sends a user_change event, the
    api handler can keep track of users in the workspace.
    """

    def test_user_change_happy_path(self, mocker):

        dynamo_mock = mocker.patch("api.lambda_handler.dynamo")
        user = {"id": "2311", "name": "Andrew"}
        event = self._get_request_for_user(user)

        response = app(event, context)

        assert response["statusCode"] == codes.ok
        dynamo_mock.add_or_update_user.assert_called_with(user)

    def test_user_change_invalid_user(self, mocker):
        dynamo_mock = mocker.patch("api.lambda_handler.dynamo")
        event = self._get_request_for_user(None)

        response = app(event, context)

        assert response["statusCode"] == codes.bad_request
        dynamo_mock.add_or_update_user.assert_not_called()

    def test_user_change_invalid_user_id(self, mocker):
        """
        The user id is a required field! This is how we keep track of the
        users in dynamo. If a change request does not have a user with a
        valid id, then the request is NOT valid!
        """
        dynamo_mock = mocker.patch("api.lambda_handler.dynamo")
        event = self._get_request_for_user({"id": None})

        response = app(event, context)

        assert response["statusCode"] == codes.bad_request
        dynamo_mock.add_or_update_user.assert_not_called()

    def test_deactivated_user(self, mocker):
        dynamo_mock = mocker.patch("api.lambda_handler.dynamo")
        user = {"id": "2311", "name": "Andrew", "deleted": True}
        event = self._get_request_for_user(user)

        response = app(event, context)

        assert response["statusCode"] == codes.ok
        dynamo_mock.remove_user.assert_called_with(user)

    def test_deactivated_user_invalid(self, mocker):
        """
        Received API request for a user change on a deactivated user,
        but the payload has no user.
        """

        dynamo_mock = mocker.patch("api.lambda_handler.dynamo")
        event = self._get_request_for_user(None)

        response = app(event, context)

        assert response["statusCode"] == codes.bad_request
        dynamo_mock.remove_user.assert_not_called()

    def _get_request_for_user(self, user):
        return create_api_event(
            "/events",
            body={
                "type": "event_callback",
                "event": {"type": "user_change", "user": user},
            },
        )
