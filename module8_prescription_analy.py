"""import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

print(df.head())

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

medicine_prescriptions = df.groupby('Medicine_Name')['Units_Sold'].sum()

print("\nMOST PRESCRIBED MEDICINES")
print(medicine_prescriptions.sort_values(ascending=False))

category_prescriptions = df.groupby('Category')['Units_Sold'].sum()

print("\nCATEGORY WISE PRESCRIPTIONS")
print(category_prescriptions)

prescription_required = df.groupby('Prescription_Required')['Units_Sold'].sum()

print("\nPRESCRIPTION REQUIRED ANALYSIS")
print(prescription_required)

top_medicines = medicine_prescriptions.sort_values(ascending=False).head(10)

print("\nTOP 10 MEDICINES")
print(top_medicines)

monthly_trend = df.groupby('Purchase_Date')['Units_Sold'].sum()

print("\nPURCHASE DATE TREND")
print(monthly_trend)

prescription_report = df.groupby('Medicine_Name').agg({
    'Units_Sold': 'sum',
    'Stock_Quantity': 'sum',
    'Price_per_unit': 'mean'
})

prescription_report.columns = [
    'Total_Prescriptions',
    'Available_Stock',
    'Average_Price'
]

print("\nPRESCRIPTION REPORT")
print(prescription_report)

prescription_report.to_csv("prescription_trend_report.csv")

plt.figure(figsize=(12,6))

top_medicines.plot(kind='bar')

plt.title("Top 10 Prescribed Medicines")
plt.xlabel("Medicine Name")
plt.ylabel("Units Sold")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,8))

category_prescriptions.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Category Wise Prescription Share")
plt.ylabel("")

plt.show()

plt.figure(figsize=(12,6))

monthly_trend.plot()

plt.title("Prescription Trend Over Time")
plt.xlabel("Purchase Date")
plt.ylabel("Units Sold")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))

prescription_required.plot(kind='bar')

plt.title("Prescription Required vs Non-Prescription Medicines")
plt.xlabel("Prescription Required")
plt.ylabel("Units Sold")

plt.tight_layout()
plt.show()

print("\nFINAL INSIGHTS")

most_prescribed = medicine_prescriptions.idxmax()

print(f"Most Prescribed Medicine: {most_prescribed}")

highest_category = category_prescriptions.idxmax()

print(f"Highest Prescription Category: {highest_category}")

print("\nMODULE 8 – PRESCRIPTION TREND ANALYSIS COMPLETED SUCCESSFULLY")"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================================================
# MAIN FUNCTION
# ======================================================

def main():

    st.set_page_config(
        page_title="Prescription Trend Analysis",
        layout="wide"
    )

    st.title("Pharmacy Analytics System")
    st.header("Prescription Trend Analysis")

    # ======================================================
    # LOAD DATA
    # ======================================================

    try:
        df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

    except FileNotFoundError:
        st.error("Dataset file not found.")
        return

    # ======================================================
    # DATA PREVIEW
    # ======================================================

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # ======================================================
    # NULL VALUES
    # ======================================================

    st.subheader("Missing Values")

    st.write(df.isnull().sum())

    # ======================================================
    # REMOVE DUPLICATES
    # ======================================================

    df.drop_duplicates(inplace=True)

    # ======================================================
    # MOST PRESCRIBED MEDICINES
    # ======================================================

    medicine_prescriptions = (
        df.groupby('Medicine_Name')['Units_Sold']
        .sum()
    )

    st.subheader("Most Prescribed Medicines")

    st.dataframe(
        medicine_prescriptions
        .sort_values(ascending=False)
    )

    # ======================================================
    # CATEGORY WISE PRESCRIPTIONS
    # ======================================================

    category_prescriptions = (
        df.groupby('Category')['Units_Sold']
        .sum()
    )

    st.subheader("Category Wise Prescriptions")

    st.dataframe(category_prescriptions)

    # ======================================================
    # PRESCRIPTION REQUIRED ANALYSIS
    # ======================================================

    prescription_required = (
        df.groupby('Prescription_Required')['Units_Sold']
        .sum()
    )

    st.subheader("Prescription Required Analysis")

    st.dataframe(prescription_required)

    # ======================================================
    # TOP 10 MEDICINES
    # ======================================================

    top_medicines = (
        medicine_prescriptions
        .sort_values(ascending=False)
        .head(10)
    )

    st.subheader("Top 10 Medicines")

    st.dataframe(top_medicines)

    # ======================================================
    # PURCHASE DATE TREND
    # ======================================================

    monthly_trend = (
        df.groupby('Purchase_Date')['Units_Sold']
        .sum()
    )

    st.subheader("Purchase Date Trend")

    st.dataframe(monthly_trend)

    # ======================================================
    # PRESCRIPTION REPORT
    # ======================================================

    prescription_report = df.groupby('Medicine_Name').agg({
        'Units_Sold': 'sum',
        'Stock_Quantity': 'sum',
        'Price_per_unit': 'mean'
    })

    prescription_report.columns = [
        'Total_Prescriptions',
        'Available_Stock',
        'Average_Price'
    ]

    st.subheader("Prescription Report")

    st.dataframe(prescription_report)

    # ======================================================
    # SAVE REPORT
    # ======================================================

    prescription_report.to_csv(
        "prescription_trend_report.csv"
    )

    # ======================================================
    # TOP 10 PRESCRIBED MEDICINES GRAPH
    # ======================================================

    st.subheader("Top 10 Prescribed Medicines Graph")

    fig1, ax1 = plt.subplots(figsize=(12, 6))

    top_medicines.plot(
        kind='bar',
        ax=ax1
    )

    ax1.set_title("Top 10 Prescribed Medicines")
    ax1.set_xlabel("Medicine Name")
    ax1.set_ylabel("Units Sold")

    plt.xticks(rotation=45)

    st.pyplot(fig1)

    # ======================================================
    # CATEGORY SHARE PIE CHART
    # ======================================================

    st.subheader("Category Wise Prescription Share")

    fig2, ax2 = plt.subplots(figsize=(8, 8))

    category_prescriptions.plot(
        kind='pie',
        autopct='%1.1f%%',
        ax=ax2
    )

    ax2.set_title(
        "Category Wise Prescription Share"
    )

    ax2.set_ylabel("")

    st.pyplot(fig2)

    # ======================================================
    # PRESCRIPTION TREND GRAPH
    # ======================================================

    st.subheader("Prescription Trend Over Time")

    fig3, ax3 = plt.subplots(figsize=(12, 6))

    monthly_trend.plot(ax=ax3)

    ax3.set_title("Prescription Trend Over Time")
    ax3.set_xlabel("Purchase Date")
    ax3.set_ylabel("Units Sold")

    plt.xticks(rotation=45)

    st.pyplot(fig3)

    # ======================================================
    # PRESCRIPTION REQUIRED GRAPH
    # ======================================================

    st.subheader(
        "Prescription Required vs Non-Prescription Medicines"
    )

    fig4, ax4 = plt.subplots(figsize=(8, 6))

    prescription_required.plot(
        kind='bar',
        ax=ax4
    )

    ax4.set_title(
        "Prescription Required vs Non-Prescription Medicines"
    )

    ax4.set_xlabel("Prescription Required")
    ax4.set_ylabel("Units Sold")

    st.pyplot(fig4)

    # ======================================================
    # FINAL INSIGHTS
    # ======================================================

    st.subheader("Final Insights")

    most_prescribed = medicine_prescriptions.idxmax()

    st.success(
        f"Most Prescribed Medicine: {most_prescribed}"
    )

    highest_category = category_prescriptions.idxmax()

    st.info(
        f"Highest Prescription Category: {highest_category}"
    )

    st.success(
        "MODULE 8 – PRESCRIPTION TREND ANALYSIS COMPLETED SUCCESSFULLY"
    )

# ======================================================
# RUN APPLICATION
# ======================================================

if __name__ == "__main__":
    main()