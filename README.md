# HR Attrition ETL Pipeline | NTT DATA Project

## Overview
End-to-end ETL data pipeline analyzing 1,470 employee records to identify 
key attrition drivers. Built to mirror enterprise data workflow standards 
used in organizations like NTT DATA.

## Pipeline Architecture
| Stage | Description | Tool |
|---|---|---|
| Ingestion | Raw CSV loading with schema validation | Python, Pandas |
| Quality Checks | Null detection, duplicate flagging | Pandas |
| Cleaning | Encoding, standardization, deduplication | Pandas |
| Transformation | Derived columns — salary band, tenure group | Pandas |
| Join | Department lookup table integration | Pandas |
| Validation | 4 assertion-based data quality checks | Python |
| EDA | 4-panel dashboard + correlation heatmap | Matplotlib, Seaborn |
| SQL Analysis | 5 business queries | SQLite |

## Key Business Insights
- Sales department has highest attrition rate at **20.63%**
- Overtime employees leave at **30.53%** vs 10.44% without overtime
- Low salary band shows **28.61% attrition** vs 8.9% in Very High band
- New employees under 2 years have **28.86% attrition risk**
- Sales Representatives have highest role-level attrition at **39.76%**

## Tech Stack
Python | Pandas | NumPy | Matplotlib | Seaborn | SQLite | GitHub
## Project Structure
nttdata-etl-project/
├── notebooks/
│   ├── 01_ingest.py          # Data loading & exploration
│   ├── 02_etl_pipeline.py    # Main ETL pipeline
│   ├── 03_eda.py             # Visualizations & charts
│   └── 04_sql_analysis.py    # SQL business queries
└── outputs/
├── hr_clean.csv           # Cleaned dataset
├── pipeline_summary.csv   # Pipeline run summary
├── sql_*.csv              # SQL query results
└── charts/
├── attrition_dashboard.png
└── correlation_heatmap.png
## Results
- 1,470 records processed through 7-stage pipeline
- 40 columns after feature engineering
- 4 data validation checks passed
- 5 SQL business queries executed
- 2 visualization outputs generated

## Author
Sarika Bhukya | B.Tech AI & ML | CMR Technical Campus
bhukyasarika02@gmail.com
Python | Pandas | NumPy | Matplotlib | Seaborn | SQLite | GitHub

## Project Structure
