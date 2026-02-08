print("Hello")
print("Please Enter Your Details As Per Requested")
customer_name=input("Enter Your Name: ")
customer_contact=int(input("Enter Your Contact Number: "))

c_data=[]
c_data.append(customer_name)
c_data.append(customer_contact)


#function name should be start with smallcase, helps to identify functn effortlessly.
    
def punjabi():

            while True:
                print("1. punjabi1")
                print("2. punjabi2")
                print("3. punjabi3")
                print("4. punjabi4")
                print("5. Exit")
                print("-"*50)

                choice=int(input("Enter Your Choice: "))
                print("-"*50)
                

                if choice==1:
                    c_data.append(choice)
                    print("Punjabi1 is Successfully Ordered.")
                    

                elif choice==2:
                    c_data.append(choice)
                    print("Punjabi2 is successfully ordered.")
                    

                elif choice==3:
                    c_data.append(choice)
                    print("Punjabi3 is successfully ordered.")
                    

                elif choice==4:
                    c_data.append(choice)
                    print("Punjabi4 is successfully ordered.")
                    

                elif choice==5:
                    c_data.append(choice)
                    print("Thank You For Using Our Sevices.")
                    break
                    

                else:
                    print("Invalid Choice. Try Again.")
                    

def chinese():

    while True:
                print("1. chinese1")
                print("2. chinese2")
                print("3. chinese3")
                print("4. chinese4")
                print("5. Exit")
                print("-"*50)

                choice=int(input("Enter Your Choice: "))
                print("-"*50)
                

                if choice==1:
                    c_data.append(choice)
                    print("chinese1 is Successfully Ordered.")
                    

                elif choice==2:
                    c_data.append(choice)
                    print("chinese2 is successfully ordered.")
                    

                elif choice==3:
                    c_data.append(choice)
                    print("chinese3 is successfully ordered.")
                    

                elif choice==4:
                    c_data.append(choice)
                    print("chinese4 is successfully ordered.")
                    

                elif choice==5:
                    c_data.append(choice)
                    print("Thank You For Using Our Sevices.")
                    break
                    

                else:
                    print("Invalid Choice. Try Again.")
                                

def italian():

    while True:
                print("1. italian1")
                print("2. italian2")
                print("3. italian3")
                print("4. italian4")
                print("5. Exit")
                print("-"*50)

                choice=int(input("Enter Your Choice: "))
                print("-"*50)
                

                if choice==1:
                    c_data.append(choice)
                    print("italian1 is Successfully Ordered.")
                    

                elif choice==2:
                    c_data.append(choice)
                    print("italian2 is successfully ordered.")
                    

                elif choice==3:
                    c_data.append(choice)
                    print("italian3 is successfully ordered.")
                    

                elif choice==4:
                    c_data.append(choice)
                    print("italian4 is successfully ordered.")
                    

                elif choice==5:
                    c_data.append(choice)
                    print("Thank You For Using Our Sevices.")
                    break
                    
                else:
                    print("Invalid Choice. Try Again.")
                                

def gujarati():

    while True:
                print("1. gujarati1")
                print("2. gujarati2")
                print("3. gujarati3")
                print("4. gujarati4")
                print("5. Exit")
                print("-"*50)

                choice=int(input("Enter Your Choice: "))
                print("-"*50)
                

                if choice==1:
                    c_data.append(choice)
                    print("gujarati1 is Successfully Ordered.")
                    

                elif choice==2:
                    c_data.append(choice)
                    print("gujarati2 is successfully ordered.")
                    

                elif choice==3:
                    c_data.append(choice)
                    print("gujarati3 is successfully ordered.")
                    

                elif choice==4:
                    c_data.append(choice)
                    print("gujarati4 is successfully ordered.")
                    

                elif choice==5:
                    c_data.append(choice)
                    print("Thank You For Using Our Sevices.")
                    break
                    
                else:
                    print("Invalid Choice. Try Again.")
                                

def southindian():

    while True:
                print("1. southindian1")
                print("2. southindian2")
                print("3. southindian3")
                print("4. southindian4")
                print("5. Exit")
                print("-"*50)

                choice=int(input("Enter Your Choice: "))
                print("-"*50)
                

                if choice==1:
                    c_data.append(choice)
                    print("southindian1 is Successfully Ordered.")
                    

                elif choice==2:
                    c_data.append(choice)
                    print("southindian2 is successfully ordered.")
                    

                elif choice==3:
                    c_data.append(choice)
                    print("southindian3 is successfully ordered.")
                    

                elif choice==4:
                    c_data.append(choice)
                    print("southindian4 is successfully ordered.")
                    

                elif choice==5:
                    c_data.append(choice)
                    print("Thank You For Using Our Sevices.")
                    break
                    
                else:
                    print("Invalid Choice. Try Again.")
                                

while True:
    print("-"*50)
    print("1. Punjabi")
    print("2. Chinese")
    print("3. Italian")
    print("4. Gujarati")
    print("5. SouthIndian")
    print("6. Exit")
    print("-"*50)

    choice=int(input("Enter Your Choice: "))
    print("-"*50)

    if choice==1:
        c_data.append(choice)
        punjabi()
        break
        
    elif choice==2:
        c_data.append(choice)
        chinese()
        break

    elif choice==3:
        c_data.append(choice)
        italian()
        break

    elif choice==4:
        gujarati()
        c_data.append(choice)
        break

    elif choice==5:
        c_data.append(choice)
        southindian()
        break

    elif choice==6:
        c_data.append(choice)
        print("Thank You For Using Our Services.")
        print("-"*100)
        break

    else:
        print("Invalid Choice. Please, Try Again.")
    
print(c_data)
