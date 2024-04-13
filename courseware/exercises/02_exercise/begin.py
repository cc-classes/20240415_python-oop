
class BankAccount:
    ...

class SavingsAccount(BankAccount):
    ...

class CheckingAccount(BankAccount):
    ...

def perform_transactions(account: BankAccount) -> None:
    account.deposit(1000)
    account.withdraw(500)
    account.display_balance()

def main() -> None:
    
  accounts: list[BankAccount] = [
      SavingsAccount("SA001", 1000),
      CheckingAccount("CA001", 1000),
      BankAccount("BA001", 1000)
  ]

  for account in accounts:
      print(f"Performing transactions for {type(account).__name__}:")
      perform_transactions(account)
      print()
    

if __name__ == "__main__":
    main()