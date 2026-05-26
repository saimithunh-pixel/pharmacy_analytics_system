import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def load_data():
    try:
        df = pd.read_csv("data1/cleaned_pharmacy_data.csv")
        df.columns = df.columns.str.strip()
        return df
    except FileNotFoundError:
        st.error("❌ Data file not found. Please check the path: data1/cleaned_pharmacy_data.csv")
        return None

def inventory_validation(df):
    st.subheader("1. Inventory Calculation Testing")
    total_stock = df["Stock_Quantity"].sum()
    col1, col2 = st.columns(2)
    with col1:
        stock_lakh = total_stock / 100000
        st.metric("Total Inventory Stock", f"{stock_lakh:.1f}L")

    negative_stock = df[df["Stock_Quantity"] < 0]
    with col2:
        st.metric("Negative Stock Records", len(negative_stock))

    if len(negative_stock) == 0:
        st.success("✅ No negative stock values found.")
    else:
        st.error("⚠️ Negative stock values detected!")

    return negative_stock

def forecast_validation():
    st.subheader("2. Forecast Accuracy Testing")
    actual_sales = np.array([100, 120, 130, 150, 170])
    predicted_sales = np.array([110, 115, 128, 140, 175])

    mae = mean_absolute_error(actual_sales, predicted_sales)
    rmse = np.sqrt(mean_squared_error(actual_sales, predicted_sales))
    mape = np.mean(np.abs((actual_sales - predicted_sales) / actual_sales)) * 100

    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric("MAE", round(mae, 2))
    with col4:
        st.metric("RMSE", round(rmse, 2))
    with col5:
        st.metric("MAPE (%)", round(mape, 2))

def expiry_validation(df):
    st.subheader("3. Expiry Alert Validation")
    df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"], errors="coerce")
    today = pd.Timestamp.today()
    expiry_limit = today + pd.Timedelta(days=30)
    expiring = df[df["Expiry_Date"] <= expiry_limit]

    if len(expiring) > 0:
        st.dataframe(expiring[["Medicine_Name", "Expiry_Date", "Stock_Quantity"]])
    else:
        st.success("✅ No medicines nearing expiry.")

def supplier_validation(df):
    st.subheader("4. Supplier Metrics Validation")
    st.bar_chart(df["Supplier_Name"].value_counts())

def kpi_validation(df):
    st.subheader("5. KPI Accuracy")
    col6, col7, col8 = st.columns(3)
    with col6:
        st.metric("Average Stock", round(df["Stock_Quantity"].mean(), 2))
    with col7:
        st.metric("Maximum Stock", df["Stock_Quantity"].max())
    with col8:
        st.metric("Minimum Stock", df["Stock_Quantity"].min())

def prescription_validation(df):
    st.subheader("6. Prescription Requirement Validation")
    st.bar_chart(df["Prescription_Required"].value_counts())

def category_validation(df):
    st.subheader("7. Medicine Category Validation")
    st.bar_chart(df["Category"].value_counts())

def final_report(negative_stock):
    st.subheader("Final Validation Report")
    if len(negative_stock) == 0:
        st.success("🎉 System Validation Completed Successfully")
    else:
        st.warning("Validation completed with some issues.")

def main():
    st.markdown("""
    <h1 style='text-align:center;color:white;background-color:#1565C0;padding:15px;border-radius:10px;'>
    Testing & Validation
    </h1>
    """, unsafe_allow_html=True)

    st.write("Validate pharmacy analytics outputs.")

    df = load_data()
    if df is None:
        return

    negative_stock = inventory_validation(df)
    forecast_validation()
    expiry_validation(df)
    supplier_validation(df)
    kpi_validation(df)
    prescription_validation(df)
    category_validation(df)
    final_report(negative_stock)

if __name__ == '__main__':
    main()
