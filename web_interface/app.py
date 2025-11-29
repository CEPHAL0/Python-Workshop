import streamlit as st
import numpy as np
import pickle


# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Machine Learning Prediction App")
st.write("This app uses a trained ML model to predict values based on user input")


value = st.number_input("Enter a value: ", min_value=0.0, value=1.0)

if st.button("Predict"):
    input_array = np.array([[value]])
    pred = model.predict(input_array)[0]
    st.success(f"Predicted output: {pred:.2f}")

