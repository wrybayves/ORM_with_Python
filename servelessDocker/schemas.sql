-- Creation of database
CREATE SCHEMA IF NOT EXISTS ampersandDB;

-- Creation of places table
CREATE TABLE IF NOT EXISTS places (
  id serial,
  city varchar(250) PRIMARY KEY,
  county varchar(450) ,
  country varchar(450) 
);

-- Creation of people table
CREATE TABLE IF NOT EXISTS people (
  id serial,  
  given_name varchar(250),
  family_name varchar(250) ,
  date_of_birth DATE,
  place_of_birth varchar(250) REFERENCES places(city)
);

