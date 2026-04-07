import pandas as pd
import numpy

# Extract
df = pd.read_csv("orders.csv")

# Transform
df = df[df["amount"] > 100]

# Hello there
# Hi There (IN local, it was Hello there, here it is Hi There. This will cause a merge conflict)

# Load
df.to_csv("cleaned_orders.csv", index=False)
