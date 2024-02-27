import os
import random
from typing import Any
from collections.abc import Generator
from faker import Faker
from models.models import Cars, Color, Date, Person

faker_ru = Faker('ru_RU')
fake_en = Faker('En')
Faker.seed()


def generated_person() -> Generator[Person, Any, None]:
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file() -> tuple[str | Any, str]:
    path = rf'{os.getcwd()}\utils\text_file{random.randint(0, 999)}.txt'
    with open(path, 'w+') as file:
        file.write(f'Hello {random.randint(0, 999)}')
    return file.name, path


def generated_subject() -> str:
    subjects = [
        'Hindi',
        'English',
        'Maths',
        'Physics',
        'Chemistry',
        'Biology',
        'Computer Science',
        'Commerce',
        'Accounting',
        'Economics',
        'Arts',
        'Social Studies',
        'History',
        'Civics',
    ]
    return subjects[random.randint(0, 13)]


def generated_color() -> Generator[Color, Any, None]:
    yield Color(
        color_name=[
            'Red',
            'Blue',
            'Green',
            'Yellow',
            'Purple',
            'Black',
            'White',
            'Voilet',
            'Indigo',
            'Magenta',
            'Aqua',
        ]
    )


def generated_car() -> Generator[Cars, Any, None]:
    yield Cars(car_name=['Volvo', 'Saab', 'Opel', 'Audi'])


def generated_date() -> Generator[Date, Any, None]:
    yield Date(
        year=fake_en.year(), month=fake_en.month_name(), day=fake_en.day_of_month(), time='12:00'
    )


def generated_dropdown_option(dropdown: str) -> str:
    select_value = [
        'Group 1, option 1',
        'Group 1, option 2',
        'Group 2, option 1',
        'Group 2, option 2',
        'A root option',
        'Another root option',
    ]
    select_one = ['Dr.', 'Mr.', 'Mrs.', 'Ms.', 'Prof.', 'Other']
    if dropdown == 'select_value':
        return select_value[random.randint(0, 5)]
    else:
        return select_one[random.randint(0, 5)]
