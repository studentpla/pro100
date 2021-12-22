class ATM (object):
    def __init__(self, savings, current, cash, cashwithdrawl,balanceenquiry):
        self.savings =savings
        self.current = current
        self.cash = cash
        self.cashwithdrawl  = cashwithdrawl
        self.balanceenquiry = balanceenquiry
    def cardno (self):
        print("2010")
    def pinno (self):
        print("1598")
    
#declaring an object
john = ATM("yes", "no",400,"axis","no")
jane = ATM ("no","yes",120,"SBI","yes")
print(john.current)
print(jane.pinno())