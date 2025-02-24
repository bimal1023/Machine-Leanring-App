import streamlit as st
import pickle
import numpy as np


st.title("My ML Model Web App")
st.write("Provide the input features to get a prediction.")

# Example input fields (adjust these based on your model's requirements)
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)

if st.button("Predict"):
    # Prepare your input data. Make sure the shape aligns with what your model expects.
    input_data = np.array([[feature1, feature2]])
    prediction = model.predict(input_data)
    st.write("Prediction:", prediction)
