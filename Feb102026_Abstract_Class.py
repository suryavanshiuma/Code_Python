from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def show(self):
        pass

class B(A):

    def display(self):
        print("Display From B.")

    def show(self):
        print("Show Defined In CLASS B.")

class C(A):

    def showmsg(self):
        print("showmsg from C.")

    def show(self):
        print("Show from CLASS C.")

b1=B()
b1.display()
b1.show()

print("-"*40)

c1=C()
c1.showmsg()
c1.show()


