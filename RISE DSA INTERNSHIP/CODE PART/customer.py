#Project 3: Customer Segmentation Using K-Means

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
df = pd.read_csv("customer_data.csv")

# ✅ Corrected column names to match CSV (case-sensitive)
features = ['Age', 'Income', 'Frequency', 'Spending']
data = df[features].dropna()

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Fit KMeans model
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(scaled_data)

# Add cluster labels to original data
df['Cluster'] = kmeans.labels_

# --- 2D PCA for visualization ---
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

df['PCA1'] = pca_result[:, 0]
df['PCA2'] = pca_result[:, 1]

# Plot 2D clusters
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='tab10')
plt.title("Customer Segments (2D PCA)")
plt.tight_layout()
plt.savefig("customer_clusters_2D.png")
plt.show()

# 3D Cluster Visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['PCA1'], df['PCA2'], df['Income'], c=df['Cluster'], cmap='tab10')
ax.set_title("Customer Segments in 3D (PCA + Income)")
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_zlabel("Income")
plt.tight_layout()
plt.savefig("customer_clusters_3D.png")
plt.show()

# Save results
df.to_csv("segmented_customers.csv", index=False)

print("\n✅ Customer segmentation complete. Output saved as 'segmented_customers.csv'.")