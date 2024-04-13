# Exercise 5: Open-Closed Principle

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use AI and search engine tools to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Steps

1. Copy the starting code from the `begin.py` file to a file named `app.py`. You may use code from earlier lab exercises to help you implement the code for this exercise. All code execution should originate from the `main` function. Decorate the code with Python type hints.

2. Observe the provided code for the `BankAccount` class and the `calculate_interest` function, which violates the open-closed principle by requiring modifications to the function whenever a new account type is added.

3. Identify the problem with the current implementation and how it violates the open-closed principle.

4. Apply the open-closed principle by creating separate classes for each account type (`SavingsAccount` and `CheckingAccount`) and moving the interest calculation logic into the respective classes.

5. Modify the `calculate_interest` function to accept a `BankAccount` object and delegate the interest calculation to the account object itself.

6. Create objects of the `SavingsAccount` and `CheckingAccount` classes and demonstrate the usage of the open-closed principle.

## When You Are Done

Send me an email at [eric@cloudcontraptions.com](mailto:eric@cloudcontraptions.com) to let me know you are finished.
