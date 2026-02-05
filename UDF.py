##UDF- User Defined Function


def oddeven(a):
    if a%2==0:
        print(a, "is Even")
    else:
        print(a, " is Odd")
        
##oddeven(5)

def maxof2(a,b):
    if a>b:
        print(a, "is Max")
    else:
        print(b, "is Max")
        
##maxof2(14,17)

def maxof3(a,b,c):
    if a>b:
        if a>c:
            print(a, "is Max")
        else:
            print(c, "is Max")
##    else:
##        if b>c:
##            print(b, "is Max")
##        else:
##            print(c, "is Max")
    elif b>c:
        print(b, "is Max")
    else:
        print(c, "is Max")

##maxof3(5,6,7)
##maxof3(6,5,7)
##maxof3(15,17,16)

def fibonacci(n):
    a,b=0,1
    print(a, end=" ")
    while b<n:
        print(b, end=" ")
##      print(b, end=",")
        a,b=b,a+b
    print()

##fibonacci(56)


def prime(n):
    if n%2!=0:
        for i in range(3, int(n/2)+1, 2):
            if n%i==0:
                print(n, "is not Prime.")
                break
        else:
            print(n, "is Prime.")
    else:
        prime(n, "is not Prime.")

##prime(37)
##prime(57)
                
