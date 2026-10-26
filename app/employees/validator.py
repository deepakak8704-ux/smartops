REQUIRED_FIELDS = [
    "employee_id",
    "name",
    "email",
    "department",
    "role"
]


def validate_employee(employee):
    errors = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        value = employee.get(field)

        if value is None or str(value).strip() == "":
            errors.append(f"Missing field: {field}")

    # Basic email validation
    email = employee.get("email")

    if email:
        if "@" not in email or "." not in email.split("@")[-1]:
            errors.append("Invalid email")

    return errors