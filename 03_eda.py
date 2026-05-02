import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('outputs/charts', exist_ok=True)
df = pd.read_csv('outputs/hr_clean.csv')
sns.set_theme(style='whitegrid')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('HR Attrition Analysis Dashboard', fontsize=16)

dept_attr = df.groupby('department')['attrition'].mean().reset_index()
sns.barplot(data=dept_attr, x='department', y='attrition', ax=axes[0,0], palette='Blues_d')
axes[0,0].set_title('Attrition Rate by Department')
axes[0,0].set_ylabel('Attrition Rate')
axes[0,0].tick_params(axis='x', rotation=15)

overtime_attr = df.groupby('overtime')['attrition'].mean()
axes[0,1].pie(overtime_attr, labels=['No Overtime','Overtime'],
              autopct='%1.1f%%', colors=['#5DCAA5','#D85A30'])
axes[0,1].set_title('Attrition: Overtime vs No Overtime')

sns.boxplot(data=df, x='attrition', y='monthlyincome',
            ax=axes[1,0], palette='Set2')
axes[1,0].set_title('Monthly Income vs Attrition')
axes[1,0].set_xticklabels(['Stayed','Left'])

tenure_attr = df.groupby('tenure_group')['attrition'].mean()
sns.barplot(x=tenure_attr.index, y=tenure_attr.values,
            ax=axes[1,1], palette='Purples_d')
axes[1,1].set_title('Attrition Rate by Tenure Group')
axes[1,1].set_ylabel('Attrition Rate')

plt.tight_layout()
plt.savefig('outputs/charts/attrition_dashboard.png', dpi=150, bbox_inches='tight')
print("Dashboard saved!")

corr_cols = ['attrition','age','monthlyincome','yearsatcompany',
             'overtime','jobsatisfaction','distancefromhome']
corr = df[corr_cols].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, linewidths=0.5)
plt.title('Correlation Heatmap — Key Features')
plt.tight_layout()
plt.savefig('outputs/charts/correlation_heatmap.png', dpi=150, bbox_inches='tight')
print("Heatmap saved!")
print("\nAll charts saved to outputs/charts/")