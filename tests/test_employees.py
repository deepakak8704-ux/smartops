def test_get_employees(client):

    response = client.get(
        "/employees/"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_search_employee(client):

    response = client.get(
        "/employees/search?keyword=John"
    )

    assert response.status_code in [200, 404]


def test_employee_not_found(client):

    response = client.get(
        "/employees/999999"
    )

    assert response.status_code == 404