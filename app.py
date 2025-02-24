import streamlit as st
import pickle

import numpy as np
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
st.title("My ML Model Web App")
st.write("Provide the input features to get a prediction.")

def user_input_features():
    gender=st.sidebar.selection("Gender",("Male","Female"))
    age=st.sidebar.slider("Age",1,100,25)
    height=st.sidebar.slider("Height(cm)",50,250,170)
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
input_df = user_input_features()
st.subheader("User Input Features")
st.write(input_df)
prediction = model.predict(input_df)
st.subheader("Prediction of Calories Burned")
st.write(f"{prediction[0]:.2f} calories")
st.subheader("Model Performance")
st.write(f"Mean Absolute Error: {mae:.2f} calories")

if __name__ == "__main__":
    main()
