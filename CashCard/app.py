from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_credentials(self, entered_username, entered_password):
        return self.username == entered_username and self.password == entered_password

class Wallet:
    def __init__(self):
        self.cards = []

    def add_card(self, card_number):
        new_card = CashCard(card_number=card_number)
        self.cards.append(new_card)

    def remove_card(self, card_number):
        self.cards = [card for card in self.cards if card.number != card_number]

    def get_card(self, card_number):
        return next((card for card in self.cards if card.number == card_number), None)

    def total_balance(self):
        return sum(card.balance for card in self.cards)

class CashCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.balance = 0.0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

users = [
    User(username="user1", password="pass1"),
    User(username="user2", password="pass2"),
]

wallets = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    entered_username = request.form['username']
    entered_password = request.form['password']

    user = next((u for u in users if u.verify_credentials(entered_username, entered_password)), None)

    if user:
        wallet = wallets.get(user.username, Wallet())
        wallets[user.username] = wallet

        return redirect(url_for('dashboard', username=user.username))
    else:
        return render_template('index.html', error_message="Incorrect username or password.")

@app.route('/dashboard/<username>', methods=['GET', 'POST'])
def dashboard(username):
    wallet = wallets.get(username, Wallet())

    if request.method == 'POST':
        option = request.form['option']

        if option == 'check_balance':
            card_number = request.form['card_number']
            card = wallet.get_card(card_number)
            if card:
                balance = card.check_balance()
                return render_template('dashboard.html', username=username, wallet=wallet, balance=balance, selected_option='check_balance')
            else:
                return render_template('dashboard.html', username=username, wallet=wallet, error_message="Cash Card not found.", selected_option='check_balance')

        elif option == 'deposit_money':
            card_number = request.form['card_number']
            amount = float(request.form['amount'])
            card = wallet.get_card(card_number)
            if card:
                card.deposit(amount)
                return render_template('dashboard.html', username=username, wallet=wallet, success_message=f"Deposited {amount} to Cash Card {card_number}.", selected_option='deposit_money')
            else:
                return render_template('dashboard.html', username=username, wallet=wallet, error_message="Cash Card not found.", selected_option='deposit_money')

        elif option == 'withdraw_money':
            card_number = request.form['card_number']
            amount = float(request.form['amount'])
            card = wallet.get_card(card_number)
            if card:
                if card.withdraw(amount):
                    return render_template('dashboard.html', username=username, wallet=wallet, success_message=f"Withdrew {amount} from Cash Card {card_number}.", selected_option='withdraw_money')
                else:
                    return render_template('dashboard.html', username=username, wallet=wallet, error_message="Insufficient balance.", selected_option='withdraw_money')

            else:
                return render_template('dashboard.html', username=username, wallet=wallet, error_message="Cash Card not found.", selected_option='withdraw_money')

        elif option == 'add_cash_card':
            card_number = request.form['card_number']
            wallet.add_card(card_number)
            return render_template('dashboard.html', username=username, wallet=wallet, success_message=f"Added Cash Card {card_number} to the Wallet.", selected_option='add_cash_card')

        elif option == 'remove_cash_card':
            card_number = request.form['card_number']
            wallet.remove_card(card_number)
            return render_template('dashboard.html', username=username, wallet=wallet, success_message=f"Removed Cash Card {card_number} from the Wallet.", selected_option='remove_cash_card')

        elif option == 'check_total_balance':
            return render_template('dashboard.html', username=username, wallet=wallet, total_balance=wallet.total_balance(), selected_option='check_total_balance')

    return render_template('dashboard.html', username=username, wallet=wallet, selected_option='')
@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    url_for('submit_contact_form')
    return "Form submitted successfully"
@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
