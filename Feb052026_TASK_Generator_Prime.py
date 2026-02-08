
def prime(n):
    for num in range(2,n+1):

        if num%2!=0:
            for i in range(3,int(num/2)+1,2):
                if num%i==0:
                    break
            else:
                yield num

for j in prime(10):
    print(j, end=" ")


##
##print("-"*40)
##
##
##
##list1=[]
##list2=[]
##def prime(m):
##    for n in range(2, m+1):
##        if n%2!=0:
##            for i in range(3, int(n/2)+1, 2):
##                if n%i!=0:
##                    list1.append(n)
##                else:
##                    list2.append(n)
##
##prime(15)
##print(list1)
##print(list2)
