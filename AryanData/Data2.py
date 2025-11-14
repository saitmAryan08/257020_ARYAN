'''                                               Day -02 - 11/11/2025                                                                   '''
#Write a code to check the vote eligibility
#Task - 01
age = int(input("Enter your age - "))
if(age>=18):
    print("You are Eligilible to vote")
elif(age<18):
    print("You are not Eligible to vote !!")
else:
    print("Enter valid age entry")

#Task2
'''Write a code to print the grade if grade >= 35 then gave grade C
if the grade greater than  or equal to 65 then give grade B , if the grade
greater then 85 then give grade A and if marks greater than 95 then give A ++ grade 
'''

marks = int(input("Enter your marks - "))
grade = " "
if(marks >= 95):
    grade = "A++"
elif(marks >=85):
    grade = "A"
elif(marks >= 65):
    grade = "B"
elif(marks>=35):
    grade="C"
else:
    print("Fail")
print(grade)
    
    
        