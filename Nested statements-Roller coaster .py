#!/usr/bin/env python
# coding: utf-8

# In[13]:


print("Welcome to the roller-coaster")
height = int(input("What's your height? in cms\n"))
if height >= 120:
    print("You can go for ride")
    age = int(input("What's your age?\n"))
    if age <= 18:
        print("The ticket price is $7")
    else:
        print("The ticket price is $12")
else:
    print("You are not eligible for ride")


# In[ ]:





# In[ ]:




