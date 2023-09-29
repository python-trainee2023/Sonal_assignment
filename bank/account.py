# Create a package called bank which simulates a simple banking system.
# Inside the package, create two modules: account and transaction.
# The account module defines a base class Account with common attributes
# like account_number, holder_name and balance. After this create two subclasses
# SavingsAccount and CheckingAccount with their own methods. The transaction module
# should provide functions for deposit and withdrawal.

import transaction as tran
class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self,account_number, holder_name, balance, saveBlc):
        Account.__init__(self, account_number, holder_name, balance)
        self.saveBlc = saveBlc

    def savingBlc(self):
        print(f"Welcome {self.holder_name}, your current balance in saving account is {self.saveBlc}")


class CheckingAccount(Account):
    def __init__(self,account_number, holder_name, balance, checkBlc):
        Account.__init__(self, account_number, holder_name, balance)
        self.checkBlc = checkBlc

    def checkingBlc(self):
        print(f"Welcome account:{self.account_number}, your current balance in checking account is {self.checkBlc}")


saving = SavingsAccount("11230856","Sonal Adhikari", 50000, 30000)
saving.savingBlc()
checking = CheckingAccount("11230856", "Sonal Adhikari",50000, 20000)
checking.checkingBlc()
tran.withdraw(5500)
tran.deposit(3000)



