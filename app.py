import streamlit as st
import pickle
import pandas as pd
import numpy as np
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
st.title("My ML Model Web App")
st.write("Provide the input features to get a prediction.")

def user_input_features():
    gender=st.sidebar.selectbox("Gender",("Male","Female"))
    age=st.sidebar.slider("Age",1,100,25)
    height = st.sidebar.slider("Height (meters)", 0.5, 2.5, 1.7)
    weight=st.sidebar.slider("Weight(kg)",10,200,70)
    duration = st.sidebar.slider("Duration of Exercise (minutes)", 1, 300, 30)
    heart_rate = st.sidebar.slider("Heart Rate (bpm)", 50, 200, 120)
    body_temp = st.sidebar.slider("Body Temperature (°C)", 35, 42, 37)
    bmi = st.sidebar.slider("BMI", 10, 50, 25)
    data = {
            'Gender': 1 if gender == "Male" else 0,
            'Age': age,
            'Height': height,
            'Weight': weight,
            'Duration': duration,
            'Heart_Rate': heart_rate,
            'Body_Temp': body_temp,
            'BMI': bmi
    }
    return pd.DataFrame(data,index=[0])
input_df = user_input_features()
st.subheader("User Input Features")
st.write(input_df)
if st.button("Predict Calories Burned"):
    prediction = model.predict(input_df)
    
st.subheader("Prediction of Calories Burned")
st.write(f"{prediction[0]:.2f} calories")

