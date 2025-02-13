# 🚀 Anomaly Detection in Industrial & Urban Sensor Networks

## 🔍 Project Overview

This project focuses on detecting anomalies in **industrial and urban sensor data** using **Machine Learning** and **Deep Learning** techniques. The goal is to identify unusual patterns that could indicate **equipment failure, maintenance needs, or sensor malfunctions**.

## 📑 Workflow

1. **Data Collection & Preprocessing**
   - Load sensor data from **Kaggle**.
   - Handle missing values and normalize numerical features.
   - Encode categorical variables (e.g., `machine_status`).
2. **Exploratory Data Analysis (EDA)**
   - Generate **time-series visualizations** of sensor data.
   - Compute **correlation matrices** to understand sensor relationships.
3. **Anomaly Detection Models**
   - **K-Means Clustering**: Identifies distinct operational patterns.
   - **Autoencoder (Neural Network)**: Learns normal behavior and detects deviations.
   - **Statistical Analysis**: Detects outliers in sensor readings.
4. **Model Evaluation & Visualization**
   - Compare anomaly detection results.
   - Generate **interactive plots** for analysis.

## 📂 Repository Structure
```
anomaly_detection/
│── README.md  # Project documentation
│── anomaly_detection.ipynb  # Jupyter Notebook with full analysis
│── data/  # Raw and preprocessed datasets
│── results/  # Model outputs and visualizations
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, TensorFlow/Keras, Matplotlib, Seaborn
- **Machine Learning Models:** K-Means, Autoencoders, Outlier Detection

## 📊 Key Findings
- The **Autoencoder model** successfully detected unusual sensor behavior.
- **K-Means clustering** revealed distinct operational states.
- Anomalies aligned with real-world sensor failures and maintenance periods.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy scikit-learn tensorflow keras matplotlib seaborn
```
Then, open and run `anomaly_detection.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
