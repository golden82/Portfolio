# ☕ Coffee Roasters Quality Prediction

## 🔍 Project Overview
This project aims to predict the **quality of roasted coffee beans** using **machine learning models** based on sensor data collected during the roasting process. The quality score ranges from **0 (worst) to 100 (best)**, and our objective is to optimize roasting conditions for **premium coffee production**.

## 🎯 Objective
- Develop a **regression model** to predict the coffee bean quality.
- Analyze the impact of **temperature sensors and humidity** on the final product.
- Compare **Decision Trees, Random Forest, Gradient Boosting, and XGBoost** models.

## 📂 Dataset Description
The dataset consists of **29,131 coffee roasting observations** with 17 predictor variables:
- **Temperature Sensors**: 3 sensors in each of the 5 roasting chambers.
- **Humidity Data**: Measures moisture retention after roasting.
- **Raw Material Height**: Represents the volume of coffee beans entering the roasting chamber.
- **Quality Score**: Target variable representing the final quality assessment.

### 🔍 Data Fields:
| Column        | Description |
|--------------|-------------|
| `T_data_1_1` - `T_data_5_3` | Temperatures from 3 sensors in each of 5 chambers |
| `H_data`      | Raw material volume entering chamber (pounds) |
| `AH_data`     | Roasted coffee beans relative humidity |
| `quality`     | Final quality score (0-100) |

## 📊 Exploratory Data Analysis (EDA)
- **Key Observations**:
  - Higher chamber temperatures improve coffee quality.
  - Humidity levels significantly affect the roasting process.
  - Temperature variations across chambers influence the final product.
- **Preprocessing Steps**:
  - Handling missing values with **median imputation**.
  - Outlier detection and normalization.

## 🏗️ Model Building
### 🔢 Data Preprocessing
- **Feature Scaling** using StandardScaler.
- **Train-Test Split**: **60% training, 20% validation, 20% testing**.

### 📈 Machine Learning Models
1. **Decision Tree Regressor**
   - Initial model, but prone to overfitting.
2. **Random Forest Regressor**
   - Performed best in terms of accuracy.
3. **Gradient Boosting Regressor**
   - Moderate performance but high computational cost.
4. **XGBoost Regressor**
   - High RMSE, but still useful for feature importance analysis.

## 📊 Model Evaluation
- **Metrics used**: RMSE, MAE, Adjusted R² Score.
- **Best Model**: **Random Forest** with highest accuracy and best generalization.

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib, XGBoost)
- **Machine Learning Models**: Decision Tree, Random Forest, Gradient Boosting, XGBoost

## 🔮 Key Findings & Recommendations
- **Higher roasting temperatures (300-400°F) improve coffee quality**.
- **Humidity control is crucial** to maintain consistent quality.
- **Random Forest is the most reliable model** for predicting quality scores.

## 📌 Next Steps
- Implement **deep learning models** for improved accuracy.
- Deploy the model in a **real-time coffee quality monitoring system**.
- Extend the dataset with additional roasting parameters.

---

### 📁 Project Structure
```
📂 Coffee_Roasters_Quality_Prediction
│── 📜 Coffee_Roasters_Quality_Prediction.ipynb  # Jupyter Notebook with full analysis
│── 📊 Coffee_Roasters_Quality_Prediction.pdf    # Project summary & visualizations
│── 📜 README.md                                 # Project documentation
│── 📊 Data/                                     # Dataset (if applicable)
│── 📜 requirements.txt                          # Dependencies
```

## 📧 Contact & Contributions
- Author: **Agostino Fontana**
- Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 *If you found this project useful, feel free to ⭐ the repository!* 😊
