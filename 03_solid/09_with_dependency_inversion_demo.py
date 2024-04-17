# class PersonFileHandler:

#     def __init__(self, person: Person) -> None:
#         self.person = person

#     def save_to_file(self) -> None:
#         with open("persons.txt", "a") as file:
#             file.write(self.person.name + "\n")

# class PersonJsonFileHandler:

#         def __init__(self, person: Person) -> None:
#             self.person = person

#         def save_to_file(self) -> None:
#             with open("persons.json", "a") as file:
#                 file.write(f'{{"name": "{self.person.name}"}}\n')

# class Person:

#     def __init__(self, name: str) -> None:
#         self.name = name


# person = Person("John")
# person_file_handler = PersonFileHandler(person)
# person_file_handler.save_to_file()

# person_json_file_handler = PersonJsonFileHandler(person)
# person_json_file_handler.save_to_file()
