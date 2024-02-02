from typing import List

from pydantic import BaseModel, EmailStr


class Person(BaseModel):
    full_name: str | None = None
    firstname: str | None = None
    lastname: str | None = None
    age: int | None = None
    salary: int | None = None
    department: str | None = None
    email: EmailStr | None = None
    current_address: str | None = None
    permanent_address: str | None = None
    mobile: str | None = None


class Color(BaseModel):
    color_name:  List[str] | None = None


class Date(BaseModel):
    day: str | None = None
    month: str | None = None
    year: str | None = None
    time: str | None = None
