# 🍽️ FoodHub Data Analysis

## 📌 Project Overview
This project focuses on analyzing customer orders and behavior for **FoodHub**, an online food delivery service. The objective is to extract valuable insights from transaction data to improve customer satisfaction, optimize delivery operations, and enhance business strategies.

## 🎯 Objectives
- **Analyze customer purchase patterns** to identify key trends.
- **Segment customers** based on order frequency and spending behavior.
- **Predict customer retention** using machine learning models.
- **Optimize delivery time** through data-driven insights.

## 📂 Dataset Description
The dataset consists of **transactional data** from FoodHub, including customer details, order history, and delivery times.

### 🔍 Data Fields:
| Feature                  | Description |
|--------------------------|-------------|
| `Order_ID`               | Unique identifier for each order |
| `Customer_ID`            | Unique customer identifier |
| `Order_Date`             | Date and time of order placement |
| `Order_Amount`           | Total amount spent per order |
| `Delivery_Time`          | Time taken for order delivery (minutes) |
| `Payment_Method`         | Payment method used (Credit Card, Cash, etc.) |
| `Order_Status`           | Completed, Cancelled, or Pending |
| `Restaurant_Rating`      | Customer rating for restaurant service (1-5) |

## 📊 Exploratory Data Analysis (EDA)
- **Order Frequency Analysis:** Identified peak ordering times and customer demand trends.
- **Spending Behavior Analysis:** Grouped customers based on total spend and order volume.
- **Delivery Time Analysis:** Examined factors influencing fast vs. slow deliveries.
- **Customer Retention Trends:** Evaluated repeat order rates and loyalty factors.

## 🏗️ Model Building
### 🔢 Data Preprocessing
- Handled missing values and outliers.
- Standardized numerical features for better model performance.
- Encoded categorical variables (e.g., Payment Method, Order Status).

### 📈 Machine Learning Models
1. **Customer Segmentation (K-Means Clustering)**
   - Grouped customers into segments based on spending and frequency.
2. **Delivery Time Prediction (Regression Model)**
   - Trained models to predict expected delivery time based on order details.
3. **Churn Prediction (Classification Model)**
   - Identified high-risk customers likely to stop ordering.

## 📊 Model Evaluation
- **Metrics Used:** RMSE, R² Score (for regression), Precision-Recall, and F1-Score (for classification models).
- **Best Model:** K-Means provided meaningful customer segments, and Random Forest had the best churn prediction accuracy.

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn)
- **Machine Learning Models:** K-Means, Regression Models, Random Forest
- **Visualization Tools:** Matplotlib, Seaborn

## 🔮 Key Findings & Recommendations
- **Peak ordering hours (12 PM - 2 PM & 7 PM - 9 PM)** require better logistics planning.
- **Customers who use credit cards tend to place higher-value orders**.
- **Delivery times over 40 minutes negatively impact customer ratings**.
- **Loyalty programs can help retain high-value customers**.

## 📌 Next Steps
- Implement a **personalized recommendation system** for repeat customers.
- Enhance delivery time prediction using **real-time GPS data**.
- Develop a **dashboard** for monitoring key business KPIs.

---

### 📁 Project Structure
```
📂 FoodHub_Data_Analysis
│── 📜 FoodHub_Data_Analysis.ipynb  # Jupyter Notebook with full analysis
│── 📊 FoodHub_Data_Analysis.pdf    # Project summary & visualizations
│── 📜 README.md                     # Project documentation
│── 📊 Data/                         # Dataset (if applicable)
│── 📜 requirements.txt              # Dependencies
```

## 📧 Contact & Contributions
- Author: **Agostino Fontana**
- Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 *If you found this project useful, feel free to ⭐ the repository!* 😊
