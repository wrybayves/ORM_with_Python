from sqlalchemy import Column, String, Integer, ForeignKey
from common.base import Base

class mobile(Base):
    __tablename__='mobile'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    number = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    def __init__(sefl, model, number, owner):
        sefl.model = model
        sefl.number = number
        sefl.owner = owner