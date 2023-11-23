from datetime import date 
from person import person
from common.base import session_factory

def create_people():
    session = session_factory()
    bruno = person("BrunoKrebs", date(1984, 10, 20), 182, 84.5)
    john = person("John Doe", date(1990, 5, 17), 173, 90)
    session.add(bruno)
    session.add(john)
    session.commit()
    session.close()

def get_people():
    session = session_factory()
    people_query = session.query(person)
    session.close()
    return people_query.all()


if __name__ == "__main__":
    people = get_people()
    if len(people) == 0:
        create_people()
    people = get_people()

    for person in people:
        print(f'{person.name} was born in {person.dob}')