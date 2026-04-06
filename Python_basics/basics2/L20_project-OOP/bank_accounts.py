class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initValue, accName):
        self.balance = initValue
        self.name = accName
        print(f"Account {accName} has bean created")

    def valid_Transection(self, value):
        if self.balance >= value:
            return
        else:
            raise BalanceException(
                f"sorry the account has only balance of ${self.balance}")

    def withdraw(self, value):

        try:
            self.valid_Transection(value)
            self.balance -= value
            print(f"You successfully withdraw ${value}")
            self.getBalance()
        except BalanceException as error:
            print(f"withdraw is intrupted    error : {error} ")

    def deposit(self, value):
        self.balance += value
        print(f"You successfully deposit ${value} ✅")
        self.getBalance()

    def getBalance(self):
        print(f"Account {self.name} Balance : ${self.balance:.2f}")

    def getName(self):
        print(f"Account Name : '{self.name}'")

    def getNameOnly(self):
        return self.name

    def getAll(self):
        self.getName()
        self.getBalance()

    def transfareTo(self, value, account):
        print(f"'{self.name}' ,you received ${value} from {account.getNameOnly()}")
        self.balance += value

    def transfareFrom(self, value, account):
        try:
            print("\n**** Being Transfer ...... 💸💸💸💸\n")
            self.valid_Transection(value)
            self.balance -= value
            print(
                f"{self.name} ,you successfully transfered  ${value} to {account.getNameOnly()}   ✅💵")
            account.transfareTo(value, self)

        except BalanceException as error:
            print(f"Transefare being inturrepted  : {error} 🚫")


class RewardsAccount(BankAccount):
    def deposit(self, value):
        self.balance += (value * 1.05)
        print(f"You successfully deposit ${value}")
        self.getBalance()


class SavingAccount(RewardsAccount):
    def __init__(self, initValue, accName):
        super().__init__(initValue, accName)
        self.fee = 5

    def withdraw(self, value):
        try:
            self.valid_Transection(value + self.fee)
            self.balance -= (value + self.fee)
            print(f"You successfully withdraw ${value}")
            self.getBalance()
        except BalanceException as error:
            print(f"withdraw had been inturrepted  : {error}🚫")
