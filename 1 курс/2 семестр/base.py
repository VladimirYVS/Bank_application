import uuid, Money, Person

class Account:
    id = None
    full_name = None
    currency  = {}
    doc = {}

    def make(self):
        self.id = uuid.uuid4()
        self.full_name = Person.Name()
        self.full_name.make()
        ruble = Money.RUB()
        ruble.amount  = input('Введите колличество рублей на счету')
        ruble.load()
        self.currency = {ruble.amount : ruble.name}
        self.doc = {'ИД': self.id,
                    'Имя': self.full_name,
                    'Деньги': self.currency}

    def print_acc(self):

        print(self.doc['Имя'].upload()['Фамилия'], self.doc['Имя'].upload()['Имя'], self.doc['Имя'].upload()['Отчество'], self.currency.get())


acc = Account()
acc.make()
acc.print_acc()
