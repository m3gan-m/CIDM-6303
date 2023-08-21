# Watching the short videos at codewithmosh.com is very important for
# understanding this chapter

# Chapter 7.1 Classes
# Nothing to code. Know the following: 
# Class is a blueprint for creating new objects
# Object is instance of a class

# Chapter 7.2 Creating Classes
print("\nChapter 7.2 Creating Classes")
# Start coding here...

#Megan Moore
class Point:
    def draw(self):
        print("draw")

point = Point()
print(type(point))
print(isinstance(point,int))

#CHapter 7.3 Constructors
print("\nChapter 7.3 Constructors")
#we have to change the class name throughout this activity because classes with
#the same name cannot exist in the same app.py
class Point3:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        print(f"Point ({self.x},{self.y})")

#an object is a varibale of type class
#create an object named point from a class named Point()
#this is called instantiating an object
point = Point3(1,2)
point.draw()

#chapter 7.4 Class vs instance Attributes
print("\nChapter 7.4 class vs instance Attributes")
class Point4:
    #class attribute
    default_color = "red"

    def __init__(self,x,y):
        #instance attributes
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")
#class attributes are accessible even without instantiating an object
Point4.default_color = "yellow"
point = Point4(1,2)
#the object point can access the attribute default_color
print(point.default_color)
#the class Point4 can access the class attribute default_color
print(Point4.default_color)
point.draw()

#instantiate another object of class Point()
another = Point4(3,4)
print(another.default_color)
another.draw()

#Chapter 7.5 Class vs Instance Methods
print("\nChapter 7.5 Class vs Instance Methods")
class Point5:
    def __init__(self,x,y):
        #instance attributes
        self.x = x
        self.y = y
    @classmethod
    def zero(cls):
        return cls(0,0)
    def draw(self):
        print(f"Point ({self.x},{self.y})")

#Class methods can be run even without instantiating an object
point = Point5.zero()
point.draw()

#CHapter 7.6 Magic Methods
print("\nChapter 7.6 Magic Methods")
#remember that magic methods are methods that begin with two underscores and end with two underscores
class Point6:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def draw(Self):
        print(f"Point ({self.x}, {self.y})")

point = Point6(1,2)
print(str(point))

#CHapter 7.7 through 7.11 - nothing to code.
#chapter 7.12 Inheritance
print("\nCHapter 7.12 inheritance")
#The Mammal and Fish classes inherit the eat() method from the ANimal class
#and inherit an instance attribute 'age' from the Animal class
#Terms to know.
#Animal:Patent class or Base class
#Mammal and Fish: Child class or Sub class

class Animal:
    def __init__(self):
        self.age=1
    def eat(Self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m=Mammal()
m.eat()
print(m.age)

f=Fish()
f.eat()
f.age=3
print(f.age)

#chapters 7.13-22. Nothing to code.
