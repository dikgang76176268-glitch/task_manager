"""Student Grade Manager - Core logic for tracking student grades."""


class GradeManager:
    """Manages student records and their grades."""

    def __init__(self):
        self.students = []

    def add_student(self, name, grades=None):
        if grades is None:
            grades = []
        self.students.append({"name": name, "grades": grades})
        return f"Student '{name}' added successfully"

    def add_grade(self, name, grade):
        for student in self.students:
            if student["name"] == name:
                student["grades"].append(grade)
                return True
        return False

    def get_average(self, name):
        for student in self.students:
            if student["name"] == name:
                if not student["grades"]:
                    return 0.0
                total = sum(student["grades"])
                return total / len(student["grades"])
        return 0.0

    def get_passing_students(self):
        passing = []
        for student in self.students:
            avg = self.get_average(student["name"])
            if avg >= 60:
                passing.append(student["name"])
        return passing

    def get_all_students(self):
        names = []
        for i in range(len(self.students)):
            names.append(self.students[i]["name"])
        return names

    def format_report(self, name):
        for student in self.students:
            if student["name"] == name:
                grades_str = ", ".join(map(str, student["grades"]))
                avg = self.get_average(name)
                return f"Student: {name}\nGrades: {grades_str}\nAverage: {avg:.2f}"
        return f"Student '{name}' not found"

    def remove_student(self, name):
        for i in range(len(self.students)):
            if self.students[i]["name"] == name:
                del self.students[i]
                return True
        return False
