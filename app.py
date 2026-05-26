import streamlit as st

# IMPORT MODULE FILES
import dashboard11  # <-- STEP 3: Added KPI Dashboard import
import module5_stock_analysis
import module6_expiry
import module7_supplier_perfo
import module8_prescription_analy
import module9_inventory_optimiz_engine
import module10_demand_forecasting
import module12_sql_reporting
import module13_database_integre
import module14_api_develop
import module15_testing_validation

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Pharmacy Analytics System",
    layout="wide"
)

# ======================================================
# TITLE
# ======================================================

st.markdown("""
<h1 style='text-align:center;
color:white;
background-color:#1565C0;
padding:15px;
border-radius:10px;'>
Pharmacy Analytics System
</h1>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "KPI Dashboard",  # <-- STEP 3: Added to sidebar choices
        "Medicine Stock Analysis",
        "Expiry Monitoring",
        "Supplier Analytics",
        "Prescription Trends",
        "Inventory Optimization",
        "Demand Forecasting",
        "SQL Reporting",
        "Database Integration",
        "API Development",
        "Testing & Validation"
    ]
)

# ======================================================
# HOME PAGE
# ======================================================

if page == "Home":

    st.header("Project Overview")

    st.write("""
    This Pharmacy Analytics System helps monitor:

    ✔ Medicine inventory  
    ✔ Expiry tracking  
    ✔ Supplier performance  
    ✔ Demand forecasting  
    ✔ Prescription trends  
    ✔ KPI reporting  
    ✔ SQL Reporting  
    ✔ Database Integration  
    ✔ API integration  
    ✔ Testing & validation
    """)

# ======================================================
# KPI DASHBOARD  <-- STEP 4: Added section above Stock Analysis
# ======================================================

elif page == "KPI Dashboard":

    dashboard11.main()

# ======================================================
# STOCK ANALYSIS
# ======================================================

elif page == "Medicine Stock Analysis":

    module5_stock_analysis.main()

# ======================================================
# EXPIRY MONITORING
# ======================================================

elif page == "Expiry Monitoring":

    module6_expiry.main()

# ======================================================
# SUPPLIER ANALYTICS
# ======================================================

elif page == "Supplier Analytics":

    module7_supplier_perfo.main()

# ======================================================
# PRESCRIPTION TRENDS
# ======================================================

elif page == "Prescription Trends":

    module8_prescription_analy.main()

# ======================================================
# INVENTORY OPTIMIZATION
# ======================================================

elif page == "Inventory Optimization":

    module9_inventory_optimiz_engine.main()

# ======================================================
# DEMAND FORECASTING
# ======================================================

elif page == "Demand Forecasting":

    module10_demand_forecasting.main()

# ======================================================
# API DEVELOPMENT
# ======================================================

elif page == "API Development":

    module14_api_develop.main()

# ======================================================
# TESTING
# ======================================================

elif page == "Testing & Validation":

    module15_testing_validation.main()
<<<<<<< HEAD

elif page == "SQL Reporting":

    module12_sql_reporting.show()

elif page == "Database Integration":

    module13_database_integre.show()
=======
>>>>>>> 94b831f6c24d807b48777c03afa0df4cf2b901e9
