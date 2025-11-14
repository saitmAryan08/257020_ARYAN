'''                                         DAY -03- 12/11/25                                                                                         '''

'''Write a python code on book system
make function and store the data in dictionary atleast five books 
user call the number of the book and that book need to be display'''
'''
# Your main script
import random
import sys 
import math

print("random number between 1-10", random.randint(1,10))
color = ["red" , "green" , "Orange" , "blue" , "black ", "cyan"]
print("Random Color ", random.choice(color))
print("Platform",sys.platform)
print("Platform",sys.version)
n = int(math.pow(2,3))
sq = int(math.sqrt(25))
print("cube of 2 = ",n)
print("Squareroot of 25 = ",sq)
print("Value of pi is ",math.pi)
print("Ceil of 4.8 = ",math.ceil(4.8)) #Highest possible values
print("Floor of 5.7 = ",math.floor(5.7)) #lowest possilbe values
0


def DisplayBooks(bookNum):
    books = {1:"Amit verma",2: "Nelson Mandela" , 3:"THe great gatsby" , 4: "THe dark night", 5:"Foolish"}

    if bookNum in books:    
        books = books[bookNum]
        print(books)
    else:               
        print("Not found")


dic = int(input("Enter book number (1-5books )"))
DisplayBooks(dic)


#TASK 1
#Create a function to take random value using random module
# and check the value is postive or negative and print it \
#Check if the number is even or odd

import random

def randomValue():
    num  = random.randint(-100,100)
    return num


def check(num):
    if num % 2 == 0:
        print("The given number is even")
    else:
        print("The given number is odd")

def checkNature(num):
    if num > 0:
        print(" Given number is positive")
    elif num == 0:
        print("Given number is nuetral")
    else:
        print("Given number is negative")
num = randomValue()
print(f"{num}")     
check(num)

checkNature(num)
class abc:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = abc("Rachit",23)
print(p1.name,p1.age)

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero"


calc = Calculator(10, 5)
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())


#Create class named as Rectangle
#there is attributes in its length and width
#there is a method named as area which return area of rectangle
#get the input from user for a and b



class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

dic = int(input("Enter book number (1-5books )"))
a=int(input("Enter the length - "))
b=int(input("Enter the width - "))
area = Rectangle(a,b)
print("Area of Rectangle - ",area.Area()) 

                                                Day - 03 : 13/11/2025                                   
class Car:
    def __init__(self,brand,color):
        self.brand  = brand
        self.color  = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving")
    
car1  = Car("BMW","Black")
car2  = Car("Tesla","White")

car1.drive()
car2.drive()

class Peron:
    def __init__(self,name,age):
        self.name  = name
        self.__age  = age


p1 = Peron("Aryan",24)
p2 = Peron("Varun" , 23)
print(p1.name)
'''

#Inheritance - Child class gets properties of parent class
class Animal:
    def speak(self):
        print("Animal speaks")
        
class Dog(Animal):
    def speak(self):
        print("Dog barks")


dog = Dog()
dog.speak()


#Polymorphism -- Same function name , different behaviour
class Cat:
    def sound(self):
        return "Meow"
    
class Dog:
    def sound(self):
        return "Woof"

for animal in [Cat(),Dog()]:
    print(animal.sound())

#Abstration -- hiding details , showing only necassy things
from abc import ABC, abstractmethod

class Car(vehicle):
    def start(self):
        print("Car Started")

class Bike(vehicle):
    def start(self):
        print("Bike started")
vehicles = [Car(),Bike()]
    #inheritance , encapusliation , abstraction , polymorisphm