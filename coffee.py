import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook
# 1. Create Excel Files with Dummy Data

# Coffee Seeds Data
seed_data = {
    'Supplier': ['Coorg', '', 'Supplier C', 'Supplier A', 'Supplier B'],
    'Year': [2021, 2021, 2021, 2022, 2022],
    'Seeds Bought (kg)': [500, 600, 550, 520, 580],
    'Sales Generated ($)': [5000, 6200, 5800, 5300, 6000]
}
seeds_df = pd.DataFrame(seed_data)
seeds_df.to_excel('Coffee_Seeds.xlsx', index=False)

# Coffee Sales Data
sales_data = {
    'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Instant Coffee Sales ($)': np.random.randint(1000, 5000, 12),
    'Filter Coffee Sales ($)': np.random.randint(1500, 5500, 12)
}
sales_df = pd.DataFrame(sales_data)
sales_df.to_excel('Coffee_Sales.xlsx', index=False)

# Customer Feedback Data
feedback_data = {
    'Customer ID': range(1, 21),
    'Water Quantity Feedback': np.random.choice(['Too Much', 'Just Right', 'Too Little'], 20)
}
feedback_df = pd.DataFrame(feedback_data)
feedback_df.to_excel('Customer_Feedback.xlsx', index=False)

# Sweetener Sales Data
sweetener_data = {
    'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Sugar Sales ($)': np.random.randint(1000, 3000, 12),
    'Jaggery Sales ($)': np.random.randint(800, 2500, 12),
    'Sugar-Free Sales ($)': np.random.randint(500, 2000, 12)
}
sweetener_df = pd.DataFrame(sweetener_data)
sweetener_df.to_excel('Sweetener_Sales.xlsx', index=False)

# 2. Analyzing the Best Coffee Seed Supplier
seeds_summary = seeds_df.groupby('Supplier').agg({'Sales Generated ($)': 'sum'}).sort_values(by='Sales Generated ($)', ascending=False)
print("Best Supplier Based on Sales:\n", seeds_summary)

# 3. Comparing Instant and Filter Coffee Sales
sales_df['Difference'] = sales_df['Filter Coffee Sales ($)'] - sales_df['Instant Coffee Sales ($)']
print("\nComparison of Sales:\n", sales_df[['Date', 'Difference']])

# 4. Customer Feedback Analysis
feedback_summary = feedback_df['Water Quantity Feedback'].value_counts()
print("\nCustomer Feedback on Water Quantity:\n", feedback_summary)

# 5. Comparing Coffee Sales with Different Sweeteners
sweetener_summary = sweetener_df[['Sugar Sales ($)', 'Jaggery Sales ($)', 'Sugar-Free Sales ($)']].sum()
print("\nSweetener Sales Comparison:\n", sweetener_summary)