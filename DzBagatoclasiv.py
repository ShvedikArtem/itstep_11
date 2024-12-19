class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n{amount} ₴ успішно зараховано на рахунок {self.account_number}. Поточний баланс: {self.balance} ₴")
        else:
            print("Сума для поповнення повинна бути більше 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"\n{amount} ₴ успішно знято з рахунку {self.account_number}. Поточний баланс: {self.balance} ₴")
        elif amount > self.balance:
            print("Недостатньо коштів для зняття.")
        else:
            print("Сума для зняття повинна бути більше 0.")

    def get_balance(self):
        print(f"\nБаланс рахунку {self.account_number}: {self.balance} ₴")
        return self.balance

    def __str__(self):
        return f"Власник: {self.owner_name}, Рахунок: {self.account_number}, Баланс: {self.balance} ₴"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner_name, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Рахунок з таким номером вже існує!")
        else:
            self.accounts[account_number] = BankAccount(owner_name, account_number, initial_balance)
            print(f"\nСтворено рахунок {account_number} для {owner_name}. Початковий баланс: {initial_balance} ₴")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if not from_account:
            print("Відправник рахунку не існує.")
            return
        if not to_account:
            print("Отримувач рахунку не існує.")
            return

        if amount <= 0:
            print("Сума переказу повинна бути більше 0.")
            return

        if from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"\nПереказ {amount} ₴ з рахунку {from_account_number} на рахунок {to_account_number} успішно виконано.")
        else:
            print("Недостатньо коштів для переказу.")

    def show_all_accounts(self):
        if self.accounts:
            print("\nСписок рахунків у банку:")
            for account in self.accounts.values():
                print(account)
        else:
            print("У банку ще немає рахунків.")

if __name__ == "__main__":
    bank = Bank()

    bank.create_account("Іван Іваненко", "1001", 5000)
    bank.create_account("Марія Петренко", "1002", 3000)

    account_ivan = bank.get_account("1001")
    account_maria = bank.get_account("1002")

    if account_ivan:
        account_ivan.deposit(2000)
        account_ivan.withdraw(1500)
        account_ivan.get_balance()

    if account_maria:
        account_maria.withdraw(500)
        account_maria.get_balance()

    bank.transfer("1001", "1002", 2500)

    bank.show_all_accounts()