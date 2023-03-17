import csv
import re


class PhoneBook:
    def __init__(self, file_path, file_path_new_book):
        self.__file_path = file_path
        self.__file_path_new_book = file_path_new_book
        self.__data = []
        self.__correct_data = []

        with open(self.__file_path, encoding='utf-8') as file:
            self.__data = list(csv.reader(file))

    def __format_file(self):
        name_patt = r'([А-Я]\w+)[ ,]([А-Я]\w+)[ ,](([А-Я]\w+((вич)|(вна))))?,{1,3}'
        name_patt2 = r'([А-Я]\w+)[ ,]([А-Я]\w+)[ ,](([А-Я]\w+((вич)|(вна))))?,{1,3}(,{2})'
        phone_pattern = r'((\+7)|(8))\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d{2}\s?)(\(?(доб\.) (\d{4})\)?)?'

        result = []
        for contact in self.__data:
            contact = ','.join(contact)

            fullname1 = re.search(name_patt, contact)
            fullname2 = re.search(name_patt2, contact)
            if fullname1:
                contact = re.sub(name_patt, r'\1,\2,\3,', contact)
            if fullname2:
                contact = re.sub(name_patt2, r'\1,\2,\3,\8,', contact)

            phone = re.search(phone_pattern, contact)
            if phone:
                contact = re.sub(phone_pattern, r'+7(\4)\5-\6-\7\9\10', contact)

            result.append(contact.split(','))

        self.__data = result

    def __merge_duplicates(self):
        merge = [self.__data[0]]

        for contact in self.__data[1:]:
            lastname, firstname, surname = contact[0], contact[1], contact[2]
            organization, position = contact[3], contact[4]
            phone, email = contact[5], contact[6]

            for column in self.__data[1:]:
                if column[0] == lastname and column[1] == firstname:
                    if surname == '' and column[2] != '':
                        contact[2] = column[2]
                    if organization == '' and column[3] != '':
                        contact[3] = column[3]
                    if position == '' and column[4] != '':
                        contact[4] = column[4]
                    if phone == '' and column[5] != '':
                        contact[5] = column[5]
                    if email == '' and column[6] != '':
                        contact[6] = column[6]

            if contact[:7] not in merge:
                merge.append(contact[:7])

        self.__correct_data = merge

    def repair_phone_book(self):
        self.__format_file()
        self.__merge_duplicates()

        with open(self.__file_path_new_book, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(self.__correct_data)


if __name__ == "__main__":
    book = PhoneBook(file_path='phonebook_raw.csv', file_path_new_book='phonebook.csv')

    book.repair_phone_book()
