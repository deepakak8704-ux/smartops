from collections import Counter
from datetime import datetime


VALID_LEVELS = {
    "INFO",
    "WARNING",
    "ERROR"
}


def parse_log_line(line: str):

    parts = line.strip().split(" ", 3)

    if len(parts) < 4:
        return None

    date_part = parts[0]
    time_part = parts[1]
    level = parts[2]
    message = parts[3]

    if level not in VALID_LEVELS:
        return None

    timestamp_text = f"{date_part} {time_part}"

    try:
        timestamp = datetime.strptime(
            timestamp_text,
            "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        return None

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }


def analyze_log_file(file_path: str):

    entries = []
    malformed = 0

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            if not line.strip():
                continue

            entry = parse_log_line(line)

            if entry is None:
                malformed += 1
            else:
                entries.append(entry)

    level_counts = Counter(
        entry["level"]
        for entry in entries
    )

    error_messages = [
        entry["message"]
        for entry in entries
        if entry["level"] == "ERROR"
    ]

    error_frequency = Counter(
        error_messages
    )

    return {
        "total_entries": len(entries),
        "valid_entries": len(entries),
        "malformed_entries": malformed,
        "info_count": level_counts["INFO"],
        "warning_count": level_counts["WARNING"],
        "error_count": level_counts["ERROR"],
        "error_frequency": dict(error_frequency),
        "entries": entries
    }