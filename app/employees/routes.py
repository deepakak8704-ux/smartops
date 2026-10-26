from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import os

from ..database import get_db
from ..schemas import EmployeeCreate, EmployeeResponse
from .service import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    search_employees,
    import_employees_from_file
)


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/", response_model=EmployeeResponse)
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    employee_data = employee.model_dump()

    created_employee, errors = create_employee(
        db,
        employee_data
    )

    if errors:
        raise HTTPException(
            status_code=400,
            detail=errors
        )

    return created_employee


@router.get("/", response_model=list[EmployeeResponse])
def list_employees(
    db: Session = Depends(get_db)
):
    return get_all_employees(db)


@router.get("/search", response_model=list[EmployeeResponse])
def search_employee(
    keyword: str,
    db: Session = Depends(get_db)
):
    return search_employees(db, keyword)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: str,
    db: Session = Depends(get_db)
):
    employee = get_employee_by_id(
        db,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.post("/import")
async def import_employees(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected"
        )

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in [".csv", ".json"]:
        raise HTTPException(
            status_code=400,
            detail="Only CSV and JSON files are supported"
        )

    temp_file = f"data/{file.filename}"

    try:
        with open(temp_file, "wb") as buffer:
            buffer.write(await file.read())

        result = import_employees_from_file(
            db,
            temp_file
        )

        return {
            "filename": file.filename,
            "message": "Employee import completed",
            "result": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Import failed: {str(error)}"
        )