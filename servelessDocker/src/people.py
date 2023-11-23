#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class people(Base):
    __tablename__='people'
    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)
    date_of_birth = Column(Date)
    place_of_birth = Column(String, ForeignKey('places.city'))
    places = relationship('places', back_populates='people')

    def __init(self, given_name, family_name, date_of_birth, place_of_birth):
        self.given_name = given_name
        self.family_name = family_name
        self.date_of_birth = date_of_birth
        self.place_of_birth = place_of_birth

    def __repr__(self):
        return f"<people(gname={self.given_name}, fname={self.family_name}, dob={self.date_of_birth}, pol={self.place_of_birth})>"