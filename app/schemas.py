from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict

class EmployeeBase(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    department: str
    role: str
    phone: str | None = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )
    

class LogEntryResponse(BaseModel):
    id: int
    timestamp: str
    level: str
    message: str

    model_config = {
        "from_attributes": True
    }

class APIMonitorResponse(BaseModel):
    id: int
    endpoint: str
    status_code: int | None
    status: str
    response_time: str
    error_message: str | None

    model_config = {
        "from_attributes": True
    }

class ServiceRequestCreate(BaseModel):
    title: str
    description: str
    priority: str = "Medium"
    assigned_employee_id: str | None = None
    source: str | None = None
    related_error: str | None = None


class ServiceRequestUpdate(BaseModel):
    status: str | None = None
    priority: str | None = None
    assigned_employee_id: str | None = None


class ServiceRequestResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    assigned_employee_id: str | None
    source: str | None
    related_error: str | None
    created_at: str

    model_config = {
        "from_attributes": True
    }