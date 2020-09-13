import datetime

from sqlalchemy_serializer import SerializerMixin
from app.db import db


class DemoModel(db.Model, SerializerMixin):
    __tablename__ = 'demo_model'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_at = db.Column('create_at',
                          db.DateTime,
                          default=datetime.datetime.now)
