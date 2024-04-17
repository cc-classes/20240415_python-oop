from typing import Protocol


class Address(Protocol):
    def mailing_label(self) -> str:
        pass


class USAddress:
    def __init__(
        self, street: str, city: str, state: str, zip_code: str
    ) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def mailing_label(self) -> str:
        return f"{self.street}\n" f"{self.city}, {self.state} {self.zip_code}"


class ChineseAddress:
    def __init__(
        self,
        province: str,
        city: str,
        district: str,
        street: str,
        postal_code: str,
    ) -> None:
        self.province = province
        self.city = city
        self.district = district
        self.street = street
        self.postal_code = postal_code

    def mailing_label(self) -> str:
        return (
            f"{self.street}\n"
            f"{self.district}, {self.city}, {self.province}\n"
            f"{self.postal_code}"
        )


class Person:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        address: Address,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def move_residence(self, address: Address) -> None:
        self.address = address

    def __str__(self) -> str:
        return (
            f"{self.first_name} {self.last_name}\n"
            f"{self.address.mailing_label()}"
        )


def main() -> None:
    us_address = USAddress("123 Elm St", "Springfield", "IL", "62701")
    person = Person("John", "Doe", us_address)
    print(person)

    chinese_address = ChineseAddress(
        "Shanghai", "Shanghai", "Pudong", "123 Elm St", "200000"
    )
    person.move_residence(chinese_address)
    print(person)


if __name__ == "__main__":
    main()
