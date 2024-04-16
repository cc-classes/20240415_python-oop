# Exercise 2 - Re-implement the Calc App Run Method

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use Google and ChatGPT to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Requirements

1. In a terminal, from the `begin` folder, run the calculator program.

```bash
python ./calc.py
```

2. Review the `run` method of the `CalcApp` class in the `calc.py` file. Observe how it uses `if-elif-else` block to process commands.

3. Create a new version `CalcApp` that uses a `match` statement instead of an `if-elif-else` the code. The final solution should allow me to change between the `if-elif-else` version and the `match` version without having to continually modify any version of the `CalcApp` class.

4. The solution must not modify the implementation of `start_app` function, but the call to `start_app` can be modified.

