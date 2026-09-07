import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Check dataset
print("Dataset Shape:", df.shape)

# -----------------------------------
# 1. City with highest number of restaurants
# -----------------------------------

city_counts = df["City"].value_counts()

top_city = city_counts.idxmax()
top_city_count = city_counts.max()

print("\nCity with Highest Number of Restaurants:")
print(top_city)
print("Number of Restaurants:", top_city_count)


# -----------------------------------
# 2. Average rating for each city
# -----------------------------------

city_avg_rating = (
    df.groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

print("\nAverage Rating by City:")
print(city_avg_rating)


# -----------------------------------
# 3. City with highest average rating
# -----------------------------------

highest_rating_city = city_avg_rating.idxmax()
highest_rating = city_avg_rating.max()

print("\nCity with Highest Average Rating:")
print(highest_rating_city)
print("Average Rating:", highest_rating)


# -----------------------------------
# 4. Create chart - Top 10 cities by restaurant count
# -----------------------------------

top_10_cities = city_counts.head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_10_cities.index,
    top_10_cities.values
)

plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save chart
plt.savefig("top_10_cities_restaurants.png", dpi=300)

plt.show()
