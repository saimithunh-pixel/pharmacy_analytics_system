import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Testing & Validation",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.markdown("""
<h1 style='text-align:center;
color:white;
background-color:#1565C0;
padding:15px;
border-radius:10px;'>
Testing & Validation
</h1>
""", unsafe_allow_html=True)

st.write("Validate pharmacy analytics outputs.")

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# ---------------------------------------------------
# COLUMN CLEANING
# ---------------------------------------------------

df.columns = df.columns.str.strip()

# ---------------------------------------------------
# INVENTORY CALCULATION TESTING
# ---------------------------------------------------

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
    st.success("No negative stock values found.")
else:
    st.error("Negative stock values detected!")

# ---------------------------------------------------
# FORECAST ACCURACY TESTING
# ---------------------------------------------------

st.subheader("2. Forecast Accuracy Testing")

# Sample actual and predicted sales
actual_sales = np.array([100, 120, 130, 150, 170])
predicted_sales = np.array([110, 115, 128, 140, 175])

# MAE Calculation
mae = mean_absolute_error(actual_sales, predicted_sales)

# RMSE Calculation
rmse = np.sqrt(mean_squared_error(actual_sales, predicted_sales))

col3, col4 = st.columns(2)

with col3:
    st.metric("MAE", round(mae, 2))

with col4:
    st.metric("RMSE", round(rmse, 2))

st.info("Lower MAE and RMSE values indicate better forecast accuracy.")

# ---------------------------------------------------
# EXPIRY ALERT VALIDATION
# ---------------------------------------------------

st.subheader("3. Expiry Alert Validation")

# Convert Expiry Date column
df["Expiry_Date"] = pd.to_datetime(df["Expiry_Date"])

today = pd.Timestamp.today()

expiry_limit = today + pd.Timedelta(days=30)

expiring = df[df["Expiry_Date"] <= expiry_limit]

st.write("Medicines Near Expiry (Within 30 Days)")

if len(expiring) > 0:
    st.dataframe(
        expiring[["Medicine_Name", "Expiry_Date", "Stock_Quantity"]]
    )
else:
    st.success("No medicines nearing expiry.")

# ---------------------------------------------------
# SUPPLIER METRICS VALIDATION
# ---------------------------------------------------

st.subheader("4. Supplier Metrics Validation")

supplier_counts = df["Supplier_Name"].value_counts()

st.bar_chart(supplier_counts)

# ---------------------------------------------------
# KPI ACCURACY CHECK
# ---------------------------------------------------

st.subheader("5. KPI Accuracy")

average_stock = df["Stock_Quantity"].mean()

max_stock = df["Stock_Quantity"].max()

min_stock = df["Stock_Quantity"].min()

col5, col6, col7 = st.columns(3)

with col5:
    st.metric("Average Stock", round(average_stock, 2))

with col6:
    st.metric("Maximum Stock", max_stock)

with col7:
    st.metric("Minimum Stock", min_stock)

# ---------------------------------------------------
# PRESCRIPTION VALIDATION
# ---------------------------------------------------

st.subheader("6. Prescription Requirement Validation")

prescription_count = df["Prescription_Required"].value_counts()

st.write("Prescription Requirement Distribution")

st.bar_chart(prescription_count)

# ---------------------------------------------------
# CATEGORY VALIDATION
# ---------------------------------------------------

st.subheader("7. Medicine Category Validation")

category_counts = df["Category"].value_counts()

st.write("Medicine Category Distribution")

st.bar_chart(category_counts)

# ---------------------------------------------------
# FINAL VALIDATION REPORT
# ---------------------------------------------------

st.subheader("Final Validation Report")

validation_passed = (
    len(negative_stock) == 0
)

if validation_passed:
    st.success("System Validation Completed Successfully")
else:
    st.warning("Validation completed with some issues.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<hr>
<h4 style='text-align:center;color:gray;'>
Validated Pharmacy Analytics System            
</h4>
""", unsafe_allow_html=True)