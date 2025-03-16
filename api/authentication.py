"""Authentication module."""

from requests import request

from secret_reader import AUTH_KEY


class Authentication:
    """Authentication class."""

    token_cache: dict[str, str] = {}
    # Дата и время истечения действия токена в миллисекундах, в формате unix timestamp.
    # ToDO: add token cache with time to live.

    @staticmethod
    def get_token_request() -> str | None:
        """Get auth token."""
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

        payload = {"scope": "GIGACHAT_API_PERS"}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": "d921e213-ffb5-4e3c-bbe3-0a00a4c84ec7",
            "Authorization": f"Basic {AUTH_KEY}",
        }

        response = request(method="POST", url=url, headers=headers, data=payload, verify=False)

        return response.json()["access_token"]
