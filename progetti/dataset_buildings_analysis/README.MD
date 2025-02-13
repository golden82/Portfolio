# 🏢 Dataset Buildings Analysis

## 🔍 Project Overview

This project analyzes the "Buildings1" dataset, focusing on electricity consumption across different buildings. The study includes data cleaning, statistical analysis, principal component analysis (PCA), and linear regression modeling to predict energy consumption based on various factors.

## 📑 Workflow

1. **Data Collection** - Import the dataset from the `MLANP` package.
2. **Data Cleaning** - Handle missing values, detect outliers, and transform categorical variables.
3. **Exploratory Data Analysis (EDA)** - Identify correlations, summary statistics, and key trends.
4. **Principal Component Analysis (PCA)** - Reduce dimensionality and highlight key contributors.
5. **Linear Regression Modeling** - Estimate energy consumption using multiple predictors.
6. **Model Validation** - Use AIC score and backward selection to refine the model.
7. **Visualization** - Generate heatmaps, scatter plots, and regression diagnostics.

## 📂 Repository Structure
```
dataset_buildings_analysis/
│── README.md  # Project documentation
│── Agostino_Fontana_Dataset_Buildings.md  # Detailed report
│── Agostino_Fontana_Dataset_Buildings.Rmd  # R Markdown file with analysis code
│── Building_Dataset.pdf  # Reference document
│── data/  # Contains raw dataset files
│── results/  # Stores processed outputs and visualizations
```

## 🛠 Tools & Technologies
- **Programming Language:** R
- **Libraries:** ggplot2, dplyr, tidyr, readr, caret, factoextra, plotly
- **Statistical Methods:** PCA, Linear Regression, Correlation Analysis

## 📊 Key Findings
- Identified key variables influencing energy consumption (e.g., `sq.feet`, `primary_use`, `floor.count`).
- Used PCA to highlight major contributors and reduce dimensionality.
- Developed multiple regression models, optimizing with backward selection.
- Validated models using AIC and residual analysis.

## 📜 How to Run the Project
To execute the analysis in R:
```r
install.packages(c("ggplot2", "dplyr", "tidyr", "readr", "caret", "factoextra", "plotly"))
```
Then, open and run `Agostino_Fontana_Dataset_Buildings.Rmd` in RStudio.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
