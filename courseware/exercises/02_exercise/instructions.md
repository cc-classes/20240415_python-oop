# Exercise 2: Polymorphism

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use AI and search engine tools to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Steps

1. Copy the file `begin.py` to a new file named `app.py`. Perform all coding in the `app.py` file. Utilize the `main` function to execute the code.

2. Update the existing base class named `BankAccount` with the following methods:
   - `__init__(self, account_number, balance)`: Initializes the `account_number` and `balance` attributes.
   - `deposit(self, amount)`: Adds the specified `amount` to the account balance.
   - `withdraw(self, amount)`: Subtracts the specified `amount` from the account balance.
   - `display_balance(self)`: Prints the current account balance.

3. Update the existing two derived classes: `SavingsAccount` and `CheckingAccount`. Each class should inherit from the `BankAccount` class and override the `withdraw` method as follows:
   - For `SavingsAccount`, apply an additional 2% interest to the balance after each withdrawal.
   - For `CheckingAccount`, apply a flat $1 fee for each withdrawal.

4. Utilize Python type hints throughout the entire solution.

5. Review how the `deposit`, `withdraw`, and `display_balance` methods are called for each account type in the `perorm_transactions` function.


## When You Are Done

Send me an email at [eric@cloudcontraptions.com](mailto:eric@cloudcontraptions.com) to let me know you are finished.