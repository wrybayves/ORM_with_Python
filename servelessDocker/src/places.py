#!/usr/bin/env python

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship 
from base import Base

class places(Base):
    __tablename__="places"

    id = Column(Integer, primary_key=True)
    city = Column(String, primary_key=True)
    county = Column(String)
    country = Column(String)
    people = relationship('people', back_populates="places")

    def __init__(self, city, county, country):
        self.city = city
        self.county = county
        self.country = country

    def __repr__(self):
        return f"<places(gname={self.city}, fname={self.county}, dob={self.country})>"
