from abc import ABC, abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self, r):
        pass

class SBI(RBI):

    def display(self):
        print("This is SBI.")

    def roi(self, r):
        print("roi in SBI is: ", r)

class AXIS(RBI):

    def display(self):
        print("This is AXIS.")

    def roi(self, r):
        print("roi in AXIS is: ",r)

class HDFC(RBI):

    def display(self):
        print("This is HDFC.")

    def roi(self, r):
        print("roi in HDFC is: ", r)

a1=SBI()
a1.display()
a1.roi(6)

print("-"*40)

a2=AXIS()
a2.display()
a2.roi(7)

print("-"*40)

a3=HDFC()
a3.display()
a3.roi(7.5)
