# Exercise 7: Interface Segregation Principle

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use AI and search engine tools to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Steps

1. Copy the starting code from the `begin.py` file to a file named `app.py`. You may use code from earlier lab exercises to help you implement the code for this exercise. All code execution should originate from the `main` function. Decorate the code with Python type hints.

2. Observe the provided code for the `BankAccount` class and its subclasses, which violates the Interface Segregation Principle by having a single interface with methods that are not applicable to all subclasses.

3. Identify the problem with the current implementation and how it violates the Interface Segregation Principle.

4. Apply the Interface Segregation Principle by creating separate interfaces for different sets of functionality and ensuring that classes only implement the interfaces they need.

5. Modify the existing classes and create new interfaces to adhere to the Interface Segregation Principle.

6. Create objects of the `SavingsAccount` and `CheckingAccount` classes and demonstrate the usage of the segregated interfaces.

7. Upgrade the final solution code to use Protocol classes instead of Abstract Classes.

## When You Are Done

Send me an email at [eric@cloudcontraptions.com](mailto:eric@cloudcontraptions.com) to let me know you are finished.
