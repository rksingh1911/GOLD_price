# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 02:53:41 2022

@author: ROHIT SINGH
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 
#pip install streamlit
from statsmodels.tsa.arima_model import ARIMA
from pickle import dump
from pickle import load

st.title('Model Deployment: forecasting')

st.sidebar.header('User Input Parameters')

def main():
    forecasting = st.sidebar.number_input("Insert the forecast point")
    data = {'forecasting':forecasting,}
    features = pd.DataFrame(data,index = [0])
    return features 

df = main()
st.subheader('User Input parameters')
st.write(df)

# load the model from disk
pickle_in = open("model_1_fit.pkl","rb")
loaded_model =pickle.load(pickle_in)


prediction = loaded_model.forecast(df)

st.subheader('forecasted Result')
st.write(prediction)
