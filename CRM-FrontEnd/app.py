import streamlit as st
import pandas as pd
import pickle
import io
from sklearn.base import BaseEstimator, TransformerMixin
import xgboost
import os




# Define the custom transformer class for education mapping
class EducationMapper(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.education_mapping = {
            'SSC': 1,
            '12TH': 2,
            'GRADUATE': 3,
            'UNDER GRADUATE': 3,
            'POST-GRADUATE': 4,
            'OTHERS': 1,
            'PROFESSIONAL': 3
        }

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['EDUCATION'] = X['EDUCATION'].map(self.education_mapping)
        return X


# Load necessary components
file_path1  = os.path.join(os.path.dirname(__file__), 'columns_to_be_kept_numerical.pkl')
file_path2 = os.path.join(os.path.dirname(__file__), 'column_transformer.pkl')
file_path3 = os.path.join(os.path.dirname(__file__), 'model.pkl')
numerical_columns = pickle.load(open(file_path1, 'rb'))
column_transformer = pickle.load(open(file_path2, 'rb'))
model = pickle.load(open(file_path3, 'rb'))
# numerical_columns = pickle.load(open('/Users/subhadeepchoudhury/Desktop/Projects/credit risk modelling/CRM-FrontEnd/columns_to_be_kept_numerical.pkl', 'rb'))
# column_transformer = pickle.load(open('/Users/subhadeepchoudhury/Desktop/Projects/credit risk modelling/CRM-FrontEnd/column_transformer.pkl', 'rb'))
# model = pickle.load(open('/Users/subhadeepchoudhury/Desktop/Projects/credit risk modelling/CRM-FrontEnd/model.pkl', 'rb'))
cat_columns = ['MARITALSTATUS', 'GENDER', 'last_prod_enq2', 'first_prod_enq2']

# Set the title and description for the app
st.title("Credit Risk Prediction Tool")
st.markdown("""
Welcome to the Credit Risk Prediction Tool! Upload an Excel file with customer data, 
and the model will predict credit risk based on the provided inputs. 
The processed data, including the predictions, will be available for download.
""")

# Upload Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])


# Define a function to convert DataFrame to Excel
def to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    processed_data = output.getvalue()
    return processed_data


# Process the file if uploaded
if uploaded_file:
    try:
        # Read the uploaded Excel file
        input_df = pd.read_excel(uploaded_file)

        # Display the input data
        st.subheader("Uploaded Data")
        st.dataframe(input_df)

        # Process the data using the column transformer and model
        input_df_transformed = column_transformer.transform(input_df)

        # Extract the feature names from the OneHotEncoder
        encoded_columns = column_transformer.named_transformers_['onehot'].get_feature_names_out(cat_columns)

        # Combine encoded categorical and numerical columns
        all_columns = list(encoded_columns) + numerical_columns + ['EDUCATION']

        # Convert transformed data into a DataFrame
        input_encoded = pd.DataFrame(input_df_transformed, columns=all_columns)

        # Make predictions using the model
        predictions = model.predict(input_encoded)

        # Add predictions to the original input DataFrame
        output_df = input_df.copy()
        output_df['Credit Risk Prediction'] = predictions

        # Display the output data with predictions
        st.subheader("Processed Data with Predictions")
        st.dataframe(output_df)

        # Allow download of the processed data
        processed_file = to_excel(output_df)
        st.download_button(
            label="Download Processed Excel File",
            data=processed_file,
            file_name="processed_data_with_predictions.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.info("Please upload an Excel file to start.")
