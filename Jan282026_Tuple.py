##Tuple - Fixed List
##Data/Elements cannot be changed.
##Round brackets are used to represent Tuple.
##
##Tuple - Ordered, Fixed collection of values.

t= (1, 2, 1.1, 2.2, "tops", True, [100, 200, 300], "python", 10, 20, 30, 1, 2, 3)
print(t)

print(t.count(1))
print(t.index(10))
print(t.index(1.1))

print("----------------------------------------")
print(t.index(True))
print("----------------------------------------")
for i in t:
    print(i)

print("----------------------------------------")

print(100 in t)

print("----------------------------------------")
print(t[6])

print("----------------------------------------")
t[6].append(400)
print(t)
