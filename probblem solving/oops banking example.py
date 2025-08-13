# File: oops_example.py

from abc import ABC, abstractmethod  # For abstraction

# Encapsulation: Using private variables and providing getter and setter methods
class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.__account_holder = account_holder  # Private variable
        self.__balance = balance  # Private variable

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Invalid withdraw amount or insufficient balance.")

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance
    def set_balance(self, amount: float):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

# Inheritance: Derived class from the BankAccount base class
class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(account_holder, balance)  # Calling parent class constructor
        self.interest_rate = interest_rate  # New attribute for SavingsAccount

    # New method to calculate interest
    def calculate_interest(self):
        return self.get_balance() * self.interest_rate

# Polymorphism: Overriding parent class method in the derived class
class CurrentAccount(BankAccount):
    def __init__(self, account_holder: str, balance: float = 0.0, overdraft_limit: float = 1000.0):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}. Remaining balance: {self.get_balance()}")
        else:
            print("Withdraw amount exceeds overdraft limit.")

# Abstraction: Abstract base class defining a blueprint
class Loan(ABC):
    @abstractmethod
    def calculate_emi(self, principal: float, tenure_years: int, interest_rate: float):
        pass

# Concrete class implementing the abstract method
class HomeLoan(Loan):
    def calculate_emi(self, principal: float, tenure_years: int, interest_rate: float):
        monthly_rate = interest_rate / (12 * 100)
        tenure_months = tenure_years * 12
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
              ((1 + monthly_rate) ** tenure_months - 1)
        return emi

# Demonstration
if __name__ == "__main__":
    # Encapsulation demonstration
    account = BankAccount("Alice", 1000)
    account.deposit(500)
    account.withdraw(300)
    print("Final balance:", account.get_balance())

    # Inheritance and polymorphism demonstration
    savings = SavingsAccount("Bob", 2000, 0.03)
    print("Savings interest:", savings.calculate_interest())

    current = CurrentAccount("Charlie", 1500, 2000)
    current.withdraw(3000)  # Uses overridden method

    # Abstraction demonstration
    loan = HomeLoan()
    emi = loan.calculate_emi(500000, 15, 7.5)
    print(f"Home loan EMI: {emi:.2f}")
