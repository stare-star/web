'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: ent.py
@time: 2020-03-16 20:30
@desc:
'''
from collections import Counter

from app.models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class entResult(Base):
    __tablename__ = 'ent5_copy1'

    entname = Column(String(255), primary_key=True, nullable=False)
    label = Column(String(255), unique=False, nullable=False)
    clu_num = Column(String(255), unique=False, nullable=False)
    class_num = Column(Integer(), nullable=False)

    # def __init__(self, nickname, email, password, phone_number=None):
    #     self.nickname = nickname
    #     self._password = generate_password_hash(password)
    #     self.email = email
    #     self.phone_number = phone_number
    #     super(User, self).__init__()

    # @property
    # def label(self):
    #     return self.label

    # @label.setter
    # def password(self, label):
    #     self.label = label
    @property
    def summary(self):
        return dict(
            entname=self.entname,
            label=self.label,
        )

    def get_pie(self):
        ents = entResult.query.filter_by(status=1).all()
        type_list = [i.label for i in ents]
        type_c = Counter(type_list)
        names = []
        values = []

        for k, v in type_c.items():
            names.append(k)
            values.append(v)
        return  values, names
