'''                                               Day -02 - 11/11/2025                                                                   '''
#List: are used to store the multiple values in the single variable
a=["Rachit", "Aryan" , 'Varun' , 17]
print(type(a))

#Tuple: are used to store the multiple values in the single variable but tuples are immutable 
c=("Aryan","Varun",'Rehan', 19,)
print(type(c))

#Sets: are used to store the multiple values in the single variable but sets are unordered and unindexed
a={1,2,3,4,5,"Aryan","Suhani"}
if "Aryan" in a:
    print("Aryan name exists in the given set")
print(a)
print(type(a))

#Dictionary: are used to store the multiple values in the single  variable in key:value pair

dic = {"Name": "Varun","Age":19}
print(type(dic))
print(dic)
print(dic["Age"])