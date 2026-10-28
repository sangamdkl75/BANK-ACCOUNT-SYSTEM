
#                       BANK ACCOUNT SYSTEM

class BankAccount():

    # Initialise the owner name and balance in account.

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.__balance = balance


    # returns the current balance

    def get_balance(self):
        return self.__balance

    # deposit the money in the account

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")

    # Withdraw the money if the balance is sufficient.

    def withdrawl(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawl successfully.")
        else:
            print("Invalid amount or Balance is not sufficient.")

    # Display the details of the account

    def display_details(self):
        print(f"\n    BANK ACCOUNT DETAILS        \n")
        print(f"Owner: {self.owner_name}")
        print(f"Balance: {self.get_balance()}")

    
    
account = BankAccount("Ram", 2000)

account.deposit(500)

account.withdrawl(200)

account .display_details()


