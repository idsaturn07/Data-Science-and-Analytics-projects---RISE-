#Project 7: Traffic Pattern Analysis

import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Create 30 days of hourly data
rng = pd.date_range(start='2024-06-01', end='2024-06-30 23:00:00', freq='H')
np.random.seed(0)
# base traffic with morning & evening peaks
base = 100 + 50 * np.sin(2 * np.pi * rng.hour / 24) + 80 * np.sin(2 * np.pi * (rng.hour-17) / 24)
noise = np.random.normal(0, 15, len(rng))
vehicle_count = np.maximum(0, base + noise).astype(int)

traffic_df = pd.DataFrame({'timestamp': rng, 'vehicle_count': vehicle_count})
traffic_df.to_csv('traffic_data.csv', index=False)

# Plot traffic density over time
plt.figure(figsize=(12,4))
plt.plot(traffic_df['timestamp'], traffic_df['vehicle_count'])
plt.title('Hourly Traffic Volume - June 2024')
plt.xlabel('Timestamp')
plt.ylabel('Vehicle Count')
plt.tight_layout()
plt.show()

# Detect anomalies using Z-score
traffic_df['zscore'] = np.abs(stats.zscore(traffic_df['vehicle_count']))
anomalies = traffic_df[traffic_df['zscore']>3]

# Show head and anomalies count
print(traffic_df.head())
print('\
Number of detected anomalies:', len(anomalies))