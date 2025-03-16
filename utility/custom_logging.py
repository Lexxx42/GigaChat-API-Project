"""Logger creation, settings."""

import sys
import uuid
from argparse import Namespace

from loguru import logger
from requests import PreparedRequest, Response

from utility.tools import get_curl, save_value_if_exceeds_limit


def create_logger(log_level: str, params: Namespace) -> None:
    """Create a logger instance.

    Args:
        log_level: log level.
        params: startup parameters.
    """
    try:
        logger.remove()

        if getattr(params, "xmlpath", None):
            logger.add(
                sink=sys.stdout,
                level=log_level,
                format="\n{time:HH:mm:ss.SSS} | <level>{level}</level> | <level>{message}</level>",
            )

        else:
            logger.add(
                sink=sys.stdout,
                format=(
                    "\n<fg #ff7e00>{time:HH:mm:ss.SSS}</fg #ff7e00> | "
                    "<level>{level}</level> | "
                    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
                    "<level>{message}</level>"
                ),
                level=log_level,
                colorize=True,
            )

    except ValueError:
        logger.error(f"Error: Invalid log level: {log_level=}")
        raise InvalidLogLevel(log_level=log_level, available_log_levels=logger._core.levels.keys()) from None  # noqa


def log_request(
    request: PreparedRequest,
    is_compressed: bool = False,
    is_insecure: bool = False,
) -> None:
    """Log request.

    Args:
        request: request.
        is_compressed: parameter allowing to form a curl for "zipped" response.
        is_insecure: parameter allowing to form a curl for "unsafe" SSL connection and data transmission.
    """
    curl = None
    color = "blue"
    msg = (
        f"HTTP-Method: <{color}><n>{request.method}</n></{color}>\n"
        f"\t URL:     <{color}><n>{request.url}</n></{color}>\n"
        f"\t Headers: <{color}><n>{request.headers}</n></{color}>\n"
    )

    request_uuid = str(uuid.uuid4())

    if "boundary" not in request.headers and request.method != "GET":
        result_body = save_value_if_exceeds_limit(file_name=f"{request_uuid}_req_body.json", value=request.body)

        msg += f"\t Body:    <{color}><n>{result_body}</n></{color}>\n"

    if "boundary" not in request.headers:
        curl = get_curl(request=request, is_compressed=is_compressed, is_insecure=is_insecure, is_breaks=True)

        result_curl = save_value_if_exceeds_limit(file_name=f"{request_uuid}_curl.txt", value=curl, limit=0)

        msg += f"\t CURL:    <{color}><n>{result_curl}</n></{color}>"

    try:
        logger.opt(colors=True).debug(msg)

    except ValueError:
        logger.debug(f'Error while logging a request:\n\tCURL: {curl if curl else "None"}')
        logger.opt(colors=False).debug(msg.replace("<{color}><n>", "").replace("</n></{color}>", ""))


def log_response(response: Response) -> None:
    """Log response.

    Args:
        response: response.
    """
    color = {1: "light-blue", 2: "green", 3: "yellow", 4: "red", 5: "red"}.get(response.status_code // 100, "y")

    response_body = save_value_if_exceeds_limit(file_name=f"{uuid.uuid4()}_res_body.json", value=response.text)

    try:
        logger.opt(colors=True).debug(
            f"Code: <{color}><n>{response.status_code}</n></{color}>\n"
            f"\t Headers: <{color}><n>{response.headers}</n></{color}>\n"
            f"\t Body:    <{color}><n>{response_body}</n></{color}>",
        )

    except ValueError:
        logger.opt(colors=True).debug(
            f"Code: <{color}><n>{response.status_code}</n></{color}>\n"
            f"\t Headers: <{color}><n>{response.headers}</n></{color}>\n",
        )
        logger.debug(f"Body: {response_body}")
