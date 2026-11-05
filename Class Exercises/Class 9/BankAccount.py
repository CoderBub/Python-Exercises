#Abstraction
class BankAccount:
    def __init__(self):
        self.__balance = 50      # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(250)
print(account.get_balance())