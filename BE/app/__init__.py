import logging
from logging.config import dictConfig
from .core.config import settings

# Configurazione di logging
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        },
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "formatter": "default",
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["default"],
    },
}

dictConfig(logging_config)
logger = logging.getLogger(__name__)

# Caricamento delle configurazioni
logger.info(f"Loading configurations from {settings.ENVIRONMENT}")

__all__ = ["logger"]
