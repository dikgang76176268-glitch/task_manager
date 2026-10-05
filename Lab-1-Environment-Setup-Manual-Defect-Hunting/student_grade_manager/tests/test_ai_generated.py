"""Lab 5: AI-Generated Unit Tests"""

import pytest
from grade_manager import GradeManager


@pytest.fixture
def manager():
    mgr = GradeManager()
    mgr.add_student("Alice", grades=[80, 90, 70])
    mgr.add_student("Bob", grades=[50, 60, 55])
    mgr.add_student("Charlie", grades=[])
    return mgr


def test_average_returns_correct_mean(manager):
    assert manager.get_average("Alice") == 80.0


def test_average_returns_zero_for_empty_grades(manager):
    assert manager.get_average("Charlie") == 0.0


def test_average_returns_zero_for_unknown_student(manager):
    assert manager.get_average("Nobody") == 0.0


def test_passing_includes_eligible_student(manager):
    assert "Alice" in manager.get_passing_students()


def test_passing_excludes_failing_student(manager):
    assert "Bob" not in manager.get_passing_students()


def test_passing_respects_custom_threshold(manager):
    assert "Bob" in manager.get_passing_students(threshold=50)


def test_report_contains_name(manager):
    assert "Alice" in manager.format_report("Alice")


def test_report_contains_grades(manager):
    r = manager.format_report("Alice")
    assert "80" in r and "90" in r and "70" in r


def test_report_not_found_message(manager):
    assert "not found" in manager.format_report("Unknown").lower()
