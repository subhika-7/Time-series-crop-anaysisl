# src/trend_analysis.py

import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_csv = os.path.join(BASE_DIR, '../outputs/crop_metrics.csv')

# Read the CSV from Hour 2
df = pd.read_csv(input_csv)

# Add columns for trend and insight
trends = []
insights = []

for i in range(1, len(df)):
    prev_green = df.loc[i-1, 'green_ratio']
    curr_green = df.loc[i, 'green_ratio']
    delta = curr_green - prev_green

    # Assign trend
    if delta > 0.1:  # threshold can be adjusted
        trend = 'Healthy'
        insight = 'Crop is growing normally.'
    elif delta > 0:
        trend = 'Stable'
        insight = 'Growth is steady.'
    else:
        trend = 'Critical'
        insight = 'Growth is declining; check for stress or disease.'

    trends.append(trend)
    insights.append(insight)

# Add first row as NA
df['trend'] = ['NA'] + trends
df['insight'] = ['NA'] + insights

# Save updated CSV
output_csv = os.path.join(BASE_DIR, '../outputs/crop_metrics_trend.csv')
df.to_csv(output_csv, index=False)
print(f"Trend analysis saved to {output_csv}\n")

# Optional: print trends
for i in range(1, len(df)):
    print(f"{df.loc[i-1, 'image']} → {df.loc[i, 'image']}: {df.loc[i, 'trend']} ({df.loc[i, 'green_ratio'] - df.loc[i-1, 'green_ratio']:.3f})")
    print(f"Insight: {df.loc[i, 'insight']}\n")
