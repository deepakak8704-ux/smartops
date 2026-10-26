def test_get_monitor_results(client):

    response = client.get(
        "/monitor/"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)