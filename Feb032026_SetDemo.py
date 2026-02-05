s={1,2,3,1.1,2.2,"tops",True,"Python",10,20,1,2,4}

print(s)

s.add(100)
print(s)

s.discard(10)
print(s)

s.pop()#this will remove first element of set
print(s)

s.remove(2.0)
print(s)

s.remove(20)
print(s)

s1={100,3, 200,300,500}
s.update(s1)#this will add one set to another set without repeating element
print(s)
