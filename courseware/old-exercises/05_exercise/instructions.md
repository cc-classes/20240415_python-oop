# Exercise 5 - Increase History Cohesion and Reduce Analysis Coupling

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use Google and ChatGPT to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Requirements

1. In a terminal, from the `begin` folder, run the calculator program.

```bash
python ./calc.py
```

2. Review the History class. It appears there may be a violation of the Single Responsbility Principle and Low Cohesion. Can you spot it? Look at the `calculate_result_from_history` method relative to the other methods. Is the `History` class doing two things?

3. The `calculate_result_from_history` method in the History class needs to be refactored into a new `Calculator` class. Create a new `Calculator` class that has the following methods:

- `result`: calculate the result from operation in the history object
- `operation_count`: calculates the number of operations in the history object

4. With the creation of the new `Calculator` class, duplicate functionality needs to removed from the History class. You will need to update all implementations of the History class, `HistoryCustomObject` and `HistoryDict`.

The new `Calculator` class will increase cohesion and reduce coupling between how the history of calculator operations is manage and the analysis of those operations. 

4. Update the code to use this new class to display the result and operation count. Add a new command named `result` for displaying the result and the number of operations. Review how operations such as `command_show_history` and `command_clear_history` are structured in the program.


