"""Tests unitarios para el módulo TaskManager."""

import sys
from pathlib import Path

import pytest

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from task_manager import (
    CLIApplication,
    EmptyTaskDescriptionError,
    InvalidTaskIndexError,
    TaskManager,
)


class TestTaskManager:
    """Suite de tests para la clase TaskManager."""

    @pytest.fixture
    def manager(self) -> TaskManager:
        """Fixture que proporciona una nueva instancia de TaskManager."""
        return TaskManager()

    def test_init_creates_empty_list(self, manager: TaskManager) -> None:
        """Test: inicialización crea lista vacía."""
        assert manager.is_empty() is True
        assert manager.count() == 0

    def test_add_valid_task(self, manager: TaskManager) -> None:
        """Test: agregar tarea válida retorna True."""
        result = manager.add("Estudiar Python")
        assert result is True
        assert manager.count() == 1

    def test_add_task_with_whitespace(self, manager: TaskManager) -> None:
        """Test: agregar tarea con espacios es trimmed."""
        manager.add("   Hacer ejercicio   ")
        tasks = manager.get_all()
        assert tasks[0] == "Hacer ejercicio"

    def test_add_empty_task_raises_error(self, manager: TaskManager) -> None:
        """Test: agregar tarea vacía levanta EmptyTaskDescriptionError."""
        with pytest.raises(EmptyTaskDescriptionError):
            manager.add("")

    def test_add_whitespace_only_raises_error(self, manager: TaskManager) -> None:
        """Test: agregar solo espacios levanta excepción."""
        with pytest.raises(EmptyTaskDescriptionError):
            manager.add("   ")

    def test_add_non_string_raises_typeerror(self, manager: TaskManager) -> None:
        """Test: agregar no-string levanta TypeError."""
        with pytest.raises(TypeError):
            manager.add(123)  # type: ignore
        with pytest.raises(TypeError):
            manager.add(None)  # type: ignore

    def test_get_all_returns_copy(self, manager: TaskManager) -> None:
        """Test: get_all retorna copia, no referencia."""
        manager.add("Tarea 1")
        tasks = manager.get_all()
        tasks.append("Tarea Falsa")  # Modificar la copia
        assert manager.count() == 1  # Original no cambia

    def test_delete_valid_index(self, manager: TaskManager) -> None:
        """Test: eliminar con índice válido funciona."""
        manager.add("Tarea 1")
        manager.add("Tarea 2")
        deleted = manager.delete(0)
        assert deleted == "Tarea 1"
        assert manager.count() == 1

    def test_delete_negative_index_raises_error(self, manager: TaskManager) -> None:
        """Test: índice negativo levanta InvalidTaskIndexError."""
        manager.add("Tarea 1")
        with pytest.raises(InvalidTaskIndexError):
            manager.delete(-1)

    def test_delete_index_out_of_range_raises_error(
        self, manager: TaskManager
    ) -> None:
        """Test: índice fuera de rango levanta excepción."""
        manager.add("Tarea 1")
        with pytest.raises(InvalidTaskIndexError):
            manager.delete(5)

    def test_delete_non_int_raises_typeerror(self, manager: TaskManager) -> None:
        """Test: índice no-int levanta TypeError."""
        manager.add("Tarea 1")
        with pytest.raises(TypeError):
            manager.delete("0")  # type: ignore

    def test_multiple_operations(self, manager: TaskManager) -> None:
        """Test: múltiples operaciones funciona correctamente."""
        assert manager.is_empty() is True

        manager.add("Tarea A")
        manager.add("Tarea B")
        manager.add("Tarea C")
        assert manager.count() == 3

        deleted = manager.delete(1)  # Elimina Tarea B
        assert deleted == "Tarea B"
        assert manager.count() == 2

        tasks = manager.get_all()
        assert tasks == ["Tarea A", "Tarea C"]


class TestCLIApplication:
    """Suite de tests para la clase CLIApplication."""

    @pytest.fixture
    def app(self) -> CLIApplication:
        """Fixture que proporciona una aplicación CLI."""
        manager = TaskManager()
        return CLIApplication(manager)

    def test_app_initialization(self, app: CLIApplication) -> None:
        """Test: inicialización de CLIApplication."""
        assert app.manager is not None
        assert app.manager.is_empty() is True

    def test_is_empty_returns_true_for_empty_manager(
        self, app: CLIApplication
    ) -> None:
        """Test: aplicación detecta cuando está vacía."""
        assert app.manager.is_empty() is True

    def test_count_reflects_manager_count(self, app: CLIApplication) -> None:
        """Test: count de app refleja count de manager."""
        app.manager.add("Tarea 1")
        assert app.manager.count() == 1
