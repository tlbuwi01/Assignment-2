from App.database import db
from werkzeug.security import check_password_hash, generate_password_hash

class Staff(db.Model):
    staffID = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(120), nullable=False, unique=True) 
    password = db.Column(db.String(128), nullable=True)
    
    # The 'HoursRecorded' model uses 'staffID' as the ForeignKey
    confirmedHours = db.relationship('HoursRecorded', backref='staff', lazy=True)

    def __init__(self, name,password):
        self.name = name
        self.set_password(password)

    def __repr__(self):
        return f'<Staff {self.staffID}: {self.name}>'
    
    def to_dict(self):
        return {
            'staffID': self.staffID,
            'name': self.name,
            'confirmedHoursCount': len(self.confirmedHours)
        }
    
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    

