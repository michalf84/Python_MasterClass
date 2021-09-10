import datetime
import pytz

class Account:
    # single acount class with balance

    @staticmethod
    def current_time():
        utc_time=datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self,name,balance):
        self._name=name
        self.__balance=balance
        self._transaction_list=[(Account.current_time(), balance)]
        print("account created for " + self._name)
        self.show_balance()

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amount)) added funciton below
            self._transaction_list.append((Account.current_time(), amount))
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        else:
            print("amount must be greater than zero or balance of account")
            self.show_balance()

    def show_transactions(self):
        for date,amount in self._transaction_list:
            if amount>0:
                tran_type="deposit"
            else:
                tran_type="withdrawa"
                amount*=-1
            print("{:6} {} on {} (local time was {})".format(amount,tran_type,date,date.astimezone()))

    def show_balance(self):
        print("balance is {}".format(self.__balance))

if __name__=="__main__":
    tim=Account("TIm",0)
    tim.show_balance()

    tim.deposit(10000)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()
    tim.show_transactions()

    steph=Account("sTEPH",800)
    steph.deposit(400)
    steph.withdraw(32)
    steph.show_balance()
    steph.show_transactions()
    steph.__balance=-22 #balance won't change
    steph.show_balance()
    print(steph.__dict__) #check _name of attrbiute does not have class infront
    steph._Account__balance=40 #i can override it
    steph.show_balance()

