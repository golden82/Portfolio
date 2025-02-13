# 🕵️ Enron Network Analysis

## 🔍 Project Overview
This project explores the **Enron email network** using graph theory to identify key individuals and relationships within the organization. The dataset includes email interactions between **50 senior officials**, allowing for **network-based insights** into how information flowed within Enron before its infamous collapse.

## 📑 Workflow

1. **Data Loading & Processing**
   - Load the email dataset containing sender-receiver interactions.
   - Convert the data into an **edge list** for network creation.
2. **Network Graph Construction**
   - Create a **directed graph (DiGraph)** using `NetworkX`.
   - Visualize **network structures** using different layouts.
3. **Centrality Analysis**
   - Compute key **centrality measures**:
     - **Degree Centrality** (Most connected nodes).
     - **Eigenvector Centrality** (Most influential nodes).
     - **Betweenness Centrality** (Nodes controlling information flow).
     - **Closeness Centrality** (Nodes best positioned for communication).
   - Identify and color **important individuals** in the network.
4. **Graph Visualization & Interpretation**
   - Highlight key nodes using **color coding**.
   - Draw different network structures (`spring`, `shell`, `circular`).
   - Interpret the roles of the most central individuals.

## 📂 Repository Structure
```
enron_network_analysis/
│── README.md  # Project documentation
│── enron_network_analysis.ipynb  # Jupyter Notebook with full analysis
│── data/  # Email interaction dataset
│── results/  # Visualizations and centrality metrics
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, NetworkX, Matplotlib, Seaborn
- **Graph Theory Methods:** Degree, Betweenness, Eigenvector, and Closeness Centrality

## 📊 Key Findings
- A **single individual** (Node 1) acts as the main information hub.
- Several nodes (e.g., **56, 74, 53, 54**) play secondary key roles.
- The **network structure suggests hierarchical communication patterns**.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy networkx matplotlib seaborn
```
Then, open and run `enron_network_analysis.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
