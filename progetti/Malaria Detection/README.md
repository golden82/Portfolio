# 🦠 Malaria Detection Using Convolutional Neural Networks (CNNs)

## 📌 Project Overview
Malaria remains one of the most severe global health challenges, with millions of infections and over 400,000 deaths reported annually. This project aims to develop an **automated, efficient, and accurate** malaria detection system leveraging **Deep Learning** and **Computer Vision** techniques. By analyzing microscopic images of blood smear slides, our Convolutional Neural Network (CNN) model classifies cells as **parasitized** or **uninfected** with high precision.

## 🚀 Key Features
- **High Accuracy**: Achieved **98.46%** accuracy on the test dataset.
- **Advanced Preprocessing**: Applied **data augmentation**, **HSV color space transformations**, and **Gaussian blurring** to enhance model generalization.
- **Multiple Deployment Options**:
  - **Web Application** for healthcare professionals.
  - **Mobile App** for field diagnostics in remote areas.
  - **Cloud API** for hospital and laboratory integration.
  - **Embedded AI** for real-time detection in microscopes.
- **Business and Market Potential**: The model has applications in **hospitals, research institutions, pharmaceutical companies, NGOs, and government health programs**.

## 📂 Dataset
- **Total Images**: 27,558 microscopic blood cell images.
- **Classes**: 
  - **Parasitized**: Cells containing Plasmodium parasites.
  - **Uninfected**: Healthy red blood cells.

## 🔬 Model Architecture
The CNN model consists of:
1. **Three Convolutional Layers** with **ReLU activation**, Batch Normalization, and **MaxPooling**.
2. **Dropout Regularization** to prevent overfitting.
3. **Flatten Layer** for feature extraction.
4. **Fully Connected Dense Layers** leading to a **Softmax classification layer**.

### 🔹 Performance Metrics
| Model | Accuracy | Precision | Recall | F1-Score |
|--------|---------|-----------|--------|---------|
| **CNN Augmented Model** | **98.46%** | **0.97** | **0.99** | **0.98** |
| Standard CNN | 98.12% | 0.96 | 0.98 | 0.97 |
| CNN Model 2 | 97.77% | 0.95 | 0.97 | 0.96 |
| VGG16 | 91.19% | 0.90 | 0.92 | 0.91 |

## 📊 Data Preprocessing & Augmentation
- **Image Rescaling**: Converted images to **64x64 RGB format**.
- **Normalization**: Scaled pixel values to the **0-1 range**.
- **Data Augmentation**:
  - Horizontal & Vertical Flips
  - Rotation (±25°)
  - Zooming & Brightness Adjustment
- **HSV Color Space Conversion**: To enhance malaria parasite features.
- **Gaussian Blurring**: Applied for noise reduction.

## 📌 Implementation Strategy
The system can be implemented as:
1. **AI-Powered Diagnostic Support System** for hospitals and clinics.
2. **Mobile Health App** for on-the-go malaria detection.
3. **Cloud-Based API Service** for hospitals, research institutions, and startups.
4. **Embedded AI Software** for diagnostic microscopes.

## 💡 Business Impact
✔ **Accelerates malaria detection** – reduces diagnosis time from hours to minutes.  
✔ **Improves accuracy and reduces misdiagnosis** – minimizing human error.  
✔ **Scalable & cost-effective solution** for remote healthcare settings.  

## 🏗️ Future Enhancements
- **Transfer Learning**: Experimenting with ResNet, InceptionV3, and EfficientNet models.
- **Explainability & Interpretability**: Applying **Grad-CAM visualization** for model explainability.
- **Federated Learning Approach**: Enhancing privacy in medical AI applications.

---

## 🛠️ Tech Stack
- **Python**
- **TensorFlow / Keras**
- **OpenCV**
- **Matplotlib / Seaborn**
- **Scikit-learn**

## 📁 Repository Structure
```
📂 Malaria-Detection
 ┣ 📂 dataset/              # Blood smear image dataset
 ┣ 📂 models/               # Trained models and weights
 ┣ 📂 notebooks/            # Jupyter notebooks for training and evaluation
 ┣ 📂 src/                  # Python scripts for preprocessing & model training
 ┣ 📂 deployment/           # Web app, API integration, and deployment scripts
 ┣ 📜 README.md             # Project documentation
 ┣ 📜 malaria_detection.py  # Main Python script
```

## 📜 Citation
If you use this model or dataset, please cite the project:
> "Malaria Detection Using CNNs: A Deep Learning Approach for Automated Diagnosis" - Agostino Fontana (2024).

## 📩 Contact
For inquiries, collaborations, or contributions, reach out to **[fontana.agostino@gmail.com](mailto:fontana.agostino@gmail.com)**.

---
🔬 *"AI for healthcare innovation: faster, more accessible, and life-saving solutions."* 🚀
