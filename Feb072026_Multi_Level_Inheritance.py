#   MULTI LEVEL INHERITANCE:

class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A: ",self.a)

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B: ",self.b)

class C(B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C: ",self.c)

c1=C()

c1.getC(300)
c1.getB(200)
c1.getA(400)
c1.putC()
c1.putB()
c1.putA()
    
