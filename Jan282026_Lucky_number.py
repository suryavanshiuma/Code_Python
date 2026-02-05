import random

##print (random.randint(1000, 9999))
##print (random.randint(100000, 999999))
##
##print(random.choice([1, 2, 1.1, 2.2, "tops", "python", True, False]))

##two functions have been used here named: randint and choice

##task is print 1 to 100 in list L
##Now another list Lucky will have 10 random numbers from L,
##however whtever the numbers will be printed to Lucky will be automatically removed from L.

l=[]
Lucky=[]

for i in range (1, 101):
    l.append(i)



for i in range (10):
    num=random.choice(l)
    Lucky.append(num)
    l.remove(num)

print(l)
print(Lucky)
