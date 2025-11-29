import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import streamlit as st
import pickle

df = pd.read_csv("Titanic-Dataset.csv")

df.drop(columns=["Cabin", "Ticket"], inplace=True)

df["Age"].fillna(df["Age"].median(), inplace=True)

df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

df["Title"] = df["Name"].str.extract(" ([A-Za-z]+)\. ")

df.drop(columns=["Name", "PassengerId"], inplace=True)

df = pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True)

df[["Sex_male", "Embarked_Q", "Embarked_S"]] = df[
    ["Sex_male", "Embarked_Q", "Embarked_S"]
].astype(int)

X = df.drop(["Survived", "Title"], axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=45
)


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
score = accuracy_score(y_pred, y_test)
print(f"The accuracy score of the model is {score}")

with open("knn_model.pkl", "wb") as f:
    pickle.dump(knn, f)

with open("columns.pkl", "wb") as f:
    pickle.dump(X.columns.to_list(), f)
