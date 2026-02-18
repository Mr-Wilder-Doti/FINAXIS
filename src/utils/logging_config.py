from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any


LOGGER_NAME = "global_portfolio_bot"


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "logger": record.name,
            "level": record.levelname,
            "message": record.getMessage(),
        }
        return json.dumps(payload, ensure_ascii=False)


def configure_logging(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(level.upper())
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)

    return logger


def log_event(logger: logging.Logger, event: str, **extra: Any) -> None:
    payload = {"event": event, **extra}
    logger.info(json.dumps(payload, ensure_ascii=False))
