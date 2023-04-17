#!/usr/bin/env python
# coding: utf-8

# In[2]:


num=int(input("Enter a no : "))
print("hexadecimal")


# In[3]:


letters = ["a", "b", "c"]

letters += ["d"]

print(len(letters))


# In[4]:


x ="abc"

x *= 2

print(len(x))


# In[5]:


nums = [9, 8, 7, 6, 5]

nums.append(4)

nums.insert(2, 11)

print(len(nums))


# In[9]:


nums = [2,4,8,9,5]


nums.insert(1, 3)

nums.remove(9)

nums.insert(0, nums.count(8))

print(nums[3])


# In[7]:


list = [8, 4, 2, 6]

list.remove(2)

print(len(list)+list.count(6))


# In[10]:


print("{0}{1}{0}".format("abra", "cad"))


# In[8]:


n = [2, 4, 6, 8]
res = 2
for x in n[1:3]:
  res *= x

print(res)


# In[13]:


fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))


# In[15]:


x, y = [1, 2]
x, y = y, x


# In[23]:


a, b, c, d, *e, f, g = range(10)
print(len(e))


# In[27]:


letters = {"a", "b", "c", "d"}
if "1" not in letters:
  print(1)
else: 
  print(2)


# In[29]:


nums = [i*2 for i in range(10)]


# In[34]:


nums = (55, 44, 33, 22)
print(max(min(nums[0:2])))


# In[ ]:





# In[ ]:




