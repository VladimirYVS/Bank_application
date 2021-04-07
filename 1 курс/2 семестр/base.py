import uuid, Money

class Account:
    id = None
    name = None
    surname = None
    patronymic = None
    money = {}
    doc = {}

    def make(self):
        self.id = uuid.uuid4()
        self.name = input('Введите имя: ')
        self.surname = input('Введите фамилию: ')
        self.patronymic = input('Введите Отчество: ')

        self.money += {RUB().amount = input('Введите количество рублей: '): 112}
        self.doc = {'ИД': self.id,
                    'Имя': self.name,
                    'Фамилия': self.surname,
                    'Отчество': self.patronymic,
                    'Деньги': self.money}

    def print_acc(self):
        print(self.doc.items())


acc = Account()
acc.make()
acc.print_acc()
