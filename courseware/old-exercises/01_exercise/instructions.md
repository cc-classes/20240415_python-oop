# Exercise 1 - Implement the History Class

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use Google and ChatGPT to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Requirements

1. In the `begin` folder, run the `calc.py` code. Review the code. Observe how the calculator operations are tracked in a list of dictionaries.

```bash
python ./calc.py
```

2. Upgrade the application to track the calculator operations as a list of `HistoryEntry` objects. Define the `HistoryEntry` class based upon the existing dictionary structure as revealed in the code.

3. In the various commands, there are operations that update the list of `HistoryEntry` objects. Refactor the list of `HistoryEntry` objects and the methods that manipulate the list into a `History` class. Update the application to use the `History` class.

4. Review the `HistoryEntry` and `History` classes. Did you implement encapsulation for internal details? Which techniques did you use to implement encapsulation?

5. Make the `History` class iterable such that when the `History` object is iterated over it will return the `HistoryEntry` objects in the list. The `History` class should be able to be iterated over multiple times.

