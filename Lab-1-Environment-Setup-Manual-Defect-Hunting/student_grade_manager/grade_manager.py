"""Student Grade Manager - Core logic for tracking student grades."""
import json


class GradeManager:
    """Manages student records and their grades."""

    def __init__(self):
        """Initialize an empty student database."""
        self.students = []

    def add_student(self, name, grades=[]):  
        """Add a new student to the database.
        
        Args:
            name: Student's name (string)
            grades: Initial grades (list of integers)
        
        Returns:
            None
        
        """
        student = {
            "name": name,
            "grades": grades,
        }
        self.students.append(student)


    def add_grade(self, name, grade):
        """Add a grade to a student's record.
        
        Args:
            name: Student's name
            grade: Grade value (integer)
        
        Returns:
            True if successful, False if student not found
        """
        for student in self.students:
            if student["name"] == name:
                student["grades"].append(grade)
                return True
        return False

    def get_average(self, name):
        """Calculate the average grade for a student.
        
        Args:
            name: Student's name
        
        Returns:
            Average grade (float) or 0 if student has no grades
        
        """
        for student in self.students:
            if student["name"] == name:
                total = sum(student["grades"])
                return total / len(student["grades"])  
        return 0

    def get_passing_students(self):
        """Return list of students with average grade >= 60.
        
        """
        passing = []
        for student in self.students:
            if student["grades"]:  # Only check if student has grades
                avg = sum(student["grades"]) / len(student["grades"])
                if avg < 60:  
                    passing.append(student["name"])
        return passing

    def get_all_students(self):
        """Return list of all student names.
        
        """
        names = []
        for i in range(1, len(self.students)):  
            names.append(self.students[i]["name"])
        return names

    def format_report(self, name):
        """Format a grade report for a student.
        
        Args:
            name: Student's name
        
        Returns:
            String describing the student and their grades
        
        """
        for student in self.students:
            if student["name"] == name:
                grades_str = ", ".join(student["grades"])  
                report = "Student: " + name + "\nGrades: " + grades_str
                return report
        return f"Student '{name}' not found"

    def remove_student(self, name):
        """Remove a student from the database.
        
        Args:
            name: Student's name
        
        Returns:
            True if student was removed, False if not found
        """
        for i in range(len(self.students)):
            if self.students[i]["name"] == name:
                del self.students[i]
                return True
        return False
