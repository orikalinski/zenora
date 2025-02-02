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

CDN_URL = "https://cdn.discordapp.com"
BASE_URL = "https://discord.com/api/v9"

# CDN Endpoints
USER_AVATAR = "/avatars"
ICONS = "/icons"
GUILD_ICON = CDN_URL + ICONS + "/{}" + "/{}.png"

# Oauth
OAUTH_TOKEN_URL = "/oauth2/token"

# Users
GET_CURRENT_USER = "/users/@me"
GET_USER = "/users/{}"
GET_USER_CONNECTIONS = GET_CURRENT_USER + "/connections"
CHANNELS = "/channels"
DM_URL = GET_CURRENT_USER + CHANNELS
GET_CHANNEL = CHANNELS + "/{}"
CHANNEL_MESSAGE = GET_CHANNEL + "/messages" + "/{}"
CHANNEL_MESSAGES = GET_CHANNEL + "/messages"
GUILDS = "/guilds"
GET_GUILD = GUILDS + "/{}"
GET_GUILD_PREVIEW = GUILDS + "/{}" + "/preview"
