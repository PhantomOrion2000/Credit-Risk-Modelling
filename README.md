# Credit Risk Modeling

This project focuses on predicting credit risk using machine learning techniques. It utilizes various data preprocessing steps, feature engineering, and an optimized XGBoost model for accurate risk assessment. The final model is deployed as an interactive web application using **Streamlit Cloud**.

---

## 🚀 Features
- **Custom Transformer**: A custom pipeline transformer to map education levels for feature preprocessing.
- **Model Optimization**: Hyperparameter tuning for XGBoost to improve prediction accuracy.
- **Interactive Deployment**: An easy-to-use Streamlit web app for visualizing predictions.
- **Comprehensive Workflow**: End-to-end machine learning pipeline from data preparation to deployment.

---

## 📂 Project Structure

### Explanation of Key Items:
- **`.idea/`**: Folder for IDE-specific configuration files (should be ignored in `.gitignore` if committing to version control).
- **`.gitignore`**: Defines files and folders to exclude from version control (e.g., `.idea`, `.DS_Store`, `.pkl` files).
- **`Procfile`**: Required by Heroku to specify how the app should run.
- **`.pkl` Files**: Saved artifacts for transformers, numeric columns, and the machine learning model.
- **`.ipynb` Files**:
  - `CRM.ipynb`: Likely contains analysis or workflows for CRM-specific tasks.
  - `Data_cleanin.ipynb`: Steps for cleaning and preprocessing data.
  - `Model.ipynb`: Code for training and evaluating the machine learning model.
- **Excel Files**:
  - `Unseen_Dataset.xlsx`: Data for testing the model or for future predictions.
  - `case_study1.xlsx` and `case_study2.xlsx`: Datasets used for specific case studies.
  - `merged_data.xlsx`: Merged dataset for modeling or analysis.
- **`requirements.txt`**: Lists all the Python libraries needed to run this project.
- **`README.md`**: Contains documentation for understanding and running the project.

---

Let me know if you'd like further refinements or additional explanations!


---

## ⚙️ Tools & Technologies
- **Languages**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, XGBoost, Streamlit
- **Deployment**: Streamlit Cloud

---

## 📊 Data Preprocessing
- **Handling Missing Values**: Replaced with suitable measures.
- **Categorical Encoding**: Custom mapping for educational qualifications and one-hot encoding for other features.
- **Feature Scaling**: Standardized numerical features for model input compatibility.
- **Train-Test Split**: Ensured balanced datasets for training and evaluation.

---

## 🧠 Modeling
- **Model**: XGBoost
- **Performance Metrics**: Evaluated using precision, recall, and F1-score to handle class imbalance effectively.
- **Feature Importance**: Identified key predictors using SHAP analysis.

---

## 🖥️ Deployment
The project is deployed using **Streamlit Cloud**, offering:
- **Prediction Input**: Users can input features to get predictions on credit risk.
- **Model Insights**: Visualizations to understand model performance and feature contributions.

---

## 📝 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/PhantomOrion2000/Credit-Risk-Modelling.git
2. Navigate to the project directory:
   ```bash
   cd Credit-Risk-Modelling
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Streamlit app:
   ```bash
   streamlit run app/app.py
