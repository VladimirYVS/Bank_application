from random import randint
from os import chdir, mkdir, listdir


class Name:
    information = {'Фамилия': None,
                   'Имя': None,
                   'Отчество': None,
                   'Дата рождения': None,
                   'Пол': None}

    def make(self):
        name = input('Введите имя: ')
        surname = input('Введите Фамилию: ')
        patronymic = input('Введите Отчество(если нет то "-"): ')
        date = input('Ввведите дату рождения: ')
        gender = input('Ввведите пол: ')
        self.information = {'Фамилия': surname,
                            'Имя': name,
                            'Отчество': patronymic,
                            'Дата рождения': date,
                            'Пол': gender}

    def upload(self):
        return self.information

    def download(self, strings):
        string = strings.split('|')
        self.information = {'Фамилия': string[0],
                            'Имя': string[1],
                            'Отчество': string[2],
                            'Дата рождения': string[3],
                            'Пол': string[4]}

    def safe(self):
        strings = ''
        for key, value in self.information.items():
            strings += value + '|'
        return strings

    def print_name(self):
        for key, value in self.information.items():
            print(key, value)


class Address:

    information = {'Страна': None,
                   'Субъект': None,
                   'Район': None,
                   'Населенный пунк': None,
                   'Улица': None,
                   'Дом': None,
                   'Квартира': None}

    def make(self):
        country = input('Введите страну: ')
        state = input('Введите субъект: ')
        district = input('Введите район: ')
        city = input('Введите населенный пункт: ')
        street = input('Введите улицу: ')
        house = input('Введите дом: ')
        apartment = input('Введите квартиру: ')

        self.information = {'Страна': country,
                            'Субъект': state,
                            'Район': district,
                            'Населенный пункт': city,
                            'Улица': street,
                            'Дом': house,
                            'Квартира': apartment}

    def upload(self):
        return self.information

    def download(self, strings):
        string = strings.split('|')
        self.information = {'Страна': string[0],
                            'Субъект': string[1],
                            'Район': string[2],
                            'Населенный пункт': string[3],
                            'Улица': string[4],
                            'Дом': string[5],
                            'Квартира': string[6]}

    def safe(self):
        strings = ''
        for key, value in self.information.items():
            strings += value + '|'
        return strings

    def print_address(self):
        for key, value in self.information.items():
            print(key, value)


class Document:
    information = {'Номер': None,
                   'Серия': None,
                   'Выдан': None,
                   'Дата выдачи': None}

    def make(self):
        number = input('Введите номер документа : ')
        series = input('Введите серию документа : ')
        date = input('Введите дату выдачи документа : ')
        issued = input('Введите кем выдан документ : ')

        self.information = {'Номер': number,
                            'Серия': series,
                            'Выдан': issued,
                            'Дата выдачи': date}

    def upload(self):
        return self.information

    def download(self, strings):
        string = strings.split('|')
        self.information = {'Номер': string[0],
                            'Серия': string[1],
                            'Выдан': string[2],
                            'Дата выдачи': string[3]}

    def safe(self):
        strings = ''
        for key, value in self.information.items():
            strings += value + '|'
        return strings

    def print_document(self):
        for key, value in self.information.items():
            print(key, value)


class Passport:

    passport = {'Атрибуты паспорта': Document(),
                'Данные держателя': Name(),
                'Место рождения': Address(),
                'Адрес прописки': Address()}

    def make(self):
        print('Заполинте данные паспорта')
        print("Заполните данные о держателе паспорта")
        self.passport['Данные держателя'].make()
        print("Заполните о паспорте")
        self.passport['Атрибуты паспорта'].make()
        print("Заполните данные о месте рождения")
        self.passport['Место рождения'].make()
        print("Заполните данные о месте прописки")
        self.passport['Адрес прописки'].make()

    def print_document(self):
        print('Реквезиты паспорта: ')
        info = self.passport['Атрибуты паспорта'].upload()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_name(self):
        print('ФИО: ')
        info = self.passport['Данные держателя'].upload()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_address(self):
        print('Адрес прописки: ')
        info = self.passport['Адрес прописки'].upload()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_address_birth(self):
        print('Место Рождения: ')
        info = self.passport['Место рождения'].upload()
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
                string = value.safe() + '\n'
                passport_text.write(string)

    def load_passport(self):

        if 'passport.txt' in set(listdir()):
            with open('passport.txt', 'r') as passport_text:
                passport = passport_text.readlines()

                self.passport['Атрибуты паспорта'].download(passport[0].strip('\n'))
                self.passport['Данные держателя'].download(passport[1].strip('\n'))
                self.passport['Место рождения'].download(passport[2].strip('\n'))
                self.passport['Адрес прописки'].download(passport[3].strip('\n'))


class SNILS:

    snils = {'Атрибуты СНИЛС': Document(),
             'Данные держателя': Name(),
             'Место рождения': Address()}

    def make(self):

        print('Заполинте данные СНИЛС')
        print("Заполните данные о держателе Снилс")
        self.snils['Данные держателя'].make()
        print("Заполните о СНИЛС")
        self.snils['Атрибуты СНИЛС'].make()
        print("Заполните данные о месте рождения")
        self.snils['Место рождения'].make()

    def print_document(self):
        print('Реквезиты СНИЛС: ')
        info = self.snils['Атрибуты СНИЛС'].upload()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_name(self):
        print('ФИО: ')
        info = self.snils['Данные держателя'].upload()
        for key, value in info.items():
            if value != '-':
                print(key, '->', value)

    def print_address_birth(self):
        print('Место Рождения: ')
        info = self.snils['Место рождения'].upload()
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
                string = value.safe() + '\n'
                snils_text.write(string)

    def load_snils(self):

        if 'snils.txt' in set(listdir()):
            with open('snils.txt', 'r') as snils_text:
                snils = snils_text.readlines()

                strings = []
                for i in snils:
                    strings += i[0:-1]
                self.snils['Атрибуты СНИЛС'].download(strings[0])
                self.snils['Данные держателя'].download(strings[1])
                self.snils['Место рождения'].download(strings[2])
