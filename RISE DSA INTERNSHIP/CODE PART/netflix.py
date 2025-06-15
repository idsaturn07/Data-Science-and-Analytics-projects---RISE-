#Project 6: Netflix User Behavior Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_data.csv")

# Preview data
print("🔍 Dataset Preview:")
print(df.head())

# Total watch time per genre
genre_watch = df.groupby('genre')['watch_time'].sum().sort_values(ascending=False)

# Plot genre vs total watch time
plt.figure(figsize=(8, 5))
sns.barplot(x=genre_watch.values, y=genre_watch.index, hue=genre_watch.index, palette='rocket', legend=False)
plt.title("Total Watch Time by Genre")
plt.xlabel("Total Watch Time (hrs)")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("watch_time_by_genre.png")
plt.show()

# Total watch time per user
user_watch = df.groupby('user_id')['watch_time'].sum().sort_values(ascending=False).head(10)

# Plot top 10 users by watch time
plt.figure(figsize=(8, 5))
sns.barplot(x=user_watch.index.astype(str), y=user_watch.values, hue=user_watch.index.astype(str), palette='coolwarm', legend=False)
plt.title("Top 10 Binge Watchers")
plt.xlabel("User ID")
plt.ylabel("Total Watch Time (hrs)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_users_watchtime.png")
plt.show()

# Ratings by genre
avg_rating = df.groupby('genre')['rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=avg_rating.values, y=avg_rating.index, hue=avg_rating.index, palette='viridis', legend=False)
plt.title("Average Rating by Genre")
plt.xlabel("Average Rating")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("avg_rating_by_genre.png")
plt.show()

# --- Optional Time Trend Visualization ---
# Fix: parse date with dayfirst=True
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Aggregate daily watch time
daily_watch = df.groupby('date')['watch_time'].sum()

plt.figure(figsize=(10, 5))
daily_watch.plot(kind='line', color='crimson')
plt.title("Daily Total Watch Time Trend")
plt.xlabel("Date")
plt.ylabel("Total Watch Time (hrs)")
plt.grid(True)
plt.tight_layout()
plt.savefig("daily_watch_trend.png")
plt.show()

print("\n✅ Netflix user behavior insights generated and visualized.")