##JUMPING STATEMENT : BREAK

print("I:", end=" ")
for i in range (1,10):
    if i==5:
        break
    else:
        
        print(i, end=" ")



print()

print("-------------------------------------------------")

##JUMPING STATEMENT : CONTINUE

print("I:", end=" ")
for i in range (1, 10):
    if i==5:
        continue
    else:
        print(i, end=" ")

print()

print("-------------------------------------------------")

print("I:", end=" ")
for i in range (1, 10):
    if i!=5:
        continue
    else:
        print(i, end=" ")

print()

print("-------------------------------------------------")

print("I:", end=" ")
for i in range (1, 10):
    if i>5:
        break
    else:
        print(i, end=" ")

print()

print("-------------------------------------------------")

print("I:", end=" ")
for i in range (6, 10):
    if i<5:
        break
    else:
        print(i, end=" ")        
