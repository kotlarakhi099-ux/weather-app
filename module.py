class account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no

       
    def debit(self,amount):
            self.balance-=amount
            print("total:",self.balance)

    def credit(self,amount):
         self.balance+=amount
         print("total:",self.balance)


    def get_bal(self):
         return self.balance

ac1_no=int(input("enter account no:"))
if(ac1_no==12345):
     print("you are allowed")
     ac1=account(1000,ac1_no)
ac1.debit(400)
ac1.credit(700)
print("total bal:",ac1.get_bal())
