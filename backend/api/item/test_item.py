

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
