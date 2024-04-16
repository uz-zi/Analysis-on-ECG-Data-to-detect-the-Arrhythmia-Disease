import os
import pandas as pd
import pywt
import numpy as np

# Function to denoise a single column
def denoise_signal(signal, wavelet='db4', level=1):
    # Decompose to get the coefficients
    coeff = pywt.wavedec(signal, wavelet, mode="per", level=level)
    # Calculate a threshold
    sigma = (1/0.6745) * np.median(np.abs(coeff[-level] - np.median(coeff[-level])))
    threshold = sigma * np.sqrt(2 * np.log(len(signal)))
    # Apply soft thresholding
    coeff[1:] = (pywt.threshold(i, value=threshold, mode='soft') for i in coeff[1:])
    # Reconstruct the signal
    return pywt.waverec(coeff, wavelet, mode='per')

# Create the directory for the new dataset if it does not exist
new_dataset_dir = './NewDataset'
if not os.path.exists(new_dataset_dir):
    os.makedirs(new_dataset_dir)

# Load the dataset
file_path = './WFDBRecords/10/106/JS10092.csv'  # Replace this with the path to your CSV file


df = pd.read_csv(file_path)

# Apply denoising
for column in df.columns:
    if column != 'time':  # Exclude the time column
        df[column] = denoise_signal(df[column])

# Save the cleaned dataset
new_file_path = os.path.join(new_dataset_dir, '10_106_JS10092_cleaned_data.csv')
df.to_csv(new_file_path, index=False)

print(f"Data cleaned and saved to {new_file_path}")
