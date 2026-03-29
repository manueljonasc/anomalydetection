

# ================================
# Step 3a: Data Preprocessing
# ================================

import pandas as pd
import numpy as np

# ----------------
# Load datasets
# ----------------
logon_df = pd.read_csv("logon_sample.csv")
device_df = pd.read_csv("device_sample.csv")
file_df   = pd.read_csv("file_sample.csv", on_bad_lines='skip', engine='python')

# ----------------
# Standardize categorical values
# ----------------
for df in [logon_df, device_df, file_df]:
    df['user'] = df['user'].str.strip().str.upper()
    df['pc'] = df['pc'].str.strip().str.upper()
    df['activity'] = df['activity'].str.strip().str.lower()

# ----------------
# Convert timestamps
# ----------------
for df in [logon_df, device_df, file_df]:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Remove invalid timestamps
    df.dropna(subset=['date'], inplace=True)

    df['date_day'] = df['date'].dt.date
    df['hour'] = df['date'].dt.hour
    df['day_of_week'] = df['date'].dt.dayofweek

# ----------------
# Sort data
# ----------------
for df in [logon_df, device_df, file_df]:
    df.sort_values(by=['user','date'], inplace=True)

# ----------------
# Handle missing values & duplicates
# ----------------
logon_df = logon_df.drop_duplicates().dropna(subset=['user','pc','activity'])
device_df = device_df.drop_duplicates().dropna(subset=['user','pc','activity'])
file_df   = file_df.drop_duplicates().dropna(subset=['user','pc','activity','filename'])

# ----------------
# Behavioral feature flags
# ----------------

# After-hours login
logon_df['is_after_hours'] = ((logon_df['hour'] < 6) | (logon_df['hour'] > 20)).astype(int)

# Time difference between actions
logon_df['time_diff'] = logon_df.groupby('user')['date'].diff().dt.total_seconds().fillna(0)

# USB usage flag
file_df['is_usb_activity'] = (file_df['to_removable_media'] == True).astype(int)

# ----------------
# Initial anomaly indicators
# ----------------
logon_outliers = logon_df[logon_df['is_after_hours'] == 1]
device_outliers = device_df.groupby(['user','date_day']).filter(lambda x: len(x) > 10)
file_outliers = file_df[file_df['is_usb_activity'] == 1]

# ----------------
# Data Validation
# ----------------
print("Logon missing values:\n", logon_df.isnull().sum())
print("Device missing values:\n", device_df.isnull().sum())
print("File missing values:\n", file_df.isnull().sum())

print("Logon duplicates:", logon_df.duplicated().sum())
print("Device duplicates:", device_df.duplicated().sum())
print("File duplicates:", file_df.duplicated().sum())

# ----------------
# Dataset Summary
# ----------------
print("Logon dataset shape:", logon_df.shape)
print("Device dataset shape:", device_df.shape)
print("File dataset shape:", file_df.shape)

print("Memory usage (MB):", logon_df.memory_usage(deep=True).sum() / 1e6)

print(logon_df.head())