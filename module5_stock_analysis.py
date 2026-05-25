import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def main():
    st.header("Medicine Stock Analysis")
    
    # Load cleaned dataset
    try:
        df = pd.read_csv("data1/cleaned_pharmacy_data.csv")
    except FileNotFoundError:
        st.error("Data file not found. Please ensure 'data1/cleaned_pharmacy_data.csv' exists.")
        return

    # Low stock detection
    low_stock = df[df['Stock_Quantity'] < 20]
    
    # Overstock analysis
    overstock = df[df['Stock_Quantity'] > 150]
    
    # Fast moving medicines
    fast_moving = df.sort_values(by='Stock_Quantity', ascending=False).head(10)
    
    # Display metrics in Streamlit instead of terminal print statements
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Low Stock Items Count", value=len(low_stock))
    with col2:
        st.metric(label="Overstock Items Count", value=len(overstock))
        
    st.subheader("Fast Moving Medicines (Top 10)")
    st.dataframe(fast_moving)

    # Save reports to CSV files
    low_stock.to_csv("low_stock_report.csv", index=False)
    overstock.to_csv("overstock_report.csv", index=False)
    fast_moving.to_csv("fast_moving_report.csv", index=False)
