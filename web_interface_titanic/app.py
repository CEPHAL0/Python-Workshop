import streamlit as st
import numpy as np
import pickle
import pandas as pd

st.title("🛳️ Titanic Survival Predcition App")

model = pickle.load(open("knn_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.sidebar.header("Passenger Input Features")

Pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
Age = st.sidebar.number_input("Age", 1, 100, 25)
SibSp = st.sidebar.number_input("Sibling/Spouse Count", 0, 10, 0)
Parch = st.sidebar.number_input("Parent/Children Count", 0, 10, 0)
Fare = st.sidebar.number_input("Fare Paid", 0, 600, 32)

Sex_male = st.sidebar.selectbox("Sex", ["Male", "Female"])
Embarked = st.sidebar.selectbox("Port of Embarkation", ["S", "C", "Q"])


FamilySize = SibSp + Parch + 1
Sex_male = 1 if Sex_male == "Male" else 0
Embarked_S = 1 if Embarked == "S" else 0
Embarked_Q = 1 if Embarked == "Q" else 0

input_data = pd.DataFrame(
    [[Pclass, Age, SibSp, Parch, Fare, FamilySize, Sex_male, Embarked_S, Embarked_Q]],
    columns=columns,
)


if st.button("Predict Survival"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("The passenger would likely to Survive")
    else:
        st.error("The passenger would not survive")
