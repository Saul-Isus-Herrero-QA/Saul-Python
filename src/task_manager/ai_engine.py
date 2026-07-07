"""AI Engine for intelligent task management."""

import logging
import re
from collections import Counter
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


class AIEngine:
    """
    Intelligent AI engine for task analysis, NLP processing, and smart suggestions.

    Provides:
    - Natural Language Processing (NLP) for task extraction
    - Intelligent suggestions based on task history
    - Productivity analytics and pattern detection
    """

    # Keywords for task extraction
    TASK_KEYWORDS = {
        "study": ["study", "learn", "educate", "research", "read"],
        "work": ["work", "code", "develop", "build", "create"],
        "exercise": ["exercise", "run", "gym", "workout", "train"],
        "shopping": ["buy", "purchase", "shop", "get", "shop for"],
        "meeting": ["meet", "meeting", "call", "discuss", "talk"],
        "clean": ["clean", "organize", "tidy", "arrange", "declutter"],
        "cook": ["cook", "prepare", "bake", "make", "cook food"],
        "rest": ["rest", "sleep", "relax", "chill", "nap"],
    }

    def __init__(self) -> None:
        """Initialize the AI Engine."""
        self._tasks_history: List[Dict[str, any]] = []
        logger.info("AIEngine initialized")

    def extract_task_from_text(self, text: str) -> Tuple[str, Optional[str]]:
        """
        Extract task description and category from natural language text.

        Uses keyword matching and pattern detection to categorize tasks.

        Args:
            text: Natural language input (e.g., "Tomorrow I need to study Python")

        Returns:
            Tuple of (cleaned_task_description, detected_category)
            Category is None if no match found.

        Example:
            >>> engine = AIEngine()
            >>> task, category = engine.extract_task_from_text("I need to study Python")
            >>> task
            'study Python'
            >>> category
            'study'
        """
        if not isinstance(text, str):
            logger.error(f"extract_task_from_text: invalid type {type(text)}")
            raise TypeError("Input must be a string")

        # Clean text: lowercase, remove punctuation, trim whitespace
        cleaned = re.sub(r"[^\w\s]", " ", text.lower()).strip()
        words = cleaned.split()

        # Extract category based on keywords
        detected_category = None
        for category, keywords in self.TASK_KEYWORDS.items():
            if any(word in words for word in keywords):
                detected_category = category
                break

        # Remove common stopwords for cleaner task description
        stopwords = {
            "i",
            "need",
            "to",
            "the",
            "a",
            "an",
            "and",
            "or",
            "is",
            "am",
            "are",
            "be",
            "been",
            "have",
            "has",
            "do",
            "does",
            "did",
            "will",
            "should",
            "could",
            "would",
            "tomorrow",
            "today",
            "tonight",
            "next",
            "this",
        }
        filtered_words = [w for w in words if w not in stopwords]
        task_description = " ".join(filtered_words)

        logger.debug(
            f"extract_task_from_text: '{text}' -> '{task_description}' (category: {detected_category})"
        )
        return task_description or "Unspecified task", detected_category

    def add_task_to_history(
        self, task: str, category: Optional[str] = None, timestamp: Optional[datetime] = None
    ) -> None:
        """
        Add a task to the analysis history.

        Args:
            task: Task description.
            category: Task category.
            timestamp: When the task was added (defaults to now).
        """
        if not isinstance(task, str):
            raise TypeError("Task must be a string")

        if not task.strip():
            raise ValueError("Task cannot be empty")

        record = {
            "task": task.strip(),
            "category": category,
            "timestamp": timestamp or datetime.now(),
            "completed": False,
        }

        self._tasks_history.append(record)
        logger.info(f"add_task_to_history: '{task}' added (category: {category})")

    def mark_task_completed(self, task: str) -> bool:
        """
        Mark a task as completed in the history.

        Args:
            task: Task description to mark as completed.

        Returns:
            True if task was found and marked, False otherwise.
        """
        for record in self._tasks_history:
            if record["task"].lower() == task.lower():
                record["completed"] = True
                logger.info(f"mark_task_completed: '{task}' marked as completed")
                return True

        logger.warning(f"mark_task_completed: task '{task}' not found in history")
        return False

    def get_suggestions(self, current_tasks: List[str], limit: int = 3) -> List[str]:
        """
        Generate intelligent task suggestions based on history patterns.

        Analyzes frequency of task categories and suggests similar tasks
        that haven't been added recently.

        Args:
            current_tasks: List of current tasks to avoid duplicates.
            limit: Maximum number of suggestions to return.

        Returns:
            List of suggested task descriptions.

        Example:
            >>> engine = AIEngine()
            >>> engine.add_task_to_history("study Python")
            >>> engine.add_task_to_history("study JavaScript")
            >>> engine.add_task_to_history("study TypeScript")
            >>> suggestions = engine.get_suggestions([])
            >>> len(suggestions) > 0
            True
        """
        if not isinstance(current_tasks, list):
            raise TypeError("current_tasks must be a list")

        if not self._tasks_history:
            logger.debug("get_suggestions: no history, returning empty list")
            return []

        # Count category frequency
        categories = [r["category"] for r in self._tasks_history if r["category"]]
        category_counts = Counter(categories)

        if not category_counts:
            logger.debug("get_suggestions: no categories found")
            return []

        # Get most common categories
        most_common = category_counts.most_common(3)
        suggested_tasks = []

        for category, _ in most_common:
            # Find tasks in this category
            category_tasks = [r["task"] for r in self._tasks_history if r["category"] == category]

            if category_tasks:
                # Pick the most similar task that's not already in current tasks
                for task in category_tasks:
                    if task not in current_tasks:
                        suggested_tasks.append(task)

        logger.info(f"get_suggestions: generated {len(suggested_tasks[:limit])} suggestions")
        return suggested_tasks[:limit]

    def analyze_productivity(self) -> Dict[str, any]:
        """
        Analyze productivity metrics from task history.

        Returns:
            Dictionary containing:
            - total_tasks: Total tasks added
            - completed_tasks: Tasks marked as completed
            - completion_rate: Percentage of completed tasks
            - most_common_category: Category with most tasks
            - categories: Dictionary with count per category
        """
        if not self._tasks_history:
            logger.debug("analyze_productivity: no history, returning defaults")
            return {
                "total_tasks": 0,
                "completed_tasks": 0,
                "completion_rate": 0.0,
                "most_common_category": None,
                "categories": {},
            }

        total = len(self._tasks_history)
        completed = sum(1 for r in self._tasks_history if r["completed"])
        completion_rate = (completed / total * 100) if total > 0 else 0.0

        # Category analysis
        categories = [r["category"] for r in self._tasks_history if r["category"]]
        category_counts = Counter(categories)
        most_common_category = (
            category_counts.most_common(1)[0][0] if category_counts else None
        )

        analysis = {
            "total_tasks": total,
            "completed_tasks": completed,
            "completion_rate": round(completion_rate, 2),
            "most_common_category": most_common_category,
            "categories": dict(category_counts),
        }

        logger.info(f"analyze_productivity: {analysis}")
        return analysis

    def get_productivity_report(self) -> str:
        """
        Generate a human-readable productivity report.

        Returns:
            Formatted report string with statistics and insights.
        """
        analysis = self.analyze_productivity()

        report = "\n" + "=" * 50 + "\n"
        report += "📊 PRODUCTIVITY REPORT\n"
        report += "=" * 50 + "\n\n"
        report += f"Total Tasks Added:     {analysis['total_tasks']}\n"
        report += f"Completed Tasks:       {analysis['completed_tasks']}\n"
        report += f"Completion Rate:       {analysis['completion_rate']:.1f}%\n"

        if analysis["most_common_category"]:
            report += f"Most Common Category:  {analysis['most_common_category'].upper()}\n"

        if analysis["categories"]:
            report += "\nTasks by Category:\n"
            for category, count in sorted(analysis["categories"].items(), key=lambda x: x[1],
                                         reverse=True):
                report += f"  - {category.capitalize()}: {count} tasks\n"

        report += "=" * 50 + "\n"

        logger.debug("get_productivity_report: report generated")
        return report

    def get_history(self) -> List[Dict[str, any]]:
        """
        Get the complete task history.

        Returns:
            List of task records with metadata.
        """
        logger.debug(f"get_history: returning {len(self._tasks_history)} records")
        return self._tasks_history.copy()

    def clear_history(self) -> None:
        """Clear all task history."""
        self._tasks_history.clear()
        logger.info("clear_history: history cleared")

    def get_statistics(self) -> Dict[str, any]:
        """
        Get detailed statistics about tasks.

        Returns:
            Dictionary with various statistics.
        """
        if not self._tasks_history:
            return {
                "average_tasks_per_day": 0.0,
                "most_productive_category": None,
                "oldest_task_age_days": 0,
            }

        # Days span
        timestamps = [r["timestamp"] for r in self._tasks_history]
        if len(timestamps) > 1:
            days_span = (max(timestamps) - min(timestamps)).days or 1
        else:
            days_span = 1

        avg_per_day = len(self._tasks_history) / days_span

        # Most productive category
        categories = [r["category"] for r in self._tasks_history if r["category"]]
        most_productive = (
            Counter(categories).most_common(1)[0][0] if categories else None
        )

        # Oldest task age
        oldest_timestamp = min(timestamps)
        oldest_age = (datetime.now() - oldest_timestamp).days

        stats = {
            "average_tasks_per_day": round(avg_per_day, 2),
            "most_productive_category": most_productive,
            "oldest_task_age_days": oldest_age,
        }

        logger.debug(f"get_statistics: {stats}")
        return stats
