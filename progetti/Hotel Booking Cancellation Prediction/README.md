# 🏨 Hotel Booking Cancellation Prediction

## 📌 Project Overview
This project aims to predict **hotel booking cancellations** using machine learning models. By analyzing customer booking details, the goal is to help hotels optimize their operations by identifying which reservations are likely to be canceled, reducing revenue losses and improving resource planning.

## 🎯 Objective
- Identify key factors influencing hotel booking cancellations.
- Build predictive models to forecast cancellations in advance.
- Provide insights to hotels for policy adjustments and revenue optimization.

## 📂 Dataset Description
The dataset consists of **36,275 hotel reservations** and includes information about customer bookings, stay details, and special requests.

### 🔍 Data Fields:
| Column                          | Description |
|---------------------------------|-------------|
| `no_of_adults`                  | Number of adults in the booking |
| `no_of_children`                | Number of children in the booking |
| `no_of_weekend_nights`          | Number of weekend nights booked |
| `no_of_week_nights`             | Number of weekday nights booked |
| `type_of_meal_plan`             | Meal plan selected by the customer |
| `required_car_parking_space`    | Whether parking space was required (0/1) |
| `room_type_reserved`            | Type of room reserved |
| `lead_time`                     | Days between booking and arrival |
| `arrival_year`                  | Year of arrival |
| `arrival_month`                 | Month of arrival |
| `market_segment_type`           | Customer segment (Online, Offline, Corporate, etc.) |
| `repeated_guest`                | Whether the customer is a returning guest (0/1) |
| `no_of_previous_cancellations`  | Previous booking cancellations by the customer |
| `avg_price_per_room`            | Average price per room (in euros) |
| `no_of_special_requests`        | Number of special requests made by the customer |
| `booking_status`                | Target variable: 0 (Not Canceled), 1 (Canceled) |

## 📊 Exploratory Data Analysis (EDA)
- **Key Observations**:
  - Higher `lead_time` increases cancellation likelihood.
  - `Online market segment` bookings have a higher probability of cancellation.
  - Customers with **more special requests** are less likely to cancel.
  - **Room price and seasonality** affect cancellation trends.

## 🏗️ Model Building
### 🔢 Data Preprocessing
- **One-Hot Encoding** for categorical variables.
- **Feature Scaling** using StandardScaler.
- **Train-Test Split**: **70% training, 30% testing**.

### 📈 Machine Learning Models
1. **Decision Tree Classifier**
   - Initial model, but prone to overfitting.
2. **Random Forest Classifier**
   - Performed best in terms of predictive power and stability.
3. **Hyperparameter-Tuned Random Forest**
   - Optimized model using GridSearchCV for better generalization.

## 📊 Model Evaluation
- **Metrics used**: Accuracy, Precision, Recall, F1-score.
- **Best Model**: **Tuned Random Forest** achieved the highest accuracy with minimal overfitting.

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
- **Machine Learning Models**: Decision Trees, Random Forest, Hyperparameter Tuning

## 🔮 Key Findings & Recommendations
- **Hotels should monitor high lead-time bookings**, as they are more likely to be canceled.
- **Online bookings require stricter cancellation policies** to minimize last-minute cancellations.
- **Adding incentives for returning guests** may reduce cancellation rates.

## 📌 Next Steps
- Implement **Deep Learning models** for enhanced accuracy.
- Develop an **API for real-time cancellation prediction**.
- Extend the dataset with customer feedback to improve insights.

---

### 📁 Project Structure
```
📂 Hotel_Booking_Cancellation_Prediction
│── 📜 Hotel_Booking_Cancellation_Prediction.ipynb  # Jupyter Notebook with full analysis
│── 📊 Hotel_Booking_Cancellation_Prediction.pdf    # Project summary & visualizations
│── 📜 README.md                                     # Project documentation
│── 📊 Data/                                         # Dataset (if applicable)
│── 📜 requirements.txt                              # Dependencies
```

## 📧 Contact & Contributions
- Author: **Agostino Fontana**
- Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 *If you found this project useful, feel free to ⭐ the repository!* 😊
