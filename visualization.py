import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("dataset/train.csv")

# Plot House Price Distribution
plt.figure(figsize=(8,5))
plt.hist(data["SalePrice"], bins=30)

plt.title("House Price Distribution")
plt.xlabel("Sale Price")
plt.ylabel("Number of Houses")

plt.tight_layout()

plt.savefig("static/house_price_distribution.png")

plt.show()

print("Graph saved successfully!")
