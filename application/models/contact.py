# coding: utf-8
from datetime import datetime
from ._base import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=False)
    phone = db.Column(db.String(50), nullable=False, unique=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Contact %s>' % self.name
