#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Q1
def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
        else:
            if answer[-1] == a:
                pass
            else:
                answer.append(a)
    return answer


# In[3]:


arr = [1,1,2,3,4,4,1,1]
solution(arr)


# In[21]:


# Q2
def solution(seoul):
    answer = ''
    x = seoul.index("Kim")
    answer = f'김서방은 {x}에 있다'
#f 의 역할 : 문자열 포맷팅  = print("test{},").format(1)
#f'{}'를 사용하면 python에서 사용하는 변수명을
# {}안에 넣으면 그 반환값이 반환됨
    return answer


# In[22]:


seoul = ["Jane","Kim"]
solution(seoul)


# In[16]:


# Q3
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else :
        answer = 'Odd'
    return answer


# In[17]:


num = 3
solution(num)


# In[ ]:




