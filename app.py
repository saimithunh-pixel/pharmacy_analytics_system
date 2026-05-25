import streamlit as st

st.set_page_config(
    page_title="Pharmacy Analytics System",
    layout="wide"
)

st.title("Pharmacy Analytics System")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "KPI Dashboard",
        "Medicine Stock Analysis",
        "Expiry Monitoring",
        "Supplier Analytics",
        "Prescription Trends",
        "Inventory Optimization",
        "Demand Forecasting",
        "SQL Reports",
        "API Development",
        "Testing & Validation"
    ]
)

# HOME
if page == "Home":

    st.header("Project Overview")

    st.write("""
    This Pharmacy Analytics System helps monitor:
    - Medicine inventory
    - Expiry tracking
    - Supplier performance
    - Demand forecasting
    - Prescription trends
    - KPI reporting
    """)

# KPI DASHBOARD
elif page == "KPI Dashboard":

    st.header("KPI Dashboard")

    st.write("Add your KPI dashboard charts here.")

# STOCK ANALYSIS
elif page == "Medicine Stock Analysis":

    st.header("Medicine Stock Analysis")

    st.write("Add stock analysis graphs here.")

# EXPIRY
elif page == "Expiry Monitoring":

    st.header("Expiry Monitoring System")

    st.write("Add expiry monitoring charts here.")

# SUPPLIER
elif page == "Supplier Analytics":

    st.header("Supplier Performance Analytics")

    st.write("Add supplier analytics here.")

# PRESCRIPTION
elif page == "Prescription Trends":

    st.header("Prescription Trend Analysis")

    st.write("Add prescription trend charts here.")

# INVENTORY
elif page == "Inventory Optimization":

    st.header("Inventory Optimization Engine")

    st.write("Add optimization analysis here.")

# FORECASTING
elif page == "Demand Forecasting":

    st.header("Demand Forecasting")

    st.write("Add forecasting charts here.")

# SQL
elif page == "SQL Reports":

    st.header("SQL Reporting & Analytics")

    st.write("Add SQL outputs here.")

# API
elif page == "API Development":

    st.header("API Development")

    st.code("""
@app.route('/inventory')
def inventory():
    return "Inventory Data"
""")

# TESTING
elif page == "Testing & Validation":

    st.header("Testing & Validation")

    st.write("""
    Testing performed:
    - Forecast validation
    - Inventory validation
    - Supplier metrics testing
    """)