from backend.db.models import User


def test_create_a_user(client, db_session):
    username = "test"
    password = "test"
    email = "email@email.com"
    data = {"username": username, "password": password, "email": email}
    r = client.post('/user/create', json=data)
    created_user = db_session.query(User).first()
    assert created_user.username == username
    assert created_user.check_password(password)
    assert created_user.email == email


def test_get_me(client, db_session, normal_user_token):
    r = client.get("/user/me/", headers=normal_user_token)
    r_json = r.json()
    assert r.status_code == 200
    assert r_json['username'] == "test"
    assert r_json['email'] == "test@test.com"


def test_token(client, normal_user_token):
    data = {
        "username": "testuser",
        "password": "testpassword",
        "email": "tests@test.com"
    }
    test_user = client.post('/user/create', json=data)
    r = client.post("/token", data=data)
    r_json = r.json()
    assert test_user.status_code == 200
    assert r.status_code == 200
    # assert  == 'application/json'
