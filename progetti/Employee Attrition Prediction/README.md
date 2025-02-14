# 👨‍💼 Employee Attrition Prediction

## 🔍 Project Overview
This project focuses on predicting **employee attrition** using machine learning models. The goal is to identify key factors influencing employee turnover and build predictive models to help organizations reduce attrition rates.

## 📑 Workflow
1. **Data Collection & Preprocessing**
   - Load and clean HR dataset.
   - Handle missing values and encode categorical features.
   - Perform feature engineering.
2. **Exploratory Data Analysis (EDA)**
   - Identify patterns and correlations affecting attrition.
   - Visualize important features.
3. **Machine Learning Model Development**
   - Train models including **Decision Trees, Random Forest, and Hyperparameter Tuned Models**.
   - Tune hyperparameters to improve performance.
4. **Model Evaluation & Insights**
   - Compute **Accuracy, Precision, Recall, and F1-score**.
   - Compare the effectiveness of different models.

## 📂 Repository Structure
```
employee_attrition_prediction/
│── README.md  # Project documentation
│── employee_attrition_prediction.ipynb  # Jupyter Notebook with full analysis
│── data/  # HR dataset used for training
│── models/  # Trained models and results
│── results/  # Model evaluation metrics and visualizations
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Seaborn, Scikit-Learn, Matplotlib
- **Machine Learning Models:** Decision Trees, Random Forest, Hyperparameter Tuning

## 📊 Key Findings
- **OverTime, MonthlyIncome, and Age** are the most critical factors influencing attrition.
- **Random Forest model with hyperparameter tuning** provided the best predictive accuracy.
- Companies should focus on **work-life balance and fair compensation** to retain employees.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```
Then, open and run `employee_attrition_prediction.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
