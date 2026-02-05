list = [1,2,3,4,5,6,7,8,9]
list2 = []
list3 = []

def cube(x):
    return x*x*x

for i in list:
    list2.append(cube(i))

print(list2)
print(list)

for j in list2:
##    list3 = list(filter(lambda j: j % 2 == 0, list2))
    list3.append(filter(lambda j: j % 2 == 0, list2))
print(list3)
