#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[31]:


import random

print("Rock...")
print("Paper...")
print("Scissors...")

Player = input("Player, Make your move: \n")
rand_num = random.randint(0,2)
if rand_num == 0:
    Computer = "Rock"
elif rand_num == 1:
    Computer = "Paper"
else:
    Computer = "Scissors"
print(f"Computer plays {Computer}\n")

if Player == Computer:
    print("It's a tie")
elif Player == "Rock":
    if Computer == "Scissors":
        print("Player won")
    elif Computer == "Paper":
        print("Computer won")
elif Player =="Paper":
    if Computer == "Rock":
        print("Player won")
    elif Computer == "Scissors":
        print("Computer won")
elif Player == "Scissors":
    if Computer == "Rock":
        print("Computer won")
    elif Computer == "Paper":
        print("Player won")
else:
    print("Something went wrong")


# In[ ]:





# In[ ]:




