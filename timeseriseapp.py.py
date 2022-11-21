"""
Created on 29-07-2022 by Ankit Modak
"""

# Installing packages
import pickle
import pandas as pd
import numpy as np
import streamlit as st
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA


# Title and sidebar
st.title("WelCome to Gold price Forecast app")
st.sidebar.header("User input parameters")


# Input function
def user_input_features():
    fc_days = st.sidebar.number_input("Insert number of days to predict.")
    return int(fc_days)


prediction_days = user_input_features()


# Loading trained model and making predictions
loaded_model = pickle.load(open("C:\\Users\\91896\\excel data science\\my Jupiter class one\\result.pickle", "rb"))
forcasted = loaded_model.forecast(522 + prediction_days)


# Output predictions
st.subheader('Forecasted Result')
st.write(forcasted[522:])



