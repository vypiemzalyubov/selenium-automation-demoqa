import os
import random
from faker import Faker
from data.data import Person

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() +
        " " + faker_ru.middle_name(),
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


def generated_file():
    path = fr"{os.getcwd()}\data\text_file{random.randint(0,999)}.txt"
    with open(path, "w+") as file:
        file.write(f"Hello {random.randint(0,999)}")
    return file.name, path


def generated_subject():
    subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
                "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    return subjects[random.randint(0,13)]
