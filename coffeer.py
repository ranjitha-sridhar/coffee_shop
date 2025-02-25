import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette('pastel')

seed_data = {
    'Supplier': np.random.choice(['Blue Tokai', 'Tata Coffee', 'Nescafe', 'Lavazza'], 100),
    'Year': np.random.choice([2020, 2021, 2022, 2023, 2024], 100),
    'Seeds Bought (kg)': np.random.randint(400, 1000, 100),
    'Sales Generated ($)': np.random.randint(4000, 15000, 100)
}
seeds_df = pd.DataFrame(seed_data)
seeds_df.to_csv('Coffee_Seeds.csv', index=False)

launch_data = {
    'ProductLaunch': np.random.choice(['New Latte', 'Espresso Shot', 'Cold Brew', 'Flat White', 'Macchiato'], 100),
    'Sales': np.random.randint(500, 10000, 100)
}
launch_df = pd.DataFrame(launch_data)

menu_data = {
    'MenuItem': np.random.choice(['Espresso', 'Latte', 'Cappuccino', 'Mocha', 'Americano', 'Affogato'], 100),
    'Sales': np.random.randint(1000, 10000, 100)
}
menu_df = pd.DataFrame(menu_data)

price_data = {
    'Price': np.random.randint(50, 500, 100),
    'Sales': np.random.randint(1000, 9000, 100)
}
price_df = pd.DataFrame(price_data)

def new_product_launches(df):
    launch_data = df.groupby('ProductLaunch')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    launch_data.plot(kind='bar', color=sns.color_palette('pastel'))
    plt.title('New Product Launches')
    plt.xlabel('Product Launch')
    plt.ylabel('Sales')
    plt.show(block=False)

new_product_launches(launch_df)

def menu_optimization(df):
    menu_data = df.groupby('MenuItem')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    menu_data.plot(kind='bar', color=sns.color_palette('pastel'))
    plt.title('Menu Optimization')
    plt.xlabel('Menu Item')
    plt.ylabel('Sales')
    plt.show(block=False)

menu_optimization(menu_df)

def price_sensitivity(df):
    price_effect = df.groupby('Price')['Sales'].sum()
    plt.figure(figsize=(10, 6))
    price_effect.plot(kind='line', marker='o', color=sns.color_palette('pastel')[0])
    plt.title('Price Sensitivity')
    plt.xlabel('Price')
    plt.ylabel('Sales')
    plt.show(block=False)

price_sensitivity(price_df)

def competitor_analysis(df):
    competitor_data = df.groupby('Competitor')[['Sales', 'Rating']].mean()
    competitor_data.plot(kind='bar', color=sns.color_palette('pastel'), title='Competitor Sales and Ratings')
    plt.ylabel('Average Value')
    plt.xlabel('Competitor')
    plt.tight_layout()
    plt.show(block=False)

competitor_data = {
    'Competitor': np.random.choice(['Starbucks', 'Costa Coffee', 'Blue Tokai', 'Third Wave Coffee', 'Cafe Coffee Day'], 50),
    'Sales': np.random.randint(1000, 10000, 50),
    'Rating': np.random.uniform(1, 5, 50)
}
competitor_df = pd.DataFrame(competitor_data)
competitor_analysis(competitor_df)

plt.show()
