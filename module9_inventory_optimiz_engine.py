"""import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")
print(df.head())

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df['Inventory_Value'] = df['Stock_Quantity'] * df['Price_per_unit']

df['Reorder_Status'] = df['Stock_Quantity'] <= df['Reorder_Level']

print("\nREORDER STATUS")
print(df[['Medicine_Name',
          'Stock_Quantity',
          'Reorder_Level',
          'Reorder_Status']])

low_stock = df[df['Stock_Quantity'] <= df['Reorder_Level']]

print("\nLOW STOCK MEDICINES")
print(low_stock[['Medicine_Name',
                 'Stock_Quantity',
                 'Reorder_Level']])

overstock = df[df['Stock_Quantity'] > (df['Reorder_Level'] * 3)]

print("\nOVERSTOCK MEDICINES")
print(overstock[['Medicine_Name',
                 'Stock_Quantity',
                 'Reorder_Level']])

high_demand = df[df['Units_Sold'] > df['Stock_Quantity'] * 0.7]

print("\nHIGH DEMAND MEDICINES")
print(high_demand[['Medicine_Name',
                   'Units_Sold',
                   'Stock_Quantity']])

recommendations = []

for index, row in df.iterrows():

    if row['Stock_Quantity'] <= row['Reorder_Level']:

        recommendations.append(
            f"Reorder {row['Medicine_Name']} immediately due to low stock."
        )

    elif row['Units_Sold'] > row['Stock_Quantity'] * 0.7:

        recommendations.append(
            f"Increase stock for {row['Medicine_Name']} due to high demand."
        )

    elif row['Stock_Quantity'] > row['Reorder_Level'] * 3:

        recommendations.append(
            f"Reduce stock for {row['Medicine_Name']} to minimize inventory cost."
        )

print("\nINVENTORY RECOMMENDATIONS")

for rec in recommendations:
    print(rec)

inventory_report = df.groupby('Medicine_Name').agg({
    'Stock_Quantity': 'sum',
    'Units_Sold': 'sum',
    'Price_per_unit': 'mean',
    'Inventory_Value': 'sum'
})

inventory_report.columns = [
    'Total_Stock',
    'Units_Sold',
    'Average_Price',
    'Inventory_Value'
]

print("\nINVENTORY OPTIMIZATION REPORT")
print(inventory_report)

inventory_report.to_csv("inventory_optimization_report.csv")

plt.figure(figsize=(12,6))

low_stock.set_index('Medicine_Name')['Stock_Quantity'].plot(kind='bar')

plt.title("Low Stock Medicines")
plt.xlabel("Medicine Name")
plt.ylabel("Stock Quantity")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))

high_demand.set_index('Medicine_Name')['Units_Sold'].plot(kind='bar')

plt.title("High Demand Medicines")
plt.xlabel("Medicine Name")
plt.ylabel("Units Sold")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,8))

df.groupby('Category')['Inventory_Value'].sum().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Inventory Value by Category")
plt.ylabel("")

plt.show()

print("\nFINAL INSIGHTS")

if not low_stock.empty:
    critical_medicine = low_stock.iloc[0]['Medicine_Name']
    print(f"Immediate Reorder Needed For: {critical_medicine}")

highest_demand = df.groupby('Medicine_Name')['Units_Sold'].sum().idxmax()

print(f"Highest Demand Medicine: {highest_demand}")

highest_inventory = df.groupby('Medicine_Name')['Inventory_Value'].sum().idxmax()

print(f"Highest Inventory Value Medicine: {highest_inventory}")

print("\nMODULE 9 – INVENTORY OPTIMIZATION ENGINE COMPLETED SUCCESSFULLY")

import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATASET
df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# REMOVE DUPLICATES
df.drop_duplicates(inplace=True)

# CREATE NEW COLUMNS
df['Inventory_Value'] = df['Stock_Quantity'] * df['Price_per_unit']

df['Reorder_Status'] = (
    df['Stock_Quantity'] <= df['Reorder_Level']
)

# LOW STOCK MEDICINES
low_stock = df[
    df['Stock_Quantity'] <= df['Reorder_Level']
]

# HIGH DEMAND MEDICINES
high_demand = df[
    df['Units_Sold'] > df['Stock_Quantity'] * 0.7
]


# ==================================================
# LOW STOCK MEDICINES GRAPH
# ==================================================

top_low_stock = low_stock.sort_values(
    by='Stock_Quantity'
).head(10)

plt.figure(figsize=(12,6))

plt.bar(
    top_low_stock['Medicine_Name'],
    top_low_stock['Stock_Quantity']
)

plt.title(
    "Top 10 Low Stock Medicines",
    fontsize=16
)

plt.xlabel(
    "Medicine Name",
    fontsize=12
)

plt.ylabel(
    "Stock Quantity",
    fontsize=12
)

plt.xticks(
    rotation=30,
    ha='right'
)

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.5
)

plt.tight_layout()
plt.show()


# ==================================================
# HIGH DEMAND MEDICINES GRAPH
# ==================================================

top_high_demand = high_demand.sort_values(
    by='Units_Sold',
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

plt.plot(
    top_high_demand['Medicine_Name'],
    top_high_demand['Units_Sold'],
    marker='o',
    linewidth=3
)

plt.title(
    "Top 10 High Demand Medicines",
    fontsize=16
)

plt.xlabel(
    "Medicine Name",
    fontsize=12
)

plt.ylabel(
    "Units Sold",
    fontsize=12
)

plt.xticks(
    rotation=30,
    ha='right'
)

plt.grid(
    linestyle='--',
    alpha=0.5
)

plt.tight_layout()
plt.show()


# ==================================================
# INVENTORY VALUE BY CATEGORY PIE CHART
# ==================================================

plt.figure(figsize=(8,8))

df.groupby('Category')['Inventory_Value'].sum().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title(
    "Inventory Value by Category",
    fontsize=16
)

plt.ylabel("")

plt.tight_layout()
plt.show()"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

df.drop_duplicates(inplace=True)

df['Inventory_Value'] = (
    df['Stock_Quantity'] * df['Price_per_unit']
)

low_stock = df[
    df['Stock_Quantity'] <= df['Reorder_Level']
]

high_demand = df[
    df['Units_Sold'] >= (
        df['Stock_Quantity'] * 0.7
    )
]

low_stock_graph = (
    low_stock.groupby('Medicine_Name')['Stock_Quantity']
    .sum()
    .sort_values()
    .head(10)
)

plt.figure(figsize=(12,6))

bars = plt.bar(
    low_stock_graph.index,
    low_stock_graph.values
)

plt.title(
    "Top 10 Low Stock Medicines",
    fontsize=18
)

plt.xlabel(
    "Medicine Name",
    fontsize=13
)

plt.ylabel(
    "Stock Quantity",
    fontsize=13
)

plt.xticks(
    rotation=25,
    ha='right',
    fontsize=10
)

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.4
)

for bar in bars:
    yval = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 1,
        int(yval),
        ha='center',
        fontsize=9
    )

plt.tight_layout()
plt.show()


high_demand_graph = (
    high_demand.groupby('Medicine_Name')['Units_Sold']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

plt.plot(
    high_demand_graph.index,
    high_demand_graph.values,
    marker='o',
    linewidth=3
)

for x, y in zip(
    high_demand_graph.index,
    high_demand_graph.values
):
    plt.text(
        x,
        y + 1,
        int(y),
        ha='center',
        fontsize=9
    )

plt.title(
    "Top 10 High Demand Medicines",
    fontsize=18
)

plt.xlabel(
    "Medicine Name",
    fontsize=13
)

plt.ylabel(
    "Units Sold",
    fontsize=13
)

plt.xticks(
    rotation=25,
    ha='right',
    fontsize=10
)

plt.grid(
    linestyle='--',
    alpha=0.4
)

plt.tight_layout()
plt.show()


category_value = (
    df.groupby('Category')['Inventory_Value']
    .sum()
)

plt.figure(figsize=(8,8))

plt.pie(
    category_value.values,
    labels=category_value.index,
    autopct='%1.1f%%'
)

plt.title(
    "Inventory Value By Category",
    fontsize=18
)

plt.tight_layout()
plt.show()