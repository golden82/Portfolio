# 🌌 Celestial Object Detection

## 🔍 Project Overview
This project aims to classify **celestial objects** (Stars, Galaxies, and Quasars) using **machine learning models** based on photometric and spectroscopic features from the **Sloan Digital Sky Survey (SDSS)** dataset. The classification of astronomical objects is crucial for astrophysics research, helping in the identification of new celestial bodies and understanding their properties.

## 🎯 Objective
- Build a **multi-class classification model** to predict whether a celestial object is a **star, galaxy, or quasar**.
- Analyze the impact of **photometric and spectroscopic** features in classification.
- Compare **K-Nearest Neighbors (KNN), Decision Trees, and Random Forest** models.

## 📂 Dataset Description
The dataset consists of **250,000** celestial object observations recorded by **SDSS** and contains:
- **Photometric Features**: Light intensity captured across different bands (u, g, r, i, z).
- **Spectroscopic Features**: Redshift, right ascension, and declination angles.
- **Metadata**: Observation details like plate ID, fiber ID, and modified Julian date.

### 🔍 Data Fields:
| Column        | Description |
|--------------|-------------|
| `objid`       | Unique Object ID |
| `ra`          | Right Ascension (celestial longitude) |
| `dec`         | Declination (celestial latitude) |
| `u, g, r, i, z` | Light intensity values across different bands |
| `redshift`    | Doppler shift measurement (helps identify quasars) |
| `class`       | Object class (Galaxy, Star, Quasar) |

## 📊 Exploratory Data Analysis (EDA)
- **Class Distribution**: 
  - **51% Galaxies**, **38% Stars**, **10% Quasars**.
- **Feature Correlation**:
  - **Redshift strongly influences classification** (Quasars have high redshift values).
  - Photometric filters (g, r, i, z) are highly correlated.
- **Data Preprocessing**:
  - Dropped non-informative features (e.g., observation IDs).
  - Standardized numerical features.

## 🏗️ Model Building
### 🔢 Data Preprocessing
- **One-Hot Encoding** for categorical variables.
- **Feature Scaling** using StandardScaler.
- **Train-Test Split**: **90% training, 10% testing**.

### 📈 Machine Learning Models
1. **K-Nearest Neighbors (KNN)**
   - Before Scaling: **Accuracy ~ 81%**
   - After PCA & Scaling: **Accuracy improved to 95%**
2. **Decision Trees**
   - Moderate performance but prone to overfitting.
3. **Random Forest**
   - Achieved highest accuracy, outperforming KNN in robustness.

## 📊 Model Evaluation
- **Metrics used**: Precision, Recall, F1-Score, Confusion Matrix.
- **Best Model**: **Random Forest** with highest accuracy and better generalization.

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
- **Machine Learning Models**: KNN, Decision Trees, Random Forest
- **Data Source**: **Sloan Digital Sky Survey (SDSS)**

## 🔮 Key Findings & Recommendations
- **Quasars have distinct redshift values**, making them easier to classify.
- **Photometric bands (u, g, r, i, z) are crucial** in distinguishing object types.
- **Random Forest performed best** due to its ability to handle high-dimensional data.

## 📌 Next Steps
- Implement **Deep Learning models (CNNs)** to improve classification.
- Expand dataset with additional spectroscopic features.
- Deploy model for **real-time astronomical classification**.

---

### 📁 Project Structure
```
📂 Celestial_Object_Detection
│── 📜 Celestial_Object_Detection.ipynb  # Jupyter Notebook with full analysis
│── 📊 Celestial_Object_Detection.pdf    # Project summary & visualizations
│── 📜 README.md                          # Project documentation
│── 📊 Data/                              # Dataset (if applicable)
│── 📜 requirements.txt                   # Dependencies
```

## 📧 Contact & Contributions
- Author: **Agostino Fontana**
- Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 *If you found this project useful, feel free to ⭐ the repository!* 😊
