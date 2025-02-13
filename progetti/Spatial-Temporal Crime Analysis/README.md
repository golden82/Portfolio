# 🗺️ Spatial-Temporal Crime Analysis

## 🔍 Project Overview

This project models **spatio-temporal crime patterns** in Valencia using statistical methods in R. The study aims to identify high-risk areas and time periods, analyze relationships between crime occurrences and urban infrastructure, and develop predictive models.

## 📑 Workflow

1. **Data Collection & Preprocessing**
   - Import crime records and spatial data.
   - Convert latitude/longitude into projected coordinates.
2. **Exploratory Data Analysis (EDA)**
   - Visualize crime distributions over time and space.
   - Analyze distances between crimes and urban features (e.g., ATMs, restaurants, police stations).
3. **Spatial Analysis**
   - Compute nearest neighbor distances.
   - Generate spatial point patterns.
4. **Statistical Modeling**
   - **Generalized Linear Models (GLM)** for crime frequency prediction.
   - **Poisson regression** for time-based crime analysis.
   - **Polynomial regression** to capture hourly variations.

## 📂 Repository Structure
```
spatial_crime_analysis/
│── README.md  # Project documentation
│── CasoStudio1.pdf  # Detailed report
│── Caso_Studio_1.R  # R script with analysis code
│── data/  # Input datasets
│── results/  # Model outputs, visualizations, and diagnostics
```

## 🛠 Tools & Technologies
- **Programming Language:** R
- **Libraries:** sf, spatstat, tidygraph, ggplot2
- **Statistical Models:** GLM, Poisson regression, Polynomial regression

## 📊 Key Findings
- Crimes exhibit **strong spatial dependencies**, influenced by urban features.
- Certain **time periods and locations** have higher crime rates.
- Poisson regression models provide **accurate predictions** of crime frequency by time and day.

## 📜 How to Run the Project
To install dependencies and run the analysis:
```r
install.packages(c("sf", "spatstat", "ggplot2", "tidygraph"))
```
Then, execute `Caso_Studio_1.R` in RStudio.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
