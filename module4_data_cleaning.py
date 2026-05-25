import pandas as pd       #import pandas
df = pd.read_csv("data1/pharmacy_data_row4.csv")        #load csv dataset
print(df.head())
print(df.info())           #check dataset info
print(df.isnull().sum())
df.drop_duplicates(inplace=True)     #remove duplicates(repeated rows)
print("Duplicates removed")
df["Medicine_Name"] = df["Medicine_Name"].str.title()   #standardize medicine names(PAR to par)
df["Supplier_Name"] = df["Supplier_Name"].str.title()             #standardize supplier names
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"], errors='coerce')  #converts txt date into real date format
df["Stock_Quantity"] = df["Stock_Quantity"].fillna(0)   #fill missing values
df["Supplier_Name"] = df["Supplier_Name"].fillna("Unknown")     #fill missing supplier
print(df.info())       #check cleaned data again
print(df.head())        #confirms cleaning worked
df.to_csv("data1/cleaned_pharmacy_data.csv",index=False)
print("Module 4 data cleaning completed successfully")
#print(df.head())
print(f"Total records: {len(df)}")

