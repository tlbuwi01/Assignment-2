from flask import Flask
import click
from App import create_app
from App.controllers.student_controller import create_student, get_all_students, get_student_by_id
from App.controllers.staff_controller import create_staff, confirm_hours
from App.controllers.hours_controller import log_hours
from App.controllers.accolade_controller import award_accolade

app= create_app()    

@click.group()
def cli():
    """Student Incentive System CLI"""
    pass

@cli.command()
@click.argument('name')    
def add_student(name):
    """Add a new student"""
    with app.app_context():
        s= create_student(name)    
        print(f"Student {s.name} added with ID {s.studentID}")    


@cli.command()    
def list_students():
    """List all students"""    
    with app.app_context():    
        students= get_all_students()    
        for s in students:    
            print(f"{s.studentID}: {s.name} - {s.totalHours} hours")


@cli.command()    
@click.argument('studentID', type=int)
@click.argument('amount', type=int)    
@click.option('--description', default="", help='Description of the hours')
def log_student_hours(studentID, amount, description):
    """Log hours for a student"""    
    with app.app_context():
        record = log_hours(studentID, amount, description)
        if record:
            print(f"Logged {amount} hours for student {studentID}")
        else:
            print(f"Student {studentID} not found")


@cli.command()
@click.argument("studentID", type=int)
def view_student_accolades(studentID):
    """View accolades for a student"""
    with app.app_context():
        student = get_student_by_id(studentID)
        if student:
            if not student.accolades:
                print(f"No accolades for student {student.name}")
            else:
                print(f"Accolades for student {student.name}:")
                for accolade in student.accolades:
                    print(f"{accolade.title}: {accolade.hoursNeeded} hours needed")
        else:
            print(f"Student {studentID} not found")


@cli.command()
@click.argument('name')    
def add_staff(name):
    """Add a new staff member"""
    with app.app_context():
        s= create_staff(name)
        print(f"Staff {s.name} added with ID {s.staffID}")

@cli.command()
@click.argument("staffID", type=int)    
@click.argument("recordID", type=int)    
def confirm_staff_hours(staffID, recordID):
    """Confirm hours for a student by a staff member"""
    with app.app_context():
        success = confirm_hours(recordID, staffID)    
        if success:
            print(f"Hours confirmed by staff {staffID}")    
        else:
            print(f"Failed to confirm hours for record {recordID}. Or already confirmed")  


@cli.command()
def view_leaderboard():
    """View the leaderboard of students by total hours"""
    with app.app_context():
        students = sorted(get_all_students(), key=lambda x: x.totalHours, reverse=True)

        print("~~~~Student Leaderboard~~~~")
        for s in students:
            print(f"{s.name}: {s.totalHours} hours")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    cli()
