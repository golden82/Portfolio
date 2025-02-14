# 🏥 Hospital Length of Stay Prediction

## 🔍 Project Overview
This project aims to predict **hospital length of stay (LOS)** for patients based on admission data. By analyzing key factors influencing hospital stays, we can improve resource allocation, reduce costs, and optimize patient care.

## 📑 Workflow
1. **Data Collection & Preprocessing**
   - Load and clean hospital admission dataset.
   - Handle missing values and encode categorical variables.
   - Perform feature engineering.
2. **Exploratory Data Analysis (EDA)**
   - Analyze patterns in hospital stays.
   - Identify correlations between factors affecting LOS.
3. **Machine Learning Model Development**
   - Train models including **Decision Trees, Random Forest, XGBoost, and Gradient Boosting**.
   - Tune hyperparameters to enhance accuracy.
4. **Model Evaluation & Insights**
   - Compute **RMSE, R² Score, MAE, and MAPE**.
   - Identify the best-performing model.

## 📂 Repository Structure
```
hospital_los_prediction/
│── README.md  # Project documentation
│── hospital_los_prediction.ipynb  # Jupyter Notebook with full analysis
│── data/  # Dataset used for training
│── models/  # Saved trained models
│── results/  # Model evaluation metrics and visualizations
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Seaborn, Scikit-Learn, Matplotlib, XGBoost
- **Machine Learning Models:** Decision Trees, Random Forest, XGBoost, Gradient Boosting

## 📊 Key Findings
- **Department of admission** and **severity of illness** strongly influence hospital stay duration.
- **Random Forest** performed best in predicting LOS with the lowest RMSE.
- Feature selection improved prediction performance significantly.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
```
Then, open and run `hospital_los_prediction.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
