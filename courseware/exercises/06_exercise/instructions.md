# Exercise 6: Liskov Substitution Principle

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use AI and search engine tools to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Steps

1. Copy the starting code from the `begin.py` file to a file named `app.py`. You may use code from earlier lab exercises to help you implement the code for this exercise. All code execution should originate from the `main` function. Decorate the code with Python type hints.

2. Observe the provided code for the `BankAccount`, `SavingsAccount`, and `CheckingAccount` classes, which violates the Liskov substitution principle by raising an exception in the `withdraw` method of the `CheckingAccount` class. Why does this violate the Liskov substitution principle?

3. Identify the problem with the current implementation and how it violates the Liskov substitution principle.

4. Apply the Liskov substitution principle by ensuring that the `CheckingAccount` class can be used interchangeably with the `BankAccount` class without affecting the correctness of the program.

5. Modify the `CheckingAccount` class to adhere to the Liskov substitution principle.

6. Create objects of the `SavingsAccount` and `CheckingAccount` classes and demonstrate the usage of the Liskov substitution principle.

## When You Are Done

Send me an email at [eric@cloudcontraptions.com](mailto:eric@cloudcontraptions.com) to let me know you are finished.
