'''                                               Day -02 - 11/11/2025                                                                   '''
#Loops
#while loop
'''
i=0
while(i<8):
    print("Aryan")
    i+=1

#Write a program to print a table of a given number using while loop
num = int(input("Enter a number"))
i=1
while(i<11):
    pro = num * i
    i+=1
    print(pro)

#Write a program to check the number is even or odd at the maximum range 
count = int(input("Enter the number"))
while count > 0:
    if(count % 2 == 0):
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count-=1

#For Loop :
nums = [1,2,3,4,5,6,7,8,9,10,11]
for i in nums:
    if i % 2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")



#RANGE METHOD
for i in range(1,11):
    print(i)

for i in range(1,11,2): #the 2 represents the skip step
    print(i,end=" ")    #Output - 1 3 5 7 9

#TASK - 1

Data = (62, 75, 83, 23, 45, 55, 35, 88, 92, 100)

for i in Data:
    if i >= 95:
        grade = "A++"
    elif i > 85:
        grade = "A"
    elif i >= 65:
        grade = "B"
    elif i >= 35:
        grade = "C"
    else:
        grade = "Fail"
    print(f"Score: {i} --  Grade: {grade}")

'''
students = {"Aryan": 86,"Rehan": 89, "Anshuman": 78 , "Rishabh" : 76 }
for name,marks in students.items():
        if marks >= 95:
            grade = "A++"
        elif marks > 85:
            grade = "A"
        elif m  arks >= 65:
            grade = "B"
        elif marks >= 35:
            grade = "C"
        else:
            grade = "Fail"
        
        print(f"Score: {name} --  Grade: {grade}")