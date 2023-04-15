#!/usr/bin/env python
# coding: utf-8

# In[22]:


"""" w.a p to print like this 
Twinkle, twinkle, little star,
   	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\tLike a diamond in the sky.\n Twinkle, twinkle, little star,\n    How I wonder what you are  "    )


# In[31]:


# Write a Python program to find out what version of Python you are using
import sys
print(sys.version)
print (sys.version_info)


# In[44]:


#w.a.p to print current date and time 
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[57]:


#w.ap to print area
r=float(input("Enter the radius of circle"))
area=3.14*r*r
print("The area of the circle is "+str(area))


# In[75]:


"""" Write a Python program that accepts the user's first and last name and prints them in reverse order with
a space between them"""
first=(input("Enter your first name "))
last=(input("Enter your last name "))
print(first  +  last)
a=("Reverse of name is ", last +" "+first)


# In[79]:


print(last[::-1],first[::-1])


# In[97]:


#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
n=(input("Enter the comma seprated   no "))
list=n.split(",")
print(list)
tuple=tuple(list)
print(tuple)


# In[132]:


#Write a Python program that accepts a filename from the user and prints the extension of the file.
f_name=(input("Enter the filename with extension "))
f=f_name.split(".")
print("The Extension of the file is")
print(f[::-8])


# In[168]:


#spliting
n=(input("Enter a word :- "))
f=n.split[" ,"]
pritn(f)


# In[151]:


#. Write a Python program to display the first and last colors from the following list. Go to the editor color_list
list= ["Red","Green","White" ,"Black"]
print(list[0],list[-1])


# In[157]:


# Write a Python program to display the examination schedule. (extract the date from exam_st_date)
import datetime
date=datetime.date()
print("%Y%d%m%")


# In[196]:


def split_and_join(line):
    # write your code here
    result= line.split(" ") 
    result='-'.join(result)
    return result
   # return result1
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:




