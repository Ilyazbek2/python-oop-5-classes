class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money")

    def getBalance(self):
        return self.balance


account = BankAccount("John", 1000)

account.deposit(500)
account.withdraw(200)

print(account.getBalance())
