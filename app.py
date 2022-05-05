import streamlit as st
import pickle

file=open('model.pkl','rb')
model=pickle.load(file)

st.title('Prediction of IoT Feed')

hum=st.text_input('Enter Hum: ')
temp=st.text_input('Enter Temp: ')

if st.button('Predict'):
    outcome=model.predict([[hum,temp]])[0]
    st.success('Label Predicted: '+ str(outcome))