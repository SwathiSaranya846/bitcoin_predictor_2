import streamlit as st
from datetime import datetime
from model import predict

st.set_page_config(page_title="Bitcoin Predictor", layout="centered")

st.title("₿ Bitcoin Price Prediction")

st.write("Enter today's market values:")

open_price = st.number_input("Open Price", min_value=0.0)
high_price = st.number_input("High Price", min_value=0.0)
low_price = st.number_input("Low Price", min_value=0.0)
close_price = st.number_input("Close Price", min_value=0.0)

month = st.selectbox(
    "Month",
    list(range(1, 13)),
    index=datetime.now().month - 1
)

if st.button("Predict 🚀"):
    result = predict(open_price, high_price, low_price, close_price, month)

    st.subheader("📊 Prediction Result")

    st.success(f"Predicted Price: {result['price']}")
    st.info(f"Direction: {result['direction']}")
    st.warning(f"Confidence: {result['confidence']}")