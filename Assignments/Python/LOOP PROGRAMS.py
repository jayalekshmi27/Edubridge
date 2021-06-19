#!/usr/bin/env python
# coding: utf-8

# # reverse of a number

# In[ ]:



n=int(input('enter the number'))
a=n
reverse=0
while a>0:
    d=a%10
    reverse=reverse*10+d
    a=a//10
print('reverse of the number',reverse)


# # sum of a number and its reverse

# In[16]:



n=int(input('enter the number'))
a=n
reverse=0
while a>0:
    d=a%10
    reverse=reverse*10+d
    a=a//10
print('reverse of the number',reverse)
sum=n+reverse
print('sum of number an reverse is',sum)


# # whether a number is Armstrong or not

# In[27]:



n=int(input('enter the number'))
a=n
sum=0
while a>0:
    d=a%10
    sum=sum+d**3
    a=a//10
if sum==n:
    print('Armstrong number')
else:
    print('not an Armstrong number')


# # check whether a number is palindrome or not

# In[36]:



n=int(input('enter the number'))
a=n
reverse=0
while a>0:
    digit=a%10
    reverse=reverse*10+digit
    a=a//10
print(reverse)
if n==reverse:
    print('palindrome number')
else:
    print('not palindrome')


# # SUM OF DIGITS OF A NUMBER

# In[3]:



n=int(input('enter the number'))
a=n
sum=0
while a>0:
    d=a%10
    sum=sum+d
    a=a//10
print('sum of digits',sum)


# In[ ]:




