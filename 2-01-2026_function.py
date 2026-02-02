## In Python any function is defined with def keyword
##Function with No Argument and No Return Value:

def printLine(): #() - Parameter
    print("*"*50)

##printLine()
##print("\nWelcome to User Defined function in Python.")
##printLine()


printLine()
print("Welcome to User Defined function in Python.")
printLine()


##Function with Argument but No Return Value:

def add(a,b):
    print("Addition:", a+b)

printLine()
add(10,20)
printLine()


##Function with Argument and Return Value:

def sub(a,b):
    return a-b

##METHOD1
printLine()
print("Subtraction:", sub(10,20))
printLine()

##METHOD2
printLine()
ans=sub(10,20)
print("Subtraction:", ans)
printLine()
