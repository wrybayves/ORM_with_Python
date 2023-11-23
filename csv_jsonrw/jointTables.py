#!/usr/bin/env python

from people import people
from places import places
from common.base import session_factory
import csv_loading
import json
#from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, schema
#from sqlalchemy.orm import declarative_base, Session, relationship
from sqlalchemy.sql import func
#import csv
#Base = declarative_base()
session = session_factory()
# Perform the inner join, count, and group by

csv_loading
with open ("data/summary_output.json", 'w') as json_file:
    result = (
        session.query(places.country, func.count(people.id).label('number_of_people'))
        .join(people)
        .group_by(places.country)
        .all()
    )
    #json out put results
    rows = [{'country': row[0], 'has a number of people of: ': row[1]} for row in result]
    json.dump(rows, json_file, separators=(',', ':'))

    # Print the result
    for row in result:
        print(f"This country: {row.country}, has a number of people of: {row.number_of_people}")
