#!/usr/bin/env python
# coding: utf-8

# In[25]:


''''f  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''
n=int(input("Enter a no "))

if(n%2!=0):
    print("Weird")
elif(n%2==0 in range (2,5)) :
    print("Not Weird")


# In[28]:


if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2 != 0:
        print("Weird")
    elif n%2 == 0 and n>2 and n<=5:
        print("Not Weird")
    elif n%2 ==0 and n > 6 and n <=20:
        print("Weird")
    else:
        print("Not Weird")


# In[ ]:




