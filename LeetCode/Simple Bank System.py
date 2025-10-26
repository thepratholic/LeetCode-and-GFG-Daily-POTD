from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.account_balance = balance
        self.total_accounts = len(self.account_balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1

        if (account1 >= self.total_accounts or account1 < 0) or (account2 >= self.total_accounts or account2 < 0):
            return False


        if money <= self.account_balance[account1]:
            self.account_balance[account2] += money
            self.account_balance[account1] -= money
            return True
        
        return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if (account >= self.total_accounts or account < 0):
            return False

        else:
            self.account_balance[account] += money
            return True
        

    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if (account >= self.total_accounts or account < 0) or self.account_balance[account] < money:
            return False

         
        else:
            self.account_balance[account] -= money
            return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)