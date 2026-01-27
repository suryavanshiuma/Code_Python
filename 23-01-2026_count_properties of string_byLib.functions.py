
##string is TOPS Technologies 27012026

s=input("ENTER STRING: ")

al, nm, uc, lc, sp = 0, 0, 0, 0, 0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1

print("Number of alphabets:", al)
print("Number of Numericals:", nm)
print("Number of Space:", sp)
print("Number of Uppercase:", uc)
print("Number of Lowercase:", lc)
    
