from cashcard import CashCard

class Wallet:
    def __init__(self):
        self.cards = []

    def add_card(self, card_number):
        new_card = CashCard(card_number=card_number)
        self.cards.append(new_card)

    def remove_card(self, card_number):
        self.cards = [card for card in self.cards if card.card_number != card_number]

    def get_card(self, card_number):
        return next((card for card in self.cards if card.card_number == card_number), None)

    def total_balance(self):
        return sum(card.balance for card in self.cards)
