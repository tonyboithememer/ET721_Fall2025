"""
Antonios Takos
Oct 6, 2025
Lab 8, unit test, bank account
"""


class BankAccount:
    def __init__(self, inital_balance=0):
        self.balance = inital_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("ERROR! Can't deposit a negative amount!!")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("ERROR! Can't withdraw a negative amount!!")
        if amount > self.balance:
            raise ValueError("ERROR! Insufficient funds detected!")
        self.balance -= amount

    def get_balance(self):
        return self.balance


import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount()

    def test_inital_balance(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_multiple_deposits(self):
        self.account.deposit(50)
        self.account.deposit(150)
        self.assertEqual(self.account.get_balance(), 200)

    def test_withdraw(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 0)

    def test_withdraw_exact_balance(self):
        self.account.deposit(100)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 0)

    def test_overdraft(self):
        self.account.deposit(100)
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(150)
        self.assertEqual(str(context.exception), "ERROR! Insufficient funds detected!!")

    def test_negative_deposit(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-50)
        self.assertEqual(
            str(context.exception), "ERROR! Can't deposit a negative amount!!"
        )

    def test_negative_withdrawl(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-20)
        self.assertEqual(
            str(context.exception), "ERROR! Can't withdraw a negative amount!!"
        )


if __name__ == "__main__":
    unittest.main()
