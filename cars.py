import streamlit as st
import pickle as pkl
import pandas as pd

pipe = pkl.load(open('pipe.pkl','rb'))
data = pkl.load(open('data.pkl','rb'))

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
print(data.head())

if st.button('Predict Price'):
    st.write(type(company))
    st.write(company)
    st.write(type(name))
    st.write(name)
    st.write(type(year))
    st.write(year)
    st.write(type(kms))
    st.write(kms)
    st.write(type(fuel))
    st.write(fuel)
    #st.write(pipe.predict(pd.DataFrame([[name,company,year,kms,fuel]],columns=['name','company','year','kms_driven','fuel_type'])))
print('Its working')