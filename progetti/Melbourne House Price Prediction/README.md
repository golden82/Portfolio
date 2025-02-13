# 🚖 Uber Case 
: Data Analysis

## 🔍 Project Overview
This project analyzes **Uber trip data** to identify patterns, trends, and insights related to ride-hailing demand, trip duration, and geographical distribution. The goal is to gain a better understanding of ride usage patterns over time.

## 📑 Workflow

1. **Data Loading & Cleaning**
   - Load Uber trip dataset.
   - Handle missing values and correct data types.
   - Convert timestamps for time-based analysis.
2. **Exploratory Data Analysis (EDA)**
   - Analyze trip distribution by time of day, day of the week, and month.
   - Visualize **trip durations** and **popular pickup/drop-off locations**.
3. **Geospatial Analysis**
   - Plot Uber ride heatmaps using latitude/longitude coordinates.
   - Identify high-demand locations in different time windows.
4. **Time-Series Analysis**
   - Detect ride demand trends over different time periods.
   - Compare weekday vs. weekend usage patterns.

## 📂 Repository Structure
```
taxi_case_study/
│── README.md  # Project documentation
│── uber_case_study.ipynb  # Jupyter Notebook with full analysis
│── data/  # Uber trip datasets
│── results/  # Visualizations and insights
```

## 🛠 Tools & Technologies
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Plotly, Folium
- **Methods Used:** Data Cleaning, Visualization, Geospatial Analysis

## 📊 Key Findings
- Uber rides peak during **rush hours** and late evenings.
- **Manhattan and downtown areas** have the highest ride density.
- Weekends show higher **average trip durations** compared to weekdays.

## 📜 How to Run the Project
To install dependencies and execute the analysis:
```bash
pip install pandas numpy matplotlib seaborn plotly folium
```
Then, open and run `uber_case_study.ipynb` in Jupyter Notebook.

## 📝 Author
- **Agostino Fontana**

---
💡 *If you find this project useful, leave a ⭐ on GitHub!* 🚀
