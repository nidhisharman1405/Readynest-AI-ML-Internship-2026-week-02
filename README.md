# Retail Intelligence and Consumer Behavior Analysis

Retail Intelligence and Consumer Behavior Analysis is a data analytics project designed to explore large-scale retail transaction records from India and transform raw sales data into actionable business insights.

The project investigates purchasing trends, customer demographics, product profitability, regional performance, and consumer segmentation through interactive visual analytics.

Prepared as part of the **AI/ML Internship Program – Week 02 Submission (2026)**.

---

# Project Pipeline

```text
Retail Dataset
      │
      ▼
Data Acquisition
      │
      ▼
Data Preparation
      │
      ▼
Derived Metrics Generation
      │
      ▼
Retail Trend Analysis
      │
      ▼
Consumer Classification
      │
      ▼
Visualization Dashboard
      │
      ▼
Business Decisions
```

---

# Project Goals

* Study customer purchasing patterns
* Analyze sales performance over time
* Discover profitable products and categories
* Segment customers based on spending behavior
* Design an interactive Power BI dashboard
* Recommend strategies for improving business performance

---

# Dataset Summary

| Parameter         | Details                     |
| ----------------- | --------------------------- |
| Source            | Indian Retail Store Dataset |
| Records           | 100,000+                    |
| Period Covered    | 2020–2023                   |
| Attributes        | 25+                         |
| Format            | CSV                         |
| Processed Dataset | retail_cleaned.csv          |

---

# Tools and Technologies

### Programming

* Python
* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn
* Power BI

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# Repository Layout

```text
Retail-Intelligence-Consumer-Analysis/

├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_Data_Loading.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_EDA.ipynb
│   └── 05_Customer_Segmentation.ipynb
│
├── outputs/
├── reports/
├── scripts/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Data Processing

### Cleaning Activities

* Null value inspection
* Duplicate record removal
* Datatype optimization
* Date parsing
* Integrity verification

### Generated Features

* Order Month
* Quarter Number
* Customer Age
* Shipping Duration
* Profit Percentage
* Spending Segment

---

# Exploratory Analysis

### Consumer Insights

* Age Distribution
* Spending Distribution
* Premium Customers

### Revenue Insights

* Monthly Revenue Trend
* Quarterly Growth
* State-wise Comparison
* Regional Performance

### Product Insights

* Top Selling Products
* Category Contribution
* Discount Analysis
* Profit Analysis

### Operational Metrics

* Delivery Performance
* Variable Correlation Study

---

# Customer Classification

Customers were grouped according to their purchase contribution.

| Group    | Characteristics       |
| -------- | --------------------- |
| Platinum | Highest spenders      |
| Gold     | Moderate contributors |
| Silver   | Low spenders          |

---

# Dashboard Pages

### Sales Overview

* Revenue Summary
* Profit Analysis
* Monthly Sales Trend

### Customer Insights

* Segment Distribution
* Demographic Analysis
* Top Buyers

### Product Insights

* Category Performance
* Discount Impact
* Profitability Review

### Regional Analysis

* Geographic Sales Distribution
* Shipping Efficiency

---

# Major Observations

* A small percentage of customers generate most of the revenue.
* Seasonal trends significantly influence product demand.
* Discounts have a negative impact on profit margins.
* Certain states consistently outperform others.

---

# Suggested Actions

* Develop loyalty schemes for premium customers.
* Review discount strategies.
* Improve logistics in weaker regions.
* Promote highly profitable categories.

---

# Future Enhancements

* RFM Analysis
* Recommendation Engine
* Sales Forecasting
* Streamlit Deployment
* Real-Time Data Pipeline

---

# Author

**Nidhi Sharma**

AI/ML Internship Program • 2026

Data Analytics • Power BI • Business Intelligence
