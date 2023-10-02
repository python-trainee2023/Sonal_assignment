from account import checking, saving
# from account import *

def deposit(acc, amount):
    accountno = acc
    if checking.account_number == accountno:
        checking.checkBlc += amount
        print("Amount deposited. New checking balance: ", checking.checkBlc)
    else:
        print("account doesn't exist")


def withdraw(acc, amount):
    accountno = acc
    if checking.accountount_number == accountno and checking.checkBlc >= amount:
        checking.checkBlc -= amount
        print("Amount withdrawn: ", checking.checkBlc)
    elif checking.accountount_number != accountno or checking.checkBlc < amount:
        print("check your account number and amount")
    else:
        print("invalid")

def balance_enquiry(acc):
    accountno = acc
    if checking.accountount_number == accountno:
        print("balance: ", checking.balance)