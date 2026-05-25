import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

print(df.head())

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

medicine_prescriptions = df.groupby('Medicine_Name')['Units_Sold'].sum()

print("\nMOST PRESCRIBED MEDICINES")
print(medicine_prescriptions.sort_values(ascending=False))

category_prescriptions = df.groupby('Category')['Units_Sold'].sum()

print("\nCATEGORY WISE PRESCRIPTIONS")
print(category_prescriptions)

prescription_required = df.groupby('Prescription_Required')['Units_Sold'].sum()

print("\nPRESCRIPTION REQUIRED ANALYSIS")
print(prescription_required)

top_medicines = medicine_prescriptions.sort_values(ascending=False).head(10)

print("\nTOP 10 MEDICINES")
print(top_medicines)

monthly_trend = df.groupby('Purchase_Date')['Units_Sold'].sum()

print("\nPURCHASE DATE TREND")
print(monthly_trend)

prescription_report = df.groupby('Medicine_Name').agg({
    'Units_Sold': 'sum',
    'Stock_Quantity': 'sum',
    'Price_per_unit': 'mean'
})

prescription_report.columns = [
    'Total_Prescriptions',
    'Available_Stock',
    'Average_Price'
]

print("\nPRESCRIPTION REPORT")
print(prescription_report)

prescription_report.to_csv("prescription_trend_report.csv")

plt.figure(figsize=(12,6))

top_medicines.plot(kind='bar')

plt.title("Top 10 Prescribed Medicines")
plt.xlabel("Medicine Name")
plt.ylabel("Units Sold")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,8))

category_prescriptions.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Category Wise Prescription Share")
plt.ylabel("")

plt.show()

plt.figure(figsize=(12,6))

monthly_trend.plot()

plt.title("Prescription Trend Over Time")
plt.xlabel("Purchase Date")
plt.ylabel("Units Sold")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))

prescription_required.plot(kind='bar')

plt.title("Prescription Required vs Non-Prescription Medicines")
plt.xlabel("Prescription Required")
plt.ylabel("Units Sold")

plt.tight_layout()
plt.show()

print("\nFINAL INSIGHTS")

most_prescribed = medicine_prescriptions.idxmax()

print(f"Most Prescribed Medicine: {most_prescribed}")

highest_category = category_prescriptions.idxmax()

print(f"Highest Prescription Category: {highest_category}")

print("\nMODULE 8 – PRESCRIPTION TREND ANALYSIS COMPLETED SUCCESSFULLY")

