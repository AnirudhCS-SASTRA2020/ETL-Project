import pandas as pd

# Extract
df = pd.read_csv("orders.csv")

# Transform
df = df[df["amount"] > 100]

# Load
df.to_csv("cleaned_orders.csv", index=False)