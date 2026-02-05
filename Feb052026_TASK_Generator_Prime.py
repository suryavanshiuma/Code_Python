def prime(n):
    if n%2!=0:
        for i in range(3, (n/2)+1, 2):
            if n%i!=0:
                list1.append(n)
print(list1)
##
##pri=prime(11)
##for num in pri:
##    print(pri)
