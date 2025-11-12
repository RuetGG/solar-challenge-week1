# Solar Resource & Environmental Data Analysis

This repository contains the full exploratory data analysis (EDA) workflow for solar and environmental datasets collected from Benin, Sierra Leone, and Togo. The goal of this project is to understand how climate conditions, seasonal variation, humidity, wind, and panel cleaning influence solar irradiance and panel performance.

The analysis includes:
- Data cleaning and outlier detection
- Time series trends across seasons and daily cycles
- Solar panel cleaning impact on performance
- Correlation and variable relationship analysis
- Wind distribution patterns
- Temperature and humidity interaction study
- Bubble chart visualization linking radiation, temperature, and humidity
- Cross-country comparison of Benin, Sierra Leone, and Togo with boxplots, summary stats, and ANOVA/Kruskal–Wallis tests.
- Correlation analysis linking radiation, temperature, and humidity.

---

## Environment Setup

Follow the steps below to set up the project environment.

### 1. Clone the Repository
```bash
git clone https://github.com/RuetGG/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Create Virtual Environment (Windows)
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment (Windows)
```bash
.venv\Scripts\activate
```

### 4. Install Depencencies
```bash
pip install -r requirements.txt
pip install pandas numpy matplotlib seaborn plotly windrose
```


### 5. Add you data
```bash
data/
  ├── benin_raw.csv
  ├── sierraleone_raw.csv
  └── togo_raw.csv
  ```
### 6. Run the Analysis
You can either run the notebooks: 
```bash 
jupyter notebook
```
Or run the scripts directly:
```bash
python scripts/analysis_benin.py
```


