import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open('C:\\Users\\Khushi Verma\\Documents\\HEC-X\\Studies\\Sem 3\\02 - Tooling for Data Scientists\\Customer_Churn_Prediction\\models\\churn_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Function to predict churn based on user input
def predict_churn(input_data):
    prediction = model.predict(input_data)
    return prediction

# Streamlit app UI
st.title("Customer Churn Prediction App")

# Input fields for customer data
st.sidebar.header("Customer Input Features")
tenure = st.sidebar.number_input("Tenure (months)", min_value=0, max_value=72, value=10)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)

# Assuming we used only two features in this case for simplicity
input_data = pd.DataFrame([[tenure, monthly_charges]], columns=['tenure', 'MonthlyCharges'])

if st.button("Predict Churn"):
    prediction = predict_churn(input_data)
    st.write(f"Prediction: {'Customer will churn' if prediction == 1 else 'Customer will not churn'}")

st.write("""
### About this app:
This app uses a logistic regression model trained on the Telco Customer Churn dataset to predict if a customer will churn based on input data.
You can modify the 'Tenure' and 'Monthly Charges' using the sliders and predict if the customer is likely to churn.
""")