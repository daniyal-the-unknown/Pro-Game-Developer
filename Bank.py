class Bank:

    def __init__(self, name, bank_account):
        self.name = name
        self.bank_account = bank_account

    def deposit(self, deposit):
        if deposit <= self.bank_account:
            self.bank_account -= deposit
            print(deposit, "deposit(s) creited.")
        else:
            print("Deposit has not properly beed credited.")

    def display(self):
        print("\nMovie:", self.name)
        print("Your Bank Balance:", self.bank_account)

