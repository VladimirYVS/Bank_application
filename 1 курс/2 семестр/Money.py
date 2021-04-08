import requests


class RUB:

    name = ''
    cost = 1
    amount = 0

    def load(self):
        names = {1: 'Рубль',
                 2: 'Рубля',
                 3: 'Рубля',
                 4: 'Рубля',
                 5: 'Рублей',
                 11: 'Рублей',
                 12: 'Рублей',
                 13: 'Рублей'}
        if str(self.amount)[-1] == "1" and self.amount != 11:
            self.name = names.get(1)
        elif str(self.amount)[-1] == "2" and self.amount != 12:
            self.name = names.get(2)
        elif str(self.amount)[-1] == "3" and self.amount != 13:
            self.name = names.get(3)
        elif str(self.amount)[-1] == "4" and self.amount != 14:
            self.name = names.get(2)
        elif int(str(self.amount)[-1]) >= 5:
            self.name = names.get(11)
        else:
            self.name = names.get(11)



    def money_pr(self):
        self.load()
        print(self.amount, self.name)




class EUR:
    cost = RUB().cost * 73.2317
    amount = 87.3508
    name = 'Евро'

    def money_pr(self):

        print(self.amount, self.name)


class USD:
    cost = RUB().cost * 73.2317
    amount = 0
    name = ''

    def load(self):
        names = {1: 'Доллар',
                 2: 'Доллара',
                 3: 'Доллара',
                 4: 'Доллара',
                 5: 'Долларов',
                 11: 'Долларов',
                 12: 'Долларов',
                 13: 'Долларов'}

        if str(self.amount)[-1] == "1" and self.amount != 11:
            self.name = names.get(1)
        elif str(self.amount)[-1] == "2" and self.amount != 12:
            self.name = names.get(2)
        elif str(self.amount)[-1] == "3" and self.amount != 13:
            self.name = names.get(3)
        elif str(self.amount)[-1] == "4" and self.amount != 14:
            self.name = names.get(2)
        elif int(str(self.amount)[-1]) >= 5:
            self.name = names.get(11)
        else:
            self.name = names.get(11)



    def money_pr(self):
        self.load()
        print(self.amount, self.name)

class JPY:
    cost = RUB().cost * 11.2612
    amount = 0
    name = ''

    def load(self):
        names = {1: 'Йена',
                 2: 'Йены',
                 3: 'Йены',
                 4: 'Йены',
                 5: 'Йен',
                 11: 'Йен',
                 12: 'Йен',
                 13: 'Йен'}

        if str(self.amount)[-1] == "1" and self.amount != 11:
            self.name = names.get(1)
        elif str(self.amount)[-1] == "2" and self.amount != 12:
            self.name = names.get(2)
        elif str(self.amount)[-1] == "3" and self.amount != 13:
            self.name = names.get(3)
        elif str(self.amount)[-1] == "4" and self.amount != 14:
            self.name = names.get(2)
        elif int(str(self.amount)[-1]) >= 5:
            self.name = names.get(11)
        else:
            self.name = names.get(11)



    def money_pr(self):
        self.load()
        print(self.amount, self.name)





class CNY:
    cost = RUB().cost * 6.7105
    amount = 0
    name = ''

    def load(self):
        names = {1: 'Юань',
                 2: 'Юаня',
                 3: 'Юаня',
                 4: 'Юаня',
                 5: 'Юаней',
                 11: 'Юаней',
                 12: 'Юаней',
                 13: 'Юаней'}

        if str(self.amount)[-1] == "1" and self.amount != 11:
            self.name = names.get(1)
        elif str(self.amount)[-1] == "2" and self.amount != 12:
            self.name = names.get(2)
        elif str(self.amount)[-1] == "3" and self.amount != 13:
            self.name = names.get(3)
        elif str(self.amount)[-1] == "4" and self.amount != 14:
            self.name = names.get(2)
        elif int(str(self.amount)[-1]) >= 5:
            self.name = names.get(11)
        else:
            self.name = names.get(11)

    def money_pr(self):
        self.load()
        print(self.amount, self.name)


rub = RUB()
rub.amount = 10040
rub.money_pr()

cyn = CNY()
cyn.amount = 1212
cyn.money_pr()
