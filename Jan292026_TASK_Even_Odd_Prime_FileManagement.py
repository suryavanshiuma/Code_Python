import random

data=open("data.txt","w")

for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()

data=open("data.txt", "r")
even=open("even.txt", "w")
odd=open("odd.txt", "w")
prime=open("prime.txt", "w")

l=data.read().split(",")[ :-1]

for i in l :
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")

    if int(i)%2!=0:
        for j in range(3, int(int(i)/2)+1, 2):
            if int(i)%j==0:
                break
        else:
                prime.write(i+",")

data.close()
even.close()
odd.close()
prime.close()


print("Data File Content")
data=open("data.txt", "r")
print(data.read())
data.close()

print("even File content :", end=" ")
even=open("even.txt","r")
print(even.read())
even.close()

print("odd file content :", end=" ")
odd=open("odd.txt","r")
print(odd.read())
odd.close()

print("prime file content :", end=" ")
prime=open("prime.txt","r")
print(prime.read())
prime.close()



          
