"""GigaChat API client."""
from requests import Response

from api.api_client import ApiClient


class GigaChatApi(ApiClient):
    """GigaChat Api.

    Notes:
        Documentation: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/gigachat-api
    """

    def __init__(self, version: int = 1):
        """Initialize the GigaChat API client.

        Args:
            version: API version.
        """
        super().__init__()

        self.url = f"https://gigachat.devices.sberbank.ru/api/v{version}"

    def get_model_list(self) -> Response:
        """Get a list of AI models."""

        return self.request(method="GET", url=f"{self.url}/models")
