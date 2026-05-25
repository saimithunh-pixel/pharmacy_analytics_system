import streamlit as st
from flask import Flask, jsonify
import pandas as pd
from datetime import datetime

# ======================================================
# FLASK APP INITIALIZATION
# ======================================================

app = Flask(__name__)

# ======================================================
# LOAD DATASET
# ======================================================

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# ======================================================
# INVENTORY API
# ======================================================

@app.route('/inventory', methods=['GET'])
def inventory():

    inventory_data = df[[
        'Medicine_Name',
        'Category',
        'Stock_Quantity',
        'Supplier_Name',
        'Storage_Location'
    ]]

    return jsonify(
        inventory_data.to_dict(orient='records')
    )

# ======================================================
# FORECAST API
# ======================================================

@app.route('/forecast', methods=['GET'])
def forecast():

    forecast_data = df[[
        'Medicine_Name',
        'Units_Sold',
        'Reorder_Level'
    ]].copy()

    forecast_data['Predicted_Demand'] = (
        forecast_data['Units_Sold'] * 1.2
    )

    return jsonify(
        forecast_data.to_dict(orient='records')
    )

# ======================================================
# SUPPLIER API
# ======================================================

@app.route('/supplier', methods=['GET'])
def supplier():

    supplier_data = (
        df.groupby('Supplier_Name')[
            'Stock_Quantity'
        ]
        .sum()
        .reset_index()
    )

    return jsonify(
        supplier_data.to_dict(orient='records')
    )

# ======================================================
# EXPIRY ALERT API
# ======================================================

@app.route('/expiry', methods=['GET'])
def expiry():

    temp_df = df.copy()

    temp_df['Expiry_Date'] = pd.to_datetime(
        temp_df['Expiry_Date']
    )

    today = datetime.today()

    expiry_data = temp_df[
        (temp_df['Expiry_Date'] - today).dt.days <= 30
    ]

    expiry_result = expiry_data[[
        'Medicine_Name',
        'Expiry_Date',
        'Stock_Quantity'
    ]]

    return jsonify(
        expiry_result.to_dict(orient='records')
    )

# ======================================================
# STREAMLIT MAIN FUNCTION
# ======================================================

def main():

    st.header("API Development Module")

    st.write("""
    This module provides Flask APIs for:

    - Inventory Data
    - Demand Forecasting
    - Supplier Analytics
    - Expiry Alerts
    """)

    # ======================================================
    # SHOW SAMPLE DATA
    # ======================================================

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # ======================================================
    # AVAILABLE APIs
    # ======================================================

    st.subheader("Available API Endpoints")

    st.code("""
/inventory
/forecast
/supplier
/expiry
""")

    # ======================================================
    # INVENTORY API SAMPLE
    # ======================================================

    st.subheader("Inventory API Sample")

    inventory_data = df[[
        'Medicine_Name',
        'Category',
        'Stock_Quantity'
    ]].head(5)

    st.dataframe(inventory_data)

    # ======================================================
    # FORECAST API SAMPLE
    # ======================================================

    st.subheader("Forecast API Sample")

    forecast_data = df[[
        'Medicine_Name',
        'Units_Sold'
    ]].copy().head(5)

    forecast_data['Predicted_Demand'] = (
        forecast_data['Units_Sold'] * 1.2
    )

    st.dataframe(forecast_data)

    # ======================================================
    # SUPPLIER API SAMPLE
    # ======================================================

    st.subheader("Supplier API Sample")

    supplier_data = (
        df.groupby('Supplier_Name')[
            'Stock_Quantity'
        ]
        .sum()
        .reset_index()
        .head(5)
    )

    st.dataframe(supplier_data)

    # ======================================================
    # EXPIRY API SAMPLE
    # ======================================================

    st.subheader("Expiry Alert API Sample")

    temp_df = df.copy()

    temp_df['Expiry_Date'] = pd.to_datetime(
        temp_df['Expiry_Date']
    )

    today = datetime.today()

    expiry_data = temp_df[
        (temp_df['Expiry_Date'] - today).dt.days <= 30
    ]

    expiry_result = expiry_data[[
        'Medicine_Name',
        'Expiry_Date',
        'Stock_Quantity'
    ]].head(5)

    st.dataframe(expiry_result)

    # ======================================================
    # FINAL MESSAGE
    # ======================================================

    st.success(
        "API Development Module Loaded Successfully"
    )

# ======================================================
# RUN FLASK SERVER
# ======================================================

if __name__ == '__main__':

    main()

    # OPTIONAL:
    # Uncomment below line ONLY if running Flask separately

    # app.run(debug=False, use_reloader=False, port=5000)
