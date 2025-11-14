'''                                         DAY -01- 10/11/25                                                                                         '''
print("Hello World")
#This is a comment which can't visible to complier .
''' This is a multiline comment
that spans multiple lines which also can't visible to the complier 
...'''
x = 10
print(x)
x="Hello World"
print(x)
name  = "Aryan Srivastava"
print(name)
a=10
b=20
print(a+b)
#Casting
y = float(3)
print(y)

y= str(4)
print(y)

print(type(y))

print("Hi everyone i m changing the the line \nGood Morning")

print("Hello", end = " ")
print("Everyone")
age = 18
print("I'm ",age,"years old")
num1 = "hi"
print(num1)
a=b=c=d=e=f=g=10
print(e)
sen = "Aryan "
Sen2 = "Srivastava"
Sen3 = sen+Sen2
print(Sen3)

z= "Aryan"
print(z[0:3:2])
z=z.lower()
print(z)

e=21
print(f"my age is {a}")
a=23
b=12
print(f"Calculate {a+b}")
print(f"this is floating value {a:.2f}")

txt = "Hello world"
x = txt.capitalize()
print(x)

d = txt.count("l")
print(d)

z = txt.islower()
print(z)

#Boolean

print(7>3)
print(7<3)

#Arthmatic operator "+  , - , * , / , % , // , **"
print("Arthematic operator-----------------------------")
x=2
y=4
#2*2*2*2
print("Exponent ",x**y)
print("Addtion " ,x+y)
print("Subtraction " ,x-y)
print("Mulitplication " ,x*y)
print("Division " ,x/y)
print("Modulas " ,x%y)
print("Float",x//y)

#Assignment operator : used to assign values to variables
# =, += , -= , *= , /= , %= , //= , **=
print("Assignment operator------------------------")
j = 12
j+=8   #j = j + 8
print(j)
j *= 2
print(j)
j /= 2
print(j)

#Comparison Operator : used to compare values
print("Comparison Operator----------------------------")
# == , != , <= ,>=
print(12!=14)
print(12==12)
print(12>=14)
print(12<=14)

#Chaining condition
x = 20
print(12<x<40)

#Logical Operator : AND , OR , NOT
print("Logical Operator----------------------------------")
x= 12
print(9<x and x<14)
print(9<x or x>14)
print(not(9<x and x<14))

#Bitwise Operator
print("Bitwise Operator--------------------------------")
x=6 #0 1 1 0
y=3 #0 0 1 1
print(x & y)
print(x | y)
print(x ^ y)
print(~x)

#Conditional Statement
print("Conditional Statement------------------------")
k = 12
v = 9
if k>v:
    print("k is greater than v")
elif k == v:
    print("Values is equal")
else:
    print("v is greater than k")
