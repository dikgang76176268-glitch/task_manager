import sys
sys.path.insert(0, '.')
import pytest
from grade_manager import GradeManager

@pytest.fixture
def mgr():
    return GradeManager()

def test_messages_clear_and_complete(mgr):
    msg = mgr.add_student("Test")
    assert len(msg) > 10
    assert "'Test'" in msg

def test_error_messages_specific(mgr):
    msg = mgr.format_report("MissingStudent")
    assert "MissingStudent" in msg
    assert "not found" in msg.lower()

def test_report_labels_clear(mgr):
    mgr.add_student("Clear", grades=[50, 60])
    report = mgr.format_report("Clear")
    assert "Student:" in report
    assert "Grades:" in report
    assert "Average:" in report

def test_numeric_values_readable(mgr):
    mgr.add_student("Precision", grades=[1, 2])
    report = mgr.format_report("Precision")
    assert "1.50" in report

def test_no_empty_feedback(mgr):
    msg = mgr.add_student("Any")
    assert msg.strip() != ""
    result = mgr.add_grade("Any", 85)
    assert result is not None