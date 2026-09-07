import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Remove missing aggregate ratings
ratings = df["Aggregate rating"].dropna()

# Create rating ranges
bins = [0, 1, 2, 3, 4, 5]
labels = ["0-1", "1-2", "2-3", "3-4", "4-5"]

rating_ranges = pd.cut(
    ratings,
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Count restaurants in each rating range
result = rating_ranges.value_counts().sort_index()

# Display distribution
print("Restaurant Rating Distribution:")
print(result)

# Find most common rating range
most_common_range = result.idxmax()
most_common_count = result.max()

print("\nMost Common Rating Range:")
print("Rating Range:", most_common_range)
print("Restaurant Count:", most_common_count)

# Calculate average number of votes
average_votes = df["Votes"].mean()

print("\nAverage Number of Votes:")
print(round(average_votes, 2))

# Create chart
plt.figure(figsize=(8, 5))

plt.bar(
    result.index.astype(str),
    result.values
)

plt.title("Distribution of Restaurant Aggregate Ratings")
plt.xlabel("Aggregate Rating Range")
plt.ylabel("Number of Restaurants")

plt.tight_layout()

# Save chart
plt.savefig("restaurant_rating_distribution.png", dpi=300)

plt.show()
