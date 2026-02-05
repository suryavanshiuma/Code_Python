from functools import reduce


#1
# function to add two numbers
def add(x,y):
    return x+y

numbers = [1,2,3,4,5]

result = reduce(add, numbers)
print(result)   #output: 15


print("-"*50)

#2
# 100 is the initializer here
# calculation will be like 100+1+2+3+4+5=115
result = reduce(add, numbers, 100)
print(result)   #output: 115
