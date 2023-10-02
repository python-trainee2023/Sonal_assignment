# Create a package called bank which simulates a simple banking system.
# Inside the package, create two modules: account and transaction.
# The account module defines a base class Account with common attributes
# like account_number, holder_name and balance. After this create two subclasses
# SavingsAccount and CheckingAccount with their own methods. The transaction module
# should provide functions for deposit and withdrawal.


class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self,account_number, holder_name, balance, saveBlc):
        Account.__init__(self, account_number, holder_name, balance)
        self.saveBlc = saveBlc

    def savingBlc(self, account):
        acc = account
        if self.account_number == acc:
            print(f"Welcome {self.holder_name}, your current balance in saving account is {self.saveBlc}")
        else:
            print("invalid account number")

class CheckingAccount(Account):
    def __init__(self,account_number, holder_name, balance, checkBlc):
        Account.__init__(self, account_number, holder_name, balance)
        self.checkBlc = checkBlc

    def checkingBlc(self,account):
        acc = account
        if self.account_number == acc:
            print(f"Welcome account:{self.account_number}, your current balance in checking account is {self.checkBlc}")
        else:
            print("invaid acc number")

saving = SavingsAccount("111","Sonal Adhikari", 50000, 30000)
checking = CheckingAccount("111", "Sonal Adhikari",50000, 20000)
