import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Remove missing latitude/longitude values
geo_data = df.dropna(subset=["Latitude", "Longitude"])

# Display number of valid locations
print("Number of restaurants with valid coordinates:", len(geo_data))

# Plot restaurant locations
plt.figure(figsize=(10, 6))

plt.scatter(
    geo_data["Longitude"],
    geo_data["Latitude"],
    alpha=0.5
)

plt.title("Geographic Distribution of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()

# Save chart
plt.savefig("restaurant_geographic_distribution.png", dpi=300)

plt.show()
