class Myclass:
    x=10
    y=12
    z=14

p1 = Myclass()
print(p1.x)

#---------------Entering value-------------------------#

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

r=input("Enter Your Name: ")
s=int(input('Enter Your Age: '))

x1 = Person(r,s)
print("Your name is: "+x1.name)
print("Your age is: ",x1.age)
