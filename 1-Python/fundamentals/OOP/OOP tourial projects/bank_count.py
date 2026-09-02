# 
class BalanceExeption(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.
            balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceExeption(f"Sorry, account '{self.name}' only has a Balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n withdraw complete.")
            self.getBalance()
        except BalanceExeption as error:
            print(f"\nWithdraw interrupted: {error}")


    def transfer(self, amount, account):
        try: 
            print('\n*********\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! ✔️\n\n***********')
        except BalanceExeption as error:
            print(f'\n Transfer interrupted. ❌{error}')




        


 