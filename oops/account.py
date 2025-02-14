class Account():
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f'Amount : {amount} is deposited successfully to your account. \n Available balance {self.balance}'
    
    def withdraw(self, amount):
        if (self.balance <= amount):
            return 'Insufficient funds'
        self.balance -= amount
        return f'Amount : {amount} withdrawn successfully from your account. \n Available balance {self.balance}'
    
    def __str__(self):
        return f"Owner {self.owner} has funds {self.balance}"


account = Account('Prashanth Sagari', 1000)
print(account)
# print(account.deposit(20))
# print(account.withdraw(500))
    
        
        
    