from backend.db.models import User


def test_create_a_user(client, db_session):
    username = "test"
    password = "test"
    email = "email@email.com"
    data = {"username": username, "password": password, "email": email}
    r = client.post('/user/create', json=data)
    created_user = db_session.query(User).first()
    print(created_user.password)
    assert created_user.username == username
    assert created_user.check_password(password)
