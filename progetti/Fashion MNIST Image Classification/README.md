# 👕 Fashion MNIST Image Classification

## 🔍 Project Overview
This project involves classifying images from the **Fashion MNIST dataset** using **Artificial Neural Networks (ANNs)**. The dataset consists of **60,000 training images** and **10,000 test images**, each representing one of **10 categories** of clothing items.

## 📑 Workflow

1. **Data Collection & Preprocessing**
   - Load Fashion MNIST dataset using TensorFlow.
   - Normalize pixel values to the range [0,1].
   - Convert target labels to one-hot encoding.
2. **Exploratory Data Analysis (EDA)**
   - Visualize sample images and their labels.
   - Check class distributions.
3. **Model Building & Training**
   - Implement a **Sequential ANN model** with:
     - **Flatten Layer** to convert images into 1D vectors.
     - **Dense Layers** (fully connected layers) with ReLU activation.
     - **Softmax Layer** for classification into 10 categories.
   - Train the model using **Adam optimizer** and **Categorical Crossentropy loss**.
4. **Model Evaluation & Hyperparameter Tuning**
   - Compute **accuracy, precision, recall, and F1-score**.
   - Evaluate model performance on test data.
   - Experiment with **deeper architectures** and **increased epochs**.
5. **Visualization & Insights**
   - Plot training vs. validation accuracy and loss.
   - Generate **confusion matrix** to analyze misclassifications.
   - Visualize predictions on sample images.

## 📂 Repository Structure
```
fashion_mnist_classification/
│── README.md  # Project documentation
│── fashion_mnist_classification.ipynb  # Jupyter Notebook with full analysis
│── data/  # Dataset (loaded via TensorFlow)
│── results/  # Model performance metrics and visualizations
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** TensorFlow/Keras, NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
- **Machine Learning Models:** Neural Networks (Dense Layers)

## 📊 Key Findings
- Achieved **~89% accuracy** on the test dataset.
- Model struggles with differentiating **Shirts vs. T-Shirts**, indicating potential for improvement.
- Adding **more layers and training epochs** led to slight performance improvements but also hints at overfitting.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install tensorflow keras pandas numpy matplotlib seaborn scikit-learn
```
Then, open and run `fashion_mnist_classification.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
