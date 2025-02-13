# 🌍 Google Trends Analysis with gtrendsR

## 🔍 Project Overview

This project analyzes search trends using **Google Trends** data obtained via the `gtrendsR` package in R. The goal is to examine how search interest changes over time for specific keywords (Nike, Adidas) and identify patterns related to economic, social, or seasonal events.

## 📑 Workflow

1. **Data Extraction**
   - Use `gtrendsR` to retrieve Google search trend data for **Nike and Adidas**.
   - Filter results based on specific keywords, regions, and timeframes (last 5 years).
2. **Data Processing & Cleaning**
   - Normalize data and prepare time-series structures.
3. **Trend Analysis & Visualization**
   - Generate **time-series plots** to identify search behavior patterns.
   - **Compare search trends** across multiple regions.
   - Compute **correlation** between the search volumes of the two brands.
4. **Geospatial Analysis**
   - Map the **global search interest** using `ggplot2` and `maps`.
5. **Text Mining on Related Queries**
   - Extract **top and rising search queries**.
   - Perform **bigram analysis** to uncover relationships between search terms.
   - Visualize keyword connections using `igraph` and `ggraph`.

## 📂 Repository Structure
```
google_trends_analysis/
│── README.md  # Project documentation
│── google_trends_analysis.R  # R script for data extraction and analysis
│── data/  # Extracted Google Trends data
│── results/  # Visualization outputs
```

## 🛠 Tools & Technologies
- **Programming Language:** R
- **Libraries:** gtrendsR, ggplot2, dplyr, maps, tidytext, igraph, ggraph
- **Analysis Methods:** Time-series analysis, correlation analysis, text mining

## 📊 Key Findings
- **Search interest fluctuates** based on region and time period.
- Nike and Adidas searches **show a positive correlation** in volume trends.
- Identified **global distribution of searches**, highlighting key markets.
- **Text mining reveals** keyword associations and user search behavior.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```r
install.packages(c("gtrendsR", "ggplot2", "dplyr", "maps", "tidytext", "igraph", "ggraph"))
```
Then, run `google_trends_analysis.R` in RStudio.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
