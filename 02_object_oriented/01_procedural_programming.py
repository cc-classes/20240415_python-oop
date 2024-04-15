# Procedural Programming - where there is a hard division
# between data and code (logic)


# logic = behavior = method = function
def speak(animal_name: str) -> str:
    return f"{animal_name} says Woof!"


# data
animal_name = "Rover"

print(speak(animal_name))  # Output: Rover says Woof!
