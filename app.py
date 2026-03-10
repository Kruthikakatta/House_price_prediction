import streamlit as st
import joblib
import numpy as np

# Title
st.title("🏠 House Price Prediction App")

# Load model
model = joblib.load("house_price_model.pkl")

# Inputs
overall_qual = st.slider("Overall Quality",1,10,5)
gr_liv_area = st.number_input("Living Area (sq ft)",500,5000,1500)
garage_cars = st.slider("Garage Cars",0,4,2)
total_area = st.number_input("Total Area",500,6000,2000)
house_age = st.slider("House Age",0,100,10)

# Prediction
if st.button("Predict Price"):

    features = np.array([[overall_qual,gr_liv_area,garage_cars,total_area,house_age]])

    prediction = model.predict(features)

    st.success(f"Predicted Price: ${prediction[0]:,.2f}")