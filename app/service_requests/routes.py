from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import (
    ServiceRequestCreate,
    ServiceRequestUpdate,
    ServiceRequestResponse
)

from .service import (
    create_service_request,
    get_all_service_requests,
    get_service_request,
    update_service_request,
    search_service_requests
)


router = APIRouter(
    prefix="/service-requests",
    tags=["Service Requests"]
)


@router.post(
    "/",
    response_model=ServiceRequestResponse
)
def create_request(
    request: ServiceRequestCreate,
    db: Session = Depends(get_db)
):

    created_request, error = (
        create_service_request(
            db,
            request.model_dump()
        )
    )

    if error:
        raise HTTPException(
            status_code=400,
            detail=error
        )

    return created_request


@router.get(
    "/",
    response_model=list[ServiceRequestResponse]
)
def list_requests(
    db: Session = Depends(get_db)
):
    return get_all_service_requests(db)


@router.get(
    "/search",
    response_model=list[ServiceRequestResponse]
)
def search_requests(
    status: str | None = None,
    priority: str | None = None,
    db: Session = Depends(get_db)
):

    return search_service_requests(
        db,
        status,
        priority
    )


@router.get(
    "/{request_id}",
    response_model=ServiceRequestResponse
)
def get_request(
    request_id: int,
    db: Session = Depends(get_db)
):

    request = get_service_request(
        db,
        request_id
    )

    if not request:
        raise HTTPException(
            status_code=404,
            detail="Service request not found"
        )

    return request


@router.put(
    "/{request_id}",
    response_model=ServiceRequestResponse
)
def update_request(
    request_id: int,
    update: ServiceRequestUpdate,
    db: Session = Depends(get_db)
):

    updated_request, error = (
        update_service_request(
            db,
            request_id,
            update.model_dump(
                exclude_unset=True
            )
        )
    )

    if error:
        raise HTTPException(
            status_code=404
            if error == "Service request not found"
            else 400,
            detail=error
        )

    return updated_request