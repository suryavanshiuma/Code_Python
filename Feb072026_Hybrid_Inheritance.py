#   HYBRID INHERITANCE

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

class D(A):
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D: ",self.d)

class C(B,D):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C: ",self.c)

c1=C()

c1.getA(25)
c1.getB(45)
c1.getC(35)
c1.getD(75)
c1.putA()
c1.putC()
c1.putB()
c1.putD()
