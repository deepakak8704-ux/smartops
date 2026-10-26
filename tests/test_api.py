def test_root_endpoint(client):

    response = client.get("/")

    assert response.status_code == 200


def test_openapi_endpoint(client):

    response = client.get("/openapi.json")

    assert response.status_code == 200

    data = response.json()

    assert "openapi" in data
    assert "paths" in data