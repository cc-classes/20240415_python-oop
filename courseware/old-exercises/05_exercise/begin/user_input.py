def get_command() -> str:
    return input("Enter a command > ")


def get_entry_id_to_remove() -> int:
    return int(input("Enter an entry id to remove > "))


def get_operand() -> float:
    return float(input("Enter an operand > "))


def get_save_file_name() -> str:
    return input("Enter a file name to save the history to > ")
