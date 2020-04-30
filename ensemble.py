from flask import Flask, jsonify, request

import os
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_score
# from surprise.dump import load
from sklearn.externals import joblib

from flask_cors import CORS

# creating a Flask app
app = Flask(__name__)
CORS(app) # Let the api acces for frontends.



def embed_similarity(col_name, user_listing, city_listing):
    new = []
    for i,r in user_listing.iterrows():
        try:
            new.append(np.array([np.float(i) for i in r['summary'].strip('[').strip(']').split()])*r['ratings']*r['purpose_of_trip_sim']/10)
        except:
            continue
    user_embedding = new[0]

    for n in new[1:]:
        user_embedding = user_embedding + n

    user_embedding = user_embedding/len(new)

    store = []
    for i,r in city_listing.iterrows():
        try:
           temp = [[np.float(i) for i in r['summary'].strip('[').strip(']').split()]]
           simi_score = cosine_similarity(temp, [user_embedding])
           store.append((simi_score[0][0],r['id']))
        except:
            store.append(0,r['id'])

    return store

def load_data(data_file_path, not_include=[]):
    dataframes = []
    for r, d, f in os.walk(data_file_path):
        for file in f:
            print(file)
            if file not in not_include:
                print(file)
                df = pd.read_csv(data_file_path+'/'+file)
                dataframes.append(df)
    return dataframes

def content_based(userid, solo, business,short,listing_df, city,user_data):


    purpose = []
    if solo:
        purpose.append(1)
        purpose.append(0)
    else:
        purpose.append(0)
        purpose.append(1)

    if business:
        purpose.append(1)
        purpose.append(0)
    else:
        purpose.append(0)
        purpose.append(1)

    if short:
        purpose.append(1)
        purpose.append(0)
    else:
        purpose.append(0)
        purpose.append(1)


    df = user_data[user_data['reviewer_id'] == userid]

    purpose_of_trip_sim = []
    city = listing_df[listing_df['city']==city]
    cityx = city.drop(['city','country', 'name', 'host_neighbourhood', 'summary', 'interaction', 'house_rules', 'host_about'], axis=1)
    for i, r in df.iterrows():
        temp = []
        temp.append(r.soloTrip)
        temp.append(r.FamilyTrip)
        temp.append(r.Holiday)
        temp.append(r.Business)
        temp.append(r.short)
        temp.append(r.long)

        purpose_of_trip_sim.append(jaccard_score(purpose,temp))

    df['purpose_of_trip_sim'] = purpose_of_trip_sim

    df = df[['listings', 'ratings', 'purpose_of_trip_sim']]
    embed_merge = df.merge(listing_df, left_on='listings', right_on='id', how='inner')
    merger = df.merge(listing_df, left_on='listings', right_on='id', how='inner').drop(['city','country', 'name', 'host_neighbourhood', 'summary', 'interaction', 'house_rules', 'host_about'], axis=1)

    merger.to_csv('merger.csv')

    df = pd.read_csv('merger.csv')

    intersection = df.columns.intersection(city.columns)

    cityx = cityx[intersection]

    for col in list(df.columns):
        if (col not in ['listings', 'id','purpose_of_trip_sim', 'ratings']) and (col in intersection):
            df[col] = df[col]*df['purpose_of_trip_sim']*df['ratings']/10

    df = df[intersection]
    vectorx = []
    for col in df.columns:
        if col not in ['id']:
            vectorx.append(sum(df[col]))

    store = []
    for i,r in cityx.iterrows():
        vectory = []

        for col in cityx.columns:
            if col not in ['listings','id','purpose_of_trip_sim', 'ratings']:
                vectory.append(city.loc[i,col])
        simi = cosine_similarity([vectorx], [vectory])
        store.append((simi, r['id']))

    summaryscore = embed_similarity('summary', embed_merge,city)
    about_hostscore = embed_similarity('host_about', embed_merge, city)
    house_rulesscore = embed_similarity('house_rules', embed_merge, city)
    interaction_score = embed_similarity('interaction', embed_merge, city)

    dict_summaryscore = {k:v for v,k in summaryscore}
    dict_hostscore = {k:v for v,k in about_hostscore}
    dict_houserulescore = {k:v for v,k in house_rulesscore}
    dict_interactionscore = {k:v for v,k in interaction_score}
    dict_store = {k:v for v,k in store}
    final = []
    for key in dict_store:
        final.append(((0.2*dict_store[key]+0.4*dict_summaryscore[key]+0.1*dict_hostscore[key]+\
                       0.2*dict_houserulescore[key]+0.1*dict_interactionscore[key]),key))

    final.sort()
    return final

def machine_learning_model(userid,solo, business, short, listings, cityname, gbrdata):
    purpose = []
    if solo:
        purpose.append(1)
        purpose.append(0)
    else:
        purpose.append(0)
        purpose.append(1)

    if business:
        purpose.append(1)
        purpose.append(0)
    else:
        purpose.append(0)
        purpose.append(1)

    if short:
        purpose.append(1)
        purpose.append(0)
    else:
        purpose.append(0)
        purpose.append(1)

    gbrfeatures = gbrdata.columns
    listings = listings[['id', 'city']]
    city = listings.merge(gbrdata, left_on="id", right_on="id", how='inner')

    city = city[city['city'] == cityname]
    city = city[gbrfeatures]
    with open('gbr', 'rb') as pickle_file:
        model = pickle.load(pickle_file)
    final = []
    for i,r in city.iterrows():
        f_val = []
        for j in r:
            if j != r['id']:
                f_val.append(j)
        print(f_val)
        test = [purpose + f_val]
        ans = model.predict(test)
        final.append((ans, r['id']))

    return final

def collobrative_filtering(userid,solotrip, business, shortstay, listings, city):
    purpose = ""
    if solotrip:
        purpose = purpose + "10"
    else:
        purpose = purpose + "01"

    if business:
        purpose = purpose + "10"
    else:
        purpose = purpose + "01"

    if shortstay:
        purpose = purpose + "10"
    else:
        purpose = purpose + "01"

    city = listings[listings['city'] == city]['id']
    with open('svd', 'rb') as pickle_file:
        loadalgo1 = pickle.load(pickle_file)
    with open('knnC', 'rb') as pickle_file:
        loadalgo1 = pickle.load(pickle_file)
    with open('knn', 'rb') as pickle_file:
        loadalgo1 = pickle.load(pickle_file)
    # loadalgo1 = pickle.load('svd')
    # loadalgo2 = pickle.load('knnC')
    # loadalgo3 = pickle.load('knn')
    final = []

    for listing in city:
        temp = int(purpose+str(listing))
        predict1 = loadalgo1[1].predict(userid, temp, verbose=True).est
        predict2 = loadalgo2[1].predict(userid, temp, verbose=True).est
        predict3 = loadalgo3[1].predict(userid, temp, verbose=True).est
        ans = (predict1+predict2+predict3)/3
        final.append((ans,listing))

    return final

user_data = pd.read_csv('./data/Final_usersData_withratings_600k.csv')
listings_data = load_data('./data/final_listings')
gbrdata = pd.read_csv('./gbrdata.csv').drop(['Unnamed: 0'],axis=1)

@app.route('/ensemble/<userid>/<solotrip>/<business>/<shortstay>/<city>')
def ensemble(userid, solotrip, business,shortstay,city):

    listings = pd.concat(listings_data, ignore_index=True)
    listings = listings.fillna(0)

    content = content_based(int(userid), solotrip, business, shortstay, listings, city, user_data)
    #collobrative = collobrative_filtering(int(userid), solotrip, business, shortstay, listings, city)
    ml_filter = machine_learning_model(int(userid), solotrip, business, shortstay, listings, city, gbrdata)

    dict_content = {k: v for v, k in content}
    # dict_collobrative = {k: v for v, k in collobrative}
    dict_ml = {k:v for v, k in ml_filter}
    ans =[]
    final=[]
    for key in dict_content:
        final.append(((dict_content[key]+dict_ml[key])/3,key))

    final.sort()
    ans = [int(i[1]) for i in final[len(final)-10:]]
    return jsonify({'data':ans})
if __name__ == '__main__':
   app.run(debug = True)
