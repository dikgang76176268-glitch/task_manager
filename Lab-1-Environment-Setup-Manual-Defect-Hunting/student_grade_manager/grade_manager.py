"""Student Grade Manager — Core logic for tracking and calculating student grades."""


class GradeManager:
    """Manages student records and their associated grades."""

    def __init__(self):
        """Initialize an empty student database."""
        self.students = []

    def add_student(self, name, grades=None):
        """Add a new student to the manager.
        Args:
            name: Student's full name as a string
            grades: Optional list of numeric grades (defaults to empty list)
        Returns:
            str: Confirmation message including the student's name
        """
        if grades is None:
            grades = []
        self.students.append({"name": name, "grades": grades})
        return f"Student '{name}' added successfully"

    def add_grade(self, name, grade):
        """Append a single grade to an existing student's record.
        Args:
            name: Student's name to search for
            grade: Numeric grade value to add
        Returns:
            bool: True if student found and grade added, False otherwise
        """
        for student in self.students:
            if student["name"] == name:
                student["grades"].append(grade)
                return True
        return False

    def get_average(self, name):
        """Calculate average grade for a student.
        Args:
            name: Student's name
        Returns:
            float: Average grade, 0.0 if empty/not found
        """
        for student in self.students:
            if student["name"] == name:
                if not student["grades"]:
                    return 0.0
                total = sum(student["grades"])
                return total / len(student["grades"])
        return 0.0

    def get_passing_students(self, threshold=60):
        """Return names of students whose average meets or exceeds the threshold.
        Args:
            threshold: Minimum average to be considered passing (default: 60)
        Returns:
            list[str]: Names of passing students
        """
        passing = []
        for student in self.students:
            avg = self.get_average(student["name"])
            if avg >= threshold:
                passing.append(student["name"])
        return passing

    def get_all_students(self):
        """Return a list of all registered student names.
        Returns:
            list[str]: All student names in order of addition
        """
        return [student["name"] for student in self.students]

    def format_report(self, name):
        """Generate a formatted summary report for a student.
        Args:
            name: Student's name to generate report for
        Returns:
            str: Multi-line report or "not found" message
        """
        for student in self.students:
            if student["name"] == name:
                grades_str = ", ".join(map(str, student["grades"]))
                avg = self.get_average(name)
                return f"Student: {name}\nGrades: {grades_str}\nAverage: {avg:.2f}"
        return f"Student '{name}' not found"

    def remove_student(self, name):
        """Remove a student record from the database.
        Args:
            name: Student's name to remove
        Returns:
            bool: True if found and removed, False if not found
        """
        for index, student in enumerate(self.students):
            if student["name"] == name:
                del self.students[index]
                return True
        return False
