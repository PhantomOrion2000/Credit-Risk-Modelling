Credit Risk Modelling
This project develops a credit risk prediction model that can classify clients based on their credit risk levels. The project involves data preprocessing, model training, and deploying the model as a web application using Streamlit.

Table of Contents
Project Overview
File Structure
Setup Instructions
Deployment
Usage
Technologies Used
Project Overview
The goal of this project is to assess credit risk by predicting the probability of loan default based on historical data. The solution includes a web app interface where users can upload their data or input features to get risk predictions. This application is designed to be accessible for business use cases where predicting creditworthiness is key.

File Structure
The project repository is organized as follows:

bash
Copy code
Credit-Risk-Modelling/
├── Data_cleaning.ipynb            # Jupyter Notebook for data preprocessing and feature engineering
├── Model.ipynb                    # Jupyter Notebook for model training and evaluation
├── app.py                         # Streamlit application script for deployment
├── columns_to_be_kept_numerical.pkl  # Serialized file of selected numerical columns
├── column_transformer.pkl         # Preprocessor for categorical feature encoding
├── model.pkl                      # Trained machine learning model
├── requirements.txt               # List of required packages for setup
└── README.md                      # Project documentation
Setup Instructions
To run this project locally, follow these steps:

Clone the Repository:

bash
Copy code
git clone https://github.com/PhantomOrion2000/Credit-Risk-Modelling.git
cd Credit-Risk-Modelling
Install Dependencies:

Ensure that Python 3.x is installed.
Install the necessary packages from requirements.txt:
bash
Copy code
pip install -r requirements.txt
Ensure Necessary Files:

Confirm that the serialized files model.pkl, columns_to_be_kept_numerical.pkl, and column_transformer.pkl are available in the main project directory.
Deployment
The application is already deployed on Streamlit Cloud. You can access it via this link.

To run the app locally on Streamlit:

bash
Copy code
streamlit run app.py
Usage
Upload or Enter Data: Users can upload their own data or enter input parameters directly through the interface.
Get Prediction: The app provides a prediction of the credit risk level based on the input.
Interpret Results: View probability scores and understand the likelihood of default, which aids in decision-making for credit risk assessment.
Technologies Used
Python: Core programming language for data processing and model building.
Streamlit: Framework for deploying the model as an interactive web application.
Scikit-Learn: Used for machine learning algorithms and preprocessing.
Pickle: For saving the trained model and preprocessing objects.
Future Improvements
Potential improvements include implementing additional feature engineering steps, exploring other algorithms, and adding interpretability layers to understand model predictions better.
