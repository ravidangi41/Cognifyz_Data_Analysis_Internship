import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Check dataset
print("Dataset Shape:", df.shape)

# Count restaurants in each price range
price_counts = df["Price range"].value_counts().sort_index()

# Calculate percentage
price_percentage = (price_counts / len(df) * 100).round(2)

# Create result table
result = pd.DataFrame({
    "Price Range": price_counts.index,
    "Restaurant Count": price_counts.values,
    "Percentage": price_percentage.values
})

# Display result
print("\nPrice Range Distribution:")
print(result)

# Identify most common price range
most_common_range = price_counts.idxmax()
most_common_count = price_counts.max()
most_common_percentage = price_percentage.loc[most_common_range]

print("\nMost Common Price Range:")
print("Price Range:", most_common_range)
print("Restaurant Count:", most_common_count)
print("Percentage:", most_common_percentage, "%")

# Create bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    result["Price Range"].astype(str),
    result["Restaurant Count"]
)

plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")

plt.tight_layout()

# Save chart
plt.savefig("price_range_distribution.png", dpi=300)

plt.show()
