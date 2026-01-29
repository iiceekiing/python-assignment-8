"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""

class BankAccount:
    def __init__(self, initial_balance=0):
        self.name = {}
        self.initial_balance = initial_balance

    def deposit(self, name, amount):
        if name in self.name:
            self.name[name] += amount
        else:
            self.name[name] = amount

    def withdraw(self, name, amount):
        if name in self.name and self.name[name] >= amount:
            self.name[name] -= amount
            return True
        return False

