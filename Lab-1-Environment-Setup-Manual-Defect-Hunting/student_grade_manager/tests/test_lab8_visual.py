import sys
sys.path.insert(0, '.')
import pytest
from grade_manager import GradeManager

@pytest.fixture
def mgr():
    return GradeManager()

def test_add_student_message_format(mgr):
    msg = mgr.add_student("Zoe", grades=[75, 80])
    expected = "Student 'Zoe' added successfully"
    assert msg == expected, f"Format changed! Got: {msg!r}"

def test_format_report_structure(mgr):
    mgr.add_student("Bob", grades=[80, 90])
    report = mgr.format_report("Bob")
    expected = "Student: Bob\nGrades: 80, 90\nAverage: 85.00"
    assert report == expected, f"Structure changed!\nGot:\n{report}\nExpected:\n{expected}"

def test_not_found_message_format(mgr):
    report = mgr.format_report("Unknown")
    assert report == "Student 'Unknown' not found"

def test_passing_students_list_accuracy(mgr):
    mgr.add_student("Pass", grades=[70])
    mgr.add_student("Fail", grades=[40])
    result = mgr.get_passing_students()
    assert "Pass" in result
    assert "Fail" not in result
    assert len(result) == 1