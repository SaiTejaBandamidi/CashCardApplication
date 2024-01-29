from cashcard import CashCard
from wallet import Wallet
from user import User

# Softcoded user credentials (for demonstration purposes)
users = [
    User(username="user1", password="pass1"),
    User(username="user2", password="pass2"),

]


def display_menu():
    print("\nCash Card System Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Add Cash Card to Wallet")
    print("5. Remove Cash Card from Wallet")
    print("6. Check Total Wallet Balance")
    print("7. Exit")


def login():
    print("\nLogin:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return User(username, password)


def main():
    # User login
    user = login()
    # Verify credentials against the softcoded users
    correct_user = next((u for u in users if u.verify_credentials(user.username, user.password)), None)

    if not correct_user:
        print("Incorrect username or password. Exiting.")
        return

    print(f"Login successful. Welcome, {correct_user.username}!")

    wallet = Wallet()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            card_number = input("Enter Cash Card Number: ")
            card = wallet.get_card(card_number)
            if card:
                print(f"Balance for Cash Card {card_number}: {card.check_balance()}")
            else:
                print(f"Cash Card {card_number} not found.")

        elif choice == '2':
            card_number = input("Enter Cash Card Number: ")
            card = wallet.get_card(card_number)
            if card:
                amount = float(input("Enter the amount to deposit: "))
                card.deposit(amount)
                print(f"Deposited {amount} to Cash Card {card_number}.")
            else:
                print(f"Cash Card {card_number} not found.")

        elif choice == '3':
            card_number = input("Enter Cash Card Number: ")
            card = wallet.get_card(card_number)
            if card:
                amount = float(input("Enter the amount to withdraw: "))
                if card.withdraw(amount):
                    print(f"Withdrew {amount} from Cash Card {card_number}.")
                else:
                    print("Insufficient balance.")
            else:
                print(f"Cash Card {card_number} not found.")

        elif choice == '4':
            card_number = input("Enter the new Cash Card Number: ")
            wallet.add_card(card_number)
            print(f"Added Cash Card {card_number} to the Wallet.")

        elif choice == '5':
            card_number = input("Enter the Cash Card Number to remove: ")
            wallet.remove_card(card_number)
            print(f"Removed Cash Card {card_number} from the Wallet.")

        elif choice == '6':
            print(f"Total Wallet Balance: {wallet.total_balance()}")

        elif choice == '7':
            print("Exiting the Cash Card System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    main()
