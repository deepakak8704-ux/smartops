def test_create_service_request(client):

    response = client.post(
        "/service-requests/",
        json={
            "title": "Test Service Request",
            "description": "Testing service request creation",
            "priority": "High",
            "assigned_employee_id": "EMP001",
            "source": "Test",
            "related_error": "Test error"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test Service Request"
    assert data["priority"] == "High"
    assert data["status"] == "Open"


def test_get_service_requests(client):

    response = client.get(
        "/service-requests/"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_get_service_request_not_found(client):

    response = client.get(
        "/service-requests/999999"
    )

    assert response.status_code == 404


def test_update_service_request(client):

    create_response = client.post(
        "/service-requests/",
        json={
            "title": "Update Test",
            "description": "Testing update",
            "priority": "Medium",
            "source": "Test"
        }
    )

    assert create_response.status_code == 200

    request_id = create_response.json()["id"]

    update_response = client.put(
        f"/service-requests/{request_id}",
        json={
            "status": "Resolved",
            "priority": "Critical"
        }
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["status"] == "Resolved"
    assert data["priority"] == "Critical"