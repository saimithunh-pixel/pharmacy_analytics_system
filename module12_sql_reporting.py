import streamlit as st
import pandas as pd
import sqlite3


def show():

    st.title("SQL Reporting Module")

    # Load Dataset
    df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

    #st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Create Database Connection
    connection = sqlite3.connect("pharmacy.db")

    # Store Data into SQL Table
    df.to_sql(
        'inventory',
        connection,
        if_exists='replace',
        index=False
    )

    st.success("Database table created successfully!")

    # LOW STOCK REPORT
    query1 = """
    SELECT Medicine_Name, Stock_Quantity
    FROM inventory
    WHERE Stock_Quantity < 50;
    """

    low_stock = pd.read_sql(query1, connection)

    st.subheader("Low Stock Medicines")
    st.dataframe(low_stock)

    # EXPIRY REPORT
    query2 = """
    SELECT Medicine_Name, Expiry_Date
    FROM inventory;
    """

    expiry_report = pd.read_sql(query2, connection)

    st.subheader("Expiry Report")
    st.dataframe(expiry_report)

    # SUPPLIER REPORT
    query3 = """
    SELECT Supplier_Name,
    SUM(Stock_Quantity) AS Total_Stock
    FROM inventory
    GROUP BY Supplier_Name;
    """

    supplier_report = pd.read_sql(query3, connection)

    st.subheader("Supplier Stock Report")
    st.dataframe(supplier_report)

    # SALES REPORT
    query4 = """
    SELECT Medicine_Name,
    SUM(Units_Sold) AS Total_Sales
    FROM inventory
    GROUP BY Medicine_Name
    ORDER BY Total_Sales DESC;
    """

    sales_report = pd.read_sql(query4, connection)

    st.subheader("Medicine Sales Report")
    st.dataframe(sales_report)

    # Close Connection
    connection.close()