class CashCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.balance = 0.0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
