# Exercise 4: Single Responsibility Principle

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use AI and search engine tools to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Steps

1. Copy the starting code from the `begin.py` file to a file named `app.py`. You may use code from earlier lab exercises to help you implement the code for this exercise. All code execution should originate from the `main` function. Decorate the code with Python type hints.

2. Observe the provided code for the `BankAccount` class, which violates the single responsibility principle by mixing account management and input validation responsibilities.

3. Identify the validation logic in the `BankAccount` class methods.

4. Create a separate class named `BankAccountValidator` and move the validation logic from the `BankAccount` class to the `BankAccountValidator` class.

5. Modify the `BankAccount` class to use the `BankAccountValidator` class for validating inputs before performing operations.

6. Review the objects of the `BankAccount` class and observe the usage of the single responsibility principle by validating inputs using the `BankAccountValidator` class.

## When You Are Done

Send me an email at [eric@cloudcontraptions.com](mailto:eric@cloudcontraptions.com) to let me know you are finished.
