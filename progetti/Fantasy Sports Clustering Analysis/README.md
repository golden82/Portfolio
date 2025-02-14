# 🎮 Fantasy Sports Clustering Analysis

## 🔍 Project Overview
This project applies **unsupervised learning techniques** to cluster fantasy sports players based on their past season's performance. The analysis helps define **player pricing strategies** by grouping players with similar attributes and performance metrics.

## 📑 Workflow

1. **Data Collection & Cleaning**
   - Load and preprocess the fantasy sports dataset.
   - Handle missing values and scale numerical features.
2. **Exploratory Data Analysis (EDA)**
   - Visualize player statistics distribution.
   - Generate correlation matrices to understand feature relationships.
3. **Feature Engineering & Dimensionality Reduction**
   - Apply **Principal Component Analysis (PCA)** to optimize feature space.
4. **Clustering Algorithms**
   - **K-Means Clustering**: Identifies distinct player groups.
   - **K-Medoids Clustering**: Alternative method for handling outliers.
   - **Hierarchical Clustering**: Provides hierarchical segmentation.
5. **Cluster Profiling & Insights**
   - Analyze clusters to define player categories.
   - Compare the effectiveness of different clustering techniques.

## 📂 Repository Structure
```
fantasy_sports_clustering/
│── README.md  # Project documentation
│── fantasy_sports_clustering.ipynb  # Jupyter Notebook with full analysis
│── data/  # Raw dataset
│── results/  # Visualizations and cluster insights
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Seaborn, Matplotlib, SciPy
- **Clustering Models:** K-Means, K-Medoids, Hierarchical Clustering, PCA

## 📊 Key Findings
- **Cluster 1:** High-performing players with strong statistics.
- **Cluster 2:** Average performers with balanced performance.
- **Cluster 3:** Defensive or support players with low attacking contributions.
- **Cluster 4:** Minimal-impact players with low playing time.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy scikit-learn seaborn matplotlib scipy
```
Then, open and run `fantasy_sports_clustering.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀

