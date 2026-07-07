"""Punto de entrada principal de la aplicación."""

import sys
from pathlib import Path

# Agregar src al path para importaciones
sys.path.insert(0, str(Path(__file__).parent / "src"))

from config.logging_config import get_logger, setup_logging
from task_manager import CLIApplication, TaskManager

logger = get_logger(__name__)


def main() -> None:
    """Función principal de la aplicación."""
    # Configurar logging antes de iniciar
    setup_logging()
    logger.info("=" * 50)
    logger.info("Iniciando aplicación Task Manager")
    logger.info("=" * 50)

    try:
        # Inyección de dependencias
        task_manager = TaskManager()
        app = CLIApplication(manager=task_manager)

        # Ejecutar aplicación
        app.run()

    except Exception as e:
        logger.exception(f"Error crítico en main: {e}")
        print(f"Error crítico: {e}")
        sys.exit(1)

    finally:
        logger.info("Aplicación finalizada")
        logger.info("=" * 50)


if __name__ == "__main__":
    main()
