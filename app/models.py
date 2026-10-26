from sqlalchemy import Column, Integer, String
from .database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)
    role = Column(String, nullable=False)
    phone = Column(String, nullable=True)

class LogEntry(Base):
    __tablename__ = "log_entries"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String, nullable=False)
    level = Column(String, nullable=False, index=True)
    message = Column(String, nullable=False)

class APIMonitorResult(Base):
    __tablename__ = "api_monitor_results"

    id = Column(Integer, primary_key=True, index=True)
    endpoint = Column(String, nullable=False)
    status_code = Column(Integer, nullable=True)
    status = Column(String, nullable=False)
    response_time = Column(String, nullable=False)
    error_message = Column(String, nullable=True)

class ServiceRequest(Base):
    __tablename__ = "service_requests"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String, nullable=False)

    priority = Column(String, nullable=False, default="Medium")

    status = Column(String, nullable=False, default="Open")

    assigned_employee_id = Column(
        String,
        nullable=True
    )

    source = Column(
        String,
        nullable=True
    )

    related_error = Column(
        String,
        nullable=True
    )

    created_at = Column(
        String,
        nullable=False
    )