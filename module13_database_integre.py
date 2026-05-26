import streamlit as st
import pandas as pd
import sqlite3


def show():

    st.title("Database Integration Module")

    # Load Dataset
    df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

    # Create Database Connection
    connection = sqlite3.connect("pharmacy_database.db")

    # INVENTORY TABLE
    inventory_table = df[[
        'Medicine_Name',
        'Category',
        'Stock_Quantity',
        'Price_per_unit',
        'Reorder_Level',
        'Storage_Location'
    ]]

    inventory_table.to_sql(
        'Inventory',
        connection,
        if_exists='replace',
        index=False
    )

    # PRESCRIPTION TABLE
    prescription_table = df[[
        'Medicine_Name',
        'Prescription_Required',
        'Units_Sold'
    ]]

    prescription_table.to_sql(
        'Prescriptions',
        connection,
        if_exists='replace',
        index=False
    )

    # SUPPLIER TABLE
    supplier_table = df[[
        'Supplier_Name',
        'Medicine_Name',
        'Stock_Quantity',
        'Price_per_unit'
    ]]

    supplier_table.to_sql(
        'Supplier_Records',
        connection,
        if_exists='replace',
        index=False
    )

    # EXPIRY TABLE
    expiry_table = df[[
        'Medicine_Name',
        'Expiry_Date'
    ]]

    expiry_table.to_sql(
        'Expiry_Logs',
        connection,
        if_exists='replace',
        index=False
    )

    st.success("All database tables created successfully!")

    # SHOW INVENTORY TABLE
    query1 = "SELECT * FROM Inventory"

    inventory_data = pd.read_sql(query1, connection)

    st.subheader("Inventory Table")
    st.dataframe(inventory_data.head())

    # SHOW SUPPLIER RECORDS
    query2 = "SELECT * FROM Supplier_Records"

    supplier_data = pd.read_sql(query2, connection)

    st.subheader("Supplier Records Table")
    st.dataframe(supplier_data.head())

    connection.close()