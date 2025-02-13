# 🌐 Network Analysis & Machine Learning

## 🔍 Project Overview

This project focuses on network analysis using the "Reality Mining" dataset from MIT, which tracks interactions (calls, messages) between 100 individuals. The goal is to analyze the network structure and detect communities using multiple algorithms.

## 📑 Workflow

1. **Network Analysis** - Compute key metrics: nodes, edges, degree distribution, clustering coefficient, assortativity.
2. **Graph Visualization** - Use Cytoscape to display node connections.
3. **Community Detection** - Compare Louvain, Infomap, and Simulated Annealing methods.
4. **Optimization with Simulated Annealing** - Improve modularity through iterative optimization.

## 📂 Repository Structure
```
network_analysis/
│── README.md  # Project documentation
│── Network_analisys_Machine_Learning.docx  # Detailed report
│── simulated_annealing_ia_reality.rmd  # Notebook with code
│── data/  # Input dataset files
│── results/  # Graphs, visualizations, and detected communities
```

## 🛠 Tools & Technologies
- **Programming Language:** R
- **Libraries:** igraph, Cytoscape, Radatools
- **Algorithms Used:** Louvain, Infomap, Simulated Annealing

## 📊 Key Findings
- The **Louvain algorithm** detected **44 communities** (Modularity = 0.8730), fast and efficient.
- The **Infomap algorithm** detected **90 communities**, better for hierarchical structures.
- **Simulated Annealing** refined modularity but required more computational time.

## 📜 How to Run the Project
To execute the analysis in R:
```r
install.packages(c("igraph", "Cytoscape", "Radatools"))
```
Then, open and run `simulated_annealing_ia_reality.rmd` in RStudio.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
