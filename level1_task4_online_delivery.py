import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Check dataset
print("Dataset Shape:", df.shape)

# -----------------------------------
# 1. Percentage of restaurants
#    offering online delivery
# -----------------------------------

delivery_counts = df["Has Online delivery"].value_counts()

delivery_percentage = (
    delivery_counts / len(df) * 100
).round(2)

print("\nOnline Delivery Distribution:")
print(delivery_counts)

print("\nOnline Delivery Percentage:")
print(delivery_percentage)

# -----------------------------------
# 2. Average rating with and without
#    online delivery
# -----------------------------------

average_rating = (
    df.groupby("Has Online delivery")["Aggregate rating"]
    .mean()
    .round(2)
)

print("\nAverage Rating by Online Delivery:")
print(average_rating)

# -----------------------------------
# 3. Create comparison table
# -----------------------------------

result = pd.DataFrame({
    "Online Delivery": average_rating.index,
    "Average Rating": average_rating.values
})

print("\nComparison:")
print(result)

# -----------------------------------
# 4. Create chart
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    result["Online Delivery"].astype(str),
    result["Average Rating"]
)

plt.title("Average Rating: Online Delivery vs No Online Delivery")
plt.xlabel("Online Delivery")
plt.ylabel("Average Rating")

plt.tight_layout()

# Save chart
plt.savefig("online_delivery_rating_comparison.png", dpi=300)

plt.show()
