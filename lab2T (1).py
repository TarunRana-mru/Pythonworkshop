#!/usr/bin/env python
# coding: utf-8

# ## Lab2- Programming for Problem Solving using Python
# 

# In[1]:


## Q1


# In[2]:


a=int(input())



# In[3]:


if a%2==0:
    print("even no")


# In[4]:


if a%2!=0:
    print("odd no")


# In[5]:


## Q2


# In[6]:


print("enter the year-")
year=int(input())


# In[7]:


if year%4==0 or year%400==0:
    print("its a leap year")
else :
    print("not a leap year")


# In[8]:


## q3


# In[9]:


c=input()


# In[10]:


if c=="a" or c=="e" or c=="i" or c=="o" or c=="u" :
    print("Its a vowel")
else :
    print("its a consonant")


# In[11]:


## Q4


# In[12]:


a=int(input())


# In[13]:


b=int(input())


# In[14]:


if a<b :
    print("a is smaller")
else :
    print("b is smaller")


# In[15]:


## Q5
num=int(input())


# In[16]:


factorial=1


# In[17]:


if num<0:
    print("Sorry factorial doesnt exist")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range (1,num+1):
        factorial=factorial*i
print("the factorial of",num,"is",factorial)


# In[18]:


## Q6


# In[19]:


n=4
k=2*n-2


# In[20]:


for i in range(0, n) :
    for j in range(0, k) :
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")


# In[21]:


## Q7


# In[22]:


num=int(input())


# In[23]:


a=1
print(" ",a)
b=1
print(" ",a)
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(" ",c)


# In[24]:


## Q8


# In[ ]:


a=int(input())
for i in range (2,a):
    if(a%i==0):
        print("not a prime number")
        break
    elif(a=="2"):
        print("is a prime no.")
        break
    else :
        print("prime number")
        break


# In[26]:


## Q9


# In[27]:


symbol=input()
no1=int(input())
no2=int(input())


# In[28]:


if(symbol=="+") :
    print(no1+no2)
elif(symbol=="-") :
    print(no1-no2)
elif(symbol=="*") :
    print(no1*no2)
elif(symbol=="/") :
    print(no1/no2)
else :
    print("out of range")


# In[ ]:




