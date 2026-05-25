import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data1/pharmacy_data_rows.csv")

# Show first 5 rows
print(df.head())

# Dataset info
print(df.info())

# Total stock
print("Total Stock:", df["Stock_quantity"].sum())

# Top selling medicines
top = df.groupby("Medicine_Name")["Units_Sold"].sum().sort_values(ascending=False)

print(top.head())

# Create chart
top.head().plot(kind="bar")

plt.title("Top Selling Medicines")
plt.xlabel("Medicine Name")
plt.ylabel("Units Sold")

plt.show()