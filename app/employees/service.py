import csv
import json

from sqlalchemy.orm import Session

from ..models import Employee
from .validator import validate_employee


def create_employee(db: Session, employee_data: dict):

    errors = validate_employee(employee_data)

    if errors:
        return None, errors

    # Check duplicate employee ID
    existing_employee = (
        db.query(Employee)
        .filter(Employee.employee_id == employee_data["employee_id"])
        .first()
    )

    if existing_employee:
        return None, ["Duplicate employee ID"]

    # Check duplicate email
    existing_email = (
        db.query(Employee)
        .filter(Employee.email == employee_data["email"])
        .first()
    )

    if existing_email:
        return None, ["Duplicate email"]

    employee = Employee(
        employee_id=employee_data["employee_id"],
        name=employee_data["name"],
        email=employee_data["email"],
        department=employee_data["department"],
        role=employee_data["role"],
        phone=employee_data.get("phone")
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee, []


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee_by_id(db: Session, employee_id: str):
    return (
        db.query(Employee)
        .filter(Employee.employee_id == employee_id)
        .first()
    )


def search_employees(db: Session, keyword: str):
    return (
        db.query(Employee)
        .filter(
            (Employee.name.ilike(f"%{keyword}%"))
            | (Employee.email.ilike(f"%{keyword}%"))
            | (Employee.department.ilike(f"%{keyword}%"))
            | (Employee.role.ilike(f"%{keyword}%"))
        )
        .all()
    )


def import_employees_from_file(
    db: Session,
    file_path: str
):
    imported = 0
    skipped = 0
    errors = []

    if file_path.endswith(".csv"):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row_number, row in enumerate(
                reader,
                start=2
            ):

                employee, employee_errors = create_employee(
                    db,
                    row
                )

                if employee_errors:
                    skipped += 1

                    errors.append({
                        "row": row_number,
                        "errors": employee_errors
                    })

                else:
                    imported += 1

    elif file_path.endswith(".json"):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            employees = json.load(file)

            for index, employee_data in enumerate(
                employees,
                start=1
            ):

                employee, employee_errors = create_employee(
                    db,
                    employee_data
                )

                if employee_errors:
                    skipped += 1

                    errors.append({
                        "record": index,
                        "errors": employee_errors
                    })

                else:
                    imported += 1

    else:
        raise ValueError(
            "Only CSV and JSON files are supported"
        )

    return {
        "imported": imported,
        "skipped": skipped,
        "errors": errors
    }