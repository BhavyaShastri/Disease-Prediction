import pickle
from tkinter import OptionMenu
import streamlit as st
import streamlit_option_menu
import os


#loading the saved models
"""
directory_location = os.listdir(r'C:\Users\ASUS\OneDrive - Graphic Era University\Desktop\Disease_Predictor\saved')
for file in directory_location:
    print(file)

    #sidebar for navigation
    with st.sidebar:
        selected = OptionMenu('Disease Predictor',['Diabetes','HeartDisease','Parkinsons'])
"""
    



#clf_loaded = joblib.load('classifier_file_name.joblib')
#diabetes_model = joblib.load('C:\Users\ASUS\OneDrive - Graphic Era University\Desktop\Disease_Predictor\saved\Diabetes.joblib')

#pd.read_csv("C:/Users/ASUS/OneDrive - Graphic Era University/Desktop/Disease_Predictor/saved")
#pd.read_csv("C:/Users/ASUS/OneDrive - Graphic Era University/Desktop/Disease_Predictor")


diabetes_model = pickle.load(open(r'C:\Users\ASUS\OneDrive - Graphic Era University\Desktop\Disease_Predictor\Disease-Prediction\Diabetes.ipynb','rb'))
#heart_disease_model = pickle.load(open('C:/Users/ASUS/OneDrive - Graphic Era University/Desktop/Disease_Predictor/saved/HeartDisease','rb'))
#Parkinsons_model = pickle.load(open('C:/Users/ASUS/OneDrive - Graphic Era University/Desktop/Disease_Predictor/saved/Parkinsons','rb'))

