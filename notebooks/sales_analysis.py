import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])
df['month'] = df['date'].dt.month
df['month_name'] = df['date'].dt.strftime('%b')
df['revenue'] = df['unit_price'] * df['quantity'] * (1 - df['discount'])

print(f"Dataset loaded: {len(df)} rows")
print(f"Total Revenue: ${df['revenue'].sum():,.2f}")
print(f"Avg Order Value: ${df['revenue'].mean():.2f}")

# --- Chart 1: Monthly Revenue ---
monthly = df.groupby(['month', 'month_name'])['revenue'].sum().reset_index().sort_values('month')
months = monthly['month_name'].tolist()

fig, ax = plt.subplots(figsize=(12, 5))
colors = ['#e74c3c' if x == monthly['revenue'].max() else '#3498db' for x in monthly['revenue']]
ax.bar(months, monthly['revenue']/1000, color=colors)
ax.set_title('Monthly Revenue 2023', fontsize=16, fontweight='bold')
ax.set_ylabel('Revenue ($K)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('outputs/monthly_revenue.png', dpi=150, bbox_inches='tight')
print('Saved: monthly_revenue.png')

# --- Chart 2: Revenue by Category ---
cat = df.groupby('category')['revenue'].sum().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(cat.index, cat.values/1000, color=['#e74c3c','#e67e22','#f1c40f','#2ecc71','#3498db'])
ax.set_title('Revenue by Category 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Revenue ($K)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('outputs/revenue_by_category.png', dpi=150, bbox_inches='tight')
print('Saved: revenue_by_category.png')

# --- Chart 3: Avg Order Value by Region ---
region = df.groupby('region')['revenue'].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(region.index, region.values, color=['#9b59b6','#1abc9c','#e67e22','#e74c3c'])
ax.set_title('Avg Order Value by Region', fontsize=16, fontweight='bold')
ax.set_ylabel('Avg Order Value ($)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('outputs/region_analysis.png', dpi=150, bbox_inches='tight')
print('Saved: region_analysis.png')

# --- Chart 4: Discount Impact ---
discount = df.groupby('discount')['revenue'].mean().reset_index()
discount['label'] = discount['discount'].apply(lambda x: f"{int(x*100)}% off" if x > 0 else 'No Discount')

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(discount['label'], discount['revenue'],
       color=['#95a5a6' if d == 0 else '#e74c3c' for d in discount['discount']])
ax.set_title('Avg Revenue by Discount Level', fontsize=16, fontweight='bold')
ax.set_ylabel('Avg Revenue ($)')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('outputs/discount_impact.png', dpi=150, bbox_inches='tight')
print('Saved: discount_impact.png')

print('All charts saved to outputs/')
