"""GigaChat API client."""
from pathlib import Path

from requests import Response

from api.api_client import ApiClient
from dto.post_embeddings_request_dto import PostEmbeddingsRequestDto
from dto.post_token_count_request_dto import PostTokenCountRequestDto
from enums.supported_file_formats import SupportedFileFormats, type_of_file
from utility.config import Config


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
        """Get a list of AI models.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/get-models
        """

        return self.request(method="GET", url=f"{self.url}/models")

    def post_tokens_count(self, json: PostTokenCountRequestDto) -> Response:
        """Calculate the number of tokens in the request.

        Args:
            json: Request body.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/post-tokens-count
        """

        return self.request(method="POST", url=f"{self.url}/tokens/count", json=json.model_dump())

    def post_create_embedding(self, json: PostEmbeddingsRequestDto) -> Response:
        """Create embedding.

        Args:
            json: Request body.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/post-embeddings
        """

        return self.request(method="POST", url=f"{self.url}/embeddings", json=json.model_dump())

    def post_upload_file(self, filename: str, file_format: SupportedFileFormats, purpose: str = "general") -> Response:
        """Upload a file.

        Args:
            filename: Name of the file. Example: test.txt.
            file_format: File format. Example: txt.
            purpose: Purpose of the file. Default: general.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/post-file
        """
        full_path = Config.test_data_dir / Path(filename)

        with full_path.open("rb") as file:
            return self.request(
                method="POST",
                url=f"{self.url}/files",
                files={"file": (filename, file.read(), type_of_file[file_format])},
                data={"purpose": purpose},
            )

