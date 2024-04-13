from typing import Protocol


class UserOperations(Protocol):
    def add_user(self) -> None:
        pass

    def delete_user(self) -> None:
        pass


class ReportGeneration(Protocol):
    def generate_report(self) -> None:
        pass


class AdminUserManager:
    def add_user(self) -> None:
        print("User added")

    def delete_user(self) -> None:
        print("User deleted")

    def generate_report(self) -> None:
        print("Report generated")


class ClientReportManager:
    def generate_report(self) -> None:
        print("Report for client generated")


def print_user_reports(user_manager: ReportGeneration) -> None:
    user_manager.generate_report()


print_user_reports(ClientReportManager())
print_user_reports(AdminUserManager())
