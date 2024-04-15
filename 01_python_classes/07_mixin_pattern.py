class JSONMixin:
    # key to the mixin pattern is the mixin does not have a constructor
    # there is no __init__ method and the mixin class does not have any instance
    # attributes, and it does not inherit from any other classes that Person
    # or Animal inherit from

    # mixin method names need to be unique across the various related mixins
    # the mixin class can contain multiple methods
    def to_json(self) -> str:
        import json

        return json.dumps(self.__dict__)


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name


class JSONPerson(JSONMixin, Person):
    pass


class JSONAnimal(JSONMixin, Animal):
    pass


p = JSONPerson("Alice", 30)
print(p.to_json())  # Output: {"name": "Alice", "age": 30}

c = JSONAnimal("cat")
print(c.to_json())


class XMLMixin:
    def to_xml(self) -> str:
        from xml.etree.ElementTree import Element, tostring
        from xml.dom import minidom

        elem = Element(self.__class__.__name__)
        for key, value in self.__dict__.items():
            child = Element(key)
            child.text = str(value)
            elem.append(child)
        raw_xml = tostring(elem)
        pretty_xml = minidom.parseString(raw_xml).toprettyxml()
        return pretty_xml


class JSONXMLPerson(JSONMixin, XMLMixin, Person):
    pass


person = JSONXMLPerson("Bob", 40)
print(person.to_json())
print(person.to_xml())
