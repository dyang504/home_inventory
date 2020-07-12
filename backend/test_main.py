

def test_read_main(client):
    response = client.get('/')
    print(response.status_code)
    assert response.status_code == 200
    assert response.json() == {"message": "🏡Welcome to home inventory😀"}
