from app.models.base import db
from sqlalchemy import Column, Integer


class Test(db.Model):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    test = Column(Integer,default=1)

class Test1():
    test = 0





