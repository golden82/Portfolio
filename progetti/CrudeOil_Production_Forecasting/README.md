# 🛢️ Crude Oil Production Forecasting

## 📌 Project Overview
This project focuses on **forecasting crude oil production** using **time series analysis**. The objective is to analyze historical production data and develop predictive models to estimate future production trends. The dataset spans from **1992 to 2018** and includes oil production data for multiple countries. 

## 🎯 Objective
- Perform **time series decomposition** to identify trends.
- Build **AR, MA, ARMA, and ARIMA models** for forecasting.
- Select the **best model** using AIC and RMSE metrics.

## 📂 Dataset Description
The dataset contains the **yearly oil production** of 222 countries. For simplicity, the study focuses on the **United States** to build and evaluate forecasting models.

### 🔍 Data Fields:
| Column         | Description |
|---------------|-------------|
| `YEAR`        | Year of crude oil production (1992-2018) |
| `OIL_PRODUCTION` | Annual oil production volume (in million barrels) |

## 📊 Exploratory Data Analysis (EDA)
- **Trend Analysis**: Visualized long-term trends in oil production.
- **Seasonal Decomposition**: Showed that the data lacks seasonal patterns due to its yearly frequency.
- **Stationarity Check**: Used the **Augmented Dickey-Fuller (ADF) Test** to determine if differencing was needed.

## 🏗️ Model Building
### 🔢 Data Preprocessing
- **Differencing applied** to make the series stationary.
- **Train-Test Split**: **1992-2012 as training data, 2013-2018 as test data**.

### 🏆 Time Series Models Tested
1. **AutoRegressive (AR)**: Considered lags of past values.
2. **Moving Average (MA)**: Modeled residual errors.
3. **ARMA (AR + MA)**: Combined both models.
4. **ARIMA (ARMA + Differencing)**: Included differencing to handle non-stationarity.

## 📊 Model Evaluation
- **Metrics used**: AIC (Akaike Information Criterion) and RMSE (Root Mean Squared Error).
- **Best Model**: **ARIMA(2,3,2)** provided the best trade-off between accuracy and complexity.

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, Scikit-learn)
- **Time Series Models**: AR, MA, ARMA, ARIMA

## 🔮 Key Findings & Recommendations
- **Oil production showed a decline in the early 2000s**, followed by a sharp increase.
- **ARIMA(2,3,2) was the best predictive model** for future oil production.
- **Future work**: Incorporate external economic indicators to improve model accuracy.

## 📌 Next Steps
- Experiment with **SARIMA** to capture additional patterns.
- Deploy the model as an **interactive dashboard** for forecasting.
- Extend analysis to multiple countries for **comparative forecasting**.

---

### 📁 Project Structure
```
📂 Crude_Oil_Production_Forecasting
│── 📜 Crude_Oil_Production_Forecasting.ipynb  # Jupyter Notebook with full analysis
│── 📊 Crude_Oil_Production_Forecasting.pdf    # Project summary & visualizations
│── 📜 README.md                               # Project documentation
│── 📊 Data/                                   # Dataset (if applicable)
│── 📜 requirements.txt                        # Dependencies
```

## 📧 Contact & Contributions
- Author: **Agostino Fontana**
- Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 *If you found this project useful, feel free to ⭐ the repository!* 😊
