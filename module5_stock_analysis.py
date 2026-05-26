"""import pandas as pd          #import libraries     
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
fast_moving.to_csv("fast_moving_report.csv", index=False)"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================================================
# MAIN FUNCTION
# ======================================================

def main():

    st.header("Medicine Stock Analysis")

    # LOAD DATASET
    df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

    # SHOW DATA
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # CHECK COLUMN NAMES
    st.subheader("Column Names")
    st.write(df.columns)

    # ======================================================
    # ANALYSIS
    # ======================================================

    low_stock = df[df['Stock_Quantity'] < 20]

    overstock = df[df['Stock_Quantity'] > 150]

    fast_moving = df.sort_values(
        by='Stock_Quantity',
        ascending=False
    ).head(10)

    # ======================================================
    # METRICS
    # ======================================================

    col1, col2, col3 = st.columns(3)

    col1.metric("Low Stock Medicines", len(low_stock))

    col2.metric("Overstock Items", len(overstock))

    col3.metric("Fast Moving Medicines", len(fast_moving))

    # ======================================================
    # SAVE REPORTS
    # ======================================================

    low_stock.to_csv("low_stock_report.csv", index=False)

    overstock.to_csv("overstock_report.csv", index=False)

    fast_moving.to_csv("fast_moving_report.csv", index=False)

    # ======================================================
    # LOW STOCK TABLE
    # ======================================================

    st.subheader("Low Stock Medicines")

    st.dataframe(low_stock)

    # ======================================================
    # OVERSTOCK TABLE
    # ======================================================

    st.subheader("Overstock Medicines")

    st.dataframe(overstock)

    # ======================================================
    # FAST MOVING TABLE
    # ======================================================

    st.subheader("Top 10 Fast Moving Medicines")

    st.dataframe(fast_moving)

    # ======================================================
    # GRAPH
    # ======================================================

    st.subheader("Fast Moving Medicine Graph")

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        fast_moving['Medicine_Name'],
        fast_moving['Stock_Quantity']
    )

    plt.xticks(rotation=45)

    plt.xlabel("Medicine Name")

    plt.ylabel("Stock Quantity")

    plt.title("Top 10 Fast Moving Medicines")

    st.pyplot(fig)