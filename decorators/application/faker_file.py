from faker import Faker

from decorators.application.logger import logger

fake = Faker()


class FakerTest:
    def __init__(self):
        self.__name = fake.name()
        self.__address = fake.address()

    @logger('faker_log.log')
    def get_who(self):
        print(self.__name)

    @logger('faker_log.log')
    def get_address(self):
        print(self.__address)