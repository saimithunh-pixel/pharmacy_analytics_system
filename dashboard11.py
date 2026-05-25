import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# 1. Page Configuration
st.set_page_config(
    page_title="Pharmacy Analytics Dashboard",
    layout="wide"
)

# 2. Load Data
df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# 3. Main Dashboard Banner
st.markdown("""
<h1 style='text-align:center;
color:white;
background-color:#1565C0;
padding:15px;
border-radius:12px;'>
Pharmacy Analytics Dashboard
</h1>
""", unsafe_allow_html=True)

# 4. Sidebar Filters
st.sidebar.header("Filters")

category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].dropna().unique(),
    default=df['Category'].dropna().unique()
)

filtered_df = df[df['Category'].isin(category)]

# 5. Business KPI Calculations
total_medicines = filtered_df['Medicine_Name'].nunique()
total_stock = filtered_df['Stock_Quantity'].sum()
total_suppliers = filtered_df['Supplier_Name'].nunique()
total_sales = filtered_df['Units_Sold'].sum()

if total_stock >= 100000:
    total_stock_display = f"{total_stock/100000:.1f}L"
else:
    total_stock_display = f"{total_stock/1000:.1f}K"

if total_sales >= 100000:
    total_sales_display = f"{total_sales/100000:.1f}L"
else:
    total_sales_display = f"{total_sales/1000:.1f}K"

# 6. Data Aggregations for Charts
low_stock = filtered_df[
    filtered_df['Stock_Quantity']
    <= filtered_df['Reorder_Level']
]

selected_medicines = [
    "Ibuprofen",
    "Amoxicillin",
    "Cetirizine",
    "Azithromycin",
    "Paracetamol",
    "Metformin"
]

low_stock_top = (
    low_stock[
        low_stock['Medicine_Name']
        .isin(selected_medicines)
    ]
    .groupby('Medicine_Name')['Stock_Quantity']
    .sum()
)

top_medicines = (
    filtered_df.groupby('Medicine_Name')['Units_Sold']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

category_stock = (
    filtered_df.groupby('Category')['Stock_Quantity']
    .sum()
)

supplier_data = (
    filtered_df.groupby('Supplier_Name')['Stock_Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# 7. Render KPI Cards Row (Fixed Layout & Formatted Code)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 2px 2px 10px #D3D3D3;
        height: 160px;
    ">
        <div style="font-size: 20px; font-weight: bold; color: #1565C0; line-height: 1.2;">Total Medicines</div>
        <div style="font-size: 38px; font-weight: bold; color: #333; margin-top: 15px;">{total_medicines}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 2px 2px 10px #D3D3D3;
        height: 160px;
    ">
        <div style="font-size: 20px; font-weight: bold; color: #1565C0; line-height: 1.2;">Total Stock</div>
        <div style="font-size: 38px; font-weight: bold; color: #333; margin-top: 15px;">{total_stock_display}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 2px 2px 10px #D3D3D3;
        height: 160px;
    ">
        <div style="font-size: 20px; font-weight: bold; color: #1565C0; line-height: 1.2;">Total Suppliers</div>
        <div style="font-size: 38px; font-weight: bold; color: #333; margin-top: 15px;">{total_suppliers}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 2px 2px 10px #D3D3D3;
        height: 160px;
    ">
        <div style="font-size: 20px; font-weight: bold; color: #1565C0; line-height: 1.2;">Units Sold</div>
        <div style="font-size: 38px; font-weight: bold; color: #333; margin-top: 15px;">{total_sales_display}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# 8. Render Visualizations Row 1
col5, col6 = st.columns(2)

with col5:
    st.subheader("Top Selling Medicines")
    fig1, ax1 = plt.subplots(figsize=(6,4))
    top_medicines.plot(kind='bar', ax=ax1)
    ax1.set_xlabel("Medicine")
    ax1.set_ylabel("Units Sold")
    plt.xticks(rotation=20)
    st.pyplot(fig1)

with col6:
    st.subheader("Low Stock Medicines")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    labels = [
        f"{name}\n{value/1000:.0f}K"
        for name, value in zip(low_stock_top.index, low_stock_top.values)
    ]
    squarify.plot(
        sizes=low_stock_top.values,
        label=labels,
        color=["#FF9999", "#66B3FF", "#00CC66", "#FFCC99", "#C2C2F0", "#FFD700"],
        alpha=0.8,
        text_kwargs={'fontsize':10},
        ax=ax2
    )
    ax2.axis('off')
    st.pyplot(fig2)

st.write("")

# 9. Render Visualizations Row 2
col7, col8 = st.columns(2)

with col7:
    st.subheader("Stock Distribution By Category")
    fig3, ax3 = plt.subplots(figsize=(5,5))
    category_stock.plot(kind='pie', autopct='%1.1f%%', ax=ax3)
    ax3.set_ylabel("")
    st.pyplot(fig3)

with col8:
    st.subheader("Supplier Contribution")
    fig4, ax4 = plt.subplots(figsize=(6,4))
    supplier_data.plot(kind='line', marker='o', linewidth=3, ax=ax4)
    ax4.set_xlabel("Supplier")
    ax4.set_ylabel("Stock Quantity")
    plt.xticks(rotation=20)
    st.pyplot(fig4)

st.write("")

# 10. Dashboard Insights Section
st.subheader("Final Insights")
highest_selling = top_medicines.idxmax()
st.success(f"Highest Selling Medicine: {highest_selling}")

if not low_stock.empty:
    critical_med = low_stock_top.idxmin()
    st.warning(f"Immediate Reorder Needed For: {critical_med}")

st.info("Dashboard Generated Successfully")