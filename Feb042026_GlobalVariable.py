#global Variable


def myfunction():
    print(name)

name="Python"

myfunction()

print("-"*50)

def myfunction1():
    global name1
    print("1st", name1)
    
    name1="Python Language"
    print("2nd", name1)

name1="Python"

myfunction1()

print("3rd", name1)
