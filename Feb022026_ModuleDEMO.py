import UDF

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. Max of 2")
    print("3. Max of 3")
    print("4. Fibonacci")
    print("5. Prime")
    print("6. Exit")
    print("*"*40)

    choice=int(input("Enter Your Choice:"))
    print("*"*40)

    if choice==1:
        n1=int(input("Enter Number:"))
        UDF.oddeven(n1)

    elif choice==2:
        n1=int(input("Enter First Number:"))
        n2=int(input("Enter Second Number:"))
        UDF.maxof2(n1,n2)

    elif choice==3:
        n1=int(input("Enter First Number:"))
        n2=int(input("Enter Second Number:"))
        n3=int(input("Enter Third Number:"))
        UDF.maxof3(n1, n2, n3)

    elif choice==4:
        n1=int(input("Enter Number:"))
        UDF.fibonacci(n1)

    elif choice==5:
        n1=int(input("Enter Number:"))
        UDF.prime(n1)

    elif choice==6:
        print("Thank You For Using Our Services.")
        break
    else:
        print("Invalid choice. Please try again.")

print("*"*40)
        
