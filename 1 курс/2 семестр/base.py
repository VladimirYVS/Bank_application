import uuid
import Money
import Person


class Account(Person.Name, Person.Address):
    account_information = {}

    def __init__(self):
        super().__init__()

        self.account_information = {'id': '-',
                                    'RUB': 0,
                                    'USD': 0,
                                    'EUR': 0,
                                    'CYN': 0,
                                    'JPY': 0
                                    }

    def make(self):
        id_uuid = uuid.uuid4()
        self.account_information['id'] = str(id_uuid)

    def make_currency(self, curr, amount):
        currency = {'RUB': Money.RUB(),
                    'USD': Money.USD(),
                    'EUR': Money.EUR(),
                    'CYN': Money.CNY(),
                    'JPY': Money.JPY()
                    }

        chose_currency = currency[curr]
        chose_currency.amount = amount

        self.account_information[curr] = amount

    def download(self, string):

        string.strip()

        string_split = string.split("|")

        for item in string_split[0:-1]:

            key, value = item.split(':')
            if key in self.account_information:
                self.account_information[key] = value
            elif key in self.name_information:
                self.name_information[key] = value
            elif key in self.address_information:
                self.address_information[key] = value

    def safe(self):
        with open('base.txt', 'a+') as base:
            for key, value in self.account_information.items():
                base.write(key + ':' + str(value) + '|')
            for key, value in self.name_information.items():
                base.write(key + ':' + str(value) + '|')
            for key, value in self.address_information.items():
                base.write(key + ':' + str(value) + '|')
            base.write('\n')

    def get(self):
        gets = [self.account_information, self.name_information, self.address_information]
        return gets

    def get_address(self):
        return self.address_information

    def get_name(self):
        return self.name_information

    def get_account(self):
        return self.account_information

    def print_acc(self):

        for key, value in self.account_information.items():
            print(key, value)
        for key, value in self.name_information.items():
            print(key, value)
        for key, value in self.address_information.items():
            print(key, value)

    def __del__(self):
        del self.account_information
        del self.address_information
        del self.name_information


class DataBase:
    rows = None

    def __init__(self):
        # Constructor for initialising database
        with open('base.txt') as base:
            self.rows = base.readlines()

    def refresh(self):
        with open('base.txt') as base:
            self.rows = base.readlines()

    def get(self):
        # Get the database
        return self.rows

    def find_row(self, item):
        # Search rows than have searching item
        rows_have_items = []
        for row in self.rows:
            row = row.strip('\n')

            for value in row.split('|'):
                if value == '':
                    continue
                key, var = value.split(':')
                if str(item) in var:
                    if row not in rows_have_items and item != '':
                        rows_have_items.append(row)

        if len(rows_have_items) == 0:
            return 'Ничего не найдено'
        else:
            return rows_have_items
