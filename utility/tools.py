"""Supporting functions."""

from json import JSONDecodeError, dumps, loads

from requests import PreparedRequest

from utility.config import Config
from utility.custom_logging import logger


@logger.catch
def get_curl(
    request: PreparedRequest,
    is_compressed: bool = False,
    is_insecure: bool = False,
    is_breaks: bool = False,
) -> str:
    """GET CURL of request.

    Args:
        request: request to generate curl.
        is_compressed: parameter allowing to form a curl for "zipped" response.
        is_insecure: parameter allowing to form a curl for "unsafe" SSL connection and data transmission.
        is_breaks: return the curl string with breaks.
    """
    sep = " " if not is_breaks else "\n"

    body = request.body if request.body else ""

    if isinstance(body, bytes):
        try:
            body = body.decode("utf-8")

        except UnicodeDecodeError:
            body = body.decode("latin-1")

        body = f'-d "{body}"'

    curl_attrs = [
        f"curl -X {request.method}",
        sep.join([f'-H "{k}: {v}"' for k, v in request.headers.items()]),
        body,
        "--compressed" if is_compressed else "",
        "--insecure" if is_insecure else "",
        request.url,
    ]

    return sep.join([attr for attr in curl_attrs if attr])


def save_value_if_exceeds_limit(file_name: str, value: bytes | str, limit: int = 500) -> str:
    """Save value to file if it exceeds the limit.

    Args:
        file_name: file name.
        value: value to save.
        limit: limit of symbols that the value should not exceed.
    """
    if len(value) < limit:
        return value

    if file_name.endswith(".txt"):
        result = str(value)

    else:
        try:
            match value:
                case str():
                    jsonable_value = loads(value)
                case bytes():
                    jsonable_value = loads(value.decode())
                case _:
                    raise TypeError(f"Unexpected type: {type(value)}")

            result = dumps(jsonable_value, indent=2, ensure_ascii=False)

        except (JSONDecodeError, UnicodeDecodeError):
            logger.warning("Can't convert value to json. Save as text")
            result = str(value)
            file_name = file_name.replace(".json", ".txt")

    with open(path := Config.temp_dir / file_name, "w", encoding="utf-8") as file:
        file.write(result)

    return f'Value is too large! Saved to file by path: "{path}"'
