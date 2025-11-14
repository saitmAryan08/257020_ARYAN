'''      day - 03 / // 13/11/2025 '''
#Pandas is a python library for data manipulation and analysis
# * It is built on top of Numpy 

#Why Python used 
# Working with raw data strutures like(list,dictionary) NumpyArray has limitations

#Conclusion: - Pandas is more powerful because it combines the speed of numPy

import pandas as pd

data  = {
    "Name": ["Aryan","Suhani" , "Coco ", "golu"],
    "Age": [18,18,17,17],
    "Marks": [92,94,93,92]
}

data2 = {
    "Marks": 90 , "Science": 85 ,"English": 78
}
df = pd.Series(data2)
print(df)
print("science Score",df["Science"] )
print("Data type of series", df.dtype)
print("Shape of series",df.shape)
#Creating a panda series
''' 
    Panda allows creating Series from different data sources because data in real life
    is stored in differnt formats
'''


# s = pd.Series(data)

# print(s)
# print(pd.__version__)
# print(s.describe())

#Series is a 1D type data format


