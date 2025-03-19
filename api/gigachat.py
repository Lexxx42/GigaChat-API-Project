"""GigaChat API client."""

from pathlib import Path

from requests import Response

from api.api_client import ApiClient
from dto.post_chat_completions_text_request_dto import PostChatCompletionsTextRequestDto
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

    def get_models(self) -> Response:
        """Get a list of AI models.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/get-models
            Response model: GetModelListDto.
        """

        return self.request(method="GET", url=f"{self.url}/models")

    def post_tokens_count(self, json: PostTokenCountRequestDto) -> Response:
        """Calculate the number of tokens in the request.

        Args:
            json: Request body.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/post-tokens-count
            Response model: PostTokenCountDto.
        """

        return self.request(method="POST", url=f"{self.url}/tokens/count", json=json.model_dump(mode="json"))

    def post_embeddings(self, json: PostEmbeddingsRequestDto) -> Response:
        """Create embedding.

        Args:
            json: Request body.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/post-embeddings
            Response model: PostEmbeddingsDto.
        """

        return self.request(method="POST", url=f"{self.url}/embeddings", json=json.model_dump(mode="json"))

    def post_file(self, filename: str, file_format: SupportedFileFormats, purpose: str = "general") -> Response:
        """Upload a file.

        Args:
            filename: Name of the file. Example: test.txt.
            file_format: File format. Example: txt.
            purpose: Purpose of the file. Default: general.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/post-file
            Response model: PostFileDto.
        """
        full_path = Config.test_data_dir / Path(filename)

        with full_path.open("rb") as file:
            return self.request(
                method="POST",
                url=f"{self.url}/files",
                files={"file": (filename, file.read(), type_of_file[file_format])},
                data={"purpose": purpose},
            )

    def post_file_delete(self, file: str) -> Response:
        """Delete a file.

        Args:
            file: File ID.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/file-delete
            Response model: PostFileDeleteDto.
        """

        return self.request(method="POST", url=f"{self.url}/files/{file}/delete")

    def get_files(self) -> Response:
        """Get available files.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/get-files
            Response model: GetFilesDto.
        """

        return self.request(method="GET", url=f"{self.url}/files")

    def get_file(self, file: str) -> Response:
        """Get file info.

        Args:
            file: File ID.

        Notes:
            Docs: https://developers.sber.ru/docs/ru/gigachat/api/reference/rest/get-file
            Response model: any.
        """

        return self.request(method="GET", url=f"{self.url}/files/{file}/content")

    def post_chat_completions(self, json: PostChatCompletionsTextRequestDto) -> Response:
        """Generate text.

        Args:
            json: Request body.

        Notes:
            Docs: -
            Response model: -.
        """

        return self.request(method="POST", url=f"{self.url}/chat/completions", json=json.model_dump(mode="json"))
