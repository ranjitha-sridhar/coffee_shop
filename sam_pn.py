import pandas as pd
import matplotlib.pyplot as plt

# Load Data from Excel File
file_path = "/Users/parnikanag/Documents/PN/hakathon/Coffee_Shop.xlsx"
xls = pd.ExcelFile(file_path)

# Load the correctly formatted data
coffee_seeds_df = pd.read_excel(xls, 'Coffee Seeds')
coffee_sales_df = pd.read_excel(xls, 'Coffee Sales')
customer_feedback_df = pd.read_excel(xls, 'Customer Feedback')
sweetener_sales_df = pd.read_excel(xls, 'Sweetener Sales')

# Ensure 'Date' columns are in datetime format for proper plotting
coffee_sales_df['Date'] = pd.to_datetime(coffee_sales_df['Date'])
sweetener_sales_df['Date'] = pd.to_datetime(sweetener_sales_df['Date'])

# 1. Analyzing the Best Coffee Seed Supplier
def best_supplier(df):
    seeds_summary = df.groupby('Supplier').agg({'Sales Generated': 'sum'}).sort_values(by='Sales Generated', ascending=False)
    print("Best Supplier Based on Sales:\n", seeds_summary)
    seeds_summary.plot(kind='bar', color='brown', legend=False)
    plt.xlabel('Supplier')
    plt.ylabel('Total Sales')
    plt.title('Best Coffee Seed Supplier by Sales')
    plt.xticks(rotation=45)
    plt.show()

# 2. Comparing Instant and Filter Coffee Sales
def compare_coffee_sales(df):
    df['Difference'] = df['Filter Coffee Sales'] - df['Instant Coffee Sales']
    print("\nComparison of Sales:\n", df[['Date', 'Difference']])
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Instant Coffee Sales'], label='Instant Coffee', marker='o')
    plt.plot(df['Date'], df['Filter Coffee Sales'], label='Filter Coffee', marker='s')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Instant vs. Filter Coffee Sales')
    plt.xticks(rotation=45)
    plt.grid()
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

# 4. Detailed Sweetener Sales Analysis
def sweetener_sales_analysis(df):
    sweetener_summary = df[['Sugar Sales', 'Jaggery Sales', 'Sugar-Free Sales']].sum()
    print("\nSweetener Sales Comparison:\n", sweetener_summary)
    
    # Market Share
    plt.figure(figsize=(7,7))
    sweetener_summary.plot(kind='pie', autopct='%1.1f%%', colors=['brown', 'orange', 'gray'])
    plt.title('Sweetener Market Share')
    plt.ylabel('')
    plt.show()
    
    # Monthly Sales Trends
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Sugar Sales'], label='Sugar', marker='o', color='brown')
    plt.plot(df['Date'], df['Jaggery Sales'], label='Jaggery', marker='s', color='orange')
    plt.plot(df['Date'], df['Sugar-Free Sales'], label='Sugar-Free', marker='^', color='gray')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Sweetener Sales Trends Over Time')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Execute Functions
best_supplier(coffee_seeds_df)
compare_coffee_sales(coffee_sales_df)
customer_feedback_summary(customer_feedback_df)
sweetener_sales_analysis(sweetener_sales_df)
