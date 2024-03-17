class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if self.balance >= amount:
            self.balance -= amount

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        # ✳️ Write code to calculate the interest based on the current balance and interest rate
        # ✳️ Write code to add the calculated interest to the account balance


# Testing the functionality of the classes
if __name__ == "__main__":
# ✳️ Create a BankAccount instance with account number "123456789" and initial balance of 1000

# ✳️ Deposit 500 into the account

# ✳️ Withdraw 200 from the account

# ✳️ Get the current balance of the bank account

# ✳️ Create a SavingsAccount instance with account number "987654321", initial balance of 2000, and interest rate of 5%

# ✳️ Deposit 1000 into the savings account

# ✳️ Calculate and add interest to the savings account

# ✳️ Get the current balance of the savings account after adding interest
