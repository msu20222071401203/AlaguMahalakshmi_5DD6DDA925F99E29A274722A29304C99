'''Implement a class called BankAccount that represents account.The class should have private 
attributes for account number, account holder name, and account balance. Include methods to 
deposit money, withdraw money, and display the account balance. Ensure that the account balance
cannot be accessed directly from outside the class. Write a program to create an instance of the
BankAccount class and test the deposit and withdrawlfunctionality.'''

class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")

    @property
    def account_balance(self):
        return self.__account_balance


# Example usage:
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    my_account = BankAccount("123456789", "John Doe", 1000)

    # Deposit money
    my_account.deposit(500)
