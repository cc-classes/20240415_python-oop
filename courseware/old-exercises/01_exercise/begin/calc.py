from typing import Any


result = 0.0
history: list[dict[str, Any]] = []

while True:
    command = input("Enter a command > ")

    if command == "add":
        operand = float(input("Enter an operand > "))
        result = result + operand

        entry_ids = [entry["id"] for entry in history]

        if len(entry_ids) == 0:
            next_entry_id = 1
        else:
            next_entry_id = max(entry_ids) + 1

        history.append(
            {"id": next_entry_id, "name": command, "operand": operand}
        )

        print(f"Result: {result}")
        continue
    elif command == "subtract":
        operand = float(input("Enter an operand > "))
        result = result - operand

        entry_ids = [entry["id"] for entry in history]

        if len(entry_ids) == 0:
            next_entry_id = 1
        else:
            next_entry_id = max(entry_ids) + 1

        history.append(
            {"id": next_entry_id, "name": command, "operand": operand}
        )

        print(f"Result: {result}")
        continue
    elif command == "multiply":
        operand = float(input("Enter an operand > "))
        result = result * operand

        entry_ids = [entry["id"] for entry in history]

        if len(entry_ids) == 0:
            next_entry_id = 1
        else:
            next_entry_id = max(entry_ids) + 1

        history.append(
            {"id": next_entry_id, "name": command, "operand": operand}
        )

        print(f"Result: {result}")
        continue
    elif command == "divide":
        operand = float(input("Enter an operand > "))
        result = result / operand

        entry_ids = [entry["id"] for entry in history]

        if len(entry_ids) == 0:
            next_entry_id = 1
        else:
            next_entry_id = max(entry_ids) + 1

        history.append(
            {"id": next_entry_id, "name": command, "operand": operand}
        )

        print(f"Result: {result}")
        continue
    elif command == "history":
        for entry in history:
            print(f"{entry['id']} {entry['name']} { entry['operand']}")
    elif command == "remove":
        entry_id = int(input("Enter an entry id to remove > "))
        for entry in history:
            if entry["id"] == entry_id:
                history.remove(entry)
                break
    elif command == "clear":
        result = 0
        history = []
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")