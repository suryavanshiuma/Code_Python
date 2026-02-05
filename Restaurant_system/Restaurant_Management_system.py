print("Hello")
print("Please Enter Your Details As Per Requested")
customer_name=input("Enter Your Name: ")
customer_contact=int(input("Enter Your Contact Number: "))

while True:
    print("-"*100)
    print("1. Punjabi")
    print("2. Chinese")
    print("3. Italian")
    print("4. Gujarati")
    print("5. SouthIndian")
    print("6. Fastfood")
    print("-"*100)

    choice=int(input("Enter Your Choice: "))
    print("-"*100)

    if choice==1:
        RestaurantMenu.Punjabi()
        
    

    
    

    break
