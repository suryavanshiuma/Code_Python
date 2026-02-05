#Normally wht we do/Normal Function

def cube(x):
    return x*x*x

ans=cube(5)
print("Cube of",5, "is", ans)

print("-"*40)

#Using Lambda Function instead of any other function to get output

ans1=lambda y: y*y*y
print("Cube of",5,"is",ans1(5))

#here same output we got for same formula/logic and wrote two lines of code only using Lambda
#REMEMBER: Lambda function returns the OBJECT of function

#example1 - with two parameters

x=lambda a,b:a*b
print(x(30,20))

#example2 - even odd numbers using Lambda function

result=lambda num:"even" if num%2==0 else "odd"
print(result(7))
print(result(14))
