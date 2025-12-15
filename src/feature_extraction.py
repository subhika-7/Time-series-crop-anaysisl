# src/feature_extraction.py

import cv2
import numpy as np
import pandas as pd
import os

# Paths
data_folder = '../data'                  # folder with crop images
output_csv = '../outputs/crop_metrics.csv'  # output CSV file

# List to store results
results = []

# Loop through all images
for img_file in sorted(os.listdir(data_folder)):
    if img_file.lower().endswith(('.jpg', '.png')):
        img_path = os.path.join(data_folder, img_file)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Warning: Could not read {img_file}")
            continue

        # Feature 1: Green ratio
        green_mask = (img[:,:,1] > 100) & (img[:,:,0] < 100) & (img[:,:,2] < 100)
        green_ratio = np.sum(green_mask) / (img.shape[0] * img.shape[1])

        # Feature 2: Brightness
        brightness = np.mean(img) / 255

        # Convert to plain floats
        green_ratio = round(green_ratio,3)
        brightness = round(brightness,3)

        # Append results
        results.append({
            'image': img_file,
            'green_ratio': green_ratio,
            'brightness': brightness
        })

# Convert to DataFrame
df = pd.DataFrame(results)

# Save CSV
df.to_csv(output_csv, index=False)
print(f"Features saved to {output_csv}\n")

# Optional: print for verification
print(df)
