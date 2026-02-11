class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        super().show()
        print("Show from B")

class C(A):
    def show(self):
        super().show()
        print("Show from C")

class D(C,B):
    def show(self):
        super().show()
        print("Show from D")

d1=D()
d1.show()


print("-"*40)

class A1:
    def show(self):
        print("Show from A")

class B1(A1):
    def show(self):
        super().show()
        print("Show from B")

class C1(A1):
    def show(self):
        super().show()
        print("Show from C")

class D1(B1,C1):
    def show(self):
        super().show()
        print("Show from D")

d2=D1()
d2.show()
