import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load ECG data from the CSV file
data = pd.read_csv('./NewDataset/01_010_JS00001_cleaned_data.csv')

# Extract ECG signal data (excluding the 'time' column)
X = data.iloc[:, 1:].values

# Generate a mock dataset (100 samples, 12 features)
# This simulates the ECG data structure after preprocessing but before dimensionality reduction
np.random.seed(42)  # For reproducibility
X_mock = np.random.rand(100, 12)  # 100 samples, 12 features (as if they are 12 leads of ECG)

# Apply PCA on the mock dataset
pca_mock = PCA(n_components=2)  # Aim to reduce to 2 principal components
pca_mock.fit(X_mock)

# Get the explained variance ratio for the first two principal components
explained_variance_ratio_mock = pca_mock.explained_variance_ratio_

print("------------",explained_variance_ratio_mock)

# Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 principal components
X_pca = pca.fit_transform(X)

# Create a new DataFrame with the principal components and time
df_pca = pd.DataFrame({'time': data['time'], 'PC1': X_pca[:, 0], 'PC2': X_pca[:, 1]})

# Plot the principal components against time
plt.figure(figsize=(10,6))
plt.plot(df_pca['time'], df_pca['PC1'], label='Principal Component 1')
plt.plot(df_pca['time'], df_pca['PC2'], label='Principal Component 2')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ECG Signals Two Principal Components')
plt.legend()
plt.show()



