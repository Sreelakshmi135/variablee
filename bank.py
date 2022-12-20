class bank_account:
    def _init_(self):
        self.balance=0
        print("Welcome to the deposite and withdrawl machine")

    def deposite(self):
        amount=float(input("enter the amount to deposite"))
        self.balance+=amount
        print("/n amount deposite",amount)

    def withdraw(self):
        amount=float(input("enter the amount to withdraw"))
        if self.balance>=amount:
            self.balance-=amount
            print("/n your withdraw amount is ",amount)
        else:
            print("/n insuffficient balance")

    def display(self):
        print("/n net available balance",self.balance)

s=bank_account()
s.deposite()
s.withdraw()
s.display()