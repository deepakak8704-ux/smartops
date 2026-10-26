import time
import requests

from sqlalchemy.orm import Session

from ..models import APIMonitorResult, ServiceRequest


def create_failure_service_request(
    db: Session,
    endpoint: str,
    error_message: str
):
    request = ServiceRequest(
        title="External API failure",
        description=(
            f"API monitoring detected a failure "
            f"for endpoint: {endpoint}"
        ),
        priority="High",
        status="Open",
        assigned_employee_id=None,
        source="API Monitoring",
        related_error=error_message,
        created_at=time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    db.add(request)

    return request


def monitor_api(
    db: Session,
    endpoint: str,
    timeout: int = 5
):

    start_time = time.perf_counter()

    try:

        response = requests.get(
            endpoint,
            timeout=timeout
        )

        end_time = time.perf_counter()

        response_time = round(
            end_time - start_time,
            3
        )

        if response.status_code >= 400:

            error_message = (
                f"HTTP {response.status_code}"
            )

            result = APIMonitorResult(
                endpoint=endpoint,
                status_code=response.status_code,
                status="FAILED",
                response_time=f"{response_time}s",
                error_message=error_message
            )

            db.add(result)

            create_failure_service_request(
                db,
                endpoint,
                error_message
            )

        else:

            result = APIMonitorResult(
                endpoint=endpoint,
                status_code=response.status_code,
                status="SUCCESS",
                response_time=f"{response_time}s",
                error_message=None
            )

            db.add(result)

        db.commit()
        db.refresh(result)

        return result

    except requests.exceptions.Timeout:

        end_time = time.perf_counter()

        response_time = round(
            end_time - start_time,
            3
        )

        error_message = "Request timed out"

        result = APIMonitorResult(
            endpoint=endpoint,
            status_code=None,
            status="FAILED",
            response_time=f"{response_time}s",
            error_message=error_message
        )

        db.add(result)

        create_failure_service_request(
            db,
            endpoint,
            error_message
        )

        db.commit()
        db.refresh(result)

        return result

    except requests.exceptions.RequestException as error:

        end_time = time.perf_counter()

        response_time = round(
            end_time - start_time,
            3
        )

        error_message = str(error)

        result = APIMonitorResult(
            endpoint=endpoint,
            status_code=None,
            status="FAILED",
            response_time=f"{response_time}s",
            error_message=error_message
        )

        db.add(result)

        create_failure_service_request(
            db,
            endpoint,
            error_message
        )

        db.commit()
        db.refresh(result)

        return result