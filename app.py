import streamlit as st

# ======================================================
# IMPORT MODULE FILES
# ======================================================
import dashboard11
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
        "KPI Dashboard",
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
# PAGE ROUTING
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

elif page == "KPI Dashboard":
    dashboard11.main()

elif page == "Medicine Stock Analysis":
    module5_stock_analysis.main()

elif page == "Expiry Monitoring":
    module6_expiry.main()

elif page == "Supplier Analytics":
    module7_supplier_perfo.main()

elif page == "Prescription Trends":
    module8_prescription_analy.main()

elif page == "Inventory Optimization":
    module9_inventory_optimiz_engine.main()

elif page == "Demand Forecasting":
    module10_demand_forecasting.main()

elif page == "SQL Reporting":
    module12_sql_reporting.show()

elif page == "Database Integration":
    module13_database_integre.show()

elif page == "API Development":
    module14_api_develop.main()

elif page == "Testing & Validation":
    module15_testing_validation.main()
