# 📞 Customer Churn Prediction

## 🔍 Project Overview

This project predicts **customer churn** in the telecom sector using various machine learning models in R. The dataset contains customer attributes and their churn status, allowing us to build models that classify whether a customer is likely to leave the service.

## 📑 Workflow

1. **Data Preparation**
   - Load `Telco_customer_churn_2.csv` and clean the dataset.
   - Convert categorical variables and normalize numerical features.
2. **Exploratory Data Analysis (EDA)**
   - Visualize churn distribution.
   - Compute feature correlations.
3. **Model Training & Evaluation**
   - **Logistic Regression (GLM)**
   - **Decision Trees (rpart)**
   - **Support Vector Machines (SVM)**
   - Perform **10-fold cross-validation** for robustness.
4. **Performance Metrics**
   - Accuracy, Precision, Recall, F1-score.
   - Confusion Matrix for model comparison.

## 📂 Repository Structure
```
customer_churn_prediction/
│── README.md  # Project documentation
│── churn_prediction_analysis.R  # R script with analysis code
│── data/  # Input datasets
│── results/  # Model outputs, confusion matrices, and accuracy reports
```

## 🛠 Tools & Technologies
- **Programming Language:** R
- **Libraries:** caret, rpart, randomForest, kernlab, ggplot2
- **Validation Method:** 10-Fold Cross-Validation

## 📊 Key Findings
- Logistic regression highlights key factors influencing churn.
- Decision trees provide an **interpretable model** with good performance.
- SVM achieves **high accuracy** but is computationally expensive.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```r
install.packages(c("caret", "rpart", "randomForest", "kernlab", "ggplot2"))
```
Then, run `churn_prediction_analysis.R` in RStudio.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
