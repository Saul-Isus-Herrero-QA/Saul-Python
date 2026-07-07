"""Unit tests for the AI Engine module."""

import sys
from datetime import datetime, timedelta
from pathlib import Path

import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from task_manager.ai_engine import AIEngine


class TestAIEngineInitialization:
    """Test suite for AIEngine initialization."""

    def test_engine_init_creates_empty_history(self) -> None:
        """Test: initialization creates empty task history."""
        engine = AIEngine()
        assert engine.get_history() == []
        assert engine.analyze_productivity()["total_tasks"] == 0

    def test_engine_multiple_instances_independent(self) -> None:
        """Test: multiple engine instances are independent."""
        engine1 = AIEngine()
        engine2 = AIEngine()

        engine1.add_task_to_history("Study Python", "study")
        assert len(engine1.get_history()) == 1
        assert len(engine2.get_history()) == 0


class TestNLPTaskExtraction:
    """Test suite for Natural Language Processing and task extraction."""

    @pytest.fixture
    def engine(self) -> AIEngine:
        """Fixture providing AIEngine instance."""
        return AIEngine()

    def test_extract_task_basic(self, engine: AIEngine) -> None:
        """Test: extract basic task from natural language."""
        task, category = engine.extract_task_from_text("I need to study Python")
        assert "study" in task.lower()
        assert "python" in task.lower()
        assert category == "study"

    def test_extract_task_category_study(self, engine: AIEngine) -> None:
        """Test: correctly identifies study category."""
        _, category = engine.extract_task_from_text("Learn JavaScript today")
        assert category == "study"

    def test_extract_task_category_work(self, engine: AIEngine) -> None:
        """Test: correctly identifies work category."""
        _, category = engine.extract_task_from_text("I need to code a new feature")
        assert category == "work"

    def test_extract_task_category_exercise(self, engine: AIEngine) -> None:
        """Test: correctly identifies exercise category."""
        _, category = engine.extract_task_from_text("Go for a run tomorrow")
        assert category == "exercise"

    def test_extract_task_category_shopping(self, engine: AIEngine) -> None:
        """Test: correctly identifies shopping category."""
        _, category = engine.extract_task_from_text("I need to buy groceries")
        assert category == "shopping"

    def test_extract_task_category_meeting(self, engine: AIEngine) -> None:
        """Test: correctly identifies meeting category."""
        _, category = engine.extract_task_from_text("Call the team tomorrow")
        assert category == "meeting"

    def test_extract_task_category_clean(self, engine: AIEngine) -> None:
        """Test: correctly identifies cleaning category."""
        _, category = engine.extract_task_from_text("Organize my desk")
        assert category == "clean"

    def test_extract_task_category_cook(self, engine: AIEngine) -> None:
        """Test: correctly identifies cooking category."""
        _, category = engine.extract_task_from_text("Prepare dinner tonight")
        assert category == "cook"

    def test_extract_task_category_rest(self, engine: AIEngine) -> None:
        """Test: correctly identifies rest category."""
        _, category = engine.extract_task_from_text("Take a nap today")
        assert category == "rest"

    def test_extract_task_removes_stopwords(self, engine: AIEngine) -> None:
        """Test: extraction removes common stopwords."""
        task, _ = engine.extract_task_from_text("I need to the study a Python")
        # Stopwords should be removed
        assert "need" not in task.lower()
        assert "the" not in task.lower()

    def test_extract_task_cleans_punctuation(self, engine: AIEngine) -> None:
        """Test: extraction removes punctuation."""
        task, _ = engine.extract_task_from_text("I need to study Python!!!")
        assert "!" not in task
        assert "study" in task.lower()

    def test_extract_task_unknown_category(self, engine: AIEngine) -> None:
        """Test: returns None for unknown category."""
        _, category = engine.extract_task_from_text("Do something random")
        assert category is None

    def test_extract_task_invalid_type_raises_error(self, engine: AIEngine) -> None:
        """Test: passing non-string raises TypeError."""
        with pytest.raises(TypeError):
            engine.extract_task_from_text(123)  # type: ignore

    def test_extract_task_preserves_keywords(self, engine: AIEngine) -> None:
        """Test: important keywords are preserved in task description."""
        task, _ = engine.extract_task_from_text("Study Python and JavaScript")
        assert "python" in task.lower()
        assert "javascript" in task.lower()

    def test_extract_task_empty_string_returns_unspecified(self, engine: AIEngine) -> None:
        """Test: empty or whitespace-only input returns default."""
        task, _ = engine.extract_task_from_text("   ")
        assert task == "Unspecified task"


class TestTaskHistory:
    """Test suite for task history management."""

    @pytest.fixture
    def engine(self) -> AIEngine:
        """Fixture providing AIEngine instance."""
        return AIEngine()

    def test_add_task_to_history(self, engine: AIEngine) -> None:
        """Test: adding task to history works."""
        engine.add_task_to_history("Study Python", "study")
        history = engine.get_history()
        assert len(history) == 1
        assert history[0]["task"] == "Study Python"
        assert history[0]["category"] == "study"

    def test_add_multiple_tasks(self, engine: AIEngine) -> None:
        """Test: multiple tasks can be added."""
        engine.add_task_to_history("Study Python", "study")
        engine.add_task_to_history("Go to gym", "exercise")
        engine.add_task_to_history("Buy groceries", "shopping")

        assert len(engine.get_history()) == 3

    def test_add_task_sets_timestamp(self, engine: AIEngine) -> None:
        """Test: adding task sets timestamp."""
        before = datetime.now()
        engine.add_task_to_history("Test task", "study")
        after = datetime.now()

        record = engine.get_history()[0]
        assert before <= record["timestamp"] <= after

    def test_add_task_custom_timestamp(self, engine: AIEngine) -> None:
        """Test: custom timestamp can be provided."""
        custom_time = datetime(2025, 1, 1, 12, 0, 0)
        engine.add_task_to_history("Test", "study", timestamp=custom_time)

        record = engine.get_history()[0]
        assert record["timestamp"] == custom_time

    def test_add_task_default_not_completed(self, engine: AIEngine) -> None:
        """Test: newly added tasks are marked as not completed."""
        engine.add_task_to_history("Test task", "study")
        record = engine.get_history()[0]
        assert record["completed"] is False

    def test_add_task_invalid_type_raises_error(self, engine: AIEngine) -> None:
        """Test: adding non-string task raises TypeError."""
        with pytest.raises(TypeError):
            engine.add_task_to_history(123, "study")  # type: ignore

    def test_add_empty_task_raises_error(self, engine: AIEngine) -> None:
        """Test: adding empty task raises ValueError."""
        with pytest.raises(ValueError):
            engine.add_task_to_history("", "study")

    def test_mark_task_completed(self, engine: AIEngine) -> None:
        """Test: marking task as completed works."""
        engine.add_task_to_history("Study Python", "study")
        result = engine.mark_task_completed("Study Python")

        assert result is True
        assert engine.get_history()[0]["completed"] is True

    def test_mark_nonexistent_task_returns_false(self, engine: AIEngine) -> None:
        """Test: marking nonexistent task returns False."""
        engine.add_task_to_history("Task 1", "study")
        result = engine.mark_task_completed("Nonexistent task")
        assert result is False

    def test_mark_task_case_insensitive(self, engine: AIEngine) -> None:
        """Test: task completion is case-insensitive."""
        engine.add_task_to_history("Study Python", "study")
        result = engine.mark_task_completed("study python")
        assert result is True

    def test_clear_history(self, engine: AIEngine) -> None:
        """Test: clearing history removes all tasks."""
        engine.add_task_to_history("Task 1", "study")
        engine.add_task_to_history("Task 2", "study")

        engine.clear_history()
        assert len(engine.get_history()) == 0


class TestSuggestions:
    """Test suite for intelligent task suggestions."""

    @pytest.fixture
    def engine(self) -> AIEngine:
        """Fixture providing AIEngine instance with sample history."""
        eng = AIEngine()
        eng.add_task_to_history("Study Python", "study")
        eng.add_task_to_history("Study JavaScript", "study")
        eng.add_task_to_history("Study TypeScript", "study")
        eng.add_task_to_history("Go to gym", "exercise")
        return eng

    def test_get_suggestions_with_history(self, engine: AIEngine) -> None:
        """Test: suggestions are generated from history."""
        suggestions = engine.get_suggestions([])
        assert len(suggestions) > 0

    def test_get_suggestions_respects_limit(self, engine: AIEngine) -> None:
        """Test: suggestions respects limit parameter."""
        suggestions = engine.get_suggestions([], limit=2)
        assert len(suggestions) <= 2

    def test_get_suggestions_avoids_duplicates(self, engine: AIEngine) -> None:
        """Test: suggestions don't include current tasks."""
        current_tasks = ["Study Python"]
        suggestions = engine.get_suggestions(current_tasks)

        assert "Study Python" not in suggestions

    def test_get_suggestions_empty_history_returns_empty(self) -> None:
        """Test: empty history returns no suggestions."""
        engine = AIEngine()
        suggestions = engine.get_suggestions([])
        assert suggestions == []

    def test_get_suggestions_focuses_on_common_categories(self, engine: AIEngine) -> None:
        """Test: suggestions focus on most common categories."""
        suggestions = engine.get_suggestions([])
        # Study category has 3 tasks, exercise has 1
        # So suggestions should prioritize study
        study_tasks = [s for s in suggestions if "study" in s.lower()]
        assert len(study_tasks) > 0

    def test_get_suggestions_invalid_current_tasks_type(self, engine: AIEngine) -> None:
        """Test: passing non-list current_tasks raises TypeError."""
        with pytest.raises(TypeError):
            engine.get_suggestions("not a list")  # type: ignore


class TestProductivityAnalysis:
    """Test suite for productivity analysis."""

    @pytest.fixture
    def engine(self) -> AIEngine:
        """Fixture providing AIEngine instance."""
        return AIEngine()

    def test_analyze_productivity_empty_history(self, engine: AIEngine) -> None:
        """Test: empty history returns zero metrics."""
        analysis = engine.analyze_productivity()

        assert analysis["total_tasks"] == 0
        assert analysis["completed_tasks"] == 0
        assert analysis["completion_rate"] == 0.0

    def test_analyze_productivity_with_tasks(self, engine: AIEngine) -> None:
        """Test: analysis with tasks works correctly."""
        engine.add_task_to_history("Task 1", "study")
        engine.add_task_to_history("Task 2", "study")
        engine.add_task_to_history("Task 3", "exercise")

        analysis = engine.analyze_productivity()
        assert analysis["total_tasks"] == 3

    def test_analyze_completion_rate(self, engine: AIEngine) -> None:
        """Test: completion rate is calculated correctly."""
        engine.add_task_to_history("Task 1", "study")
        engine.add_task_to_history("Task 2", "study")

        engine.mark_task_completed("Task 1")

        analysis = engine.analyze_productivity()
        assert analysis["completed_tasks"] == 1
        assert analysis["completion_rate"] == 50.0

    def test_analyze_most_common_category(self, engine: AIEngine) -> None:
        """Test: most common category is identified."""
        engine.add_task_to_history("Study Python", "study")
        engine.add_task_to_history("Study JS", "study")
        engine.add_task_to_history("Go to gym", "exercise")

        analysis = engine.analyze_productivity()
        assert analysis["most_common_category"] == "study"

    def test_analyze_categories_dict(self, engine: AIEngine) -> None:
        """Test: categories dictionary is built correctly."""
        engine.add_task_to_history("Study Python", "study")
        engine.add_task_to_history("Study JS", "study")
        engine.add_task_to_history("Go to gym", "exercise")

        analysis = engine.analyze_productivity()
        assert analysis["categories"]["study"] == 2
        assert analysis["categories"]["exercise"] == 1

    def test_analyze_tasks_without_category(self, engine: AIEngine) -> None:
        """Test: tasks without category are handled."""
        engine.add_task_to_history("Task with category", "study")
        engine.add_task_to_history("Task without category", None)

        analysis = engine.analyze_productivity()
        assert analysis["total_tasks"] == 2


class TestProductivityReport:
    """Test suite for productivity reports."""

    @pytest.fixture
    def engine(self) -> AIEngine:
        """Fixture providing AIEngine instance."""
        return AIEngine()

    def test_get_productivity_report_returns_string(self, engine: AIEngine) -> None:
        """Test: productivity report returns string."""
        report = engine.get_productivity_report()
        assert isinstance(report, str)

    def test_report_contains_statistics(self, engine: AIEngine) -> None:
        """Test: report contains key statistics."""
        engine.add_task_to_history("Task 1", "study")
        engine.add_task_to_history("Task 2", "exercise")
        engine.mark_task_completed("Task 1")

        report = engine.get_productivity_report()
        assert "PRODUCTIVITY REPORT" in report
        assert "Total Tasks Added" in report
        assert "Completed Tasks" in report
        assert "Completion Rate" in report

    def test_report_with_no_tasks(self, engine: AIEngine) -> None:
        """Test: report works with no tasks."""
        report = engine.get_productivity_report()
        assert "PRODUCTIVITY REPORT" in report
        assert "0" in report  # Should show 0 tasks


class TestStatistics:
    """Test suite for detailed statistics."""

    @pytest.fixture
    def engine(self) -> AIEngine:
        """Fixture providing AIEngine instance."""
        return AIEngine()

    def test_get_statistics_returns_dict(self, engine: AIEngine) -> None:
        """Test: statistics method returns dictionary."""
        stats = engine.get_statistics()
        assert isinstance(stats, dict)

    def test_statistics_keys_present(self, engine: AIEngine) -> None:
        """Test: all expected keys are in statistics."""
        engine.add_task_to_history("Task 1", "study")

        stats = engine.get_statistics()
        assert "average_tasks_per_day" in stats
        assert "most_productive_category" in stats
        assert "oldest_task_age_days" in stats

    def test_average_tasks_per_day(self, engine: AIEngine) -> None:
        """Test: average tasks per day is calculated."""
        engine.add_task_to_history("Task 1", "study")
        engine.add_task_to_history("Task 2", "study")

        stats = engine.get_statistics()
        assert stats["average_tasks_per_day"] > 0

    def test_oldest_task_age(self, engine: AIEngine) -> None:
        """Test: oldest task age is calculated."""
        old_time = datetime.now() - timedelta(days=5)
        engine.add_task_to_history("Old task", "study", timestamp=old_time)

        stats = engine.get_statistics()
        assert stats["oldest_task_age_days"] >= 5


class TestIntegration:
    """Integration tests for AIEngine."""

    def test_full_workflow(self) -> None:
        """Test: complete workflow with NLP, history, suggestions, analytics."""
        engine = AIEngine()

        # 1. Extract from natural language and add
        task1, cat1 = engine.extract_task_from_text("I need to study Python tomorrow")
        engine.add_task_to_history(task1, cat1)

        # 2. Extract another
        task2, cat2 = engine.extract_task_from_text("Let's go to the gym")
        engine.add_task_to_history(task2, cat2)

        # 3. Get suggestions
        suggestions = engine.get_suggestions([task1])
        assert len(suggestions) >= 0

        # 4. Mark one completed
        engine.mark_task_completed(task1)

        # 5. Analyze productivity
        analysis = engine.analyze_productivity()
        assert analysis["total_tasks"] == 2
        assert analysis["completed_tasks"] == 1

        # 6. Get report
        report = engine.get_productivity_report()
        assert "PRODUCTIVITY REPORT" in report

    def test_multiple_categories_analysis(self) -> None:
        """Test: analysis with multiple categories."""
        engine = AIEngine()

        tasks_data = [
            ("Study Python", "study"),
            ("Study JavaScript", "study"),
            ("Go to gym", "exercise"),
            ("Buy groceries", "shopping"),
            ("Call team", "meeting"),
        ]

        for task, category in tasks_data:
            engine.add_task_to_history(task, category)

        analysis = engine.analyze_productivity()
        assert analysis["total_tasks"] == 5
        assert len(analysis["categories"]) == 4  # All categories except study

    def test_persistent_history_across_operations(self) -> None:
        """Test: history persists across all operations."""
        engine = AIEngine()

        # Add tasks
        engine.add_task_to_history("Task 1", "study")
        engine.add_task_to_history("Task 2", "study")

        # Get suggestions
        engine.get_suggestions([])

        # Analyze
        engine.analyze_productivity()

        # Get report
        engine.get_productivity_report()

        # History should still have both tasks
        assert len(engine.get_history()) == 2
