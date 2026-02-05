'''
IF CONDITION

1. Simple if

    if condition:
        statement

2. if/else

    if condition:
        statement
    else:
        statement

3. Nested if

    if condition:
        statement

        if condition:
            statement
        else:
            statement

    else:
        statement

4. Ladder if

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
'''

a=int(input("Enter A:"))
if a>0:
    print("A is Positive Number")

else:
        print("A is Negative Number")
