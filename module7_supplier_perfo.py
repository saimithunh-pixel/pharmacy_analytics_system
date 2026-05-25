import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================================================
# MAIN FUNCTION
# ======================================================

def main():

    st.header("Supplier Performance Analytics")

    # ======================================================
    # LOAD DATA
    # ======================================================

    df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

    # ======================================================
    # DATA PREVIEW
    # ======================================================

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # ======================================================
    # MISSING VALUES
    # ======================================================

    st.subheader("Missing Values")

    st.write(df.isnull().sum())

    # ======================================================
    # REMOVE DUPLICATES
    # ======================================================

    df.drop_duplicates(inplace=True)

    # ======================================================
    # TOTAL VALUE
    # ======================================================

    df['Total_Value'] = (
        df['Stock_Quantity'] * df['Price_per_unit']
    )

    # ======================================================
    # SUPPLIER MEDICINE COUNT
    # ======================================================

    supplier_medicine_count = (
        df.groupby('Supplier_Name')['Medicine_Name']
        .count()
    )

    st.subheader("Supplier Medicine Count")

    st.dataframe(supplier_medicine_count)

    # ======================================================
    # SUPPLIER STOCK
    # ======================================================

    supplier_stock = (
        df.groupby('Supplier_Name')['Stock_Quantity']
        .sum()
    )

    st.subheader("Supplier Stock Quantity")

    st.dataframe(supplier_stock)

    # ======================================================
    # SUPPLIER SALES
    # ======================================================

    supplier_sales = (
        df.groupby('Supplier_Name')['Units_Sold']
        .sum()
    )

    st.subheader("Supplier Sales Performance")

    st.dataframe(supplier_sales)

    # ======================================================
    # SUPPLIER INVENTORY VALUE
    # ======================================================

    supplier_value = (
        df.groupby('Supplier_Name')['Total_Value']
        .sum()
    )

    st.subheader("Supplier Inventory Value")

    st.dataframe(supplier_value)

    # ======================================================
    # AVERAGE PRICE
    # ======================================================

    avg_price = (
        df.groupby('Supplier_Name')['Price_per_unit']
        .mean()
    )

    st.subheader("Average Price Per Supplier")

    st.dataframe(avg_price)

    # ======================================================
    # SUPPLIER EFFICIENCY
    # ======================================================

    supplier_efficiency = (
        df.groupby('Supplier_Name')['Units_Sold'].sum()
        /
        df.groupby('Supplier_Name')['Stock_Quantity'].sum()
    )

    st.subheader("Supplier Efficiency Score")

    st.dataframe(supplier_efficiency)

    # ======================================================
    # LOW STOCK MEDICINES
    # ======================================================

    low_stock = df[
        df['Stock_Quantity'] <= df['Reorder_Level']
    ]

    st.subheader("Low Stock Medicines")

    st.dataframe(
        low_stock[
            [
                'Medicine_Name',
                'Supplier_Name',
                'Stock_Quantity',
                'Reorder_Level'
            ]
        ]
    )

    # ======================================================
    # COMPLETE SUPPLIER REPORT
    # ======================================================

    supplier_report = df.groupby('Supplier_Name').agg({
        'Medicine_Name': 'count',
        'Stock_Quantity': 'sum',
        'Units_Sold': 'sum',
        'Price_per_unit': 'mean',
        'Total_Value': 'sum'
    })

    supplier_report.columns = [
        'Medicine_Count',
        'Total_Stock',
        'Units_Sold',
        'Average_Price',
        'Inventory_Value'
    ]

    st.subheader("Complete Supplier Report")

    st.dataframe(supplier_report)

    # SAVE REPORT
    supplier_report.to_csv(
        "supplier_performance_report.csv"
    )

    # ======================================================
    # GRAPH 1
    # ======================================================

    st.subheader("Supplier Stock Contribution")

    fig1, ax1 = plt.subplots(figsize=(10,6))

    supplier_stock.plot(
        kind='bar',
        ax=ax1
    )

    ax1.set_title("Supplier Stock Contribution")

    ax1.set_xlabel("Supplier Name")

    ax1.set_ylabel("Stock Quantity")

    plt.xticks(rotation=45)

    st.pyplot(fig1)

    # ======================================================
    # GRAPH 2
    # ======================================================

    st.subheader("Supplier Sales Performance")

    fig2, ax2 = plt.subplots(figsize=(10,6))

    supplier_sales.plot(
        kind='bar',
        ax=ax2
    )

    ax2.set_title("Supplier Sales Performance")

    ax2.set_xlabel("Supplier Name")

    ax2.set_ylabel("Units Sold")

    plt.xticks(rotation=45)

    st.pyplot(fig2)

    # ======================================================
    # GRAPH 3
    # ======================================================

    st.subheader("Supplier Inventory Value Share")

    fig3, ax3 = plt.subplots(figsize=(8,8))

    supplier_value.plot(
        kind='pie',
        autopct='%1.1f%%',
        ax=ax3
    )

    ax3.set_title("Supplier Inventory Value Share")

    ax3.set_ylabel("")

    st.pyplot(fig3)

    # ======================================================
    # GRAPH 4
    # ======================================================

    st.subheader("Supplier Efficiency Score")

    fig4, ax4 = plt.subplots(figsize=(10,6))

    supplier_efficiency.plot(
        kind='bar',
        ax=ax4
    )

    ax4.set_title("Supplier Efficiency Score")

    ax4.set_xlabel("Supplier Name")

    ax4.set_ylabel("Efficiency Score")

    plt.xticks(rotation=45)

    st.pyplot(fig4)

    # ======================================================
    # FINAL INSIGHTS
    # ======================================================

    st.subheader("Final Insights")

    best_sales_supplier = supplier_sales.idxmax()

    st.success(
        f"Best Supplier by Sales: {best_sales_supplier}"
    )

    highest_stock_supplier = supplier_stock.idxmax()

    st.info(
        f"Highest Stock Supplier: {highest_stock_supplier}"
    )

    expensive_supplier = avg_price.idxmax()

    st.warning(
        f"Most Expensive Supplier: {expensive_supplier}"
    )

    best_efficiency_supplier = supplier_efficiency.idxmax()

    st.success(
        f"Best Efficiency Supplier: {best_efficiency_supplier}"
    )

    st.success(
        "MODULE 7 – SUPPLIER PERFORMANCE ANALYTICS COMPLETED SUCCESSFULLY"
    )

    # SAVE FINAL DATA
    df.to_csv(
        'supplier_performance_data.csv',
        index=False
    )
