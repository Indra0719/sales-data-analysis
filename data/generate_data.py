import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

n = 1000
cats = ['Electronics', 'Clothing', 'Food & Beverage', 'Furniture', 'Sports']
prices = {
    'Electronics': (50, 1500),
    'Clothing': (10, 200),
    'Food & Beverage': (3, 40),
    'Furniture': (40, 600),
    'Sports': (8, 300)
}

dates = pd.date_range('2023-01-01', '2023-12-31', periods=n)
c = np.random.choice(cats, n)

df = pd.DataFrame({
    'order_id': [f'ORD-{i:04d}' for i in range(1, n+1)],
    'date': dates,
    'region': np.random.choice(['North', 'South', 'East', 'West'], n),
    'category': c,
    'unit_price': [round(random.uniform(*prices[x]), 2) for x in c],
    'quantity': np.random.randint(1, 10, n),
    'discount': np.random.choice([0, 0, 0, 0.05, 0.1, 0.15, 0.2], n)
})
df['revenue'] = round(df['unit_price'] * df['quantity'] * (1 - df['discount']), 2)
df.to_csv('data/sales_data.csv', index=False)
print(f'Done! {len(df)} rows saved to data/sales_data.csv')
