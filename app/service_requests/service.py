from datetime import datetime

from sqlalchemy.orm import Session

from ..models import ServiceRequest


VALID_PRIORITIES = {
    "Low",
    "Medium",
    "High",
    "Critical"
}


VALID_STATUSES = {
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
}


def create_service_request(
    db: Session,
    request_data: dict
):

    priority = request_data.get(
        "priority",
        "Medium"
    )

    if priority not in VALID_PRIORITIES:
        return None, "Invalid priority"

    request = ServiceRequest(
        title=request_data["title"],
        description=request_data["description"],
        priority=priority,
        status="Open",
        assigned_employee_id=request_data.get(
            "assigned_employee_id"
        ),
        source=request_data.get("source"),
        related_error=request_data.get(
            "related_error"
        ),
        created_at=datetime.now().isoformat(
            sep=" ",
            timespec="seconds"
        )
    )

    db.add(request)
    db.commit()
    db.refresh(request)

    return request, None


def get_all_service_requests(
    db: Session
):
    return (
        db.query(ServiceRequest)
        .order_by(ServiceRequest.id.desc())
        .all()
    )


def get_service_request(
    db: Session,
    request_id: int
):
    return (
        db.query(ServiceRequest)
        .filter(ServiceRequest.id == request_id)
        .first()
    )


def update_service_request(
    db: Session,
    request_id: int,
    update_data: dict
):

    request = get_service_request(
        db,
        request_id
    )

    if not request:
        return None, "Service request not found"

    if (
        update_data.get("priority")
        and update_data["priority"]
        not in VALID_PRIORITIES
    ):
        return None, "Invalid priority"

    if (
        update_data.get("status")
        and update_data["status"]
        not in VALID_STATUSES
    ):
        return None, "Invalid status"

    if update_data.get("status"):
        request.status = update_data["status"]

    if update_data.get("priority"):
        request.priority = update_data["priority"]

    if update_data.get(
        "assigned_employee_id"
    ):
        request.assigned_employee_id = (
            update_data[
                "assigned_employee_id"
            ]
        )

    db.commit()
    db.refresh(request)

    return request, None


def search_service_requests(
    db: Session,
    status: str | None = None,
    priority: str | None = None
):

    query = db.query(ServiceRequest)

    if status:
        query = query.filter(
            ServiceRequest.status == status
        )

    if priority:
        query = query.filter(
            ServiceRequest.priority == priority
        )

    return (
        query
        .order_by(ServiceRequest.id.desc())
        .all()
    )