# ================================
# Step 4: Modeling & Evaluation
# ================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, f1_score, roc_auc_score

import tensorflow as tf
from tensorflow.keras import layers, models

# ----------------
# Feature Selection
# ----------------
features = ['login_frequency',
            'device_usage_frequency',
            'file_access_frequency',
            'removable_media_ratio',
            'unique_pc_count']

X = merged_features[features].fillna(0)

# ----------------
# Feature Scaling
# ----------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ----------------
# Isolation Forest
# ----------------
model_if = IsolationForest(
    n_estimators=300,         # increased for better learning
    contamination=0.05,
    random_state=42
)

if_preds = model_if.fit_predict(X_scaled)
merged_features['if_anomaly'] = (if_preds == -1).astype(int)

# ----------------
# Autoencoder
# ----------------
input_dim = X_scaled.shape[1]

autoencoder = models.Sequential([
    layers.Input(shape=(input_dim,)),

    layers.Dense(32, activation='relu'),
    layers.BatchNormalization(),

    layers.Dense(16, activation='relu'),
    layers.Dense(8, activation='relu'),

    layers.Dense(16, activation='relu'),
    layers.Dense(32, activation='relu'),

    layers.Dense(input_dim, activation='linear')
])

autoencoder.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='mse'
)

history = autoencoder.fit(
    X_scaled, X_scaled,
    epochs=30,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# ----------------
# Reconstruction Error
# ----------------
X_pred = autoencoder.predict(X_scaled)
mse = np.mean(np.square(X_scaled - X_pred), axis=1)

merged_features['ae_error'] = mse

# Better threshold (more robust)
threshold = np.mean(mse) + 2 * np.std(mse)

merged_features['ae_anomaly'] = (mse > threshold).astype(int)

# ----------------
# Evaluation
# ----------------
if 'label' in merged_features.columns:
    y_true = merged_features['label']

    print("=== Isolation Forest ===")
    print(classification_report(y_true, merged_features['if_anomaly']))
    print("F1:", f1_score(y_true, merged_features['if_anomaly']))
    print("AUC:", roc_auc_score(y_true, merged_features['if_anomaly']))

    print("\n=== Autoencoder ===")
    print(classification_report(y_true, merged_features['ae_anomaly']))
    print("F1:", f1_score(y_true, merged_features['ae_anomaly']))
    print("AUC:", roc_auc_score(y_true, merged_features['ae_error']))

else:
    print("No labels found — using model agreement")

    agreement = (
        merged_features['if_anomaly'] ==
        merged_features['ae_anomaly']
    ).mean()

    print("Model Agreement:", round(agreement, 4))

# ----------------
# Visualization
# ----------------

# 1. Reconstruction Error Distribution
plt.figure(figsize=(8,5))
plt.hist(mse, bins=50)
plt.axvline(threshold)
plt.title("Autoencoder Reconstruction Error")
plt.xlabel("Reconstruction Error")
plt.ylabel("Frequency")
plt.show()

# 2. Isolation Forest Anomalies
plt.figure(figsize=(8,5))
plt.scatter(
    merged_features['login_frequency'],
    merged_features['file_access_frequency'],
    c=merged_features['if_anomaly']
)
plt.title("Isolation Forest Anomaly Detection")
plt.xlabel("Login Frequency")
plt.ylabel("File Access Frequency")
plt.show()