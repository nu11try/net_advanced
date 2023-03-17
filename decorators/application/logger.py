import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            with open(path, 'a') as log_file:
                log_file.write(f'Дата и время вызова функции: {datetime.datetime.now()}\n')
                log_file.write(f'Имя функции: {old_function.__name__}\n')
                log_file.write(f'Аргументы функции: args={args}, kwargs={kwargs}\n')
                result = old_function(*args, **kwargs)
                log_file.write(f'Возвращаемое значение: {result}\n')
            return result

        return new_function

    return __logger
