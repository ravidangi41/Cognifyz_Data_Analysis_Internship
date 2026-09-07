import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Remove missing restaurant names
df = df.dropna(subset=["Restaurant Name"])

# Find restaurant chains
chain_counts = df["Restaurant Name"].value_counts()

# Restaurants appearing more than once are considered chains
chains = chain_counts[chain_counts > 1].head(10)

print("Top 10 Restaurant Chains:")
print(chains)

# Average rating and total votes for top chains
chain_analysis = df[df["Restaurant Name"].isin(chains.index)].groupby(
    "Restaurant Name"
).agg(
    Average_Rating=("Aggregate rating", "mean"),
    Total_Votes=("Votes", "sum"),
    Number_of_Outlets=("Restaurant Name", "count")
).sort_values("Number_of_Outlets", ascending=False)

print("\nRestaurant Chain Analysis:")
print(chain_analysis)

# Plot number of outlets
plt.figure(figsize=(10, 6))

chains.sort_values().plot(kind="barh")

plt.title("Top 10 Restaurant Chains by Number of Outlets")
plt.xlabel("Number of Outlets")
plt.ylabel("Restaurant Chain")

plt.tight_layout()

# Save chart
plt.savefig("restaurant_chains.png", dpi=300)

plt.show()
