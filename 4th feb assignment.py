#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Create a python program to sort the given list of tuples based on integer value using a
#lambda function.

#solution:

my_list = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

sorted_list = sorted(my_list, key=lambda x: x[1])

print(sorted_list)


# In[4]:


#Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
#lambda and map functions.

#Solution:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x**2, my_list))

print(squares)


# In[6]:


#Write a python program to convert the given list of integers into a tuple of strings. Use map and
#lambda functions
#Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Solution:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tuple_of_strings = tuple(map(lambda x: str(x), my_list))

print(tuple_of_strings)


# In[8]:


#Write a python program using reduce function to compute the product of a list containing numbers
# from 1 to 25.

#Solution:

from functools import reduce

my_list = list(range(1, 26))

product = reduce(lambda x, y: x * y, my_list)

print(product)


# In[11]:


#Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
#filter function.


#Solution:

my_list = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

filtered_list = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, my_list))

print(filtered_list)


# In[12]:


#Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
#function.
#['python', 'php', 'aba', 'radar', 'level']

#Solution

my_list = ['python', 'php', 'aba', 'radar', 'level']

palindromes = list(filter(lambda x: x == x[::-1], my_list))

print(palindromes)

