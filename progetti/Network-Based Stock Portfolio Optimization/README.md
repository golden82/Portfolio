# 📈 Network-Based Stock Portfolio Optimization

## 🔍 Project Overview
This project applies **network analysis techniques** to optimize stock portfolio selection. The approach identifies **central and peripheral stocks** within the S&P 500 based on **network topology** and evaluates their performance compared to the S&P 500 index.

## 📑 Workflow

1. **Data Collection & Processing**
   - Extracted S&P 500 component stocks from Wikipedia.
   - Collected stock price data (2011-2020) using Yahoo Finance.
   - Computed **log returns** and generated correlation matrices.
2. **Network Construction & Filtering**
   - Created a **correlation-based stock network**.
   - Used **Minimum Spanning Tree (MST)** to filter redundant connections.
3. **Stock Selection via Network Centrality**
   - Measured **Degree, Betweenness, and Closeness Centrality**.
   - Identified **top 15 central stocks** and **top 15 peripheral stocks**.
4. **Portfolio Simulation & Performance Evaluation**
   - Constructed **central & peripheral portfolios**.
   - Simulated portfolio performance over a 1-year investment horizon.
   - Compared against S&P 500 benchmark returns.

## 📂 Repository Structure
```
network_stock_optimization/
│── README.md  # Project documentation
│── network_portfolio_optimization.ipynb  # Jupyter Notebook with full analysis
│── data/  # Stock price data (S&P 500 historical prices)
│── results/  # Visualizations and portfolio performance metrics
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Seaborn, NetworkX, Matplotlib, Plotly, Pandas-DataReader
- **Methods Used:** Log Returns, Correlation Matrices, MST, Network Centrality Metrics

## 📊 Key Findings
- **Central stocks** exhibit higher correlation with the market and tend to be more stable.
- **Peripheral stocks** display weaker correlations and higher risk.
- Network-based portfolio construction **can outperform traditional diversification strategies**.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy seaborn networkx matplotlib plotly pandas-datareader
```
Then, open and run `network_portfolio_optimization.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
