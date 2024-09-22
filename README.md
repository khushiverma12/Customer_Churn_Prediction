# Customer Churn Prediction Project

This project predicts customer churn using a machine learning model built on the Telco Customer Churn Dataset. The prediction model is deployed in a Streamlit web app, allowing users to input customer details and receive real-time predictions on whether a customer is likely to churn. The project is containerized using Docker to ensure smooth and scalable deployment across various environments.

## Project Structure

```bash
Customer_Churn_Prediction/
├── code/                 # Contains the code files
│   ├── model_old.py      # Backup Code
│   ├── model.py          # Code for data loading, EDA, model training, evaluation
│   ├── model.ipynb       # Jupyter Notebook used for running code
│   ├── app.py            # Streamlit app for making predictions
│   ├── requirements.txt  # List of Python dependencies
│   ├── Dockerfile        # Dockerfile to containerize the app
│
├── data/                 # Contains dataset files
│   ├── full_data.csv     # Full dataset used for training
│
├── docs/                 # Documentation for the project
│   ├── README.md         # Project overview and setup instructions
│
├── models/               # Contains the trained model files
│   └── churn_model.pkl   # Final machine learning model
│   └── churn_model_old.pkl   # Backup 
│
└── README.md             # Main README with instructions and documentation 

```

## Project Overview

### Objective
The goal of this project is to predict customer churn (i.e., whether a customer will stop using a service) using machine learning techniques. Churn prediction helps businesses proactively identify customers who are likely to leave, allowing them to take actions to retain them.

### Dataset

The dataset used for this project is the Telco Customer Churn Dataset, which contains customer data such as:

Demographics: Gender, Senior Citizen status, Partner, Dependents
Service details: Contract, Payment Method, Tenure
Billing and payment information: Monthly charges, Total charges
Churn status: Whether the customer has churned or not

This data is used to train the machine learning model.

### Technologies Used

Python: For data manipulation, model building, and deployment
pandas: For data loading and manipulation
scikit-learn: For model training and evaluation
Streamlit: For building an interactive web app for users to input data and get predictions
Docker: For containerizing the app to ensure portability and scalability
Git: For version control

## Setup and Installation

Follow these steps to set up the project on your local machine.

### Prerequisites
Before you can run the app, ensure that you have the following installed:

Python 3.9+
pip (Python's package installer)
Docker (optional, if you wish to containerize the app)

### Steps to Set Up the Environment
1. Clone the Repository
```bash
git clone https://github.com/your-username/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
```

2. Create and Activate a Virtual Environment
It's good practice to work in a virtual environment to avoid conflicts with other projects.
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the Required Dependencies
```bash
pip install -r code/requirements.txt
```

### Running app locally

To run the app locally without Docker:

1. Navigate to the code directory:
```bash
cd code
```

2. Start the Streamlit app:
```bash
streamlit run app.py
```
3. Open your browser and go to http://localhost:8501 to interact with the app.

### Running on Docker

1. Build Docker image
```bash
docker build -t churn_app .
```

2. Run the container:
```bash
docker run -p 8501:8501 churn_app
```
This will make the app accessible at http://localhost:8501.

## Usage
Once the app is running, you can input customer details in the sidebar (such as tenure and monthly charges), and the app will predict whether the customer is likely to churn.

Streamlit Interface:

Tenure (months): The number of months the customer has been with the service.
Monthly Charges ($): The monthly billing amount for the customer.
Predict Churn Button: After inputting the customer details, click this button to receive a prediction:
Customer will churn: If the model predicts that the customer will likely leave.
Customer will not churn: If the customer is likely to stay.

## Model Details

The machine learning model used in this project is a Logistic Regression model, trained on features such as customer tenure, contract type, and payment method. The model was trained and evaluated using scikit-learn, and the trained model is saved as a pickle file (churn_model.pkl).

Model Training
The training script is located in code/model.py. It includes:

Data loading and cleaning
Exploratory data analysis (EDA)
Model training and evaluation
Saving the model to the models/ folder for later use in the app

## License

This project is licensed under the MIT License

## Acknowledgments

Dataset: Telco Customer Churn Dataset from Kaggle
The Team Data Science Process (TDSP) framework used to structure this project.