from threading import Thread
from history import History
from random import randint
from time import sleep


history = History()


def delay() -> float:
    return randint(1, 5) / 2


while True:
    command = input("Enter a command > ")

    if command in ["add", "subtract", "multiply", "divide"]:
        operand = float(input("Enter an operand > "))
        history.append_history_entry(command, operand)
        print(f"Result: {history.result}")
        continue
    elif command == "history":
        for entry in history:
            print(f"{entry.id} {entry.op_name} { entry.op_value}")

    elif command == "history2":
        # alternative implementation of for-in loop
        try:
            history_iter = iter(history)
            while True:
                history_entry = next(history_iter)
                print(history_entry.op_name)
        except StopIteration:
            print("Stop Iterating Over History")
    elif command == "history3":

        def print_history_entries() -> None:
            for entry in history:
                print(f"{entry.id} {entry.op_name} {entry.op_value}")
                sleep(delay())

        history_thread1 = Thread(target=print_history_entries)
        history_thread1.start()

        history_thread2 = Thread(target=print_history_entries)
        history_thread2.start()

        history_thread3 = Thread(target=print_history_entries)
        history_thread3.start()

        history_thread1.join()
        history_thread2.join()
        history_thread3.join()

    elif command == "remove":
        entry_id = int(input("Enter an entry id to remove > "))
        history.remove_history_entry(entry_id)
    elif command == "clear":
        result = 0
        history.clear_entries()
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")
