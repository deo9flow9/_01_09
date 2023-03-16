import datetime
import sqlite3
import pytz

db = sqlite3.connect("account.sqlite", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS hystory "
           "(time TAMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', h.time, 'localtime') as local_time,"
                      "h.account, h.amount FROM hystory h ORDER BY h.time")
#Changes here
class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow()).astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
            self.show_balance()
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}".format(self.name), end='')
            self.show_balance()
        cursor.close()

    def deposit(self, amount: float) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: float) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return -amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))

    def _save_update(self, amount):
        new_balance = self._balance + amount
        action_time = Account._current_time()
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO hystory VALUES(?, ?, ?)", (action_time, self.name, amount))
        db.commit()
        self._balance += amount


if __name__ == "__main__":
    karl = Account("Karl")
    karl.deposit(10)
    karl.withdraw(20)
    karl.withdraw(2)
    karl.show_balance()
    terry = Account("Terry", 900)
    marry = Account("Marry", 200)
    Jhone = Account("Jhone", 10000)
