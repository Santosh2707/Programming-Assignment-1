#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a Python program to print "Hello Python"?


# In[2]:


print("Hello Python")


# In[3]:


#2.Write a Python program to do arithmetical operations addition and division.?


# In[4]:


print("Enter any two positive integers")
N1, N2=int(input()), int(input())
sum=N1+N2
div=N1/N2
print("\n")
print("Addition        ", N1, " + ", N2, " = ", sum)
print("Division        ", N1, " / ", N2, " = ", div)


# In[5]:


#3.Write a Python program to find the area of a triangle?


# In[6]:


height=float(input("enter the height of the traingle: "))
base=float(input("enter the base of the traingle: "))
area=(1/2)*base*height
print("the area of traingle is",area)


# In[7]:


#4.Write a Python program to swap two variables?


# In[13]:


#Method 1
x=10
y=20
temp=x
print("the value of temp variable is",temp)
x=y
print("the value of x is",x)
y=temp
print("the value of y is",y)
#Method 2
x=25
y=50
x,y=y,x
print("the value of x is",x)
print("the value of y is",y)


# In[14]:


#5.Write a Python program to generate a random number?


# In[17]:


import random

num=random.randint(0,10)
print(num)


# In[ ]:




