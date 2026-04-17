An end-to-end Machine Learning project that predicts machine failure using Logistic Regression and K-Nearest Neighbors (KNN). The system includes data preprocessing, model training, evaluation, and a deployed Streamlit web application for real-time predictions.

---

## 🚀 Features

- Data cleaning and preprocessing
- Feature scaling using StandardScaler
- Handling categorical data using Label Encoding
- Prevention of data leakage
- Model training using:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
- Model evaluation:
  - Accuracy Score
  - Confusion Matrix
  - Classification Report
  - ROC Curve
- Interactive Streamlit web app for predictions

---

## 📊 Dataset

The dataset contains machine operating parameters such as:

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear
- Machine Type (L, M, H)

Target variable:
- **Machine Failure (0 = No Failure, 1 = Failure)**

Note: Leakage columns (`TWF`, `HDF`, `PWF`, `OSF`, `RNF`) were removed to ensure model integrity.

---

## 🧠 Models Used

### 1. Logistic Regression
- Handles class imbalance using `class_weight='balanced'`
- Provides interpretable feature importance

### 2. K-Nearest Neighbors (KNN)
- Tested multiple K values
- Selected best K based on accuracy

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## 📁 Project Structure
