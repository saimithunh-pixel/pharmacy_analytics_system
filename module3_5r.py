import pandas as pd 
df = pd.read_csv('data1/pharmacy_data_rows3.csv')
print("Module 3 Deliverable: Pharmacy operational dataset")
print(df.head())
print(f"Total records: {len(df)}")