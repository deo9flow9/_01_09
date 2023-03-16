class Account(object):
    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = opening_balance
        print("Account created for {}".format(self.name), end='')
        self.show_balance()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._balance += amount
            print("{} deposited".format(amount))
        return self._balance

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("{} withdrawn".format(amount))
            return amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance))


if __name__ == "__main__":
    karl = Account("Karl", 1010)
    karl.deposit(10)
    karl.withdraw(20)
    karl.withdraw(0)
    karl.show_balance()

