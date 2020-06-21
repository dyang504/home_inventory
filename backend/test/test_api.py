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
    r = client.get("/users/me/", headers=normal_user_token)
    r_json = r.json()
    assert r.status_code == 200
    assert r_json['username'] == "test"
    assert r_json['email'] == "test@test.com"


def test_create_item(client, normal_user_token):
    data = {
        "name":
        "综合果仁",
        "infos": [{
            "price": 0,
            "expiration_date": "2020-06-14T10:07:46.083Z",
            "purchase_date": "2020-06-14T10:07:46.083Z",
            "item_id": 0,
            "user_id": 0,
            "status_id": 0,
            "inventory_location_id": 0
        }],
        "nutritions": [{
            "name": "string",
            "value": 0,
            "unit": "string"
        }],
        "images": [{
            "image_url": "string"
        }],
        "category": [{
            "name": "string"
        }],
        "size": [{
            "indicator_name": "string",
            "value": 0,
            "unit": "string"
        }],
        "book_property": {
            "author": "string",
            "publisher": "string",
            "notes": "string"
        }
    }
    r = client.post('/item/create', json=data, headers=normal_user_token)
    r_json = r.json()
    print(r_json)
    assert r.status_code == 200
    assert r_json["name"] == data["name"]
