# it restricts access to certain attribute
# methods to prevent direct modification
class BankAccount:

    def __init__(self,balance):
        self.balance=balance
    def deposit (self,amount):
        if amount>0:
            self.balance +-amount
    def get_balance(self):
        return self.balance
account=BankAccount(7500)
accountdeposit=(360)
print("balance",account.get_balance())