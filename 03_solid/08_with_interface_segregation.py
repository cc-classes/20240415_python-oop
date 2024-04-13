from abc import ABC, abstractmethod


class UserOperations(ABC):
    @abstractmethod
    def add_user(self) -> None:
        pass

    @abstractmethod
    def delete_user(self) -> None:
        pass


class ReportGeneration(ABC):
    @abstractmethod
    def generate_report(self) -> None:
        pass


class AdminUserManager(UserOperations, ReportGeneration):
    def add_user(self) -> None:
        print("User added")

    def delete_user(self) -> None:
        print("User deleted")

    def generate_report(self) -> None:
        print("Report generated")


class ClientReportManager(ReportGeneration):
    def generate_report(self) -> None:
        print("Report for client generated")
