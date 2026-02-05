l=[1, 2, 1.1, 2.2, "tops", True, 10, 20,"Python", False, 90.90, 1, 2]

print(l)
l.append(100)
print(l)
##l.clear()
##print(l)
l1=l.copy()
print(l1)
print(l.count(1)) 
## print(l.count(1)) means it will count for all the one as value existing
##in the list L - here 1, True, 1
l2=[1000, 2000, 3000]
l.extend(l2)
print(l)
##append is used to add single value to the end of the list, however extend adds the whole list to end of another list.
print(l.index(10))
##print(l.index(10)) will print the index number of value 10
l.insert(5,101)
print(l)
##l.insert(5,101) will add 101 in list with/at index number 5
l.pop()
print(l)
##l.pop() will remove the last value if no index number is written in function 
l.pop(3)
print(l)
##l.pop(3) will remove the value of the index number is written in the function
##like here  l.pop(3), 3 is written in pop function means value in list which comes on 3rd place will be removed
l.remove(10)
print(l)
##l.remove(10) will remover 10 as value in list
l.reverse()
print(l)
