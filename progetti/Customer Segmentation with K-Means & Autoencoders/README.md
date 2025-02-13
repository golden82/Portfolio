# 💳 Customer Segmentation with K-Means & Autoencoders

## 🔍 Project Overview

This project applies **unsupervised learning techniques** to segment customers based on their credit card transaction behavior. Using **K-Means clustering** and **Autoencoders**, we group similar customers and analyze spending patterns.

## 📑 Workflow

1. **Data Cleaning & Preprocessing**
   - Handle missing values (`MINIMUM_PAYMENTS`, `CREDIT_LIMIT`).
   - Remove `CUST_ID` and standardize numerical variables.
2. **Exploratory Data Analysis (EDA)**
   - Visualize feature distributions.
   - Compute correlation matrix and heatmap.
3. **K-Means Clustering**
   - Determine optimal cluster count via **Elbow Method**.
   - Cluster customers into **8 groups**.
   - Extract cluster centroids for interpretation.
4. **Dimensionality Reduction**
   - Apply **PCA (Principal Component Analysis)** to visualize clusters.
5. **Deep Learning with Autoencoders**
   - Train an **Autoencoder (TensorFlow/Keras)** to compress features.
   - Run **K-Means** on reduced features for improved segmentation.
6. **Comparison & Visualization**
   - Compare K-Means clustering before and after Autoencoder transformation.
   - Scatter plot of PCA-reduced clusters.

## 📂 Repository Structure
```
customer_segmentation/
│── README.md  # Project documentation
│── customer_segmentation.py  # Python script with ML pipeline
│── data/  # Credit card transactions dataset
│── results/  # Clustering results and visualizations
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, TensorFlow, Matplotlib, Seaborn
- **Machine Learning Models:** K-Means, PCA, Autoencoders

## 📊 Key Findings
- K-Means successfully identifies customer groups with similar spending patterns.
- Autoencoder-based clustering improves segmentation compared to raw feature clustering.
- PCA visualizations help interpret clusters effectively.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy scikit-learn tensorflow matplotlib seaborn
```
Then, run `customer_segmentation.py` in Python.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
