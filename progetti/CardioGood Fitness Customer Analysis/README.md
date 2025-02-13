# 🏃‍♂️ CardioGood Fitness Customer Analysis

## 🔍 Project Overview

This project analyzes **CardioGood Fitness treadmill purchases** to identify customer profiles and compare product lines. The goal is to understand customer characteristics and behavior based on fitness habits, income, and demographics.

## 📑 Workflow

1. **Data Loading & Cleaning**
   - Import the dataset `CardioGoodFitness.csv`.
   - Check for missing values and summarize statistics.
2. **Exploratory Data Analysis (EDA)**
   - Generate **histograms** and **boxplots** for feature distributions.
   - Use **pivot tables** to analyze purchases by gender, income, and marital status.
   - Compute **correlation matrices** for variable relationships.
3. **Statistical Analysis & Visualization**
   - Cross-tabulations to compare product purchases across customer types.
   - **Pairplot analysis** using `seaborn`.
   - **Heatmap** to visualize feature correlations.
4. **Predictive Modeling**
   - **Linear Regression** to predict **distance (Miles)** based on treadmill usage and fitness level.
   - Evaluate regression coefficients to understand feature importance.

## 📂 Repository Structure
```
fitness_customer_analysis/
│── README.md  # Project documentation
│── CardioGood_Fitness_Analysis.ipynb  # Jupyter Notebook with full analysis
│── data/  # Raw dataset (CardioGoodFitness.csv)
│── results/  # Visualizations and model outputs
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib
- **Machine Learning Models:** Linear Regression

## 📊 Key Findings
- **Different treadmill models** attract different customer demographics.
- **Fitness level** and **weekly treadmill usage** strongly correlate with distance traveled.
- **Linear Regression model** helps estimate treadmill performance expectations.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy scikit-learn seaborn matplotlib
```
Then, open and run `CardioGood_Fitness_Analysis.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
