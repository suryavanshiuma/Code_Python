class Bank12():

    def openAccount12(self,acn1,cname1,bal1):
        self.acno1=acn1
        self.cnam1=cname1
        self.balance1=bal1

    def prntInputs12(self):
        print("Account No.: ", self.acno1)
        print("Customer Name: ", self.cnam1)
        print("Balance: ", self.balance1)
        
t1=Bank12()

t1.openAccount12(105,"Uma",6000)
t1.prntInputs12()

print()
print("*-"*30)
print()

class Bank():

    def accountDetails(self,acno,ahname,acbal):
        self.acno=acno
        self.ahname=ahname
        self.acbal=acbal
        print("Hello!",ahname,", Available Balance in Your Bank Account No.",acno,"is Rs.",acbal)

    def deposit(self,amount):
        self.acbal=self.acbal+amount
        print("After Deposit",amount,"Rs. Your Account Balance is Rs.", self.acbal)

    def withdraw(self,amount):
        if amount<=self.acbal:
            self.acbal=self.acbal-amount
            print("After Withdrawal Your Account Balance is Rs.",self.acbal)
        else:
            print("Sorry, You Need Another",amount-self.acbal,"Rs. To Withdraw.")

    def checkBalance(self):
        print("Your Current Balance is", self.acbal)

b1=Bank()

b1.accountDetails(105,"Ms. Uma Suryavanshi",6000)

while True:
    print("-"*50)
    print("1. accountDetails")
    print("2. deposit")
    print("3. withdraw")
    print("4. checkBalance")
    print("5. Exit")
    print("-"*50)

    choice=int(input("Enter Your Choice: "))
    print("-"*50)

    if choice==1:
        b1.accountDetails(105,"Uma",6000)

    elif choice==2:
        amount=int(input("Enter Deposit Amount: "))
        b1.deposit(amount)

    elif choice==3:
        amount=int(input("Enter Withdrawal Amount: "))
        b1.withdraw(amount)

    elif choice==4:
        b1.checkBalance()

    elif choice==5:
        print("Thank You For Using Our Services.")
        print("-"*50)
        break
    else:
        print("Invalid Choice. Please Try Again.")

    print("-"*50)


