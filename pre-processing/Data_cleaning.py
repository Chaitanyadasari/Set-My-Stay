#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize


# In[2]:


amsterdam=pd.read_csv('/Users/admin/Desktop/256/Project/CSV_files/_amsterdamonehoted.csv')
berlin=pd.read_csv('/Users/admin/Desktop/256/Project/CSV_files/_berlinonehoted.csv')
edinburgh=pd.read_csv('/Users/admin/Desktop/256/Project/CSV_files/_edinburghonehoted.csv')
madrid=pd.read_csv('/Users/admin/Desktop/256/Project/CSV_files/_madridonehoted.csv')
paris=pd.read_csv('/Users/admin/Desktop/256/Project/CSV_files/_parisonehoted.csv')
boston=pd.read_csv('/Users/admin/Desktop/256/Project/CSV_files/_bostononehoted.csv')
keypoints=['station','tram','busstop','bus','metro','freeway','airport']
list_of_amenities=[]
for amenities in amsterdam['amenities']:
    data=amenities.split(',')
    for keyword in data:
        if keyword not in list_of_amenities:
            list_of_amenities.append(keyword)
        else:
            continue


# In[3]:


### Amsterdam

amst=amsterdam
amst=amst.drop(['transit', 'amenities','host_response_rate','host_acceptance_rate'], axis=1)
amsterdam['transit'].fillna("None", inplace=True)
amsterdam['host_response_rate'].fillna("0%", inplace=True)
keypoints=['station','tram','busstop','bus','metro','freeway','airport']
transit=[[] for i in range(len(amsterdam['transit']))]
amenities=[[] for i in range(len(amsterdam['transit']))]
### Transit
i=0
for data in amsterdam['transit']:
    token=word_tokenize(data.lower())
    for keyword in keypoints:
        if keyword in token:
            transit[i].append(1)
        else:
            transit[i].append(0)
    i+=1
df = pd.DataFrame(transit, columns = ['station','tram','busstop','bus','metro','freeway','airport'])
frame=[amst,df]
amst=pd.concat(frame, join="outer",ignore_index=False,axis=1)
### Amenities
i=0
for data in amsterdam['amenities']:
    tokens=data.split(',')
    for keyword1 in list_of_amenities:
        if keyword1 in tokens:
            amenities[i].append(1)
        else:
            amenities[i].append(0)
    i+=1
df=pd.DataFrame(amenities,columns=list_of_amenities)
frame=[amst,df]
amst=pd.concat(frame,join="outer",ignore_index=False,axis=1)
### Host response rate
host_res=[]
for i in amsterdam['host_response_rate']:
    i=i[:-1]
    if (int(i)>50):
        host_res.append(1)
    else:
        host_res.append(0)
df=pd.DataFrame(host_res,columns=['response_rate'])
frame=[amst,df]
amst=pd.concat(frame,join="outer",ignore_index=False,axis=1)
amst


# In[ ]:





# In[4]:


### Berlin

ber=berlin
ber=ber.drop(['transit', 'amenities','host_response_rate','host_acceptance_rate'], axis=1)
berlin['transit'].fillna("None", inplace=True)
berlin['host_response_rate'].fillna("0%", inplace=True)
keypoints=['station','tram','busstop','bus','metro','freeway','airport']
transit=[[] for i in range(len(berlin['transit']))]
amenities=[[] for i in range(len(berlin['transit']))]
### Transit
i=0
for data in berlin['transit']:
    token=word_tokenize(data.lower())
    for keyword in keypoints:
        if keyword in token:
            transit[i].append(1)
        else:
            transit[i].append(0)
    i+=1
df = pd.DataFrame(transit, columns = ['station','tram','busstop','bus','metro','freeway','airport'])
frame=[ber,df]
ber=pd.concat(frame, join="outer",ignore_index=False,axis=1)
### Amenities
i=0
for data in berlin['amenities']:
    tokens=data.split(',')
    for keyword1 in list_of_amenities:
        if keyword1 in tokens:
            amenities[i].append(1)
        else:
            amenities[i].append(0)
    i+=1
df=pd.DataFrame(amenities,columns=list_of_amenities)
frame=[ber,df]
ber=pd.concat(frame,join="outer",ignore_index=False,axis=1)
### Host response rate
host_res=[]
for i in berlin['host_response_rate']:
    i=i[:-1]
    if (int(i)>50):
        host_res.append(1)
    else:
        host_res.append(0)
df=pd.DataFrame(host_res,columns=['response_rate'])
frame=[ber,df]
ber=pd.concat(frame,join="outer",ignore_index=False,axis=1)
ber


# In[5]:


### Edinburgh

edin=edinburgh
edin=edin.drop(['transit', 'amenities','host_response_rate','host_acceptance_rate'], axis=1)
edinburgh['transit'].fillna("None", inplace=True)
edinburgh['host_response_rate'].fillna("0%", inplace=True)
keypoints=['station','tram','busstop','bus','metro','freeway','airport']
transit=[[] for i in range(len(edinburgh['transit']))]
amenities=[[] for i in range(len(edinburgh['transit']))]
### Transit
i=0
for data in edinburgh['transit']:
    token=word_tokenize(data.lower())
    for keyword in keypoints:
        if keyword in token:
            transit[i].append(1)
        else:
            transit[i].append(0)
    i+=1
df = pd.DataFrame(transit, columns = ['station','tram','busstop','bus','metro','freeway','airport'])
frame=[edin,df]
edin=pd.concat(frame, join="outer",ignore_index=False,axis=1)
### Amenities
i=0
for data in edinburgh['amenities']:
    tokens=data.split(',')
    for keyword1 in list_of_amenities:
        if keyword1 in tokens:
            amenities[i].append(1)
        else:
            amenities[i].append(0)
    i+=1
df=pd.DataFrame(amenities,columns=list_of_amenities)
frame=[edin,df]
edin=pd.concat(frame,join="outer",ignore_index=False,axis=1)
### Host response rate
host_res=[]
for i in edinburgh['host_response_rate']:
    i=i[:-1]
    if (int(i)>50):
        host_res.append(1)
    else:
        host_res.append(0)
df=pd.DataFrame(host_res,columns=['response_rate'])
frame=[edin,df]
edin=pd.concat(frame,join="outer",ignore_index=False,axis=1)
edin


# In[6]:


### Madrid

madr=madrid
madr=madr.drop(['transit', 'amenities','host_response_rate','host_acceptance_rate'], axis=1)
madrid['transit'].fillna("None", inplace=True)
madrid['host_response_rate'].fillna("0%", inplace=True)
keypoints=['station','tram','busstop','bus','metro','freeway','airport']
transit=[[] for i in range(len(madrid['transit']))]
amenities=[[] for i in range(len(madrid['transit']))]
### Transit
i=0
for data in madrid['transit']:
    token=word_tokenize(data.lower())
    for keyword in keypoints:
        if keyword in token:
            transit[i].append(1)
        else:
            transit[i].append(0)
    i+=1
df = pd.DataFrame(transit, columns = ['station','tram','busstop','bus','metro','freeway','airport'])
frame=[madr,df]
madr=pd.concat(frame, join="outer",ignore_index=False,axis=1)
### Amenities
i=0
for data in madrid['amenities']:
    tokens=data.split(',')
    for keyword1 in list_of_amenities:
        if keyword1 in tokens:
            amenities[i].append(1)
        else:
            amenities[i].append(0)
    i+=1
df=pd.DataFrame(amenities,columns=list_of_amenities)
frame=[madr,df]
madr=pd.concat(frame,join="outer",ignore_index=False,axis=1)
### Host response rate
host_res=[]
for i in madrid['host_response_rate']:
    i=i[:-1]
    if (int(i)>50):
        host_res.append(1)
    else:
        host_res.append(0)
df=pd.DataFrame(host_res,columns=['response_rate'])
frame=[madr,df]
madr=pd.concat(frame,join="outer",ignore_index=False,axis=1)
madr


# In[7]:


### Paris

pari=paris
pari=pari.drop(['transit', 'amenities','host_response_rate','host_acceptance_rate'], axis=1)
paris['transit'].fillna("None", inplace=True)
paris['host_response_rate'].fillna("0%", inplace=True)
keypoints=['station','tram','busstop','bus','metro','freeway','airport']
transit=[[] for i in range(len(paris['transit']))]
amenities=[[] for i in range(len(paris['transit']))]
### Transit
i=0
for data in paris['transit']:
    token=word_tokenize(data.lower())
    for keyword in keypoints:
        if keyword in token:
            transit[i].append(1)
        else:
            transit[i].append(0)
    i+=1
df = pd.DataFrame(transit, columns = ['station','tram','busstop','bus','metro','freeway','airport'])
frame=[pari,df]
pari=pd.concat(frame, join="outer",ignore_index=False,axis=1)
### Amenities
i=0
for data in paris['amenities']:
    tokens=data.split(',')
    for keyword1 in list_of_amenities:
        if keyword1 in tokens:
            amenities[i].append(1)
        else:
            amenities[i].append(0)
    i+=1
df=pd.DataFrame(amenities,columns=list_of_amenities)
frame=[pari,df]
pari=pd.concat(frame,join="outer",ignore_index=False,axis=1)
### Host response rate
host_res=[]
for i in paris['host_response_rate']:
    i=i[:-1]
    if (int(i)>50):
        host_res.append(1)
    else:
        host_res.append(0)
df=pd.DataFrame(host_res,columns=['response_rate'])
frame=[pari,df]
pari=pd.concat(frame,join="outer",ignore_index=False,axis=1)
pari


# In[8]:


### Boston

bos=boston
bos=bos.drop(['transit', 'amenities','host_response_rate','host_acceptance_rate'], axis=1)
boston['transit'].fillna("None", inplace=True)
boston['host_response_rate'].fillna("0%", inplace=True)
keypoints=['station','tram','busstop','bus','metro','freeway','airport']
transit=[[] for i in range(len(boston['transit']))]
amenities=[[] for i in range(len(boston['transit']))]
### Transit
i=0
for data in boston['transit']:
    token=word_tokenize(data.lower())
    for keyword in keypoints:
        if keyword in token:
            transit[i].append(1)
        else:
            transit[i].append(0)
    i+=1
df = pd.DataFrame(transit, columns = ['station','tram','busstop','bus','metro','freeway','airport'])
frame=[bos,df]
bos=pd.concat(frame, join="outer",ignore_index=False,axis=1)
### Amenities
i=0
for data in boston['amenities']:
    tokens=data.split(',')
    for keyword1 in list_of_amenities:
        if keyword1 in tokens:
            amenities[i].append(1)
        else:
            amenities[i].append(0)
    i+=1
df=pd.DataFrame(amenities,columns=list_of_amenities)
frame=[bos,df]
bos=pd.concat(frame,join="outer",ignore_index=False,axis=1)
### Host response rate
host_res=[]
for i in boston['host_response_rate']:
    i=i[:-1]
    if (int(i)>50):
        host_res.append(1)
    else:
        host_res.append(0)
bos


# In[9]:


sum_bus=amst['bus']+amst['busstop']
for i in range(len(sum_bus)):
    if(sum_bus[i]>1):
        sum_bus[i]=1
df=pd.DataFrame(sum_bus,columns=['bus_stop'])
frame=[amst,df]
amst=pd.concat(frame,join="outer",ignore_index=False,axis=1)
sum_bus=ber['bus']+ber['busstop']
for i in range(len(sum_bus)):
    if(sum_bus[i]>1):
        sum_bus[i]=1
df=pd.DataFrame(sum_bus,columns=['bus_stop'])
frame=[ber,df]
ber=pd.concat(frame,join="outer",ignore_index=False,axis=1)
amst
sum_bus=madr['bus']+madr['busstop']
for i in range(len(sum_bus)):
    if(sum_bus[i]>1):
        sum_bus[i]=1
df=pd.DataFrame(sum_bus,columns=['bus_stop'])
frame=[madr,df]
madr=pd.concat(frame,join="outer",ignore_index=False,axis=1)

sum_bus=edin['bus']+edin['busstop']
for i in range(len(sum_bus)):
    if(sum_bus[i]>1):
        sum_bus[i]=1
df=pd.DataFrame(sum_bus,columns=['bus_stop'])
frame=[edin,df]
edin=pd.concat(frame,join="outer",ignore_index=False,axis=1)

sum_bus=pari['bus']+pari['busstop']
for i in range(len(sum_bus)):
    if(sum_bus[i]>1):
        sum_bus[i]=1
df=pd.DataFrame(sum_bus,columns=['bus_stop'])
frame=[pari,df]
pari=pd.concat(frame,join="outer",ignore_index=False,axis=1)

sum_bus=bos['bus']+bos['busstop']
for i in range(len(sum_bus)):
    if(sum_bus[i]>1):
        sum_bus[i]=1
df=pd.DataFrame(sum_bus,columns=['bus_stop'])
frame=[bos,df]
bos=pd.concat(frame,join="outer",ignore_index=False,axis=1)
amst=amst.drop(['bus','busstop'],axis=1)
madr=madr.drop(['bus','busstop'],axis=1)
ber=ber.drop(['bus','busstop'],axis=1)
edin=edin.drop(['bus','busstop'],axis=1)
pari=pari.drop(['bus','busstop'],axis=1)
bos=bos.drop(['bus','busstop'],axis=1)
amst


# In[10]:


amst.to_csv('/Users/admin/Desktop/256/Project/CSV_files/Amsterdam_final.csv')
madr.to_csv('/Users/admin/Desktop/256/Project/CSV_files/Madrid_final.csv')
ber.to_csv('/Users/admin/Desktop/256/Project/CSV_files/Berlin_final.csv')
edin.to_csv('/Users/admin/Desktop/256/Project/CSV_files/Edinburgh_final.csv')
pari.to_csv('/Users/admin/Desktop/256/Project/CSV_files/Paris_final.csv')
bos.to_csv('/Users/admin/Desktop/256/Project/CSV_files/Boston_final.csv')


# In[ ]:




