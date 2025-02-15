# 🔊 Audio MNIST Digit Recognition

## 📌 Project Overview
This project focuses on **classifying spoken digits (0-9) from the Audio MNIST dataset** using **Deep Learning models**. The goal is to convert raw audio data into **Mel-Frequency Cepstral Coefficients (MFCCs)** and use them for training a neural network model.

## 🎯 Objective
- Extract features from raw speech data using **MFCC spectrograms**.
- Train an **Artificial Neural Network (ANN)** to classify spoken digits.
- Evaluate model performance using **accuracy and confusion matrix**.

## 📂 Dataset Description
The dataset consists of **spoken digit recordings** stored as **.wav audio files**. Each file corresponds to a speaker pronouncing a digit (0-9). The dataset is structured into folders, with each folder representing a different speaker.

### 🔍 Data Fields:
| Feature       | Description |
|--------------|-------------|
| `digit`      | The spoken digit (0-9) |
| `speaker_id` | Unique identifier for each speaker |
| `mfcc_features` | Extracted MFCC coefficients |
| `audio_waveform` | Raw waveform representation |

## 📊 Exploratory Data Analysis (EDA)
- **Visualized waveform representations** of different spoken digits.
- **Converted raw audio to spectrograms** using **MFCC feature extraction**.
- **Analyzed class distribution** to ensure balanced datasets.

## 🏗️ Model Building
### 🔢 Data Preprocessing
- **Extracted MFCC features** from raw audio.
- **Standardized** numerical features.
- **Split dataset** into **75% training and 25% testing**.

### 📈 Machine Learning Model
1. **Artificial Neural Network (ANN)**
   - **3 hidden layers** with **ReLU activation**.
   - **Softmax output layer** for multi-class classification.
   - **Adam optimizer** with sparse categorical cross-entropy loss.

## 📊 Model Evaluation
- **Metrics used**: Accuracy, Precision, Recall, Confusion Matrix.
- **Final accuracy**: **Achieved >95% accuracy on test data**.

## 🛠️ Tech Stack
- **Python** (Librosa, NumPy, Pandas, Matplotlib, TensorFlow, Keras)
- **Deep Learning Model**: Fully Connected ANN

## 🔮 Key Findings & Recommendations
- **MFCC spectrograms are highly effective** for speech classification.
- **ANN performed well**, but **CNNs or RNNs could improve accuracy**.
- **Adding more speaker variations** would enhance model robustness.

## 📌 Next Steps
- Experiment with **CNNs and LSTMs** for speech recognition.
- Fine-tune hyperparameters for better generalization.
- Deploy the model as a **real-time voice recognition system**.

---

### 📁 Project Structure
```
📂 Audio_MNIST_Digit_Recognition
│── 📜 Audio_MNIST_Digit_Recognition.ipynb  # Jupyter Notebook with full analysis
│── 📊 Audio_MNIST_Digit_Recognition.pdf    # Project summary & visualizations
│── 📜 README.md                            # Project documentation
│── 📊 Data/                                # Dataset (if applicable)
│── 📜 requirements.txt                     # Dependencies
```

## 📧 Contact & Contributions
- Author: **Agostino Fontana**
- Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 *If you found this project useful, feel free to ⭐ the repository!* 😊
