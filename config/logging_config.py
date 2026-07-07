"""Configuración centralizada de logging para la aplicación."""

import logging
import logging.handlers
from pathlib import Path

# Crear directorio de logs si no existe
LOGS_DIR = Path(__file__).parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

LOG_FILE = LOGS_DIR / "task_manager.log"
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging() -> None:
    """Configura el logging para toda la aplicación."""
    # Logger root
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)

    # Formato
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    # Handler para archivo (rotativo)
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5MB
        backupCount=5,
    )
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(formatter)

    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(formatter)

    # Agregar handlers
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)


def get_logger(name: str) -> logging.Logger:
    """Retorna un logger configurado."""
    return logging.getLogger(name)
