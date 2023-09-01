from faker import Faker

from models.AccountInfo import AccountInfo
from models.AddressInfo import AddressInfo
import random

from models.PersonalInfo import PersonalInfo

fake = Faker()


def get_random_personal_info():
    return PersonalInfo(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        company=fake.company(),
        mobile_number=fake.phone_number()
    )


def get_random_account_info(personal_info):
    return AccountInfo(
        title=random.choice(["Mr.", "Mrs."]),
        name=personal_info.first_name + " " + personal_info.last_name,
        email=fake.email(),
        password=fake.password(),
        dob=fake.date_of_birth(minimum_age=18, maximum_age=80)
    )


def get_random_address_info():
    return AddressInfo(
        address_line_1=fake.street_address(),
        address_line_2=fake.secondary_address(),
        country=random.choice(["United States", "Canada", "Australia", "New Zealand"]),
        state=fake.state(),
        city=fake.city(),
        zip_code=fake.zipcode(),
    )
