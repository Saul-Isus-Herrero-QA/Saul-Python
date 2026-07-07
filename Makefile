# Makefile para Task Manager

.PHONY: help install install-dev test test-cov lint format type-check clean run pre-commit

help:
	@echo "Task Manager - Comandos disponibles"
	@echo "===================================="
	@echo "  make install          - Instalar dependencias"
	@echo "  make install-dev      - Instalar con dev dependencies"
	@echo "  make test             - Ejecutar tests"
	@echo "  make test-cov         - Tests con cobertura"
	@echo "  make lint             - Ejecutar linters"
	@echo "  make format           - Formatear código"
	@echo "  make type-check       - Type checking con mypy"
	@echo "  make clean            - Limpiar archivos temporales"
	@echo "  make run              - Ejecutar aplicación"
	@echo "  make pre-commit       - Ejecutar pre-commit en todos los archivos"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt

test:
	pytest -v

test-cov:
	pytest --cov=src/task_manager --cov-report=html --cov-report=term -v

lint:
	flake8 src/ tests/ main.py
	pylint src/task_manager

format:
	black src/ tests/ main.py config/
	isort src/ tests/ main.py config/

type-check:
	mypy src/ main.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type d -name ".mypy_cache" -delete
	find . -type d -name ".tox" -delete
	rm -rf build/ dist/ *.egg-info htmlcov/ .coverage

run:
	python main.py

pre-commit:
	pre-commit run --all-files

# Workflow completo
all: install lint test type-check
	@echo "Workflow completado exitosamente"

# CI/CD local
ci: clean install-dev lint test-cov type-check
	@echo "CI pipeline completado"
