from bert_embedding import BertEmbedding
import numpy as np
import pandas as pd
import string

bert_embedding = BertEmbedding()
airbnb_berlin = pd.read_csv('./data/translated_berlin.csv')
airbnb_paris = pd.read_csv('./data/translated_paris.csv')
airbnb_amsterdam = pd.read_csv('./data/translated_amsterdam.csv')
airbnb_boston = pd.read_csv('./data/translated_boston.csv')
airbnb_edinburgh = pd.read_csv('./data/translated_edinburgh.csv')
airbnb_madrid = pd.read_csv('./data/translated_madrid.csv')

def cleaner(sentence):
    try:
        sentence = sentence.lower()
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        sentence = sentence.replace('  ', ' ').strip().replace('/n', ' ')
        return sentence.split()
    except:
        return []

def get_sent_embedding(sentence, embedding_model):

    result = embedding_model(sentence)
    if result:
        ans = result[0][1][0]
        for i in result[1:]:
            try:
                ans = ans + i[1][0]
            except:
                continue
        ans = ans/len(sentence)
        return ans
    else:
        return np.nan

def text_to_embedding(column,dataframe,embedding_model):
    store = []
    for index, row in dataframe.iterrows():
        print(index)
        sentence = row[column]
        sentence = cleaner(sentence)
        if len(sentence):
            store.append(get_sent_embedding(sentence,embedding_model))
        else:
            temp = [0]*len(store[-1])
            store.append(temp)
    return store

important_columns = ['summary', 'house_rules', 'interaction', 'host_about']

for col in important_columns:

    temp = text_to_embedding(col, airbnb_boston, bert_embedding)
    airbnb_boston[col] = temp
    temp = text_to_embedding(col, airbnb_boston, bert_embedding)
    airbnb_boston[col] = temp
    temp = text_to_embedding(col, airbnb_amsterdam, bert_embedding)
    airbnb_amsterdam[col] = temp
    temp = text_to_embedding(col, airbnb_paris, bert_embedding)
    airbnb_paris[col] = temp
    temp = text_to_embedding(col, airbnb_edinburgh, bert_embedding)
    airbnb_edinburgh[col] = temp
    temp = text_to_embedding(col, airbnb_madrid, bert_embedding)
    airbnb_madrid[col] = temp


airbnb_boston.to_csv('./data/translated_boston.csv')
airbnb_madrid.to_csv('./data/emd_data_madrid.csv')
airbnb_boston.to_csv('./data/emb_data_boston.csv')
airbnb_edinburgh.to_csv('./data/emb_data_edinburgh.csv')
airbnb_paris.to_csv('./data/emb_data_paris.csv')
airbnb_amsterdam.to_csv('./data/emd_data_amsterdam.csv')