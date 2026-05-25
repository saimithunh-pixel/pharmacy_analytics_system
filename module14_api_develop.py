from flask import Flask, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load dataset
df = pd.read_csv("data1/cleaned_pharmacy_data.csv")

# -----------------------------
# Inventory API
# -----------------------------
@app.route('/inventory', methods=['GET'])
def inventory():

    inventory_data = df[[
        'Medicine_Name',
        'Category',
        'Stock_Quantity',
        'Supplier_Name',
        'Storage_Location'
    ]]

    return jsonify(inventory_data.to_dict(orient='records'))


# -----------------------------
# Forecast API
# -----------------------------
@app.route('/forecast', methods=['GET'])
def forecast():

    forecast_data = df[[
        'Medicine_Name',
        'Units_Sold',
        'Reorder_Level'
    ]]

    forecast_data['Predicted_Demand'] = (
        forecast_data['Units_Sold'] * 1.2
    )

    return jsonify(forecast_data.to_dict(orient='records'))


# -----------------------------
# Supplier API
# -----------------------------
@app.route('/supplier', methods=['GET'])
def supplier():

    supplier_data = df.groupby('Supplier_Name')[
        'Stock_Quantity'
    ].sum().reset_index()

    return jsonify(supplier_data.to_dict(orient='records'))


# -----------------------------
# Expiry Alert API
# -----------------------------
@app.route('/expiry', methods=['GET'])
def expiry():

    df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'])

    today = datetime.today()

    expiry_data = df[
        (df['Expiry_Date'] - today).dt.days <= 30
    ]

    expiry_result = expiry_data[[
        'Medicine_Name',
        'Expiry_Date',
        'Stock_Quantity'
    ]]

    return jsonify(expiry_result.to_dict(orient='records'))


# -----------------------------
# Run Flask App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)