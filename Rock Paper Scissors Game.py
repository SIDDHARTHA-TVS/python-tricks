#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("Rock...")
print("Paper...")
print("Scissors...")

Player1 = input("Player1, Make your move: \n")
Player2 = input("Player2, Make your move: \n")

if Player1 == "Rock" and Player2 == "Scissors":
    print("Player1 won")
elif Player1 == "Rock" and Player2 == "Paper":
    print("Player2 won")
elif Player1 == "Paper" and Player2 == "Rock":
    print("Player1 won")
elif Player1 == "Paper" and Player2 == "Scissors":
    print("Player2 won")
elif Player1 == "Scissors" and Player2 == "Rock":
    print("Player2 won")
elif Player1 == "Scissors" and Player2 == "Paper":
    print("Player1 won")    
elif Player1 == Player2:
    print("It's a tie")
else:
    print("Something went wrong")


# In[ ]:




