import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Check dataset
print("Dataset Shape:", df.shape)

# Count each cuisine
cuisine_counts = (
    df["Cuisines"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
)

# Top 3 cuisines
top_3 = cuisine_counts.head(3)

# Calculate percentage
percentage = (top_3 / len(df) * 100).round(2)

# Create result table
result = pd.DataFrame({
    "Cuisine": top_3.index,
    "Restaurant Count": top_3.values,
    "Percentage": percentage.values
})

# Display result
print("\nTop 3 Cuisines:")
print(result)

# Create chart
plt.figure(figsize=(8, 5))
plt.bar(result["Cuisine"], result["Restaurant Count"])

plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")

plt.tight_layout()

# Save chart
plt.savefig("top_3_cuisines.png", dpi=300)

plt.show()
