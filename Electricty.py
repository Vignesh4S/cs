#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel("C:\\Users\\Admin\\Documents\\Electricity.xlsx")


# In[3]:


print(df)


# In[9]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[10]:


df = pd.read_excel("C:\\Users\\Admin\\Documents\\Electricity.xlsx")


# In[11]:


df.head()


# In[12]:


df.info()


# In[13]:


df.describe()


# In[15]:


df.columns


# In[16]:


df.dtypes


# In[ ]:




