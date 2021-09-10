import pytz
class Account(object):

    def __init__(self, name:str,opening_balance:float=0.0):
        self.name=name
        self._balance=opening_balance
        print("account created for {}.".format(self.name),end='')
        self.show_balance()

    def deposit(self,amount:float)->float:
        if amount>0.0:
            new_balance=self._balance+amount
            deposit_time=pytz.utc.localize(datetime.datetime.utcnow())
            db.execute("update accounts set balance= where (name=?)",(new_balance,self.name))
            db.execute("insert into history valoues(?,?,?",(deposit_time,self.name,amount))
            db.commit()
            print("{} deposited".format(amount))
        return self._balance

    def withdraw(self,amount:float)->float:
        if 0<amount<=self._balance:
            self._balance-=amount
            print("{} withdrawn".format(amount))
            return amount
        else:
            print("the amount must be>0")
            return 0.0
    def show_balance(self):
        print("balance on account{} iss {}".format(self.name,self._balance))

if __name__=="__main__":
    john=Account("John")
    john.deposit(10.10)
    john.deposit(0.10)
    john.deposit(0.10)
    john.withdraw(0.30)
    john.withdraw(0)
    john.show_balance()


#note that because of float we get inaccuracy