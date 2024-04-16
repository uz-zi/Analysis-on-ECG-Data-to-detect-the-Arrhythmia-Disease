import os
import glob
import scipy.io
import pandas as pd
import numpy as np

header = ['time','I', 'II', 'III', 'aVR', 'aVL', 'aVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']

def convert_record_identifier_to_id(record_identifier):
    # Remove the "JS" prefix
    id_str = record_identifier.replace("JS", "")
    # Convert the remaining string to an integer
    id_int = int(id_str)
    return id_int

def read_and_save_mat_files(start_path, headers):
    counter = 0
    for root, dirs, files in os.walk(start_path):
        for file in glob.glob(os.path.join(root, '*.mat')):
            mat_data = scipy.io.loadmat(file)
            for key in mat_data:
                if not key.startswith('__'): # Ignore special keys
                    data = mat_data[key]
                    total_duration = 10 # Total duration in seconds
                    sample_rate = 1000 # Sample rate in Hz
                    time = np.linspace(0, total_duration, len(data[0]), endpoint=False)
                    data = np.vstack((time, data))
                    
                    # Create a DataFrame from the combined data
                    df = pd.DataFrame(data)
                    
                    # Transpose the DataFrame
                    df_transposed = df.T
                    
                    # Extract the record identifier from the file path
                    record_identifier = os.path.splitext(os.path.basename(file))[0]
                    # Convert the record identifier to an integer ID
                    id_int = convert_record_identifier_to_id(record_identifier)
                    print(id_int, end=' ')
                    
                    # Write the data to a CSV file
                    csv_file_path = os.path.join(root, f'{record_identifier}.csv')
                    with open(csv_file_path, 'w') as f:
                        f.write(','.join(headers) + '\n')
                        df_transposed.to_csv(f, index=False, header=False)
            counter += 1
            print(counter)

# Specify the root directory of your dataset
root_directory = './WFDBRecords'

# Call the function to read and save all .mat files
read_and_save_mat_files(root_directory, header)
