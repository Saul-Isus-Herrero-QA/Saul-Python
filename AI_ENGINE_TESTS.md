# AI Engine - Test Documentation

## Overview

The AI Engine module (`src/task_manager/ai_engine.py`) provides intelligent task management with Natural Language Processing (NLP), task suggestions, and productivity analytics.

Test suite: `tests/test_ai_engine.py` (400+ lines, 50+ tests)

---

## Test Suites

### 1. **TestAIEngineInitialization**
Tests basic engine initialization and independence.

**Tests:**
- `test_engine_init_creates_empty_history` - Verifies empty history on init
- `test_engine_multiple_instances_independent` - Ensures instances don't interfere

---

### 2. **TestNLPTaskExtraction**
Tests Natural Language Processing for task extraction and categorization.

**Tests:**
- `test_extract_task_basic` - Extract basic task from natural language
- `test_extract_task_category_study` - Identify study category
- `test_extract_task_category_work` - Identify work category
- `test_extract_task_category_exercise` - Identify exercise category
- `test_extract_task_category_shopping` - Identify shopping category
- `test_extract_task_category_meeting` - Identify meeting category
- `test_extract_task_category_clean` - Identify cleaning category
- `test_extract_task_category_cook` - Identify cooking category
- `test_extract_task_category_rest` - Identify rest category
- `test_extract_task_removes_stopwords` - Verify stopwords removal
- `test_extract_task_cleans_punctuation` - Verify punctuation removal
- `test_extract_task_unknown_category` - Handle unknown categories
- `test_extract_task_invalid_type_raises_error` - Type validation
- `test_extract_task_preserves_keywords` - Preserve important keywords
- `test_extract_task_empty_string_returns_unspecified` - Handle empty input

**Categories Detected:**
```
study, work, exercise, shopping, meeting, clean, cook, rest
```

---

### 3. **TestTaskHistory**
Tests task history management and task completion tracking.

**Tests:**
- `test_add_task_to_history` - Add single task
- `test_add_multiple_tasks` - Add multiple tasks
- `test_add_task_sets_timestamp` - Automatic timestamp
- `test_add_task_custom_timestamp` - Custom timestamp support
- `test_add_task_default_not_completed` - Default completion status
- `test_add_task_invalid_type_raises_error` - Type validation
- `test_add_empty_task_raises_error` - Empty task validation
- `test_mark_task_completed` - Mark task as completed
- `test_mark_nonexistent_task_returns_false` - Handle missing tasks
- `test_mark_task_case_insensitive` - Case-insensitive matching
- `test_clear_history` - Clear all history

---

### 4. **TestSuggestions**
Tests intelligent task suggestion generation.

**Tests:**
- `test_get_suggestions_with_history` - Generate from history
- `test_get_suggestions_respects_limit` - Respect limit parameter
- `test_get_suggestions_avoids_duplicates` - Avoid current tasks
- `test_get_suggestions_empty_history_returns_empty` - Empty history handling
- `test_get_suggestions_focuses_on_common_categories` - Prioritize common categories
- `test_get_suggestions_invalid_current_tasks_type` - Type validation

**Algorithm:**
1. Count task categories by frequency
2. Get most common categories (top 3)
3. Find tasks in those categories
4. Filter out tasks already in current list
5. Return up to `limit` suggestions

---

### 5. **TestProductivityAnalysis**
Tests productivity metrics calculation.

**Tests:**
- `test_analyze_productivity_empty_history` - Empty history metrics
- `test_analyze_productivity_with_tasks` - Metrics with tasks
- `test_analyze_completion_rate` - Calculate completion %
- `test_analyze_most_common_category` - Identify top category
- `test_analyze_categories_dict` - Category breakdown
- `test_analyze_tasks_without_category` - Handle uncategorized tasks

**Metrics Provided:**
```python
{
    "total_tasks": int,
    "completed_tasks": int,
    "completion_rate": float,  # percentage
    "most_common_category": str,
    "categories": {category: count, ...}
}
```

---

### 6. **TestProductivityReport**
Tests human-readable report generation.

**Tests:**
- `test_get_productivity_report_returns_string` - Returns string
- `test_report_contains_statistics` - Contains key metrics
- `test_report_with_no_tasks` - Works with empty history

**Report Format:**
```
==================================================
📊 PRODUCTIVITY REPORT
==================================================

Total Tasks Added:     X
Completed Tasks:       X
Completion Rate:       X.X%
Most Common Category:  CATEGORY

Tasks by Category:
  - study: X tasks
  - exercise: X tasks
  ...
==================================================
```

---

### 7. **TestStatistics**
Tests detailed statistics calculation.

**Tests:**
- `test_get_statistics_returns_dict` - Returns dictionary
- `test_statistics_keys_present` - All keys present
- `test_average_tasks_per_day` - Calculate daily average
- `test_oldest_task_age` - Calculate task age

**Statistics Provided:**
```python
{
    "average_tasks_per_day": float,
    "most_productive_category": str,
    "oldest_task_age_days": int
}
```

---

### 8. **TestIntegration**
Integration tests for complete workflows.

**Tests:**
- `test_full_workflow` - Complete end-to-end workflow
- `test_multiple_categories_analysis` - Multi-category analysis
- `test_persistent_history_across_operations` - History persistence

---

## Running Tests

### Run All Tests
```bash
pytest tests/test_ai_engine.py -v
```

### Run Specific Test Class
```bash
pytest tests/test_ai_engine.py::TestNLPTaskExtraction -v
```

### Run Specific Test
```bash
pytest tests/test_ai_engine.py::TestNLPTaskExtraction::test_extract_task_basic -v
```

### Run with Coverage
```bash
pytest tests/test_ai_engine.py --cov=src/task_manager.ai_engine --cov-report=html
```

### Run All Task Manager Tests (including AI Engine)
```bash
pytest tests/ -v
```

---

## Test Statistics

| Metric | Value |
|--------|-------|
| Total Tests | 50+ |
| Test Classes | 8 |
| Lines of Test Code | 400+ |
| Coverage Goal | >95% |
| Comments | English |

---

## Example Usage

### Basic Usage
```python
from src.task_manager import AIEngine

# Initialize engine
engine = AIEngine()

# Extract task from natural language
task, category = engine.extract_task_from_text(
    "I need to study Python tomorrow"
)
print(f"Task: {task}")
print(f"Category: {category}")
# Output:
# Task: study python
# Category: study

# Add to history
engine.add_task_to_history(task, category)

# Get suggestions
suggestions = engine.get_suggestions([])
print(f"Suggestions: {suggestions}")

# Get productivity analysis
analysis = engine.analyze_productivity()
print(f"Completion rate: {analysis['completion_rate']}%")

# Get report
report = engine.get_productivity_report()
print(report)
```

### NLP Examples
```python
# Study category
task, cat = engine.extract_task_from_text("Learn JavaScript")
# → ("learn javascript", "study")

# Work category
task, cat = engine.extract_task_from_text("Code a new feature")
# → ("code new feature", "work")

# Exercise category
task, cat = engine.extract_task_from_text("Go for a run")
# → ("run", "exercise")

# Shopping category
task, cat = engine.extract_task_from_text("I need to buy groceries")
# → ("buy groceries", "shopping")
```

---

## Key Features Tested

✅ **NLP Task Extraction**
- Keyword-based category detection
- Stopword removal
- Punctuation cleaning
- Multiple language patterns

✅ **Task Management**
- History tracking with timestamps
- Completion status
- Task matching (case-insensitive)

✅ **Intelligent Suggestions**
- Frequency-based ranking
- Duplicate prevention
- Category prioritization

✅ **Productivity Analytics**
- Completion rates
- Category distribution
- Task statistics
- Historical trends

✅ **Robustness**
- Type validation
- Empty input handling
- Error cases
- Edge conditions

---

## CI/CD Integration

Add to your CI pipeline:

```bash
# Run AI Engine tests
pytest tests/test_ai_engine.py -v --cov=src/task_manager.ai_engine

# Lint AI Engine code
flake8 src/task_manager/ai_engine.py

# Type check
mypy src/task_manager/ai_engine.py
```

---

## Debugging Tips

### Print Statement Debugging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
pytest tests/test_ai_engine.py -v -s
```

### Run Single Test with Output
```bash
pytest tests/test_ai_engine.py::TestNLPTaskExtraction::test_extract_task_basic -v -s
```

### Generate Coverage Report
```bash
pytest tests/test_ai_engine.py --cov=src/task_manager.ai_engine --cov-report=html
open htmlcov/index.html
```

---

## Next Steps

1. **Run all tests to verify installation**
   ```bash
   pytest tests/test_ai_engine.py -v
   ```

2. **Integrate AI Engine into CLI**
   - Add NLP input option to `src/task_manager/cli.py`
   - Add suggestion command to menu
   - Add productivity report command

3. **Enhance with external AI**
   - OpenAI API integration
   - Claude API integration
   - Local LLM (Ollama)

4. **Add persistence**
   - SQLite database for task history
   - JSON export/import
   - Data backup

---

## Related Files

- **Implementation:** `src/task_manager/ai_engine.py` (400+ lines)
- **Tests:** `tests/test_ai_engine.py` (400+ lines)
- **Exports:** `src/task_manager/__init__.py`
- **Main:** `main.py`

---

**Last Updated:** 2025-01-07  
**Version:** 2.1.0  
**Status:** ✅ Fully Tested
