#!/usr/bin/env python
# coding: utf-8

# In[5]:


#shell sort implementation using python

def shell_sort(n):
    dif = len(n) // 2
    while dif > 0:
        for i in range(dif, len(n)):
            j = i
            while j >= dif and n[j - dif] < n[j]:
                n[j], n[j - dif] = n[j - dif], n[j]
                j = j - dif
        dif = dif // 2
            
if __name__ == '__main__':
    x = [1, 5, 7, 3, 4, 8, 2]
    shell_sort(x)
    print(x)


# In[ ]:




