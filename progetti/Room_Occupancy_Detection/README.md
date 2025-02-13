# 🏠 Room Occupancy Detection using SVM

## 🔍 Project Overview

This project applies **Support Vector Machine (SVM)** models to predict room occupancy using passive sensor data. The goal is to estimate the number of people in a room based on environmental factors (temperature, CO2, light, humidity, motion) without using invasive image-based methods.

## 📑 Workflow

1. **Exploratory Data Analysis (EDA)** - Investigate feature correlations and dataset distribution.
2. **Data Preprocessing** - Normalize sensor readings and split into training/testing sets.
3. **Model Implementation** - Train SVM models with **Linear** and **RBF kernels**.
4. **Hyperparameter Tuning** - Use **Grid Search** and **10-Fold Cross Validation**.
5. **Model Evaluation** - Compare accuracy and confusion matrices.

## 📂 Repository Structure
```
room_occupancy_svm/
│── README.md  # Project documentation
│── Project_Work_Machine_Learning.docx  # Detailed report
│── svm_room_occupancy.ipynb  # Jupyter Notebook with ML code
│── data/  # Dataset files
│── results/  # Model outputs, accuracy scores, confusion matrices
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Scikit-learn, NumPy, Pandas, Matplotlib
- **Machine Learning Model:** SVM (Linear & RBF Kernel)
- **Validation Method:** K-Fold Cross Validation (10 folds)

## 📊 Key Findings
- **SVM with RBF Kernel** achieved better **stability** and **higher accuracy** compared to the Linear Kernel.
- The model enables **non-invasive occupancy detection**, aiding energy efficiency in smart buildings.

## 📜 How to Run the Project
To install dependencies and run the notebook:
```bash
pip install -r requirements.txt
```
Then, open and run `svm_room_occupancy.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
