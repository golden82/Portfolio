# 🛒 Market Basket Analysis using Apriori

## 🔍 Project Overview

This project applies **Market Basket Analysis** on a grocery store dataset using **association rule mining** with the **Apriori algorithm**. The goal is to uncover frequent item sets and product relationships that can help optimize sales strategies.

## 📑 Workflow

1. **Data Preparation**
   - Load the `Groceries` dataset.
   - Explore transaction structures and item frequencies.
2. **Frequent Itemset Mining**
   - Use `eclat()` to find frequent items with minimum support.
   - Visualize the most commonly bought products.
3. **Association Rule Mining**
   - Generate rules using the **Apriori algorithm**.
   - Identify **high-confidence product relationships**.
4. **Product-Specific Association Rules**
   - Discover rules related to **yogurt** and **meat** purchases.
5. **Visualization & Interpretation**
   - Plot item frequencies and association rules using `arulesViz`.
   - Graph-based visualization of the strongest rules.

## 📂 Repository Structure
```
market_basket_analysis/
│── README.md  # Project documentation
│── market_basket_analysis.R  # R script with analysis code
│── data/  # Input datasets
│── results/  # Rule outputs and visualizations
```

## 🛠 Tools & Technologies
- **Programming Language:** R
- **Libraries:** arules, arulesViz
- **Methods:** Apriori, Eclat, Item Frequency Analysis

## 📊 Key Findings
- The most frequent **grocery items** in transactions.
- **High-lift association rules** indicating strong product relationships.
- Useful insights for **recommendation systems** and **store layout optimization**.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```r
install.packages(c("arules", "arulesViz"))
```
Then, run `market_basket_analysis.R` in RStudio.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
