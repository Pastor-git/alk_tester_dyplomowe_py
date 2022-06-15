from faker import Faker
import random


class TestData:

    def __init__(self):
        fake = Faker()
        self.login = fake.login()
        self.password = fake.password()
        self.email = fake.email()

