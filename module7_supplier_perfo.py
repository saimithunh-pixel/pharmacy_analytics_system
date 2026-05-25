import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

print(df.head())

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df['Total_Value'] = df['Stock_Quantity'] * df['Price_per_unit']

supplier_medicine_count = df.groupby('Supplier_Name')['Medicine_Name'].count()

print("\nSUPPLIER MEDICINE COUNT")
print(supplier_medicine_count)

supplier_stock = df.groupby('Supplier_Name')['Stock_Quantity'].sum()

print("\nSUPPLIER STOCK QUANTITY")
print(supplier_stock)

supplier_sales = df.groupby('Supplier_Name')['Units_Sold'].sum()

print("\nSUPPLIER SALES PERFORMANCE")
print(supplier_sales)

supplier_value = df.groupby('Supplier_Name')['Total_Value'].sum()

print("\nSUPPLIER INVENTORY VALUE")
print(supplier_value)

avg_price = df.groupby('Supplier_Name')['Price_per_unit'].mean()

print("\nAVERAGE PRICE PER SUPPLIER")
print(avg_price)

supplier_efficiency = (
    df.groupby('Supplier_Name')['Units_Sold'].sum()
    /
    df.groupby('Supplier_Name')['Stock_Quantity'].sum()
)

print("\nSUPPLIER EFFICIENCY SCORE")
print(supplier_efficiency)

low_stock = df[df['Stock_Quantity'] <= df['Reorder_Level']]

print("\nLOW STOCK MEDICINES")
print(low_stock[['Medicine_Name',
                 'Supplier_Name',
                 'Stock_Quantity',
                 'Reorder_Level']])

supplier_report = df.groupby('Supplier_Name').agg({
    'Medicine_Name': 'count',
    'Stock_Quantity': 'sum',
    'Units_Sold': 'sum',
    'Price_per_unit': 'mean',
    'Total_Value': 'sum'
})

supplier_report.columns = [
    'Medicine_Count',
    'Total_Stock',
    'Units_Sold',
    'Average_Price',
    'Inventory_Value'
]

print("\nCOMPLETE SUPPLIER REPORT")
print(supplier_report)

supplier_report.to_csv("supplier_performance_report.csv")

plt.figure(figsize=(10,6))

supplier_stock.plot(kind='bar')

plt.title("Supplier Stock Contribution")
plt.xlabel("Supplier Name")
plt.ylabel("Stock Quantity")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))

supplier_sales.plot(kind='bar')

plt.title("Supplier Sales Performance")
plt.xlabel("Supplier Name")
plt.ylabel("Units Sold")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,8))

supplier_value.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Supplier Inventory Value Share")
plt.ylabel("")

plt.show()

plt.figure(figsize=(10,6))

supplier_efficiency.plot(kind='bar')

plt.title("Supplier Efficiency Score")
plt.xlabel("Supplier Name")
plt.ylabel("Efficiency Score")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print("\nFINAL INSIGHTS")

best_sales_supplier = supplier_sales.idxmax()

print(f"Best Supplier by Sales: {best_sales_supplier}")

highest_stock_supplier = supplier_stock.idxmax()

print(f"Highest Stock Supplier: {highest_stock_supplier}")

expensive_supplier = avg_price.idxmax()

print(f"Most Expensive Supplier: {expensive_supplier}")

best_efficiency_supplier = supplier_efficiency.idxmax()

print(f"Best Efficiency Supplier: {best_efficiency_supplier}")

print("\nMODULE 7 – SUPPLIER PERFORMANCE ANALYTICS COMPLETED SUCCESSFULLY")
df.to_csv('supplier_performance_data.csv', index=False)