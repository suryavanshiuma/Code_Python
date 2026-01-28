##print list where range is 2000 to 3200
##and element of list should be multiplied by 5, however it cannot be divided by 7.

l=[]

for i in range (2000, 3201):
    if i%7!=0 and i%5==0:
        l.append(i)
print(l)
