# Adapter Pattern
#
# Allows incompatible interfaces to work together. This makes one class look
# like another class by providing a wrapper around it.


class OldSystem:
    def old_request(self) -> str:
        return "Old System Request"


class NewSystem:
    def request(self) -> str:
        return "New System Request"


class Adapter(NewSystem):
    def __init__(self, old_system: OldSystem) -> None:
        self.old_system = old_system

    def request(self) -> str:
        return self.old_system.old_request()


# Client code
old_system = OldSystem()
adapter = Adapter(old_system)
print(adapter.request())  # Output: Old System Request
