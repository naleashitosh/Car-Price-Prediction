import pickle as pkl
import pandas as pd
import numpy as np
import streamlit as st

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score

from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

#data = pd.read_csv('processed_data.csv',index_col=[0])
data = pkl.load(open('data.pkl','rb'))

x = data.drop(['Price'],axis=1)
y = data['Price']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state= 436)

ohe = OneHotEncoder(categories='auto')
ohe.fit(x[['name','company','fuel_type']])

lr = LinearRegression()
transformer = make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),
                                     remainder='passthrough')

pipe = make_pipeline(transformer,lr)
pipe.fit(x_train,y_train)
#print(data.head())

data_name = sorted(list(data.name.unique()))
data_company = sorted(list(data.company.unique()))
fuel = list(data.fuel_type.unique())

st.header('Car Price Prediction')
company = st.selectbox('select the company',data_company)
model = []

for i in data_name:
    if company in i:
        model.append(i)

name = st.selectbox('select the model',model)
fuel = st.selectbox('select the fuel type',fuel)
year = st.selectbox('select the year',sorted(data.year.unique()))
kms = st.number_input('Enter kilpmeters driven')

if st.button('Predict Price'):
    st.header('Predicted Price is :')
    price = int(pipe.predict(pd.DataFrame([[name,company,year,kms,fuel]],columns=['name','company','year','kms_driven','fuel_type']))[0])
    price = "{:,}".format(price)
    st.subheader("₹ "+ price)
print('Its working')