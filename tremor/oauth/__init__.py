import random
from typing import Any, Dict, List, Optional, cast

import httpx
from httpx_oauth.oauth2 import BaseOAuth2, GetAccessTokenError, OAuth2Token

AUTHORIZE_ENDPOINT = "https://id.twitch.tv/oauth2/authorize"
ACCESS_TOKEN_ENDPOINT = "https://id.twitch.tv/oauth2/token"


class TwitchOauth2(BaseOAuth2[Dict[str, Any]]):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(
            client_id, client_secret, AUTHORIZE_ENDPOINT, AUTHORIZE_ENDPOINT
        )
        self.state_token = self._generate_state_token()

    async def get_authorization_url(
        self, redirect_uri: str, scope: Optional[List[str]] = None, **kwargs
    ) -> str:
        return await super().get_authorization_url(
            redirect_uri, state=None, scope=scope
        )

    async def get_client_access_token(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.authorize_endpoint,
                data={
                    "grant_type": "client_credentials",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                },
                headers=self.request_headers,
            )

            data = cast(Dict[str, Any], response.json())

            if response.status_code == 400:
                raise GetAccessTokenError(data)

            return OAuth2Token(data)

    def _generate_state_token(self):
        # Quick way to generate the token. Taken from
        # https://stackoverflow.com/a/2782859
        return "%030x" % random.getrandbits(120)
