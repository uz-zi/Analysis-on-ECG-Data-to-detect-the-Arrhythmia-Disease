import wfdb
import pandas as pd
import numpy as np
import scipy.io

header = ['time','I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']

def read_and_process_mat_file(file_path, headers, csv_output_path=None):
    # Load the .mat file
    mat_data = scipy.io.loadmat(file_path)
    
    # Find the key for the data in the .mat file
    # Assuming the .mat file contains a single key for the data besides the metadata
    data_key = [key for key in mat_data.keys() if not key.startswith('__')][0]
    data = mat_data[data_key]
    
    # Assuming the data needs to be divided by 1000 to convert to the correct unit
    data = data / 1000.0
    
    # Calculate the time array based on the number of samples and a default sample rate
    total_samples = data.shape[1]
    sample_rate = 1000  # Adjust this value according to your specific data
    time = np.linspace(0, total_samples/sample_rate, total_samples, endpoint=False)
    
    # Combine time and signals for the DataFrame
    combined_data = np.vstack((time, data))
    
    # Create a DataFrame
    df = pd.DataFrame(combined_data.T, columns=headers[:combined_data.shape[0]])  # Adjust headers as needed
    
    # Optionally, write to CSV
    if csv_output_path:
        df.to_csv(csv_output_path, index=False)
    
    return df


# Example usage:
file_path = './WFDBRecords/01/010/JS00001.mat'  # Replace with your actual file path
csv_output_path = './WFDBRecords/01/010/000001fileoutput.csv'  # Replace with your desired output path

# Read and process the file, and save to CSV
df = read_and_process_mat_file(file_path, header, csv_output_path)

# If you just want to read and not save, you can call it without specifying `csv_output_path`
# df = read_and_process_ecg_file(file_path)
