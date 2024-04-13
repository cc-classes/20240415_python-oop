# Exercise 3: Inheritance & Composition

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use AI and search engine tools to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Steps

1. Copy the starting code from the `begin.py` file to a file named `app.py`. You may use code from earlier lab exerices to help you implement the code for this exercise. All code execution should originate from the `main` function.

2. Define a class named `Customer` with the following attributes and methods:
   - `__init__(self, name, email)`: Initializes the `name` and `email` attributes.
   - `display_info(self)`: Prints the customer's name and email.

3. Define a class named `BankAccount` with the following attributes and methods:
   - `__init__(self, account_number, balance, customer)`: Initializes the `account_number`, `balance`, and `customer` attributes. The `customer` attribute should be an instance of the `Customer` class.
   - `deposit(self, amount)`: Adds the specified `amount` to the account balance.
   - `withdraw(self, amount)`: Subtracts the specified `amount` from the account balance.
   - `display_balance(self)`: Prints the customer information and the current account balance.

4. Create a derived class named `SavingsAccount` that inherits from the `BankAccount` class. Add an additional attribute `interest_rate` and override the `deposit` method to add the interest amount to the balance.

5. Create objects of the `Customer`, `BankAccount`, and `SavingsAccount` classes, and demonstrate the usage of composition and inheritance.

6. What is the relationship between the `Customer` and `BankAccount` classes? What is the relationship between the `BankAccount` and `SavingsAccount` classes? Where was composition used and where was inheritance used?

7. Decorate the code with Python type hints.


## When You Are Done

Send me an email at [eric@cloudcontraptions.com](mailto:eric@cloudcontraptions.com) to let me know you are finished.
