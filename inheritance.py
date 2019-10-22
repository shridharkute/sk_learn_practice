#!/usr/bin/python3

class myparents():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printname(self):
        print(self.name, self.age)


S = myparents("shridhar", 35)
S.printname()


class kid(myparents):
    def __init__(self,name,age):
        #myparents.__init__(self, name, age)
        super().__init__(name,age)
        self.birthyear = 1984

    def welcome(self):
        print("welcome", self.name, self.age, "your birth year is ", self.birthyear)
K = kid("kavi", 5)
K.printname()
print("K.birhyear", K.birthyear)
<<<<<<< HEAD
K.welcome()

=======
 
>>>>>>> DEV
