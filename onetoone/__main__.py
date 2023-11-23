from mobile import mobile
from user import users
from common.base import session_factory

def populate_database():
    session = session_factory()

    bruno = users("Bruno Krebs")
    john = users("John Doe")

    brunos_mobile = mobile("android", "99991111", bruno)
    johns_mobile = mobile("iphone", "55554444", john)

    session.add(brunos_mobile)
    session.add(johns_mobile)

    session.commit()
    session.close()

def query_users():
    session = session_factory()
    users_query = session.query(users)
    session.close()
    return users_query.all()

def query_mobile():
    session = session_factory()
    mobile_query = session.query(mobile)
    session.close()
    return mobile_query.all()

if __name__ == "__main__":
    user = query_users()
    if len(user) == 0:
        populate_database()
    
    user = query_users()
    for user in user:
        print(f'{user.name} has an {user.mobile.model} with number {user.mobile.number}')