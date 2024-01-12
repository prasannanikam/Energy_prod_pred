import streamlit as st
import pandas as pd
from joblib import load

# Load the trained Linear Regression model
model = load('EGGBR.pkl')  # Replace with the path to your saved model file


# Streamlit app header
st.title('Energy Production Prediction')

# Input fields for user to enter values
st.sidebar.header('Input Parameters')
temperature = st.sidebar.number_input('Temperature (in degrees Celsius)', value=0.0)
exhaust_vacuum = st.sidebar.number_input('Exhaust Vacuum (in cm Hg)', value=0.0)
amb_pressure = st.sidebar.number_input('Ambient Pressure (in millibar)', value=0.0)
r_humidity = st.sidebar.number_input('Relative Humidity (in percentage)', value=0.0)

# Create a DataFrame with user input data
user_input = pd.DataFrame({
    'temperature': [temperature],
    'exhaust_vacuum': [exhaust_vacuum],
    'amb_pressure': [amb_pressure],
    'r_humidity': [r_humidity]
})

# Prediction button
if st.sidebar.button('Predict Energy Production'):
    # Predict using the loaded model
    prediction = model.predict(user_input)
    st.write(f'Predicted Energy Production: {prediction[0]:.2f} MW')
