import typing

from zenora.api.channel_api import ChannelAPI
from zenora.models.button import Button
from zenora.models.channel import Channel
from zenora.models.guild import Guild
from zenora.models.menu import Menu
from zenora.models.message import Message
from zenora.models.user import User
from zenora.request import Request
from zenora.routes import (
    BASE_URL,
    GET_CHANNEL, CHANNEL_MESSAGE, CHANNEL_MESSAGES, GET_GUILD, GET_GUILD_PREVIEW, GUILD_ICON,
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

    def get_guild(self, guild_id):
        url = BASE_URL + GET_GUILD.format(guild_id)
        request = Request(self._token, url, "GET")
        payload = request.execute()
        return Guild(**payload)

    def get_guild_preview(self, guild_id):
        url = BASE_URL + GET_GUILD_PREVIEW.format(guild_id)
        request = Request(self._token, url, "GET")
        payload = request.execute()
        return Guild(**payload)

    @staticmethod
    def get_guild_icon_url(guild_id, icon_hash):
        return GUILD_ICON.format(guild_id, icon_hash)

    def parse_message(self, message_payload):
        message_payload["author"] = User(**message_payload["author"])
        referenced_message = message_payload.get("referenced_message")
        if referenced_message:
            message_payload["referenced_message"] = self.parse_message(referenced_message)
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

    def send_message(self, channel_id, content, menu=None):
        url = BASE_URL + CHANNEL_MESSAGES.format(channel_id)
        json_data = {"content": content}
        if menu:
            json_data["components"] = menu.to_components()
        request = Request(self._token, url, "POST", json_data=json_data)
        request.execute()

    def edit_message(self, channel_id, message_id, content, menu=None):
        url = BASE_URL + CHANNEL_MESSAGES.format(channel_id)
        json_data = {"content": content}
        if menu:
            json_data["components"] = menu.to_components()
        request = Request(self._token, url, "PATCH", json_data=json_data)
        request.execute()
