class Bank(object):
    """docstring for ."""
    def __init__(self, bal):
        #super(, self).__init__()
        self.bal = 0

    def deposit(self, amount):
        self.bal = self.bal + amount
        return self.bal

    def withdraw(self, amount):
        self.bal = self.bal - amount
        return self.bal

    def print(self):
        print("Current Balance = ", self.bal)

obj = Bank(0)
obj.deposit(25)
obj.withdraw(10)
obj.print()
