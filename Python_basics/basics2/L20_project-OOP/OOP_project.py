from bank_accounts import *

Mrwan = BankAccount(1000, "Mrawn")
Leana = BankAccount(3000, "Leana")
Mrwan.withdraw(3000)
print()

Mrwan.deposit(500)
Mrwan.withdraw(1500)

Mrwan.deposit(1700)
print()

Leana.transfareFrom(10009, Mrwan)
print()

Salah = RewardsAccount(1000, "Salah")
Salah.deposit(100)
Salah.transfareFrom(500, Mrwan)

print()
Fahad = SavingAccount(3000, "Fahad")
Fahad.deposit(100)
Fahad.withdraw(300)
