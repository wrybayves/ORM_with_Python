#!/usr/bin/env python

from people import people
from places import places
from base import structure, engine, connection
import csv

# Define the file paths for your CSV files
meta = structure.MetaData(engine)

# define places table structure
places = structure.Table('places', meta, autoload=True, autoload_with=engine)
# read the CSV data file into the table
with open('data/places.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader:
    connection.execute(places.insert().values(city = row[0]),county = row[1], country = row[2])

# define people table structure
people = structure.Table('people', meta, autoload=True, autoload_with=engine)
# read the CSV data file into the table
with open('data/people.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader:
    connection.execute(people.insert().values(given_name = row[0]),family_name = row[1], date_of_birth = row[2], place_of_birth = row[3])

