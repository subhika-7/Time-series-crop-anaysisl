🌱 Time-Series Crop Growth Analysis

A Python-based data science project that analyzes crop growth over time using image-derived features. The project extracts vegetation metrics from sequential crop images, performs trend analysis, and produces structured datasets for downstream analytics and modeling.

📌 Project Overview

Monitoring crop growth over time is crucial for understanding plant health, detecting stress early, and supporting data-driven agricultural decisions.

This project implements a time-series analysis pipeline that:

Extracts vegetation-related features from crop images

Stores metrics in structured tabular form (CSV)

Analyzes growth trends between time intervals

Generates interpretable insights on crop health progression

The focus is on data processing, feature engineering, and trend interpretation, making this project highly relevant to Data Science and Data Engineering roles.

🧠 Key Concepts Used

Feature Extraction from Images

Time-Series Analysis

DataFrame-based Pipelines

Trend Classification Logic

CSV-based Data Engineering Workflow

🗂 Project Structure
Time-series-crop-analysis/
│
├── data/                   # Input crop images (time-ordered)
│
├── src/
│   ├── feature_extraction.py   # Extracts vegetation features from images
│   ├── trend_analysis.py       # Performs time-series trend analysis
│
├── outputs/
│   ├── crop_metrics.csv        # Extracted features per image
│   ├── crop_metrics_trend.csv  # Metrics with trend insights
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignored files (venv, outputs, cache)

⚙️ Features Extracted

For each image in the time series:

Green Ratio: Proportion of green pixels (proxy for vegetation presence)

Brightness: Average image brightness (lighting and visual clarity)

These features are stored in a structured CSV file for analysis.

📈 Trend Analysis Logic

Growth trends are computed between consecutive images based on changes in vegetation metrics.

Each interval is classified as:

Healthy – Positive growth trend

Stable – Minimal change

Critical – Declining trend indicating possible stress

Insights are automatically generated and saved for interpretation.

🚀 How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run feature extraction
python3 src/feature_extraction.py

3️⃣ Run trend analysis
python3 src/trend_analysis.py

📊 Outputs

crop_metrics.csv
Contains extracted features for each image.

crop_metrics_trend.csv
Contains features + growth trend classification + insights.

These outputs can be directly used for:

Visualization

Statistical analysis

Machine learning models

Cloud-based data pipelines

🎯 Why This Project Matters

This project demonstrates:

Practical data science workflow

Image-to-tabular data transformation

Time-series reasoning

Clean, modular Python code

Readiness for ML and cloud extensions

It is designed to be extended further with:

Advanced vegetation indices (NDVI-like features)

Machine learning models

Cloud storage and serverless execution

🧩 Future Enhancements

Growth-stage-aware trend logic

ML-based health prediction

Visualization dashboards

Cloud integration (AWS S3 + Lambda)

🧑‍💻 Author

Built as a hands-on data science project to explore real-world agricultural analytics using Python.
