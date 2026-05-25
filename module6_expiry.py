"""import pandas as pd

import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# Current date
current_date = pd.Timestamp.today()

# Convert expiry date column
df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])

# Calculate remaining days
df['days_to_expiry'] = (
    df['Expiry_Date'] - current_date
).dt.days

# Create status category
def expiry_status(days):
    if days < 0:
        return "Expired"
    elif days <= 30:
        return "Critical"
    elif days <= 90:
        return "Warning"
    else:
        return "Safe"

df['Status'] = df['days_to_expiry'].apply(expiry_status)

# Display result
print(df.head())
df.to_csv('expired_medicine_report.csv', index=False)"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ======================================================
# MAIN FUNCTION
# ======================================================

def main():

    st.header("Expiry Monitoring System")

    # ======================================================
    # LOAD DATA
    # ======================================================

    df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

    # ======================================================
    # CURRENT DATE
    # ======================================================

    current_date = pd.Timestamp.today()

    # ======================================================
    # CONVERT EXPIRY DATE
    # ======================================================

    df['Expiry_Date'] = pd.to_datetime(
        df['Expiry_Date']
    )

    # ======================================================
    # DAYS TO EXPIRY
    # ======================================================

    df['days_to_expiry'] = (
        df['Expiry_Date'] - current_date
    ).dt.days

    # ======================================================
    # EXPIRY STATUS FUNCTION
    # ======================================================

    def expiry_status(days):

        if days < 0:
            return "Expired"

        elif days <= 30:
            return "Critical"

        elif days <= 90:
            return "Warning"

        else:
            return "Safe"

    # ======================================================
    # APPLY STATUS
    # ======================================================

    df['Status'] = df['days_to_expiry'].apply(
        expiry_status
    )

    # ======================================================
    # DATA PREVIEW
    # ======================================================

    st.subheader("Expiry Monitoring Dataset")

    st.dataframe(df.head())

    # ======================================================
    # SAVE REPORT
    # ======================================================

    df.to_csv(
        'expired_medicine_report.csv',
        index=False
    )

    # ======================================================
    # STATUS COUNT
    # ======================================================

    status_count = df['Status'].value_counts()

    st.subheader("Medicine Expiry Status Count")

    st.dataframe(status_count)

    # ======================================================
    # PIE CHART
    # ======================================================

    st.subheader(
        "Medicine Expiry Status Distribution"
    )

    fig, ax = plt.subplots(figsize=(8,8))

    status_count.plot(
        kind='pie',
        autopct='%1.1f%%',
        ax=ax
    )

    ax.set_title(
        "Medicine Expiry Status Distribution"
    )

    ax.set_ylabel("")

    st.pyplot(fig)

    # ======================================================
    # FINAL INSIGHTS
    # ======================================================

    st.subheader("Final Insights")

    expired_count = (
        df['Status'] == 'Expired'
    ).sum()

    critical_count = (
        df['Status'] == 'Critical'
    ).sum()

    st.error(
        f"Expired Medicines: {expired_count}"
    )

    st.warning(
        f"Critical Medicines: {critical_count}"
    )

    st.success(
        "Expiry Monitoring Completed Successfully"
    )
