import pandas as pd
from googletrans import Translator
import time
import random

important_columns = ['summary', 'house_rules', 'interaction', 'host_about']

#airbnb_amsterdam = pd.read_csv('./data/amsterdam_listings_filtered.csv', nrows=2000).dropna(subset=important_columns)[:100]
#airbnb_paris = pd.read_csv('./data/paris_listings_filtered.csv', nrows=2000).dropna(subset=important_columns)[:100]
#airbnb_berlin = pd.read_csv('./data/berlin_listings_filtered.csv', nrows=2000).dropna(subset=important_columns)[:100]
airbnb_boston = pd.read_csv('./data/boston_listings_filtered.csv',nrows=2000).dropna(subset=important_columns)[:100]
#airbnb_madrid = pd.read_csv('./data/madrid_listings_filtered.csv', nrows=2000).dropna(subset=important_columns)[:100]
#airbnb_edinburgh = pd.read_csv('./data/edinburgh_listings_filtered.csv', nrows=2000).dropna(subset=important_columns)[:100]

def translate(column_name, dataframe):
    trans = Translator()
    i=0
    for index, row in dataframe.iterrows():
        randomd = random.randint(1,3)
        translated = trans.translate(row[column_name])
        dataframe.loc[index, column_name]  = translated.text
        print(i)
        i+=1
        time.sleep(randomd)

for col in important_columns:
    #translate(col, airbnb_paris)
    #translate(col, airbnb_edinburgh)
    #translate(col, airbnb_madrid)
    #translate(col, airbnb_amsterdam)
    #translate(col, airbnb_berlin)
    print(col)

#airbnb_berlin.to_csv('./data/translated_berlin.csv')
#airbnb_amsterdam.to_csv('./data/translated_amsterdam.csv')
#airbnb_madrid.to_csv('./data/translated_madrid.csv')
#airbnb_edinburgh.to_csv('./data/translated_edinburgh.csv')
#airbnb_paris.to_csv('./data/translated_paris.csv')
airbnb_boston.to_csv('./data/translated_boston.csv')