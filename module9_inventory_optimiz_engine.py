import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================================================
# MAIN FUNCTION
# ======================================================

def main():

    st.header("Inventory Optimization")

    # ======================================================
    # LOAD DATA
    # ======================================================

    df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

    # ======================================================
    # DATA CLEANING
    # ======================================================

    df.drop_duplicates(inplace=True)

    # ======================================================
    # INVENTORY VALUE
    # ======================================================

    df['Inventory_Value'] = (
        df['Stock_Quantity'] * df['Price_per_unit']
    )

    # ======================================================
    # LOW STOCK ANALYSIS
    # ======================================================

    low_stock = df[
        df['Stock_Quantity'] <= df['Reorder_Level']
    ]

    # ======================================================
    # HIGH DEMAND ANALYSIS
    # ======================================================

    high_demand = df[
        df['Units_Sold'] >= (
            df['Stock_Quantity'] * 0.7
        )
    ]

    # ======================================================
    # LOW STOCK GRAPH
    # ======================================================

    st.subheader("Top 10 Low Stock Medicines")

    low_stock_graph = (
        low_stock.groupby('Medicine_Name')['Stock_Quantity']
        .sum()
        .sort_values()
        .head(10)
    )

    fig1, ax1 = plt.subplots(figsize=(12,6))

    bars = ax1.bar(
        low_stock_graph.index,
        low_stock_graph.values
    )

    ax1.set_title(
        "Top 10 Low Stock Medicines",
        fontsize=18
    )

    ax1.set_xlabel(
        "Medicine Name",
        fontsize=13
    )

    ax1.set_ylabel(
        "Stock Quantity",
        fontsize=13
    )

    plt.xticks(
        rotation=25,
        ha='right',
        fontsize=10
    )

    ax1.grid(
        axis='y',
        linestyle='--',
        alpha=0.4
    )

    for bar in bars:

        yval = bar.get_height()

        ax1.text(
            bar.get_x() + bar.get_width()/2,
            yval + 1,
            int(yval),
            ha='center',
            fontsize=9
        )

    st.pyplot(fig1)

    # ======================================================
    # HIGH DEMAND GRAPH
    # ======================================================

    st.subheader("Top 10 High Demand Medicines")

    high_demand_graph = (
        high_demand.groupby('Medicine_Name')['Units_Sold']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig2, ax2 = plt.subplots(figsize=(12,6))

    ax2.plot(
        high_demand_graph.index,
        high_demand_graph.values,
        marker='o',
        linewidth=3
    )

    for x, y in zip(
        high_demand_graph.index,
        high_demand_graph.values
    ):

        ax2.text(
            x,
            y + 1,
            int(y),
            ha='center',
            fontsize=9
        )

    ax2.set_title(
        "Top 10 High Demand Medicines",
        fontsize=18
    )

    ax2.set_xlabel(
        "Medicine Name",
        fontsize=13
    )

    ax2.set_ylabel(
        "Units Sold",
        fontsize=13
    )

    plt.xticks(
        rotation=25,
        ha='right',
        fontsize=10
    )

    ax2.grid(
        linestyle='--',
        alpha=0.4
    )

    st.pyplot(fig2)

    # ======================================================
    # INVENTORY VALUE PIE CHART
    # ======================================================

    st.subheader("Inventory Value By Category")

    category_value = (
        df.groupby('Category')['Inventory_Value']
        .sum()
    )

    fig3, ax3 = plt.subplots(figsize=(8,8))

    ax3.pie(
        category_value.values,
        labels=category_value.index,
        autopct='%1.1f%%'
    )

    ax3.set_title(
        "Inventory Value By Category",
        fontsize=18
    )

    st.pyplot(fig3)
