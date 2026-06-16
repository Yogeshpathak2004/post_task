"""Create a class BankAccount with: 
• Private variable __balance = 10000
• Method deposit(amount) fi add to balance and print new balance
• Method withdraw(amount) fi if amount > balance print 'Insufficient!', else deduct
• Method get_balance() fi print current balance
Create 2 objects and perform deposit and withdraw operations on both"""

class BankAccount:
    def __init__(self):
        self.__balance = 10000

    def deposit(self, amount):
        self.__balance += amount
        print("New Balance:", self.__balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient!")
        else:
            self.__balance -= amount
            print("Withdraw Successful. Balance:", self.__balance)

    def get_balance(self):
        print("Current Balance:", self.__balance)


acc1 = BankAccount()
acc2 = BankAccount()

acc1.deposit(5000)
acc1.withdraw(2000)
acc1.get_balance()

acc2.deposit(3000)
acc2.withdraw(15000)
acc2.get_balance()