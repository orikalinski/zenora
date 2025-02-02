# Copyright (c) 2021 K.M Ahnaf Zamil

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from zenora.api.channel_api import ChannelAPI
from zenora.api.oauthapi import OauthAPI
from zenora.api.userapi import UserAPI
from zenora.exceptions import AuthenticationError, BadTokenError

import typing


__all__: typing.Final[typing.List[str]] = ["APIClient"]

from zenora.impl.channel_api import ChannelAPIImpl
from zenora.impl.oauthapi import OauthAPIImpl
from zenora.impl.userapi import UserAPIImpl


class APIClient:
    """The API client for accessing the Discord REST API

    Args:
        token (str): Token for the bot/user
        validate_token (bool, optional): Whether the token should be validated during API instantiation. Defaults to True.
        client_secret ([type], optional): Client secret for bot, especially if you are using Oauth. Defaults to None.
        bearer (bool, optional): Enable bearer tokens, necessary when you are using Oauth. Defaults to False.
    """

    def __init__(
        self,
        token: str,
        *,
        validate_token: bool = True,
        client_secret=None,
        bearer=False,
    ):
        self._token_prefix = "Bot" if not bearer else "Bearer"
        self._token = f"{self._token_prefix} {token}"
        self._client_secret = client_secret
        self._user_client = UserAPIImpl(self)
        self._channel_client = ChannelAPIImpl(self)
        self._oauth_client = None
        self.user = None

        if client_secret:
            self._oauth_client = OauthAPIImpl(self, client_secret)

        if validate_token:
            self.user = self._validate_token()

    def _validate_token(self):
        try:
            return self.users.get_current_user()
        except AuthenticationError:
            raise BadTokenError("Invalid token has been passed")

    def set_token(self, token: str):
        """Sets the token for the API client instance"""
        self._token = f"{self._token_prefix} {token}"
        self._validate_token()

    @property
    def users(self) -> UserAPI:
        """Returns an instance of the UserAPI class"""
        return self._user_client

    @property
    def channels(self) -> ChannelAPI:
        """Returns an instance of the UserAPI class"""
        return self._channel_client

    @property
    def oauth(self) -> typing.Optional[OauthAPI]:
        """Returns an instance of the OauthAPI class"""
        return self._oauth_client
