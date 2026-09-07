import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Remove missing cuisine values
df = df.dropna(subset=["Cuisines"])

# Find most common cuisine combinations
cuisine_counts = df["Cuisines"].value_counts().head(10)

print("Top 10 Most Common Cuisine Combinations:")
print(cuisine_counts)

# Calculate average rating for cuisine combinations
cuisine_ratings = (
    df.groupby("Cuisines")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Cuisine Combinations by Average Rating:")
print(cuisine_ratings)

# Plot most common cuisine combinations
plt.figure(figsize=(10, 6))

plt.bar(
    cuisine_counts.index.astype(str),
    cuisine_counts.values
)

plt.title("Top 10 Most Common Cuisine Combinations")
plt.xlabel("Cuisine Combination")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save chart
plt.savefig("top_10_cuisine_combinations.png", dpi=300)

plt.show()