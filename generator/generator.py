import random
from faker import Faker
from data.data import Person, Color, Date


faker_ua = Faker('uk_UA')
fake_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ua.first_name() + " " + faker_ua.last_name(),
        firstname=faker_ua.first_name(),
        lastname=faker_ua.last_name(),
        #middle_name=faker_ua.middle_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ua.job(),
        email=faker_ua.email(),
        current_address=faker_ua.address(),
        permanent_address=faker_ua.address(),
        mobile=faker_ua.msisdn(),
    )


def generated_file():
    path = rf'C:\Users\User\Desktop\example\automation\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=fake_en.year(),
        month=fake_en.month_name(),
        day=fake_en.day_of_month(),
        time="12:00"
    )