from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import APIMonitorResponse
from .service import monitor_api
from ..models import APIMonitorResult

router = APIRouter(
    prefix="/monitor",
    tags=["API Monitoring"]
)


@router.post(
    "/",
    response_model=APIMonitorResponse
)
def monitor_endpoint(
    endpoint: str,
    db: Session = Depends(get_db)
):

    if not endpoint.startswith(
        ("http://", "https://")
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid URL"
        )

    result = monitor_api(
        db,
        endpoint
    )

    return result

@router.get(
    "/",
    response_model=list[APIMonitorResponse]
)
def get_monitor_results(
    db: Session = Depends(get_db)
):
    return (
        db.query(APIMonitorResult)
        .order_by(APIMonitorResult.id.desc())
        .all()
    )