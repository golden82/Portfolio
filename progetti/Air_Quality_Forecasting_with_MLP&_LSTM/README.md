# 🌍 Air Quality Forecasting with MLP & LSTM

## 🔍 Project Overview

This project analyzes air quality data from **2018 and 2019**, using Machine Learning models to predict pollutant levels. The goal is to use **Multi-Layer Perceptron (MLP)** and **Long Short-Term Memory (LSTM)** networks to forecast **PM10 and PM2.5 concentrations** and evaluate their predictive performance.

## 📑 Workflow

1. **Data Collection & Storage** - Extract air quality data and store it in **MongoDB**.
2. **Data Cleaning & Selection** - Identify the stations with the highest PM10 and PM2.5 concentration in **2018**.
3. **Exploratory Data Analysis (EDA)** - Visualize trends in air pollution levels.
4. **Machine Learning Model Training**:
   - Train an **MLP model** with PyTorch and Spark using 2018 data.
   - Test the model on **2019 data** and evaluate its performance.
5. **LSTM Implementation** - Train and compare results with the MLP model.
6. **Forecast for 2020** - Predict air pollution levels for **one week in 2020** and compute **error metrics**.

## 📂 Repository Structure
```
air_quality_forecasting/
│── README.md  # Project documentation
│── Jupyter Notebook with ML code
│── Guidelines
│── data/  # Raw datasets
│── models/  # Trained MLP and LSTM models
│── results/  # Forecast outputs and evaluation metrics
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** PySpark, PyTorch, Pandas, Matplotlib
- **Databases:** MongoDB
- **Machine Learning Models:** MLP & LSTM

## 📊 Key Findings
- **MLP Model:** Trained with 2018 data and validated on 2019 data.
- **LSTM Model:** Provides a comparison to measure time-series dependencies.
- **Prediction for 2020:** One-week air quality forecast with error evaluation.

## 📜 How to Run the Project
To install dependencies and run the notebook:
```bash
pip install -r requirements.txt
```
Then, open and execute `Progetto_Tecnologie_Quadrante2.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
