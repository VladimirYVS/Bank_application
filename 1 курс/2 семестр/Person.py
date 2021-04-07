from random import randint
from os import chdir, mkdir, listdir


class Name:

    def __init__(self, name, surname, patronymic, date, gender):
        self.information = {'Фамилия': surname,
                            'Имя': name,
                            'Отчество': patronymic,
                            'Дата рождения': date,
                            'Пол': gender}

    def load(self):
        return self.information

    def print_name(self):
        for key, value in self.information.items():
            print(key, value)


class Address:

    def __init__(self, country, state, city, street, house, apartment):
        if street == '-' and house == '-' and apartment == '-':
            self.information = {'Страна': country,
                                'Субъект': state,
                                'Город': city}
        else:
            self.information = {'Страна': country,
                                'Субъект': state,
                                'Город': city,
                                'Улица': street,
                                'Дом': house,
                                'Квартира': apartment}

    def load(self):
        return self.information

    def print_address(self):
        for key, value in self.information.items():
            print(key, value)


class Document:

    def __init__(self, number, series, date, issued):
        self.information = {'Номер: ': number,
                            'Серия: ': series,
                            'Выдан: ': issued,
                            'Дата выдачи': date}

    def load(self):
        return self.information

    def print_document(self):
        for key, value in self.information.items():
            print(key, value)


class Passport:

    name = Name(None, None, None, None, None)

    address_birth = Address(None, None, None, '-', '-', '-')

    passport_num = Document(None, None, None, None)

    address_post = Address(None, None, None, None, None, None)

    passport = {'Атрибуты паспорта': passport_num,
                'ФИО': name,
                'Место рождения': address_birth,
                'Адрес прописки': address_post}

    def make(self):
        print('Заполинте данные паспорта')
        print("Имя, Фамилия, Отчество")
        self.name = Name(input('Введите имя: '),
                         input('Введите Фамилию: '),
                         input('Введите Отчество(если нет то "-"): '),
                         input('Ввведите дату рождения'),
                         input('Ввведите пол'))

        print("Реквезиты паспорта")
        self.passport_num = Document(input('Введите номер паспорта: : '),
                                     input('Введите серию паспорта: '),
                                     input('Введите дату выдачи паспорта: '),
                                     input('Введите кем выдан паспорт: '))

        print("Место рождения")
        self.address_birth = Address(input('Введите Страну: '),
                                     input('Введите Субъект: '),
                                     input('Введите Город: '),
                                     '-',
                                     '-',
                                     '-')

        print("Место прописки")
        self.address_post = Address(input('Введите Страну: '),
                                    input('Введите Субъект: '),
                                    input('Введите Город: '),
                                    input('Введите Улицу: '),
                                    input('Введите Дом: '),
                                    input('Введите Квартиру: '))

        self.passport = {'Атрибуты паспорта': self.passport_num,
                         'ФИО': self.name,
                         'Место рождения': self.address_birth,
                         'Адрес прописки': self.address_post}

    def print_document(self):
        print('Реквезиты паспорта: ')
        info = self.passport_num.load()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_name(self):
        print('ФИО: ')
        info = self.name.load()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_address(self):
        print('Адрес прописки: ')
        info = self.address_post.load()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_address_birth(self):
        print('Место Рождения: ')
        info = self.address_birth.load()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_passport(self):

        self.print_document()
        self.print_name()
        self.print_address_birth()
        self.print_address()

    def safe_passport(self):
        with open('passport.txt', 'w') as passport_text:
            for name, value in self.passport.items():

                for name_2, value_2 in value.load().items():
                    passport_text.write(str(value_2) + '|')
                passport_text.write('\n')

    def load_passport(self):

        if 'passport.txt' in set(listdir()):
            with open('passport.txt', 'r') as passport_text:
                passport = passport_text.readlines()

                ser, num, date, issued = passport[0].split('|')[0:-1]
                self.passport_num = Document(ser, num, date, issued)

                surname, name, patronymic, date, gender = passport[1].split('|')[0:-1]
                self.name = Name(name, surname, patronymic, date, gender)

                country, state, city = passport[2].split('|')[0:-1]
                self.address_birth = Address(country, state, city, '-', '-', '-')

                country, state, city, street, house, apartment = passport[3].split('|')[0:-1]
                self.address_post = Address(country, state, city, street, house, apartment)

                self.passport = {'Атрибуты паспорта': self.passport_num,
                                 'ФИО': self.name,
                                 'Место рождения': self.address_birth,
                                 'Адрес прописки': self.address_post}


class SNILS:

    snils_nom = Document(None, None, None, None)
    snils_name = Name(None, None, None, None, None)
    snils_address_birth = Address(None, None, None, '-', '-', '-')

    snils = {'Атрибуты СНИЛС': snils_nom,
             'ФИО': snils_name,
             'Место рождения': snils_address_birth}

    def make(self):
        self.snils_nom = Document(input('ВВедите номер СНИЛС: '), '-', input('ВВедите дату регистрации: '), '-')
        self.snils_name = Name(input('Введите имя: '),
                               input('Введите Фамилию: '),
                               input('Введите Отчество(если нет то "-"): '),
                               input('Ввведите дату рождения'),
                               input('Ввведите пол'))
        self.snils_address_birth = Address(input('Введите Страну: '),
                                           input('Введите Субъект: '),
                                           input('Введите Город: '),
                                           '-',
                                           '-',
                                           '-')
        self.snils = {'Атрибуты СНИЛС': self.snils_nom,
                      'ФИО': self.snils_name,
                      'Место рождения': self.snils_address_birth}

    def print_document(self):
        print('Реквезиты СНИЛС: ')
        info = self.snils_nom.load()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_name(self):
        print('ФИО: ')
        info = self.snils_name.load()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_address_birth(self):
        print('Место Рождения: ')
        info = self.snils_address_birth.load()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_snils(self):
        self.print_document()
        self.print_name()
        self.print_address_birth()

    def safe_snils(self):
        with open('snils.txt', 'w') as snils_text:
            for name, value in self.snils.items():

                for name_2, value_2 in value.load().items():
                    snils_text.write(str(value_2) + '|')
                snils_text.write('\n')

    def load_snils(self):

        if 'snils.txt' in set(listdir()):
            with open('snils.txt', 'r') as snils_text:
                snils = snils_text.readlines()

                num, series, date, issued = snils[0].split('|')[0:-1]
                self.snils_nom = Document(num, series, date, issued)

                name, surname, patronymic, date, gender = snils[1].split('|')[0:-1]
                self.snils_name = Name(name, surname, patronymic, date, gender)

                country, state, city = snils[2].split('|')[0:-1]
                self.snils_address_birth = Address(country, state, city, '-', '-', '-')

                self.snils = {'Атрибуты СНИЛС': self.snils_nom,
                              'ФИО': self.snils_name,
                              'Место рождения': self.snils_address_birth}



