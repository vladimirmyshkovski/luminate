# coding: utf-8
from datetime import datetime
from ._base import db
#from sqlalchemy.dialects.postgresql import JSON

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(150), nullable=False)
    size = db.Column(db.String(150))
    image = db.Column(db.String(150))
    images = db.Column(db.String(350))
    specials = db.Column(db.String(350))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "'%s'" % self.name
