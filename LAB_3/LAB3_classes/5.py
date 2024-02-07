class bank_account():
    def __init__(self):
        self.owner="Azamat"
        self.balance=0
    def deposit(self,summa):
        self.balance+=summa
        print(f"Balance:{self.balance} tg")
    def withdraw(self,tg):
        if tg<self.balance:
            self.balance-=tg
            print(f"Removed:{tg} tg -> Remainder balance: {self.balance} tg")
        else: 
            print( "Overdrawn!!!!!")
            print("Missing:",tg-self.balance,"tg")

bank1=bank_account()
bank2=bank_account()
bank3=bank_account()
bank1.deposit(100000)
bank1.withdraw(120000) 
#2
bank2.deposit(35000)
bank2.withdraw(12000) 
#3
bank3.deposit(4000)
bank3.withdraw(12304) 