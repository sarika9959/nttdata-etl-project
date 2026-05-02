import pandas as pd
import sqlite3
import os

os.makedirs('outputs', exist_ok=True)
df = pd.read_csv('outputs/hr_clean.csv')

conn = sqlite3.connect(':memory:')
df.to_sql('employees', conn, index=False, if_exists='replace')

queries = {
    "attrition_by_department": """
        SELECT department,
               COUNT(*) as total_employees,
               SUM(attrition) as left_company,
               ROUND(AVG(attrition)*100, 2) as attrition_rate_pct
        FROM employees
        GROUP BY department
        ORDER BY attrition_rate_pct DESC
    """,
    "attrition_by_salary_band": """
        SELECT salary_band,
               COUNT(*) as total,
               SUM(attrition) as attrited,
               ROUND(AVG(attrition)*100, 2) as attrition_pct,
               ROUND(AVG(monthlyincome), 0) as avg_income
        FROM employees
        GROUP BY salary_band
        ORDER BY attrition_pct DESC
    """,
    "top_attrition_roles": """
        SELECT jobrole,
               ROUND(AVG(attrition)*100,2) as attrition_rate,
               ROUND(AVG(jobsatisfaction),2) as avg_satisfaction,
               ROUND(AVG(monthlyincome),0) as avg_income,
               COUNT(*) as headcount
        FROM employees
        GROUP BY jobrole
        HAVING headcount > 20
        ORDER BY attrition_rate DESC
        LIMIT 5
    """,
    "overtime_impact": """
        SELECT overtime,
               COUNT(*) as employees,
               ROUND(AVG(attrition)*100,2) as attrition_pct,
               ROUND(AVG(monthlyincome),0) as avg_income
        FROM employees
        GROUP BY overtime
    """,
    "tenure_attrition": """
        SELECT tenure_group,
               COUNT(*) as headcount,
               SUM(attrition) as left_count,
               ROUND(AVG(attrition)*100,2) as attrition_rate,
               ROUND(AVG(yearsatcompany),1) as avg_years
        FROM employees
        GROUP BY tenure_group
        ORDER BY attrition_rate DESC
    """
}

for name, query in queries.items():
    result = pd.read_sql_query(query, conn)
    result.to_csv(f'outputs/sql_{name}.csv', index=False)
    print(f"\n=== {name.upper()} ===")
    print(result.to_string(index=False))

conn.close()
print("\n=== ALL SQL QUERIES DONE ===")
print("Results saved to /outputs folder")