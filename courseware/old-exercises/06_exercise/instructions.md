# Exercise 6 - Update CalcApp to use the Builder Pattern

## Instructions

You are encouraged to review the solution as you complete the exercise. You may use Google and ChatGPT to ask general questions to complete the exercises.

**Important:** If a requirement is confusing or seems to be in error, please ask the instructor to confirm. Do not lose a ton of time because something seems off, please ask!

## Requirements

1. In a terminal, from the `begin` folder, run the calculator program.

```bash
python ./calc.py
```

2. Create a new class named `ConsoleCommands` to organize the command functions. When creating the `ConsoleCommands` think about the relationship between the `History` and `Calculator` classes. How should the `ConsoleCommands` class be designed and integrated with the `History` and `Calculator` classes to reduce coupling and increase cohesion?

3. Upgrade the `CalcApp` class to use the Builder Pattern for passing in an instance of the `History` class, the `Calculator` class, and the new `Command` class.
