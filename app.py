import streamlit as st
import numpy as np
import pickle

st.title("🌱 Smart Agriculture Prediction App")

# Load model (if available)
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    model = None

# Inputs
ACHP = st.number_input("Average chlorophyll (ACHP)")
PHR = st.number_input("Plant height rate (PHR)")
AWWG = st.number_input("Avg wet weight growth (AWWG)")
ALAP = st.number_input("Avg leaf area (ALAP)")
ANPL = st.number_input("Avg number of leaves (ANPL)")
ARD = st.number_input("Avg root diameter (ARD)")
ADWR = st.number_input("Avg dry root weight (ADWR)")
PDMVG = st.number_input("Dry matter veg growth (%)")
ARL = st.number_input("Avg root length (ARL)")
AWWR = st.number_input("Avg wet root weight (AWWR)")
ADWV = st.number_input("Avg dry veg weight (ADWV)")
PDMRG = st.number_input("Dry matter root growth (%)")

if st.button("Predict"):
    features = np.array([[ACHP, PHR, AWWG, ALAP, ANPL, ARD,
                          ADWR, PDMVG, ARL, AWWR, ADWV, PDMRG]])

    if model:
        prediction = model.predict(features)
        st.success(f"Prediction: {prediction[0]}")
    else:
        st.warning("Model not found. Showing dummy result.")
        st.success(f"Sum: {features.sum()}")
