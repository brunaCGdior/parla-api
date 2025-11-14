import re

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")

def is_valid_email(email: str) -> bool:
    return bool(email and EMAIL_REGEX.match(email))

def is_valid_password(password: str, min_len: int = 8) -> bool:
    return bool(password and len(password) >= min_len)

def required_fields(data: dict, fields: list):
    missing = [f for f in fields if f not in data or data.get(f) in (None, "")]
    return missing  # list empty => ok
