from datetime import datetime
from flask import current_app
import hashlib
from app import db


class Position:
    STUDENT = 1
    MENTOR = 2
    COACH = 4
    PARENT = 8

class Team(db.Model):
    # cardid = 0014538996
    # id,last,first,position,email,cardid,status,active,timestamp
	# 1,Akishin,Hayden,1,haydenda6@outlook.com,,0,1,2023-07-03 09:48:22.891656
    # 2,Anderson,Eric,1,eander42@icloud.com,,0,1,2023-07-03 09:48:22.8916560
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    last = db.Column(db.String(64), nullable=False)
    first = db.Column(db.String(64), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    cardid = db.Column(db.String(64))
    status = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(Team, self).__init__(**kwargs)
        if self.position is None:
            self.position = 1
        if self.timestamp is None:
            self.timestamp = datetime.utcnow

    def checkin(self):
        if not self.status:
            self.status = True
            self.timestamp = datetime.utcnow()
            db.session.add(self)

    def checkout(self):
        if self.status:
            self.status = False
            self.timestamp = datetime.utcnow()
            db.session.add(self)

    def ping(self):
        self.timestamp = datetime.utcnow()
        db.session.add(self)

    def is_checked_in(self):
        return self.status == True

    def __repr__(self):
        return '<Member %r, %r>' % (self.first, self.last)
