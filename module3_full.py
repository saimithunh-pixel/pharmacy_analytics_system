import pandas as pd

# Load your dataset
df = pd.read_csv("data1/pharmacy_data_row4.csv")

print("Module 3 Deliverable: Pharmacy operational dataset")

# Instruct pandas to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Print the full DataFrame
print(df)

print(f"Total records: {len(df)}")