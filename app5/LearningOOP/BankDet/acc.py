class Account:
    
    
    
    #creates self== object, balance== instance variable
    def __init__(self, filepath):
        
        #creating an attribute to save filepath 
        self.attr_filepath=filepath
        with open(filepath) as file:
            self.balance=int(file.read())


    def print(self):
        print(self.balance)

    
    #not writing to database yet
    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount 

    #writing to database
    def  confirm(self):
        with open(self.attr_filepath, "w") as myfile:
            myfile.write(str(self.balance))

#Inheritance "inherits" from a general class new class is reffered to as
#subclass


#takes Account as a class
class Checking(Account):
    """This is a checking account object with a new trasfer """

    typ="CheckingAccount"
    def __init__(self, filepath,fee):
        Account.__init__(self, filepath)
        self.fee=fee
    
    def transfer(self, money):
        self.balance=self.balance-money-self.fee




avyanshscash=Account("balance.txt")
#print(avyanshscash) returns object location
#print(avyanshscash.balance)
#avyanshscash.print()

#avyanshscash.withdraw(100)
#avyanshscash.print()
avyanshscash.confirm()



avy_check_cash=Checking("balance.txt",1)

avy_check_cash.transfer(1000)
avy_check_cash.confirm()
avy_check_cash.print()
print(avy_check_cash.__doc__)

# Account = class
# avy_check_cash = object instance
# confirm is instance variable
# """This is a checking account object with a new trasfer """ == docstring
# init==constructor
# transfer == methad
# instantiation is creating object class avy_check_cash=Checking("balance.txt",1)
# datamember are class variables and instance variables
# attribute of a class is class instance