import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('model.joblib2')

# Define the input fields
st.title('Malaikas Tech Salary Prediction App')

st.header('Enter the details:')
work_year = st.number_input('Work Year', min_value=1980, max_value=2024, value=2023)
experience_level = st.selectbox('Experience Level', ['EN', 'MI', 'SE', 'EX'])
employment_type = st.selectbox('Employment Type', ['FT', 'PT', 'CT', 'FL'])
job_title = st.text_input('Job Title')
salary = st.number_input('Salary', value=0)
salary_currency = st.text_input('Salary Currency')
employee_residence = st.text_input('Employee Residence')
remote_ratio = st.slider('Remote Ratio', min_value=0, max_value=100, value=0)
company_location = st.text_input('Company Location')
company_size = st.selectbox('Company Size', ['S', 'M', 'L'])

# Make prediction when the button is pressed
if st.button('Predict Salary'):
    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'work_year': [work_year],
        'experience_level': [experience_level],
        'employment_type': [employment_type],
        'job_title': [job_title],
        'salary': [salary],
        'salary_currency': [salary_currency],
        'employee_residence': [employee_residence],
        'remote_ratio': [remote_ratio],
        'company_location': [company_location],
        'company_size': [company_size]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.subheader(f'Predicted Salary in USD: ${prediction[0]:,.2f}')
