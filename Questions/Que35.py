# Write a Python program to implement data hiding. 

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable (data hidden)

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")


# Object create
acc = BankAccount("Aditya", 5000)

acc.show_balance()
acc.deposit(1000)
acc.withdraw(2000)
acc.show_balance()