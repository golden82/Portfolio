# 🍞🥣🍏 Food Image Classification

## 📌 Project Overview
This project focuses on **image classification** for food categories using **Convolutional Neural Networks (CNNs)**. The dataset consists of three food categories:
- **Bread**
- **Soup**
- **Vegetables & Fruits**

The goal is to **automatically classify food images** into these three categories, assisting a stock photography company in labeling images efficiently.

## 🎯 Objectives
- Build a **deep learning-based image classifier** using CNN.
- Train and evaluate **two different CNN architectures** to improve performance.
- Analyze and optimize the model using **dropout layers** to reduce overfitting.

## 📂 Dataset Description
The dataset is structured into **Training** and **Testing** folders, each containing subfolders for the three food categories. Images are resized and preprocessed before training.

### 🔍 Data Fields:
| Feature       | Description |
|--------------|-------------|
| `image_data` | Raw image pixels converted into arrays |
| `category`   | Label (Bread, Soup, Vegetables-Fruits) |

## 📊 Exploratory Data Analysis (EDA)
- **Visualized random images** from each category.
- **Observed key patterns**, such as utensils in bread and soup images causing misclassification.
- **Balanced dataset** but with some class imbalance in Vegetables-Fruits.

## 🏗️ Model Building
### 🛠️ Preprocessing
- **Resized images to 150x150 pixels**.
- **Normalized pixel values** (0-255 scaled to 0-1).
- **One-hot encoding** applied to categorical labels.

### 📈 Model Architectures
#### **CNN Model 1** (Baseline)
- **3 Conv2D layers** followed by MaxPooling2D.
- **Dense layer** with ReLU activation.
- **Final softmax layer** for multi-class classification.
- **SGD optimizer** with a learning rate of 0.01.

📊 **Results**:
- Validation accuracy: **~68%**
- Model showed signs of **overfitting**.

#### **CNN Model 2** (Optimized)
- **4 Conv2D layers** with increased filters.
- **Dropout layers** after each block to reduce overfitting.
- **Adam optimizer** for improved convergence.

📊 **Results**:
- Validation accuracy: **~79%** (significant improvement).
- **Reduced misclassification** between food categories.
- **Better generalization** on unseen test images.

## 📊 Model Evaluation
- **Confusion Matrix** showed better classification in Model 2.
- **Precision & Recall improved**, especially for Vegetables-Fruits.
- **Prediction tests confirmed the model’s effectiveness**.

## 🛠️ Tech Stack
- **Python** (TensorFlow, Keras, OpenCV, NumPy, Pandas, Matplotlib, Seaborn)
- **Deep Learning Framework**: CNN with Keras/TensorFlow
- **Google Colab** for GPU acceleration

## 🔮 Key Findings & Recommendations
- **Dropout layers significantly improved generalization**.
- **Vegetables-Fruits category performed best** in classification.
- **Adding more diverse data could further boost accuracy**.

## 🚀 Next Steps
- Implement **data augmentation** for better generalization.
- Experiment with **pre-trained models (ResNet, VGG16, EfficientNet)**.
- Deploy model in a **real-time image classification web app**.

---

### 📁 Project Structure
```
📂 Food_Image_Classification
│── 📜 Food_Image_Classification.ipynb  # Jupyter Notebook with full analysis
│── 📊 Food_Image_Classification.pdf    # Project summary & visualizations
│── 📜 README.md                         # Project documentation
│── 📊 Data/                             # Dataset (if applicable)
│── 📜 requirements.txt                  # Dependencies
```

## 📧 Contact & Contributions
- Author: **Agostino Fontana**
- Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 *If you found this project useful, feel free to ⭐ the repository!* 😊
