"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""
#SOLUTION


class AttendanceRegister:
    def __init__(self):
        self.register = {}

    def mark_present(self, student_name):
        self.register[student_name] = "Present"

    def mark_absent(self, student_name):
        self.register[student_name] = "Absent"

    def get_status(self, student_name):
        return self.register.get(student_name, "No record found")

    def show_register(self):
        return self.register   
    

# Example Usage
if __name__ == "__main__":  
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}        

    