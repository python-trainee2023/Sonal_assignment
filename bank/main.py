# from bank.account import saving, checking
from account import SavingsAccount, Account, CheckingAccount
from transaction import deposit, withdraw, balance_enquiry


def main(arg):
    match arg:
        case 1:
            print("d")
            account = input("enter account number")
            SavingsAccount.savingBlc(account)
        case 2:
            account = input("enter account number")
            CheckingAccount.checkingBlc(account)
        case 3:
            account = input("enter account number")
            amount = int(input("enter amount"))
            deposit(account, amount)
        case 4:
            account = input("enter account number")
            amount = int(input("enter amount"))
            withdraw(account, amount)
        case 5:
            account = input("enter account number")
            balance_enquiry(account)


args = int(input("enter 1 - 5:\n 1:check saving balance\n 2: check checking balance\n 3: deposit\n "
             "4: withdraw \n 5: balance enquiry\n"))
print(args)
main(args)
