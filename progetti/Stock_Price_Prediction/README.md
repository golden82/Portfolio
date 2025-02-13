# 📈 Stock Price Prediction (AAPL)

## 🔍 Project Overview

This project analyzes and predicts **Apple (AAPL) stock prices** using both **Ridge Regression** and **LSTM-based deep learning models**. The objective is to forecast stock price trends based on historical data.

## 📑 Workflow

1. **Data Collection**
   - Fetch historical stock data for **AAPL** using `yfinance`.
   - Export data to CSV (`dataset_AAPL.csv`).
2. **Data Preprocessing**
   - Extract relevant columns (`Date`, `Close`, `Volume`).
   - Normalize numerical features using `MinMaxScaler`.
3. **Ridge Regression Model**
   - Split data (65% training, 35% test).
   - Train a **Ridge Regression** model.
   - Compute accuracy and visualize predictions.
4. **LSTM Neural Network**
   - Prepare time-series data for deep learning.
   - Build an **LSTM model** using TensorFlow/Keras.
   - Train the model for **20 epochs**.
   - Generate **future price predictions** and compare them with actual data.
5. **Visualization**
   - Display stock trends and predictions using `plotly`.

## 📂 Repository Structure
```
stock_price_prediction/
│── README.md  # Project documentation
│── stock_price_prediction.py  # Python script for data collection and prediction
│── data/  # Stock price dataset
│── results/  # Prediction results and plots
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** yfinance, pandas, numpy, sklearn, TensorFlow/Keras, Matplotlib, Plotly
- **Machine Learning Models:** Ridge Regression, LSTM Neural Network

## 📊 Key Findings
- Ridge Regression provides a **baseline prediction model**.
- LSTM achieves **better long-term forecasting** of stock prices.
- Interactive visualization helps interpret prediction performance.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install yfinance pandas numpy scikit-learn tensorflow keras matplotlib plotly
```
Then, run `stock_price_prediction.py` in Python.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀

