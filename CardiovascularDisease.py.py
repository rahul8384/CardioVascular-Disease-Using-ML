# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved model 
loaded_model = pickle.load(open('E:/cardioD/heart_disease_model.sav', 'rb'))

#Input_data = (42,1,3,148,244,0,0,178,0,0.8,2,2,2)
#Input_data_as_numpy_array = np.asarray(Input_data)
#Input_data_reshaped = Input_data_as_numpy_array.reshape(1,-1)
#Prediction = loaded_model.predict(Input_data_reshaped)
#print(Prediction)

#if(Prediction[0]== 0):
 # print('the person does not have a cardiovascular disease')
#else:
 # print('the person have a cardiovascular disease')
 
 #sidebar for navigation
 
 with st.sidebar:
