# Exercise 8: Dependency Inversion Principle

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use AI and search engine tools to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Steps

1. Copy the starting code from the `begin.py` file to a file named `app.py`. You may use code from earlier lab exercises to help you implement the code for this exercise. All code execution should originate from the `main` function. Decorate the code with Python type hints.

2. Observe the provided code for the `BankAccount` and `Notification` classes, which violates the Dependency Inversion Principle by directly depending on concrete implementations.

3. Identify the problem with the current implementation and how it violates the Dependency Inversion Principle.

4. Apply the Dependency Inversion Principle by introducing abstractions (interfaces) and inverting the dependencies. Use Protocol classes to define the interfaces.

5. Modify the existing classes and create new interfaces to adhere to the Dependency Inversion Principle.

6. Create objects of the `BankAccount` class with different notification mechanisms and demonstrate the usage of the inverted dependencies.

## When You Are Done

Send me an email at [eric@cloudcontraptions.com](mailto:eric@cloudcontraptions.com) to let me know you are finished.
