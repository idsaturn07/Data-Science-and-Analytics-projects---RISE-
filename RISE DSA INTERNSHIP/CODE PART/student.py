#Project 2: Student Performance Analytics Dashboard

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("student_performance.csv")

# Handle missing values
df = df.dropna(subset=["marks", "attendance", "logins"])

# --- Basic Statistics ---
print("\n--- Basic Statistics ---")
print(df.describe())

# --- Correlation Matrix ---
correlation = df[["marks", "attendance", "logins"]].corr()
print("\n--- Correlation Matrix ---")
print(correlation)

# --- Correlation Heatmap ---
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()

# --- Categorize Students ---
df["status"] = df["marks"].apply(lambda x: "Top Performer" if x >= 75 else "Struggling")
df["status"] = pd.Categorical(df["status"])  # For hue warning fix

# --- Bar Chart: Top vs Struggling Students ---
plt.figure(figsize=(5, 4))
sns.countplot(data=df, x="status", hue="status", palette="Set2", legend=False)  # Fix warning
plt.title("Performance Category Count")
plt.tight_layout()
plt.savefig("performance_bar.png")
plt.show()

# --- Attendance Impact on Marks ---
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x="attendance", y="marks", hue="status", palette="muted")
plt.title("Attendance vs Marks")
plt.tight_layout()
plt.savefig("attendance_vs_marks.png")
plt.show()

# --- Save a Performance Summary Report ---
summary = df.groupby("status", observed=False)[["marks", "attendance", "logins"]].mean().round(2)
summary.to_csv("performance_summary.csv")

# --- Print Final Message ---
print("\n✅ Dashboard complete. Charts saved as PNG files and summary as CSV.")