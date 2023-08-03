#!/usr/bin/env python
# coding: utf-8

# # Pandas Basic Assignmnet

# # Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[1]:


pip install pandas


# In[2]:


import pandas as pd

data = [4,8,15,16,23,42]

series= pd.Series(data)

print(series)


# # Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on thevariable print it.

# In[4]:


l = [1,2,3,4,5,6,7,8,9,10]

series_var = pd.Series(l)

print(series_var)


# # Q3. Create a Pandas DataFrame that contains the following data:
# 
# Name        Age       Gender
# 
# Alice       25        Female
# 
# Bob         30        Male
# 
# Claire      27        Female

# In[5]:


Data = {
    'Name' : ['Alice' , 'Bob' , 'Claire'],
    'Age' : [25 , 30 , 27],
    'Gender' : ['Female' , 'Male' , 'Female']
}

df = pd.DataFrame(Data)

print(df)


# # Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# The DataFrame is a fundamental data structure that represents a two-dimensional, size-mutable, and heterogeneous tabular data structure. It is similar to a spreadsheet or a SQL table, where data is organized in rows and columns. 
# 
# On the other hand, a Series is another data structure provided by pandas, which represents a one-dimensional labeled array. It can be thought of as a single column of data with an associated label, called an index. 

# In[6]:


data1 = {
    'Name': ['Rakesh', 'Manish', 'Gopal', 'Vivek'],
    'Age': [25, 30, 22, 28],
    'City': ['Bihar', 'Uttrakhand', 'Chennai', 'Himachal']
}

df = pd.DataFrame(data1)

ages = pd.Series([25, 30, 22, 28], name='Age')

print("DataFrame:")
print(df)
print("\nSeries:")
print(ages)


# # Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Canyou give an example of when you might use one of these functions?

# Some Functions that we have taught in Pandas class to Manpulate data in a Pandas DataFrame.
# 
# Here are they....
# 
# 

# 1. Head() and Tail():
# 
# These functions allow you to view the first few or last few rows of a DataFrame.

# In[ ]:


import pandas as pd

df1 = pd.read_excel(r"C:\Users\HP\Downloads\Online Retail.xlsx")


# In[ ]:


df


# In[ ]:




