class Account:

    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счёт на {money} рублей. Остаток на счёте: {self.balance} рублей")

    def withdraw(self, money):
        if money > self.balance:
            print("Недостаточно средств на счёте")
        else:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счёте: {self.balance} рублей")

    def all_balance(self):
        print(f"Остаток на счёте: {self.balance} рублей")


man = Account(12323132, 10000)
man.all_balance()
man.withdraw(1500)
man.withdraw(2200)
man.deposit(15000)
