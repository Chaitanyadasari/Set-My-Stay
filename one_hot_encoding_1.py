import pandas as pd
import numpy as np

def one_hot_encoding(filename):

    airbnb = pd.read_csv(filename)
    dum_df = pd.get_dummies(airbnb, columns=["cancellation_policy"])
    airbnb = airbnb.merge(dum_df).drop(columns=["cancellation_policy"])
    
    dum_df = pd.get_dummies(airbnb, columns=['bed_type'])
    airbnb = airbnb.merge(dum_df).drop(columns=['bed_type'])
    
    dum_df = pd.get_dummies(airbnb, columns=["host_response_time"])
    airbnb = airbnb.merge(dum_df).drop(columns=["host_response_time"])
    
    airbnb.loc[airbnb['property_type'] == 'Bed and breakfast', 'property_type'] = 'Bed & Breakfast'
    airbnb.loc[airbnb['property_type'] == 'Boat', 'property_type'] = 'Houseboat'
    dum_df = pd.get_dummies(airbnb,columns=["property_type"])
    airbnb = airbnb.merge(dum_df).drop(columns=["property_type"])
    
    dum_df = pd.get_dummies(airbnb,columns=["room_type"])
    airbnb = airbnb.merge(dum_df).drop(columns=["room_type"])
    
    airbnb.loc[airbnb['bedrooms'] > 3, 'bedrooms'] = 3
    dum_df = pd.get_dummies(airbnb,columns=["bedrooms"])
    airbnb = airbnb.merge(dum_df).drop(columns=["bedrooms"])
    
    dum_df = pd.get_dummies(airbnb,columns=["bathrooms"])
    airbnb = airbnb.merge(dum_df).drop(columns=["bathrooms"])
    
    airbnb.loc[airbnb['beds'] > 4, 'beds'] = 4
    dum_df = pd.get_dummies(airbnb,columns=["beds"])
    airbnb = airbnb.merge(dum_df).drop(columns=["beds"])
    
    airbnb = airbnb.drop(columns='access')
    airbnb = airbnb.drop(columns='space')
    airbnb = airbnb.drop(columns='monthly_price')
    airbnb = airbnb.drop(columns='latitude')
    airbnb = airbnb.drop(columns='longitude')
    
    airbnb.loc[airbnb['host_is_superhost'] == 't', 'host_is_superhost'] = 1
    airbnb.loc[airbnb['host_is_superhost'] == 'f', 'host_is_superhost'] = 0
    
    airbnb.loc[airbnb['host_identity_verified']=='t', 'host_identity_verified'] =1
    airbnb.loc[airbnb['host_identity_verified']=='f', 'host_identity_verified'] =0
    
    airbnb.loc[airbnb['is_location_exact'] == 't', 'is_location_exact'] = 1
    airbnb.loc[airbnb['is_location_exact'] == 'f', 'is_location_exact'] = 0
    
    airbnb.loc[airbnb['requires_license'] == 'f', 'requires_license'] = 1
    airbnb.loc[airbnb['requires_license'] == 't', 'requires_license'] = 0
    
    airbnb.loc[airbnb['minimum_nights'] > 4, 'minimum_nights'] = 4
    dum_df = pd.get_dummies(airbnb,columns=["minimum_nights"])
    airbnb = airbnb.merge(dum_df).drop(columns=["minimum_nights"])
    
    airbnb.loc[airbnb['guests_included'] > 3, 'guests_included'] = 3
    dum_df = pd.get_dummies(airbnb,columns=["guests_included"])
    airbnb = airbnb.merge(dum_df).drop(columns=["guests_included"])
    
    airbnb.loc[airbnb['accommodates'] > 3, 'accommodates'] = 3
    dum_df = pd.get_dummies(airbnb, columns=["accommodates"])
    airbnb = airbnb.merge(dum_df).drop(columns=['accommodates'])
    
    airbnb['cleaning_fee'] = airbnb['cleaning_fee'].fillna('$0')
    airbnb['cleaning_fee']=airbnb['cleaning_fee'].str.strip('$').astype(float)
    airbnb.loc[airbnb['cleaning_fee'] == 0, 'cleaning_fee'] = 1
    airbnb.loc[airbnb['cleaning_fee'] > 0, 'cleaning_fee'] = 1/airbnb.loc[airbnb['cleaning_fee'] > 0, 'cleaning_fee']
    
    airbnb['security_deposit'] = airbnb['security_deposit'].fillna('$0')
    for index, row in airbnb.iterrows():
        airbnb.loc[index, 'price'] = int(row['price'].strip('$').replace(',', '').split('.')[0])
        airbnb.loc[index, 'security_deposit'] = int(row['security_deposit'].strip('$').replace(',', '').split('.')[0])
    
    avg = airbnb['price'].mean()
    dev = airbnb['price'].std()
    
    for index, row in airbnb.iterrows():
        if row['price'] > avg+dev:
            airbnb.loc[index , 'price'] = '$$$'
        elif (row['price'] < avg+dev) and (row['price'] > avg-dev):
            airbnb.loc[index, 'price'] = '$$'
        else:
            airbnb.loc[index, 'price'] = '$'
    
        if (row['country'] in row['host_location']) or (row['city'] in row['host_location']):
            airbnb.loc[index, 'host_location'] = 'local'
        else:
            airbnb.loc[index, 'host_location'] = 'non-local'
    
    dum_df = pd.get_dummies(airbnb,columns=["host_location"])
    airbnb = airbnb.merge(dum_df).drop(columns=["host_location"])
    
    dum_df = pd.get_dummies(airbnb,columns=["price"])
    airbnb = airbnb.merge(dum_df).drop(columns=['price'])
    
    airbnb.loc[airbnb['security_deposit'] == 0, 'security_deposit'] = 1
    airbnb.loc[airbnb['security_deposit'] > 0, 'security_deposit'] = 1/airbnb.loc[airbnb['security_deposit'] > 0, 'security_deposit']
    
    filename =  filename.strip('.csv').strip('translated')+'onehoted.csv'
    airbnb.to_csv(filename)

one_hot_encoding('translated_madrid.csv')
one_hot_encoding('translated_edinburgh.csv')
one_hot_encoding('translated_amsterdam.csv')
one_hot_encoding('translated_boston.csv')
one_hot_encoding('translated_paris.csv')
one_hot_encoding('translated_berlin.csv')