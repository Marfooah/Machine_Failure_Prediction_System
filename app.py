import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ------------------------------
# LOAD MODELS & SCALER
# ------------------------------
lr = pickle.load(open("log.pkl", "rb"))
knn = pickle.load(open("knn.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
le = pickle.load(open("encoder.pkl", "rb"))

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="Machine Failure Prediction", layout="centered")

st.title("⚙️ Machine Failure Prediction System")
st.write("Predict whether a machine will fail based on input parameters.")

# ------------------------------
# SIDEBAR NAVIGATION
# ------------------------------
page = st.sidebar.selectbox("Navigate", ["Home", "Predict", "About"])

# ------------------------------
# HOME PAGE
# ------------------------------
if page == "Home":
    st.header("Welcome 👋")
    st.write("""
    This system uses Machine Learning models (Logistic Regression & KNN)
    to predict machine failure.

    👉 Go to **Predict** to test the model.
    """)

# ------------------------------
# PREDICTION PAGE
# ------------------------------
elif page == "Predict":
    st.header("Enter Machine Details")

    type_input = st.selectbox("Type", ["L", "M", "H"])
    air_temp = st.number_input("Air Temperature (K)", value=298.0)
    process_temp = st.number_input("Process Temperature (K)", value=308.0)
    rpm = st.number_input("Rotational Speed (rpm)", value=1500)
    torque = st.number_input("Torque (Nm)", value=40.0)
    tool_wear = st.number_input("Tool Wear (min)", value=10)

    model_choice = st.selectbox("Select Model", ["Logistic Regression", "KNN"])

    if st.button("Predict"):
        # Create DataFrame
        input_data = pd.DataFrame([{
            "Type": type_input,
            "Air temperature [K]": air_temp,
            "Process temperature [K]": process_temp,
            "Rotational speed [rpm]": rpm,
            "Torque [Nm]": torque,
            "Tool wear [min]": tool_wear
        }])

        # Encode Type
        input_data["Type"] = le.transform(input_data["Type"])

        # Scale
        input_scaled = scaler.transform(input_data)

        # Predict
        if model_choice == "Logistic Regression":
            prediction = lr.predict(input_scaled)[0]
        else:
            prediction = knn.predict(input_scaled)[0]

        # Output
        if prediction == 1:
            st.error("⚠️ Machine Failure Predicted")
        else:
            st.success("✅ No Failure Predicted")

# ------------------------------
# ABOUT PAGE
# ------------------------------
elif page == "About":
    st.header("About Project")
    st.write("""
    - Models Used: Logistic Regression, KNN  
    - Dataset: Machine Failure Dataset  
    - Features: Temperature, Speed, Torque, Tool Wear  
    - Goal: Predict machine failure in advance  

    Built using Streamlit.
    """)
