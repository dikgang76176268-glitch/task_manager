import sys

sys.path.insert(0, ".")
import pytest
from grade_manager import GradeManager


@pytest.fixture
def fresh_manager():
    return GradeManager()


@pytest.fixture
def populated():
    m = GradeManager()
    m.add_student("Zoe", grades=[100, 95])
    m.add_student("Mark", grades=[60, 59])
    m.add_student("Nina", grades=[60])
    m.add_student("Omar", grades=[])
    return m


def test_average_single_grade(fresh_manager):
    fresh_manager.add_student("Solo", grades=[75])
    assert fresh_manager.get_average("Solo") == 75.0


def test_average_decimal_result(fresh_manager):
    fresh_manager.add_student("Dec", grades=[1, 2])
    assert fresh_manager.get_average("Dec") == 1.5


def test_average_empty_list_returns_zero(fresh_manager):
    fresh_manager.add_student("Empty", grades=[])
    assert fresh_manager.get_average("Empty") == 0.0


def test_average_nonexistent_returns_zero(populated):
    assert populated.get_average("Ghost") == 0.0


def test_passing_exact_boundary(populated):
    result = populated.get_passing_students()
    assert "Nina" in result


def test_passing_below_boundary_excluded(populated):
    result = populated.get_passing_students()
    assert "Mark" not in result


def test_passing_empty_list(populated):
    result = populated.get_passing_students()
    assert "Omar" not in result


def test_passing_custom_threshold_high(populated):
    result = populated.get_passing_students(threshold=90)
    assert "Zoe" in result and "Nina" not in result


def test_report_returns_multiline_string(fresh_manager):
    fresh_manager.add_student("Line", grades=[50, 60])
    report = fresh_manager.format_report("Line")
    assert "\n" in report


def test_report_includes_average_line(fresh_manager):
    fresh_manager.add_student("AvgCheck", grades=[80, 80])
    report = fresh_manager.format_report("AvgCheck")
    assert "Average:" in report


def test_report_nonexistent_student(fresh_manager):
    report = fresh_manager.format_report("NoName")
    assert report == "Student 'NoName' not found"


def test_report_grades_comma_separated(fresh_manager):
    fresh_manager.add_student("Sep", grades=[10, 20, 30])
    report = fresh_manager.format_report("Sep")
    assert "10, 20, 30" in report
