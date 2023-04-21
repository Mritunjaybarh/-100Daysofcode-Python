#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
s=set("Mritunjay ")
s.add('h')
print(s)
set(["a","c","d","e","c","z"])
print (s.add("Hackerrank "))


# In[42]:


s = set('HackerRank')
s.add('H')
print (s)
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
print (s.add('HackerRank'))
for i in s i==0,i>=n,i++:
    
    print(i)


# In[58]:


"""#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----"""
def solve(n):
   for i in range(n-1,-1,-1):
      for j in range(i):
         print(end="--")
      for j in range(n-1,i,-1):
         print(chr(j+97),end="-")
      for j in range(i,n):
         if j != n-1:
            print(chr(j+97),end="-")
         else:
            print(chr(j+97),end="")
      for j in range(2*i):
         print(end="-")
      print()
   for i in range(1,n):
      for j in range(i):
         print(end="--")
      for j in range(n-1,i,-1):
         print(chr(j+97),end="-")
      for j in range(i,n):
         if j != n-1:
            print(chr(j+97),end="-")
         else:
            print(chr(j+97),end="")
      for j in range(2*i):
         print(end="-")
   print()

n = 8
solve(n)
   


# In[62]:


import string
def rangoli_pattern(n):
    L = [  ]
    alpha = string.ascii_lowercase
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))

n = int(input("Enter the size of the pattern: "))
rangoli_pattern(n)


# In[ ]:




