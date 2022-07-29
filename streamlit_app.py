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
       fc_days = st.sidebar.number_input("Insert number of days to predict.")
       return int(fc_days)


prediction_days = main()

# Loading trained model and making predictions
loaded_model = pickle.load(open("C:\\Users\\91896\\excel data science\\my Jupiter class one\\model_1_fit.pkl", "rb"))
predictions = loaded_model.forecast(652 + prediction_days)


# Output predictions
st.subheader('Predicted Result')
st.write(predictions[652:])
