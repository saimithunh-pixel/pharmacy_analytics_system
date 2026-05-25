"""import pandas as pd

import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# Current date
current_date = pd.Timestamp.today()

# Convert expiry date column
df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])

# Calculate remaining days
df['days_to_expiry'] = (
    df['Expiry_Date'] - current_date
).dt.days

# Create status category
def expiry_status(days):
    if days < 0:
        return "Expired"
    elif days <= 30:
        return "Critical"
    elif days <= 90:
        return "Warning"
    else:
        return "Safe"

df['Status'] = df['days_to_expiry'].apply(expiry_status)

# Display result
print(df.head())
df.to_csv('expired_medicine_report.csv', index=False)"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

current_date = pd.Timestamp.today()

df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])

df['days_to_expiry'] = (
    df['Expiry_Date'] - current_date
).dt.days

def expiry_status(days):
    if days < 0:
        return "Expired"
    elif days <= 30:
        return "Critical"
    elif days <= 90:
        return "Warning"
    else:
        return "Safe"

df['Status'] = df['days_to_expiry'].apply(expiry_status)

print(df.head())

df.to_csv('expired_medicine_report.csv', index=False)

status_count = df['Status'].value_counts()

plt.figure(figsize=(8,8))

status_count.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Medicine Expiry Status Distribution")
plt.ylabel("")

plt.show()