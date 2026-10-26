def test_get_log_analysis(client):

    response = client.get(
        "/logs/"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_log_analysis_handles_missing_file(client):

    response = client.get(
        "/logs/nonexistent.log"
    )

    assert response.status_code in [404, 422]