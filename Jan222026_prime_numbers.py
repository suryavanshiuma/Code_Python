num=int(input("Enter N: "))

if num%2!=0:
    for i in range (3, int(num/2)+1, 2):
        if num%i==0:
            print(num, "is not prime")
    else:
        print(num, "is Prime")
else:
    print(num, "is not prime")
        
    
