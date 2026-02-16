import pandas as pd

print("Loading files...")

features = pd.read_csv('../data/Features data set.csv')
sales = pd.read_csv('../data/sales data-set.csv')
stores = pd.read_csv('../data/stores data-set.csv')

print("Merging datasets...")

df = sales.merge(stores, on="Store", how="left")
df = df.merge(features, on=["Store", "Date"], how="left")

print("Cleaning data...")
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

df.to_csv('../data/final_dataset.csv', index=False)

print("ETL Done ✅")
