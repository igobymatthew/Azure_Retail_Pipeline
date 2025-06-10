import pandas as pd

# Load sample sales data
df = pd.read_csv('../data/sales_data.csv')

# Detect anomalies (e.g., high quantity)
anomalies = df[df['Quantity'] > 3]
print("Anomalies detected:")
print(anomalies)
