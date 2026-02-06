print("Hello")
print("Please Enter Your Details As Per Requested")
customer_name=input("Enter Your Name: ")
customer_contact=int(input("Enter Your Contact Number: "))

#function name should be start with smallcase, helps to identify functn effortlessly.

def punjabi():
    print("punjabi1")
    print("punjabi2")
    print("punjabi3")
    print("punjabi4")

def chinese():
    print("Chinese1")
    print("Chinese2")
    print("Chinese3")
    print("Chinese4")
    

def italian():
    print("Italian1")
    print("Italian2")
    print("Italian3")
    print("Italian4")

def gujarati():
    print("Gujarati1")
    print("Gujarati2")
    print("Gujarati3")
    print("Gujarati4")

def southindian():
    print("SouthIndian1")
    print("SouthIndian2")
    print("SouthIndian3")
    print("SouthIndian4")


while True:
    print("-"*100)
    print("1. Punjabi")
    print("2. Chinese")
    print("3. Italian")
    print("4. Gujarati")
    print("5. SouthIndian")
    print("6. Exit")
    print("-"*100)

    choice=int(input("Enter Your Choice: "))
    print("-"*100)

    if choice==1:
        punjabi()
        
    elif choice==2:
        chinese()

    elif choice==3:
        italian()

    elif choice==4:
        gujarati()

    elif choice==5:
        southindian()

    elif choice==6:
        print("Thank You For Using Our Services.")
        print("-"*100)
        break

    else:
        print("Invalid Choice. Please, Try Again.")
    
