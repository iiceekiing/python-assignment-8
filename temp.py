import datetime

class AttendanceRegister:
    def __init__(self):
        """
        Constructor method that initializes the main dictionary to store
        all students' attendance records.
        Example structure:
        {
            "Alice": {"present_days": ["2025-09-03"], "absent_days": []},
            "Bob":   {"present_days": [], "absent_days": ["2025-09-03"]}
        }
        """
        self.attendance_records = {}

    def register_student(self, student_name):
        """
        Registers a student in the attendance register.
        Each student starts with empty present_days and absent_days lists.
        """
        if student_name not in self.attendance_records:
            self.attendance_records[student_name] = {
                "present_days": [],
                "absent_days": []
            }
        else:
            print(f"Student '{student_name}' is already registered.")

    def mark_present(self, student_name):
        """
        Marks the student as present for today's date.
        If the student was previously marked absent, remove that record.
        """
        today_date = str(datetime.date.today())
        if student_name in self.attendance_records:
            if today_date not in self.attendance_records[student_name]["present_days"]:
                self.attendance_records[student_name]["present_days"].append(today_date)

            # If mistakenly marked absent, remove from absent_days
            if today_date in self.attendance_records[student_name]["absent_days"]:
                self.attendance_records[student_name]["absent_days"].remove(today_date)
        else:
            print(f"Student '{student_name}' is not registered.")

    def mark_absent(self, student_name):
        """
        Marks the student as absent for today's date.
        If the student was previously marked present, remove that record.
        """
        today_date = str(datetime.date.today())
        if student_name in self.attendance_records:
            if today_date not in self.attendance_records[student_name]["absent_days"]:
                self.attendance_records[student_name]["absent_days"].append(today_date)

            # If mistakenly marked present, remove from present_days
            if today_date in self.attendance_records[student_name]["present_days"]:
                self.attendance_records[student_name]["present_days"].remove(today_date)
        else:
            print(f"Student '{student_name}' is not registered.")

    def get_status(self, student_name):
        """
        Checks if the student is marked as present or absent today.
        Returns 'Present', 'Absent', or 'Not marked'.
        """
        today_date = str(datetime.date.today())
        if student_name in self.attendance_records:
            student_record = self.attendance_records[student_name]
            if today_date in student_record["present_days"]:
                return "Present"
            elif today_date in student_record["absent_days"]:
                return "Absent"
            else:
                return "Not marked"
        else:
            return f"Student '{student_name}' is not registered."

    def show_register(self):
        """
        Returns the complete attendance register dictionary.
        """
        return self.attendance_records
   