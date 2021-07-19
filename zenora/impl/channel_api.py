import typing

from zenora import Channel, Message, User
from zenora.api.channel_api import ChannelAPI
from zenora.request import Request
from zenora.routes import (
    BASE_URL,
    GET_CHANNEL, CHANNEL_MESSAGE, CHANNEL_MESSAGES,
)

__all__: typing.Final[typing.List[str]] = ["ChannelAPIImpl"]


class ChannelAPIImpl(ChannelAPI):
    _token: str

    def __init__(self, app):
        self._token = app._token
        self._app = app

    def get_channel(self, channel_id):
        url = BASE_URL + GET_CHANNEL.format(channel_id)
        request = Request(self._token, url, "GET")
        payload = request.execute()
        return Channel(**payload)

    @staticmethod
    def parse_message(message_payload):
        message_payload["author"] = User(**message_payload["author"])
        return Message(**message_payload)

    def get_message(self, channel_id, message_id):
        url = BASE_URL + CHANNEL_MESSAGE.format(channel_id, message_id)
        request = Request(self._token, url, "GET")
        payload = request.execute()
        return self.parse_message(payload)

    def get_messages(self, channel_id):
        url = BASE_URL + CHANNEL_MESSAGES.format(channel_id)
        request = Request(self._token, url, "GET")
        payload = request.execute()
        messages = list()
        for message_payload in payload:
            messages.append(self.parse_message(message_payload))
        return messages

    def delete_message(self, channel_id, message_id):
        url = BASE_URL + CHANNEL_MESSAGE.format(channel_id, message_id)
        request = Request(self._token, url, "DELETE")
        request.execute()

    def send_message(self, channel_id, content):
        url = BASE_URL + CHANNEL_MESSAGES.format(channel_id)
        request = Request(self._token, url, "POST", json_data={"content": content})
        request.execute()

    def edit_message(self, channel_id, message_id, content):
        url = BASE_URL + CHANNEL_MESSAGES.format(channel_id)
        request = Request(self._token, url, "PATCH", json_data={"content": content})
        request.execute()
