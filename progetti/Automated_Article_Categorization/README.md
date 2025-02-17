# 🤖 Transformers Case Study: Articles Categorization

## 📌 Project Overview
This project explores **automated article categorization** using **Transformer-based models (BERT)**. The goal is to classify news articles into predefined categories using advanced Natural Language Processing (NLP) techniques.

## 🎯 Objective
- **Automate article classification** to improve efficiency in the media industry.
- **Leverage Transformers (BERT)** to enhance text classification accuracy.
- **Reduce manual effort** in sorting and organizing vast amounts of news data.

## 📂 Dataset Description
The dataset consists of **4,000+ news articles**, each labeled with a category. The dataset includes:
- **Article text** (full news content)
- **Metadata** (publish date, section, keywords)
- **Category labels** (news, sports, world, etc.)

### 🔍 Data Fields:
| Feature        | Description |
|--------------|-------------|
| `Date_published` | Date when the article was released |
| `Category` | Main category of the article (Target variable) |
| `Section` | Sub-category of the news |
| `Headline` | Article title |
| `Description` | Short article summary |
| `Keywords` | Tags associated with the content |
| `Article_text` | Full content of the news article |

## 📊 Exploratory Data Analysis (EDA)
- **Class Distribution**: Sports and news articles dominate the dataset.
- **Text Preprocessing**: 
  - Lowercased text
  - Removed special characters and numbers
  - Tokenized using BERT tokenizer

## 🏗️ Model Building
### 🔢 Data Preprocessing
- **Converted text into numerical features** using **BERT Tokenizer**.
- **Split dataset** into **80% training, 10% validation, 10% testing**.
- **Applied Label Encoding** to categorical labels.

### 📈 Transformer-Based Model
1. **BERT (Bidirectional Encoder Representations from Transformers)**
   - Fine-tuned using **TFBertForSequenceClassification**.
   - Trained for **3 epochs** with Adam optimizer.
   - Applied class weighting to handle imbalanced categories.

## 📊 Model Evaluation
- **Metrics used**: Accuracy, Precision, Recall, F1-Score, Confusion Matrix.
- **Final Accuracy**: **~93% on validation set**.
- **Confusion Matrix Analysis**: Misclassification mostly occurs in overlapping categories.

## 🛠️ Tech Stack
- **Python** (Pandas, NumPy, TensorFlow, Sklearn, Hugging Face Transformers)
- **Deep Learning Model**: BERT
- **Google Colab** for training with GPU acceleration

## 🔮 Key Findings & Recommendations
- **BERT significantly improves classification accuracy** over traditional models.
- **Keyword-based pre-filtering** could further improve classification.
- **Handling dataset bias** is crucial for generalizing across different article types.

## 📌 Next Steps
- Experiment with **RoBERTa or GPT models** for further improvements.
- Deploy the model as a **real-time API** for article categorization.
- Expand dataset to include multilingual articles.

---

### 📁 Project Structure
```
📂 Transformers_Article_Categorization
│── 📜 Transformers_Case_Study_Articles_Categorization.ipynb  # Jupyter Notebook with full analysis
│── 📊 Transformers_Case_Study_Articles_Categorization.pdf    # Project summary & visualizations
│── 📜 README.md                                              # Project documentation
│── 📊 Data/                                                  # Dataset (if applicable)
│── 📜 requirements.txt                                       # Dependencies
```

## 📧 Contact & Contributions
- Author: **Agostino Fontana**
- Contributions are welcome! Feel free to open an issue or submit a pull request.

---
🚀 *If you found this project useful, feel free to ⭐ the repository!* 😊
