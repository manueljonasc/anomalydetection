# anomalydetection
AIM Capstone Project
Insider Threat Detection Using AI/ML
📌 Overview
Insider threats such as data exfiltration and system sabotage pose significant risks due to legitimate access and difficulty in detection.
This project implements an unsupervised anomaly detection framework to flag users exhibiting multi-source anomalies across logon, device, and file access data.

Dataset: CERT Insider Threat Center synthetic datasets (realistic simulations).
Approach: Isolation Forest (tree-based) and Autoencoder (neural network-based).
Goal: Identify deviations from normal user behavior without labeled malicious activity.

🎯 Objectives
Detect anomalous user behavior using unsupervised ML models.
Integrate multi-source data (logon, device, file access).
Provide explainable insights for security teams.
Demonstrate end-to-end workflow from preprocessing to evaluation.
📂 Repository Structure
your-capstone-project/ │ ├── README.md ← Project overview ├── requirements.txt ← Python dependencies │ ├── notebooks/ │ ├── 01_EDA.ipynb │ ├── 02_Feature_Engineering.ipynb │ ├── 03_Modeling.ipynb │ └── 04_Evaluation.ipynb │ ├── src/ │ ├── data_preprocessing.py │ ├── feature_engineering.py │ └── model_training.py │ ├── data/ │ ├── raw/ ← Original data (or link to source) │ └── processed/ ← Cleaned data │ ├── models/ │ └── best_model.pkl ← Saved model artifacts │ ├── reports/ │ ├── technical_presentation.pdf │ └── business_presentation.pdf │ └── docs/ └── data_dictionary.md

🔍 Methodology
Data Preprocessing
Timestamp alignment, ID standardization, handling missing values.
Feature Engineering
Temporal features (hour, day_of_week, after_hours flag).
Behavioral indicators (login_frequency, device_usage_frequency, file_access_frequency, removable_media_ratio).
Aggregated features merged into a unified dataset (merged_features).
Dimensionality Reduction (PCA)
Captured ~70% variance with two principal components, revealing clustered user behavior.
Modeling
Isolation Forest: Tree-based ensemble isolating anomalies.
Autoencoder: Neural network reconstructing inputs; anomalies flagged via high reconstruction error.
Evaluation & Comparison
Agreement between IF and AE ~95%.
Adjusting contamination parameter improved overlap, yielding 4,132 common anomalies.
📊 Key Findings
EDA revealed skewed distributions and outliers in login, device, and file access frequencies.
Correlation heatmap showed strong relationships (e.g., login_frequency ↔ unique_pc_count).
PCA visualization demonstrated effective clustering of user behavior.
Model synergy: High agreement between IF and AE, with robust common anomalies identified.
🛡️ Business Impact
Reduced investigation time by focusing on high-confidence anomalies.
Mitigated risk through proactive detection of unusual activity.
Improved compliance with explainable AI techniques (SHAP, reconstruction error analysis).
📈 Explainability
SHAP Summary Plot (Isolation Forest):
login_frequency and unique_pc_count were most influential.
High values pushed predictions toward anomalies.
Autoencoder Reconstruction Error:
High errors indicated unusual patterns (e.g., excessive device usage or file access).
Feature-level analysis guided targeted investigations.
⚠️ Limitations
Class imbalance: anomalies are rare.
Synthetic data may not fully generalize to real-world environments.
Risk of proxy bias (e.g., user IDs acting as sensitive proxies).
🚀 Future Work
Real-time anomaly detection pipeline.
Integration of additional data sources (HR, network traffic, communications).
Advanced explainability (granular, human-readable insights).
Feedback loop with analysts for continuous refinement.
Semi-supervised learning if labeled anomaly data becomes available.

## Dataset
The dataset used in this project is the CERT Insider Threat Dataset.
You can access it here:
https://drive.google.com/drive/folders/1nYcliXINlP5zWNkzIA7bB-mwH5THjWaw?usp=sharing

🛠️ How to Run
# Clone the repository
git clone https://github.com/yourusername/your-capstone-project.git
cd your-capstone-project

# Install dependencies
pip install -r requirements.txt

# Run notebooks or scripts
jupyter notebook notebooks/01_EDA.ipynb
python src/model_training.py

💻Technologies Used
- Python (NumPy, Pandas, Scikit-learn, TensorFlow/Keras, SHAP)
- Google Colab Notebook
- Matplotlib / Seaborn
- GitHub for version control

📬 Contact
Author: JeyC
Email: your.email@example.com

