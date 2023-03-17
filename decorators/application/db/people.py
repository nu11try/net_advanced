from decorators.application.logger import logger


class People:
    def __init__(self):
        self.__msg = 'Test people'

    @logger('people_log.log')
    def get_employees(self):
        print(self.__msg)
