from App.models import Student, HoursRecorded
from App.database import db


def add_student_hours(studentID: int, staffID: int, amount: int):
    """Record hours for a student"""
    student = Student.query.get(studentID)    
    if not student:
        return f"Student {studentID} not found"


    hours= HoursRecorded (
        studentID=studentID,
        staffID=staffID,
        amount=amount,
        confirmed=False
    )
    db.session.add(hours)
    db.session.commit()
    return f"Added {amount} hours for {studentID} pending confirmation"

def confirm_student_hours(hourID:int):
    """Confirm for a student and check accolades"""
    record = HoursRecorded.query.get(hourID)
    if not record:
        return f"Record {hourID} not found"
        if record.confirmed:
            return f"Record {hourID} already confirmed"

    record.confirmed = True
    record.student.hours_completed += record.amount

    db.session.commit()
    return f"Confirmed {record.amount} hours for {record.studentID}"