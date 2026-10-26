from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import LogEntryResponse
from .service import (
    analyze_and_store_logs,
    get_all_logs,
    get_logs_by_level
)


router = APIRouter(
    prefix="/logs",
    tags=["Application Logs"]
)


@router.post("/analyze")
def analyze_logs(
    db: Session = Depends(get_db)
):
    try:

        result = analyze_and_store_logs(
            db,
            "data/application.log"
        )

        return {
            "message": "Log analysis completed",
            "summary": {
                "total_entries": result["total_entries"],
                "malformed_entries": result["malformed_entries"],
                "info_count": result["info_count"],
                "warning_count": result["warning_count"],
                "error_count": result["error_count"]
            },
            "error_frequency": result["error_frequency"]
        }

    except FileNotFoundError:

        raise HTTPException(
            status_code=404,
            detail="Application log file not found"
        )


@router.get(
    "/",
    response_model=list[LogEntryResponse]
)
def list_logs(
    db: Session = Depends(get_db)
):
    return get_all_logs(db)


@router.get(
    "/level/{level}",
    response_model=list[LogEntryResponse]
)
def list_logs_by_level(
    level: str,
    db: Session = Depends(get_db)
):
    if level.upper() not in {
        "INFO",
        "WARNING",
        "ERROR"
    }:
        raise HTTPException(
            status_code=400,
            detail="Invalid log level"
        )

    return get_logs_by_level(
        db,
        level
    )