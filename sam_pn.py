import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import Workbook

# Load Data from Excel File
file_path ="/Users/parnikanag/Documents/PN/hakathon/Coffee_Business_Data.xlsx"

xls = pd.ExcelFile(file_path)

coffee_seeds_df = pd.read_excel(xls, 'Coffee Seeds')
coffee_sales_df = pd.read_excel(xls, 'Coffee Sales')
customer_feedback_df = pd.read_excel(xls, 'Customer Feedback')
sweetener_sales_df = pd.read_excel(xls, 'Sweetener Sales')

# 1. Analyzing the Best Coffee Seed Supplier
def best_supplier(df):
    seeds_summary = df.groupby('Supplier').agg({'Sales Generated ($)': 'sum'}).sort_values(by='Sales Generated ($)', ascending=False)
    print("Best Supplier Based on Sales:\n", seeds_summary)

# 2. Comparing Instant and Filter Coffee Sales
def compare_coffee_sales(df):
    df['Difference'] = df['Filter Coffee Sales ($)'] - df['Instant Coffee Sales ($)']
    print("\nComparison of Sales:\n", df[['Date', 'Difference']])
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Instant Coffee Sales ($)'], label='Instant Coffee')
    plt.plot(df['Date'], df['Filter Coffee Sales ($)'], label='Filter Coffee')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Sales ($)')
    plt.title('Instant vs. Filter Coffee Sales')
    plt.show()

# 3. Customer Feedback Analysis
def customer_feedback_summary(df):
    feedback_summary = df['Water Quantity Feedback'].value_counts()
    print("\nCustomer Feedback on Water Quantity:\n", feedback_summary)
    feedback_summary.plot(kind='bar', color=['red', 'green', 'blue'])
    plt.xlabel('Feedback')
    plt.ylabel('Count')
    plt.title('Customer Feedback on Water Quantity')
    plt.show()

# 4. Comparing Coffee Sales with Different Sweeteners
def sweetener_sales_comparison(df):
    sweetener_summary = df[['Sugar Sales ($)', 'Jaggery Sales ($)', 'Sugar-Free Sales ($)']].sum()
    print("\nSweetener Sales Comparison:\n", sweetener_summary)
    sweetener_summary.plot(kind='bar', color=['brown', 'orange', 'gray'])
    plt.xlabel('Sweetener Type')
    plt.ylabel('Total Sales ($)')
    plt.title('Sweetener Sales Comparison')
    plt.show()

# Execute Functions
best_supplier(coffee_seeds_df)
compare_coffee_sales(coffee_sales_df)
customer_feedback_summary(customer_feedback_df)
sweetener_sales_comparison(sweetener_sales_df)
