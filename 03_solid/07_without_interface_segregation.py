from abc import ABC, abstractmethod


class UserManager(ABC):
    @abstractmethod
    def add_user(self) -> None:
        pass

    @abstractmethod
    def delete_user(self) -> None:
        pass

    @abstractmethod
    def generate_report(self) -> None:
        pass


class AdminUserManager(UserManager):
    def add_user(self) -> None:
        print("User added")

    def delete_user(self) -> None:
        print("User deleted")

    def generate_report(self) -> None:
        print("Report generated")


class ClientUserManager(UserManager):
    def add_user(self) -> None:
        # Not relevant for this client
        pass

    def delete_user(self) -> None:
        # Not relevant for this client
        pass

    def generate_report(self) -> None:
        print("Report for client generated")


def print_user_reports(user_manager: UserManager) -> None:
    print(user_manager.generate_report())


print_user_reports(ClientUserManager())
print_user_reports(AdminUserManager())
