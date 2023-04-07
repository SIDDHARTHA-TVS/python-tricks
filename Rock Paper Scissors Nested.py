#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("Rock...")
print("Paper...")
print("Scissors...")

Player1 = input("Player1, Make your move: \n")
Player2 = input("Player2, Make your move: \n")

if Player1 == Player2:
    print("It's a tie")
elif Player1 == "Rock":
    if Player2 == "Scissors":
        print("Player1 won")
    elif Player2 == "Paper":
        print("Player2 won")
elif Player1 =="Paper":
    if Player2 == "Rock":
        print("Player1 won")
    elif Player2 == "Scissors":
        print("Player2 won")
elif Player1 == "Scissors":
    if Player2 == "Rock":
        print("Player2 won")
    elif Player2 == "Paper":
        print("Player1 won")
else:
    print("Something went wrong")


# In[ ]:




