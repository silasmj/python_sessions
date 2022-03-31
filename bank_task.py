"""class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Account(Customer):
    def __init__(self, balance):
        self.balance = balance
        Customer.__init__(self, balance)

class Bank(Account):

    owner = 'Silas Jensen'

    def __init__(self, balance):
        Account.__init__(self, Customer, balance)"""


class Bank:
    def __init__(self):
        self.account = []

class Account:
    def __init(self, number):
        self.number = number

class Customer:
    def __init(self, name, age):
        self.name = name
        self.age = age