#!/usr/bin/env python
# coding: utf-8

# In[31]:


print("BMI Report")
Height = float(input("What is your height? in m\n"))
Weight = float(input("What is your weight? in kg\n"))
BMI = round(float(Weight/Height), 2)
if BMI <= 18.5:
    print(f"Your BMI is {BMI}, You are under-weight.")
elif BMI > 18.5 and BMI <= 25:
    print(f"Your BMI is {BMI}, You have a normal weight.")
elif BMI > 25 and BMI <= 30:
    print(f"Your BMI is {BMI}, You are over-weight.")
elif BMI > 30 and BMI <= 35:
    print(f"Your BMI is {BMI}, You are obese.")
else:
    print(f"Your BMI is {BMI}, You are clinically obese.")


# In[ ]:




