#!/usr/bin/env python
# coding: utf-8

# In[1]:


list = []



for j in range(2,100) :    

    for i in range(2,j):  

        if (j %i ) == 0: 

            break

    else: 

        list.append(j)

        

print(list)


# In[ ]:




