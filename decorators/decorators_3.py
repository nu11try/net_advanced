import datetime

from application import FakerTest, Selary, People

if __name__ == '__main__':
    print(f'{datetime.datetime.now()}\n')

    Selary().calculate_salary()
    People().get_employees()

    print('\n')

    FakerTest().get_who()
    FakerTest().get_address()
