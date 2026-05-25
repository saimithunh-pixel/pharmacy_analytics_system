import pandas as pd          #import libraries     
import matplotlib.pyplot as plt

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")     #load cleaned dataset

print(df.head())
print(df.columns)       #check column names

low_stock = df[df['Stock_Quantity'] < 20]      #low stock detection
overstock = df[df['Stock_Quantity'] > 150]     #overstock analysis
fast_moving = df.sort_values(by='Stock_Quantity', ascending=False).head(10)      #fastmoving medicines

print("Low Stock Medicines:", len(low_stock))
print("Overstock Items:", len(overstock))
print("Fast Moving Medicines:", len(fast_moving))

low_stock.to_csv("low_stock_report.csv", index=False)
overstock.to_csv("overstock_report.csv", index=False)
fast_moving.to_csv("fast_moving_report.csv", index=False)