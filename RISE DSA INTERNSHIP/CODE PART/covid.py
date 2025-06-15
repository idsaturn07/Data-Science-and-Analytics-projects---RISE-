#Project 4: COVID-19 Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data with dayfirst=True to avoid warning ---
df = pd.read_csv("covid_data.csv", parse_dates=["Date"], dayfirst=True)

# --- Clean Data ---
df = df.dropna()
df.sort_values("Date", inplace=True)

# --- Group by Date for Global Summary ---
global_daily = df.groupby("Date")[["Confirmed", "Recovered", "Deaths"]].sum().reset_index()

# --- Plot 1: Line Chart - Global Cumulative Cases ---
plt.figure(figsize=(10, 6))
plt.plot(global_daily["Date"], global_daily["Confirmed"], label="Confirmed", color="orange")
plt.plot(global_daily["Date"], global_daily["Recovered"], label="Recovered", color="green")
plt.plot(global_daily["Date"], global_daily["Deaths"], label="Deaths", color="red")
plt.title("Global COVID-19 Cumulative Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend()
plt.tight_layout()
plt.savefig("global_covid_trends.png")
plt.show()

# --- Plot 2: Area Chart for Top 5 Countries ---
top_countries = df.groupby("Country")["Confirmed"].max().sort_values(ascending=False).head(5).index
df_top = df[df["Country"].isin(top_countries)]

plt.figure(figsize=(12, 7))
for country in top_countries:
    country_data = df_top[df_top["Country"] == country].groupby("Date")["Confirmed"].sum()
    plt.fill_between(country_data.index, country_data.values, label=country, alpha=0.5)
plt.title("Top 5 Countries - Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.tight_layout()
plt.savefig("top_countries_area_chart.png")
plt.show()

# --- Plot 3: Heatmap of Last Day's Data ---
latest_date = df["Date"].max()
latest_df = df[df["Date"] == latest_date][["Country", "Confirmed", "Recovered", "Deaths"]].set_index("Country")
latest_df = latest_df.sort_values("Confirmed", ascending=False).head(10)

plt.figure(figsize=(8, 5))
sns.heatmap(latest_df, annot=True, fmt="d", cmap="YlOrBr")
plt.title(f"COVID-19 Summary for Top 10 Countries on {latest_date.date()}")
plt.tight_layout()
plt.savefig("covid_heatmap.png")
plt.show()