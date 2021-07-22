import typing
from abc import ABC, abstractmethod

from zenora.models.guild import Guild
from zenora.models.menu import Menu
from zenora.models.message import Message
from zenora.models.snowflake import Snowflake
from zenora.models.channel import Channel

__all__: typing.Final[typing.List[str]] = ["ChannelAPI"]


class ChannelAPI(ABC):
    """A client for using all the channel related API functionality"""

    @abstractmethod
    def get_channel(self, channel_id: typing.Union[str, Snowflake]) -> Channel:
        """Returns a channel with the corresponding ID

        Args:
            channel_id (typing.Union[str, Snowflake]): Snowflake ID of the channel

        Returns:
            Channel: An object representing a channel on Discord
        """

    @abstractmethod
    def get_guild(self, guild_id: typing.Union[str, Snowflake]) -> Guild:
        """Returns a guild with the corresponding ID

        Args:
            guild_id (typing.Union[str, Snowflake]): Snowflake ID of the channel

        Returns:
            Channel: An object representing a guild on Discord
        """

    @abstractmethod
    def get_guild_preview(self, guild_id: typing.Union[str, Snowflake]) -> Guild:
        """Returns a guild with the corresponding ID

        Args:
            guild_id (typing.Union[str, Snowflake]): Snowflake ID of the channel

        Returns:
            Guild: An object representing a guild on Discord
        """

    @staticmethod
    @abstractmethod
    def get_guild_icon_url(guild_id: typing.Union[str, Snowflake], icon_hash: str) -> str:
        """Returns a guild with the corresponding ID

        Args:
            guild_id (typing.Union[str, Snowflake]): Snowflake ID of the channel
            icon_hash (str): the hash of the guild's icon

        Returns:
            str: the file path of an icon of a guild on Discord
        """

    @abstractmethod
    def get_message(self, channel_id: typing.Union[str, Snowflake],
                    message_id: typing.Union[str, Snowflake]) -> Message:
        """Returns a channel with the corresponding ID

        Args:
            channel_id (typing.Union[str, Snowflake]): Snowflake ID of the channel
            message_id (typing.Union[str, Snowflake]): Snowflake ID of the channel

        Returns:
            Message: An object representing a channel's message on Discord
        """

    @abstractmethod
    def get_messages(self, channel_id: typing.Union[str, Snowflake]):
        """"""

    @abstractmethod
    def delete_message(self, channel_id: typing.Union[str, Snowflake],
                       message_id: typing.Union[str, Snowflake]):
        """Returns a channel with the corresponding ID

        Args:
            channel_id (typing.Union[str, Snowflake]): Snowflake ID of the channel
            message_id (typing.Union[str, Snowflake]): Snowflake ID of the channel

        Returns:
        """

    @abstractmethod
    def edit_message(self, channel_id: typing.Union[str, Snowflake],
                     message_id: typing.Union[str, Snowflake], content: str):
        """Returns a channel with the corresponding ID

        Args:
            channel_id (typing.Union[str, Snowflake]): Snowflake ID of the channel
            message_id (typing.Union[str, Snowflake]): Snowflake ID of the channel
            content (str): Snowflake ID of the channel

        Returns:
        """

    @abstractmethod
    def send_message(self, channel_id: typing.Union[str, Snowflake], content: str, menu: typing.Optional[Menu]):
        """Returns a channel with the corresponding ID

        Args:
            channel_id (typing.Union[str, Snowflake]): Snowflake ID of the channel
            content (str): Snowflake ID of the channel
            menu: typing.Optional[Menu]

        Returns:
        """