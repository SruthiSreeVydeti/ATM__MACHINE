class ATM:
    def __init__(self, initial_balance, pin):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, pin):
        """Check if the entered PIN is correct."""
        return self.pin == pin

    def inquire_balance(self):
        """Return the current balance."""
        return self.balance5

    def withdraw_cash(self, amount):
        """Withdraw a specified amount of cash if the balance is sufficient."""
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"

    def deposit_cash(self, amount):
        """Deposit a specified amount of cash."""
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def change_pin(self, old_pin, new_pin):
        """Change the PIN if the old PIN is correct."""
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            return "PIN successfully changed"
        else:
            return "Incorrect old PIN"

    def get_transaction_history(self):
        """Return the transaction history."""
        return self.transaction_history

def main():
    # Take initial balance and PIN from the user
    initial_balance = float(input("Enter initial balance: "))
    pin = int(input("Enter initial PIN: "))
    
    # Initialize ATM with the user-provided starting balance and PIN
    atm = ATM(initial_balance=initial_balance, pin=pin)
    
    # Perform ATM operations with user input
    while True:
        print("\nATM Menu:")
        print("1. Balance Inquiry")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            print(f"Balance: ${atm.inquire_balance()}")
        
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw_cash(amount))
        
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit_cash(amount))
        
        elif choice == "4":
            old_pin = int(input("Enter old PIN: "))
            new_pin = int(input("Enter new PIN: "))
            print(atm.change_pin(old_pin, new_pin))
        
        elif choice == "5":
            history = atm.get_transaction_history()
            if history:
                print("Transaction History:")
                for transaction in history:
                    print(transaction)
            else:
                print("No transactions yet.")
        
        elif choice == "6":
            print("Exiting ATM. Have a nice day!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
