#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program that accepts an integer (n) and computes the value of n+n**2+n**3+...n**n
n=int(input("Enter a no "))
sum=0
for i in range(1,n+1,1):
    sum=sum+(n**i);
    print(sum)


# In[2]:


def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


# W.a.p to print sum of n given no 
n=int(input("Enter a no ")
      for i in range(n):
         sum = (n(n+1)/2
print(s)


# In[5]:


#Write a Python program to get the volume of a sphere with radius six.
r=6
v=(4/3)*r*r*r*3.14
print("Volume of the sphere is "+str(v));


# In[1]:


v=4.3
print(v)


# In[36]:


# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum
a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
if a==b==c:
    print(sum*3);
else:
        print(sum);


# In[43]:


"""" Write a Python program that determines whether a given number (accepted from the user) is even or odd,
and prints an appropriate message to the user"""
n=int(input())
if n%2==0:
    print("No is even")
else:
    print(str(n) + " is odd")


# In[44]:


# Write a Python program to count the number 4 in a given list

def list_count(nums):
    count=0
    for num in nums:
        if num==4:
            count=count+1
    return count
print(list_count([4,5,4,6,7,5,4,5,]))
    


# In[9]:


def str_count(strs):
    count=0
    for str in strs[str]:
        if str==s:
            count=count+1
        return count
strs=(str_count("Ram is aggod boy"))


# In[ ]:




