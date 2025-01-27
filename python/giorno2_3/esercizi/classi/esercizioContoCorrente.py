class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, num):
        self.balance += num  # Aggiungo dindini al conto
    def withdraw(self, num): # Prendo dindini dal conto
        self.balance -=num
        if self.balance <= 0:
            raise Exception("InsufficientFundsError")


account = Account(name="Rigel")
assert account.name == "Rigel"
assert account.balance == 0

account.deposit(500)
assert account.balance == 500

account.withdraw(200)
assert account.balance == 300

account.withdraw(400)