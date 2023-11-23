from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from common.base import Base

class users(Base):
    __tablename__= 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mobile = relationship("mobile", uselist=False, backref="owner")

    def __init__(self, name):
        self.name = name