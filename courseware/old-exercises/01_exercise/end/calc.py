from typing import Any
from history import History


def calc_app(math_ops: dict[str, Any]) -> None:
    history = History(math_ops)
    while True:
        command = input("Enter a command > ")

        if command in math_ops:
            operand = float(input("Enter an operand > "))
            history.append_history_entry(command, operand)

            print(f"Result: {history.calculate_result_from_history()}")
            continue
        elif command == "history":
            for entry in history:
                print(f"{entry.id} {entry.name} { entry.operand}")
        elif command == "remove":
            entry_id = int(input("Enter an entry id to remove > "))
            history.remove_history_entry(entry_id)
        elif command == "clear":
            history.clear_history_entries()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


math_ops = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y,
    "pow": lambda x, y: x ** y,
}


calc_app(math_ops)
