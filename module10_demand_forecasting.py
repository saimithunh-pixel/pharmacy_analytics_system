"""import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# Convert Purchase_Date to datetime
df['Purchase_Date'] = pd.to_datetime(
    df['Purchase_Date'],
    dayfirst=True,
    errors='coerce'
)

# Remove invalid dates
df = df.dropna(subset=['Purchase_Date'])

# Select medicines you want
medicine_list = [
    'Paracetamol',
    'Dolo650',
    'Vitamin C',
    'Azithromycin',
    'Cetirizine',
    'Amoxicillin',
    'Ibuprofen',
    'Metformin',
    'Aspirin',
    'Omeprazole'
]

# Create big figure
plt.figure(figsize=(16, 8))

# Loop through medicines
for medicine in medicine_list:

    # Filter medicine data
    medicine_df = df[df['Medicine_Name'] == medicine]

    # Skip if medicine not found
    if medicine_df.empty:
        print(f"{medicine} not found in dataset")
        continue

    # Group by date
    forecast_df = medicine_df.groupby('Purchase_Date')['Units_Sold'].sum().reset_index()

    # Rename columns for Prophet
    forecast_df.columns = ['ds', 'y']

    # Sort values
    forecast_df = forecast_df.sort_values('ds')

    # Skip if very few rows
    if len(forecast_df) < 2:
        continue

    # Create and train model
    model = Prophet(
        daily_seasonality=True,
        yearly_seasonality=True
    )

    model.fit(forecast_df)

    # Create future dates
    future = model.make_future_dataframe(periods=30)

    # Predict
    forecast = model.predict(future)

    # Plot forecast line only
    plt.plot(
        forecast['ds'],
        forecast['yhat'],
        linewidth=2,
        label=medicine
    )

# Graph settings
plt.title(
    "Medicine Demand Forecast for Multiple Medicines",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel("Date", fontsize=12)
plt.ylabel("Predicted Units Sold", fontsize=12)

plt.xticks(rotation=45)

plt.grid(True)

plt.legend()

plt.tight_layout()

# Save chart
plt.savefig(
    "multi_medicine_forecast.png",
    dpi=300,
    bbox_inches='tight'
)

# Show chart
plt.show()

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# Convert date column
df['Purchase_Date'] = pd.to_datetime(
    df['Purchase_Date'],
    dayfirst=True,
    errors='coerce'
)

# Remove invalid dates
df = df.dropna(subset=['Purchase_Date'])

# Filter medicine
medicine_df = df[df['Medicine_Name'] == 'Paracetamol']

# Group sales by date
forecast_df = medicine_df.groupby('Purchase_Date')['Units_Sold'].sum().reset_index()

# Rename columns for Prophet
forecast_df.columns = ['ds', 'y']

# Sort by date
forecast_df = forecast_df.sort_values('ds')

# Create model
model = Prophet(
    daily_seasonality=True,
    yearly_seasonality=True
)

# Train model
model.fit(forecast_df)

# Create future dates
future = model.make_future_dataframe(periods=30)

# Predict
forecast = model.predict(future)

# Save forecast output
forecast_output = forecast[['ds', 'yhat']]
forecast_output.to_csv(
    "demand_forecast_report.csv",
    index=False
)

# -------------------------------
# CUSTOM BEAUTIFUL GRAPH
# -------------------------------

plt.figure(figsize=(14, 7))

# Actual sales data
plt.plot(
    forecast_df['ds'],
    forecast_df['y'],
    label='Actual Sales',
    linewidth=2
)

# Forecast line
plt.plot(
    forecast['ds'],
    forecast['yhat'],
    label='Forecast',
    linewidth=2,
    linestyle='--'
)

# Confidence interval
plt.fill_between(
    forecast['ds'],
    forecast['yhat_lower'],
    forecast['yhat_upper'],
    alpha=0.2
)

# Titles and labels
plt.title(
    "Paracetamol Demand Forecast",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel("Date", fontsize=12)
plt.ylabel("Units Sold", fontsize=12)

# Grid
plt.grid(True)

# Legend
plt.legend()

# Rotate dates
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Save chart
plt.savefig(
    "forecast_chart.png",
    dpi=300,
    bbox_inches='tight'
)

# Show graph
plt.show()"""
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import streamlit as st  # Added for rendering in Streamlit

def main():
    st.header("Medicine Demand Forecasting")
    st.write("Generating demand forecasts for key medicines...")

    # Load dataset
    df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

    # Convert Purchase_Date to datetime
    df['Purchase_Date'] = pd.to_datetime(
        df['Purchase_Date'],
        dayfirst=True,
        errors='coerce'
    )

    # Remove invalid dates
    df = df.dropna(subset=['Purchase_Date'])

    # Select medicines you want
    medicine_list = [
        'Paracetamol',
        'Dolo650',
        'Vitamin C',
        'Azithromycin',
        'Cetirizine',
        'Amoxicillin',
        'Ibuprofen',
        'Metformin',
        'Aspirin',
        'Omeprazole'
    ]

    # Create big figure and capture the fig object explicitly
    fig, ax = plt.subplots(figsize=(16, 8))

    # Loop through medicines
    for medicine in medicine_list:

        # Filter medicine data
        medicine_df = df[df['Medicine_Name'] == medicine]

        # Skip if medicine not found
        if medicine_df.empty:
            print(f"{medicine} not found in dataset")
            continue

        # Group by date
        forecast_df = medicine_df.groupby('Purchase_Date')['Units_Sold'].sum().reset_index()

        # Rename columns for Prophet
        forecast_df.columns = ['ds', 'y']

        # Sort values
        forecast_df = forecast_df.sort_values('ds')

        # Skip if very few rows
        if len(forecast_df) < 2:
            continue

        # Create and train model
        model = Prophet(
            daily_seasonality=True,
            yearly_seasonality=True
        )

        model.fit(forecast_df)

        # Create future dates
        future = model.make_future_dataframe(periods=30)

        # Predict
        forecast = model.predict(future)

        # Plot forecast line only using the ax object
        ax.plot(
            forecast['ds'],
            forecast['yhat'],
            linewidth=2,
            label=medicine
        )

    # Graph settings using ax object
    ax.set_title(
        "Medicine Demand Forecast for Multiple Medicines",
        fontsize=18,
        fontweight='bold'
    )

    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Predicted Units Sold", fontsize=12)

    plt.xticks(rotation=45)
    ax.grid(True)
    ax.legend()
    plt.tight_layout()

    # Save chart
    plt.savefig(
        "multi_medicine_forecast.png",
        dpi=300,
        bbox_inches='tight'
    )

    # Display the chart directly inside the Streamlit Web UI
    st.pyplot(fig)

# This allows you to still test the file individually if needed
if __name__ == "__main__":
    main()