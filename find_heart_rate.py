import pandas as pd
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Load the ECG data from the CSV file
ecg_data = pd.read_csv('./NewDataset/10_106_JS10092_cleaned_data.csv')

lead = 'V1'

# Signal processing to find R-peaks
# First, let's find the sampling rate from the time column
sampling_rate = 1 / np.mean(np.diff(ecg_data['time']))

peaks, _ = signal.find_peaks(ecg_data[lead], height=np.max(ecg_data[lead])*0.5, distance=sampling_rate*0.2)

# Assuming a regular rhythm for simplicity, calculate the average distance between peaks in terms of number of samples
if len(peaks) > 1:
    avg_distance_samples = np.mean(np.diff(peaks))
    # Convert average distance in samples to large squares (each large square is 0.2 seconds, or sampling_rate*0.2 samples)
    avg_distance_large_squares = avg_distance_samples / (sampling_rate * 0.2)
    # Calculate heart rate
    heart_rate = 300 / avg_distance_large_squares
else:
    heart_rate = None

# Plot the ECG signal and R-peaks
plt.figure(figsize=(12, 5))
plt.plot(ecg_data['time'], ecg_data[lead])
plt.plot(ecg_data['time'].iloc[peaks], ecg_data[lead].iloc[peaks], 'ro', label='R-peaks')
plt.xlabel('Time (s)')
plt.ylabel(lead.upper())
plt.title('ECG Signal with R-Peaks')
plt.legend()
plt.grid(True)
plt.show()

print(sampling_rate, heart_rate)