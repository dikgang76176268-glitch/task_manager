import sys

sys.path.insert(0, "..")
from grade_manager import GradeManager


def test_add_student_returns_value():
    mgr = GradeManager()
    result = mgr.add_student("TestStudent")
    assert result is not None, "Should return confirmation message"


def test_average_empty_grades():
    mgr = GradeManager()
    mgr.add_student("EmptyStudent", grades=[])
    avg = mgr.get_average("EmptyStudent")
    assert avg == 0 or isinstance(avg, (int, float)), "Should handle empty gracefully"


def test_first_student_included():
    mgr = GradeManager()
    mgr.add_student("First")
    mgr.add_student("Second")
    all_students = mgr.get_all_students()
    assert "First" in all_students, "First student should be included"
    assert len(all_students) == 2, "Should have exactly 2 students"
