from sqlalchemy.orm import Session

from ..models import LogEntry
from .analyzer import analyze_log_file


def analyze_and_store_logs(
    db: Session,
    file_path: str
):
    result = analyze_log_file(file_path)

    for entry in result["entries"]:

        log_entry = LogEntry(
            timestamp=entry["timestamp"].isoformat(
                sep=" "
            ),
            level=entry["level"],
            message=entry["message"]
        )

        db.add(log_entry)

    db.commit()

    return result


def get_all_logs(db: Session):
    return (
        db.query(LogEntry)
        .order_by(LogEntry.id.desc())
        .all()
    )


def get_logs_by_level(
    db: Session,
    level: str
):
    return (
        db.query(LogEntry)
        .filter(LogEntry.level == level.upper())
        .order_by(LogEntry.id.desc())
        .all()
    )