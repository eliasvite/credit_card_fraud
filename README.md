# Home Credit Default Risk - Business Data Analytics

## Project Overview
This repository contains a Data Analytics pipeline designed to inspect, clean, and analyze client data for risk assessment, heavily inspired by commercial retail and e-commerce analytical frameworks. The main objective is to identify key risk drivers and behavioral patterns that influence credit defaults, enabling data-driven decisions to protect capital and mitigate financial loss.

## Repository Structure
```text
credit_card_fraud/
│
├── data/
│   └── [Dataset Files]
├── notebooks/
│   └── eda.ipynb         # Main Jupyter Notebook containing data cleaning & business charts
├── src/
│   └── ingestion.py      # Automated data ingestion pipeline
└── README.md

## Methodology & Pipeline Steps
1. Data Ingestion

An automated, dynamic script searches the local environment for downloaded data chunks directly from Kaggle. It prevents tracking heavy CSV files inside Git by applying optimization strategies while identifying the internal schema structure.
2. Data Cleaning & Preprocessing (Step-by-Step)

To achieve a standardized dataset without missing information or format gaps, the data undergoes three independent, isolated processing steps:

    Missing Value Imputation: Fills numerical gaps using the column's median to prevent outlier skewness. Categorical text gaps are completed using the mode (most frequent value).

    Label Encoding: Converts categorical or text variables (such as contract type, gender, or suite metadata) into sequential integers so mathematical operations can read them.

    Standard Scaling: Normalizes numerical features (excluding unique identifiers and the TARGET column) to a common distribution with a mean of 0 and a standard deviation of 1. This ensures features with large numbers (e.g., total income) do not eclipse smaller counts (e.g., family size).

Key Business Insights & Findings
Risk Drivers (Top Correlations)

Our financial correlation analysis isolated the variables most closely tied to financial default (TARGET):

    Age (DAYS_BIRTH): Strongest positive correlation to risk. Younger applicants statistically present a higher default rate.

    Regional Evaluation (REGION_RATING_CLIENT_W_CITY): The socioeconomic rating of the client’s city heavily impacts credit performance. Higher ratings (worse socioeconomic environments) double the financial risk.

    Operational Instability (DAYS_LAST_PHONE_CHANGE): Frequent or recent phone changes correlate with higher repayment difficulties.

Data Visualizations Recap

    Credit Default by Region Economic Rating:

        Region 1 (High Socioeconomic Level): Low baseline risk (~5% default rate).

        Region 3 (Low Socioeconomic Level): Highest exposure (~11% default rate). Operational recommendation: Tighter credit restrictions or lower limits should apply here.

    Average Credit Amount by Contract Type:

        Found a stark capital concentration in Contract Type 0 (traditional cash loans), while Contract Type 1 (revolving loans) represents minimal capital exposure.

    Average Income vs. Target Status:

        A counter-intuitive revelation showed that clients who defaulted actually had a slightly higher average income than those who repaid on time. This proves that credit default risk in this portfolio is driven by over-indebtedness or stability metrics rather than insufficient income.