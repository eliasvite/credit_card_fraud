# Home Credit Default Risk - Business Data Analytics Pipeline

## Project Overview
This repository contains a professional Data Analytics pipeline built to inspect, clean, and profile client data for credit risk assessment. Rather than pursuing standard Machine Learning modeling, this project focuses heavily on **Commercial and Retail Analytics Methodology** (similar to E-Commerce Sales Performance Frameworks) to isolate key risk drivers, identify high-exposure financial segments, and uncover behavioral KPIs that directly impact capital preservation and business profitability.

---

## Repository Structure
```text
credit_card_fraud/
│
├── data/
│   └── [Dataset Files / Kaggle API Config]
├── notebooks/
│   └── eda.ipynb         # Main Jupyter Notebook with cleaning, dashboards & customer segments
├── src/
│   └── ingestion.py      # Automated data ingestion scripts
└── README.md             # Project documentation and business insights
```

# Methodology & Pipeline Steps

The analytical workflow was meticulously structured into non-overlapping, sequential cells to guarantee clean execution, prevent variables from cross-contaminating, and ensure complete independence across operations.
1. Data Ingestion & Schema Discovery

A robust python script inspects the local directory for chunked data sourced directly from Kaggle. The pipeline automatically analyzes the internal structural format without tracking heavy files under Git control.
2. Isolated Preprocessing & Standardization

To create an optimal foundation for financial metrics calculation, the tracking dataframe goes through three independent stages:

    Missing Value Imputation: Fills numerical gaps using the feature's median to completely neutralize outlier distortions. Categorical gaps are seamlessly completed using the mode (the most frequent string attribute).

    Label Encoding: Dynamically extracts text columns (such as contract types or geographic ratings) and maps them into progressive integers, rendering them completely readable for statistical arrays.

    Standard Scaling: Converts numerical features to a standardized scale (mean = 0, standard deviation = 1), while strictly protecting internal identity targets (SK_ID_CURR, TARGET). This normalizes extreme range gaps (e.g., total income vs. family count).

Key Business Insights & Financial KPIs

By treating the portfolio metrics exactly like an e-commerce segment analysis (analyzing "sales leakage" as loan defaults), we isolated several powerful insights:
1. Primary Risk Drivers (Correlation Analysis)

An extraction of statistical dependencies with the TARGET field revealed the most critical business indicators:

    Age (DAYS_BIRTH): Holds the highest statistical risk correlation. Younger demographics show a markedly higher rate of credit distress.

    Regional Disparities (REGION_RATING_CLIENT_W_CITY): The local socioeconomic environment significantly steers repayment behavior. Worse-rated locations represent higher exposure.

    Operational Friction (DAYS_LAST_PHONE_CHANGE): Frequent or very recent telephone changes directly flag customer or financial instability.

2. Strategic Customer Segmentation (The High-Alert Segment)

By combining regional macroeconomic attributes with operational friction variables, we separated the portfolio into two specific commercial risk brackets:

    High-Alert Risk Segment: Comprises 25,725 clients with a severe 13.15% default rate.

    Standard Portfolio: Comprises 281,786 clients maintaining a healthy 7.60% default rate.

    Business Action: The high-alert segment scales risk to nearly double the baseline. Strategic mitigation recommends lowering credit assignment ceilings or applying stricter verification gates specifically to this demographic to prevent capital leaks without harming standard portfolio acquisition.

3. The Income Paradox

    Counter-intuitively, grouping data by payment status proved that defaulted clients maintain a slightly higher average total income than users who fulfill payments on schedule.

    Strategic Conclusion: Default risk in this business portfolio is not driven by insufficient income, but rather by over-leverage, local market volatility, and structural household instability.
