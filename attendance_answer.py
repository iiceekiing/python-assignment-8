
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


import datetime

class AttendanceRegister:

attendance = {}

def register_student(student_id, name):
    if student_id not in attendance:
        attendance[student_id] = {
            "name": name,
            "present_days": [],
            "absent_days": []
        }
    else:
        print(f"Student ID {student_id} already exists.")

def mark_present(student_ids):
    today = str(datetime.date.today())
    for student in student_ids:
        if student in attendance:
            if today not in attendance[student]["present_days"]:
                attendance[student]["present_days"].append(today)
            # remove from absent if wrongly marked
            if today in attendance[student]["absent_days"]:
                attendance[student]["absent_days"].remove(today)
        else:
            print(f"Student ID {student} not registered.")

def mark_absent(student_ids):
    today = str(datetime.date.today())
    for student in student_ids:
        if student in attendance:
            if today not in attendance[student]["absent_days"]:
                attendance[student]["absent_days"].append(today)

            if today in attendance[student]["present_days"]:
                attendance[student]["present_days"].remove(today)
        else:
            print(f"Student ID {student} not registered.")
            

def get_report(**kwargs):
    report = {}
    for student, data in attendance.items():
        if kwargs.get("only_present") and not data["present_days"]:
            continue
        if kwargs.get("only_absent") and not data["absent_days"]:
            continue
        report[student] = data
    return report



register_student("S1", "Alice")
register_student("S2", "Bob")
register_student("S3", "Charlie")

mark_present(["S1", "S2"])   # Alice & Bob present
mark_absent(["S3"])          # Charlie absent


print("Full Report:", get_report())
print("Only Present:", get_report(only_present=True))
print("Only Absent:", get_report(only_absent=True))