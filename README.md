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
