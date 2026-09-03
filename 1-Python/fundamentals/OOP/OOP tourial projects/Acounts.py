from bank_count import *


Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)


Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)


Jim = interestRewardsAcc(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)


Blaze = SavingsAcc(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)