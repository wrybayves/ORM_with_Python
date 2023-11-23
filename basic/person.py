from sqlalchemy import Column, String, Date, Integer, Numeric
from common.base import Base

class person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True,nullable=False,unique=True)
    name = Column(String)
    dob = Column(Date)
    height = Column(Integer)
    weight = Column(Numeric)

    def __init__(self, name, dob, height, weight):
        self.name = name
        self.dob = dob
        self.height = height
        self.weight = weight

