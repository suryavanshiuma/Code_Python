class Tops():

    def getData(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def putData(self):
        print("First Name:", self.fname)
        print("Last Name:", self.lname)

t1=Tops()

t1.getData("Uma","Suryavanshi")
t1.putData()


print("-"*40)


t1=Tops()
t2=Tops()
t1.getData("Kinjal","Patel")
t2.putData()
