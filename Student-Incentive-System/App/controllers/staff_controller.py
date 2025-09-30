from App.models.staff import Staff
from App.database import db
from App.models.hours_recorded import HoursRecorded

def create_staff(name):
    staff = Staff(name=name)  
    db.session.add(staff)
    db.session.commit()  
    return staff

def confirm_hours(recordId, staffID):
    staff = Staff.query.get(staffID)  
    record = HoursRecorded.query.get(recordId)
    if staff and not record.confirmed:
        record.confirmed = True
        record.staffID = staffID
        record.student.totalHours += record.amount
        db.session.commit()
        return True  
        return False  
      
    