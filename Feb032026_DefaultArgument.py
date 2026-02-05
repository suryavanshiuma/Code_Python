def test(a,b,c,d):
    print("A:",a, "B:",b, "C:",c, "D:",d)

test(10,20,50,40)

def test1(a=40,b=30,c=20,d=10):
    print("A:",a, "B:",b, "C:",c, "D:",d)

test1(b=100,d=200)#this is KEYWORD ARGUMENT

def test2(a,b,c,*d,**e):
    print("A:",a, "B:",b, "C:",c, "D:",d, "E:",e)#ARBITRARY ARGUMENT

test2(1,2,3,4,5,6,7,8,9,x=10,y=20,z=30)
    

    
