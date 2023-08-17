# a class is a blueprint for creating object
# objects are instances of creating a class
class Students:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def sayhello(self):
        print("my name is",self.name,self.gender,"im",self.age,"years")
myobj=Students("shadrack","male",30)
myobje=Students("kosh","male",22)
myobjec=Students("korir","female",30)
myobjec.sayhello()
myobje.sayhello()
myobj.sayhello()