# Adapter Pattern
#
# Allows incompatible interfaces to work together. This makes one class look
# like another class by providing a wrapper around it.


class AccelebrateTrainingCompany:
    def performing_eval(self) -> None: ...

    def student_report(self) -> None: ...


class ExitCertifiedTrainingCompany:
    def capturing_eval(self) -> None: ...

    def training_report(self) -> None: ...


class AxcelILTTrainingCompany:
    def performing_eval(self) -> None: ...

    def generate_report(self) -> None: ...


def print_report(companies: list[AxcelILTTrainingCompany]) -> None:
    for company in companies:
        company.generate_report()


class AccelebrateAdapter(AxcelILTTrainingCompany):
    def __init__(self, accelebrate: AccelebrateTrainingCompany) -> None:
        self.accelebrate = accelebrate

    def generate_report(self) -> None:
        self.accelebrate.student_report()


class ExitCertifiedAdapter(AxcelILTTrainingCompany):
    def __init__(self, exit_certified: ExitCertifiedTrainingCompany) -> None:
        self.exit_certified = exit_certified

    def generate_report(self) -> None:
        self.exit_certified.training_report()


# Client code
accelebrate = AccelebrateTrainingCompany()
accelebrate.performing_eval()

exit_certified = ExitCertifiedTrainingCompany()
exit_certified.capturing_eval()

accelebrate_adapter = AccelebrateAdapter(accelebrate)
exit_certified_adapter = ExitCertifiedAdapter(exit_certified)

print_report([accelebrate_adapter, exit_certified_adapter])


# class OldSystem:
#     def old_request(self) -> str:
#         return "Old System Request"


# class NewSystem:
#     def request(self) -> str:
#         return "New System Request"


# class Adapter(NewSystem):
#     def __init__(self, old_system: OldSystem) -> None:
#         self.old_system = old_system

#     def request(self) -> str:
#         return self.old_system.old_request()


# Client code
# old_system = OldSystem()
# adapter = Adapter(old_system)
# print(adapter.request())  # Output: Old System Request
