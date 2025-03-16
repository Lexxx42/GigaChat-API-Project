"""Base API client."""

from http.cookiejar import CookieJar

from requests import Request, Response, Session

from api.authentication import Authentication
from utility.custom_logging import log_request, log_response


class ApiClient:
    """Base API client."""

    def __init__(
        self,
        headers: dict | None = None,
        cookies: dict | CookieJar | None = None,
        verify: str | bool = False,
        cert: str | tuple[str, str] | None = None,
        timeout: int | float | None = 10,
        allow_redirects: bool = True,
        *args,
        **kwargs,
    ):
        """Constructor.

        Args:
            headers: headers, if any.
            cookies: cookies, if any.
            verify: verify, cert if any.
            cert: SSL/TLS-certificate, if any.
            timeout: timeout of response.
            allow_redirects: allow redirects or not.
            *args: additional arguments.
            **kwargs: additional keywords arguments.
        """
        self.headers = headers if headers else {}
        self.cookies = cookies
        self.verify = verify
        self.cert = cert
        self.timeout = timeout
        self.allow_redirects = allow_redirects

        self.auth = Authentication()

    def __get_headers_with_auth(self, headers: dict[str, str] | None) -> dict[str, str]:
        """Add authorization token to headers."""
        if self.auth is not None:
            headers = headers if headers else {}
            headers["Authorization"] = f"Bearer {self.auth.get_token_request()}"

        return headers

    def request(
        self,
        url: str,
        method: str = "GET",
        data: dict | list | str | bytes | None = None,
        params: dict | None = None,
        files: dict | list | None = None,
        json: dict | list | None = None,
        headers: dict | None = None,
        cookies: dict | CookieJar | None = None,
        cert: str | tuple[str, str] | None = None,
        timeout: int | float | None = None,
        allow_redirects: bool | None = None,
        **kwargs,
    ) -> Response:
        """Send request.

        Args:
            url: URL.
            method: HTTP-method.
            data: data of the request, if any.
            params: query parameters, if any.
            files: files for multipart/form-data, if any.
            json: body of the request as JSON, if any.
            headers: headers, if any.
            cookies: cookies, if any.
            cert: certificate for SSL/TLS-connection, if any.
            timeout: timeout of response.
            allow_redirects: allow redirects or not.
            **kwargs: additional keywords arguments.
        """
        prepared_request = Request(
            url=url,
            method=method,
            params=params,
            data=data,
            files=files,
            json=json,
            headers=self.__get_headers_with_auth(headers=headers),
            cookies=cookies if cookies else self.cookies,
            **kwargs,
        ).prepare()

        log_request(
            request=prepared_request,
            is_insecure=self.verify is False,
        )

        with Session() as session:
            response = session.send(
                request=prepared_request,
                verify=self.verify,
                timeout=timeout if timeout is not None else self.timeout,
                cert=cert if cert else self.cert,
                allow_redirects=allow_redirects if allow_redirects is not None else self.allow_redirects,
            )

        log_response(response=response)

        return response
