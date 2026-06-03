import time
import logging

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


# Configure logger
logger = logging.getLogger("request_logger")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class RequestLoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next
    ):
        start_time = time.time()

        method = request.method
        path = request.url.path
        client_ip = request.client.host if request.client else "Unknown"

        logger.info(
            f"REQUEST | {client_ip} | {method} | {path}"
        )

        try:

            response = await call_next(request)

            process_time = round(
                time.time() - start_time,
                4
            )

            logger.info(
                f"RESPONSE | {method} | {path} | "
                f"Status={response.status_code} | "
                f"Time={process_time}s"
            )

            return response

        except Exception as ex:

            process_time = round(
                time.time() - start_time,
                4
            )

            logger.error(
                f"ERROR | {method} | {path} | "
                f"Time={process_time}s | "
                f"Message={str(ex)}"
            )

            raise ex