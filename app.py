import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load your trained model
try:
    with open('price_prediction_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'price_prediction_model.pkl' exists.")
    st.stop()

st.title('Area Price Prediction')

# Input fields
area = st.number_input('Area (sq ft)', min_value=1)
bedrooms = st.number_input('Number of Bedrooms', min_value=1)
# Add more input fields as per your model's features (e.g., location, etc.)
# If location is a categorical variable, use st.selectbox, or st.text_input if it is a text variable.

# Create a DataFrame from the input
input_data = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    # Add other features here
})

if st.button('Predict Price'):
    try:
        prediction = model.predict(input_data)
        st.success(f'Predicted Price: ${prediction[0]:,.2f}') #format the number.
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")