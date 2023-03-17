from decorators.application.logger import logger


class Selary:
    def __init__(self):
        self.__msg = 'Test selary'

    @logger('salary_log.log')
    def calculate_salary(self):
        print(self.__msg)
