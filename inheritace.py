# inheritance allows one class to inherit attributes and methods from another class
class Animal:
    def __init__(self,name):
        self.name=name
    def speaks(self):
        pass
class dog(Animal):
    def speaks(self):
        return "woofs"
class cat(Animal):
    def speaks(self):
        return "meows"
# this are objects
doggy=dog("buddy")
cat=cat("uscat")
print(doggy.speaks())
print(cat.speaks())