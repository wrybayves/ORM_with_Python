#!/usr/bin/env python

from sqlalchemy import create_engine, schema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://ampersandDB:password@database/ampersandDB")
connection = engine.connect()

structure = schema

_SessionFactory = sessionmaker(bind = engine)

Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
