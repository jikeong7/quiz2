#!/usr/bin/env python
# coding: utf-8

# In[1]:


#quiz 1

def solution(n, m):
    gcd = 1
    answer = [gcd]
    for i in range(2,1000000):
        if n % i ==0 and m % i ==0:
            gcd = i
            answer=[gcd]
    if n > m :
        if n % m == 0:
            answer.append(n)
        else:
            answer.append(n*m)
    elif n < m :
        if m % n ==0:
            answer.append(m)
        else:
            answer.append(n*m)
    else:
        answer.append(n)
    return answer


# In[2]:


solution(3,12)


# In[3]:


solution(2,5)


# In[ ]:




