import cv2
import numpy as np
import os

# ----------------------------
# Step 0: Path to your images
# ----------------------------
data_path = "../data/"  # Adjust if your images are elsewhere

# Get all image files, sorted by name (assumes sequential dates in filenames)
images = sorted([f for f in os.listdir(data_path) if f.endswith(".jpg") or f.endswith(".png")])

# ----------------------------
# Step 1: Calculate metrics
# ----------------------------
results = []

for img_file in images:
    img_path = os.path.join(data_path, img_file)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Warning: {img_file} could not be read.")
        continue

    # Convert to HSV for green detection
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define green color range
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])

    # Create mask and calculate green pixel ratio
    mask = cv2.inRange(hsv, lower_green, upper_green)
    green_ratio = np.sum(mask > 0) / (mask.shape[0]*mask.shape[1])

    # Average brightness
    brightness = np.mean(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)) / 255

    # Store metrics as plain Python float
    results.append({
        "image": img_file,
        "green_ratio": float(round(green_ratio, 3)),
        "brightness": float(round(brightness, 3))
    })

# ----------------------------
# Step 2: Print metrics
# ----------------------------
print("\n--- Image Metrics ---")
for r in results:
    print(r)

# ----------------------------
# Step 3: Growth Trend Analysis
# ----------------------------
growth_results = []

for i in range(1, len(results)):
    prev = results[i-1]
    curr = results[i]

    delta = curr["green_ratio"] - prev["green_ratio"]

    # Classify growth status
    if delta > 0.02:
        status = "Healthy"
        insight = "Crop is growing normally."
    elif -0.02 <= delta <= 0.02:
        status = "Warning"
        insight = "Growth is stagnating; monitor water and nutrients."
    else:
        status = "Critical"
        insight = "Growth is declining; check for stress or disease."

    growth_results.append({
        "from_image": prev["image"],
        "to_image": curr["image"],
        "green_delta": float(round(delta, 3)),
        "status": status,
        "insight": insight
    })

# ----------------------------
# Step 4: Print trend analysis
# ----------------------------
print("\n--- Growth Trend Analysis ---")
for r in growth_results:
    print(f"{r['from_image']} → {r['to_image']}: {r['status']} ({r['green_delta']})")
    print(f"Insight: {r['insight']}\n")

