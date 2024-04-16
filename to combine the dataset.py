import os
import glob
import pandas as pd

def combine_csv_files_incrementally(root_path, output_file):
    first_file = True  # Flag to check if it's the first file being processed
    counter = 0  # Initialize a counter to track the number of files processed
    
    with open(output_file, 'w', newline='') as f_out:  # Open the output file once, for writing
        for root, dirs, files in os.walk(root_path):
            for file in glob.glob(os.path.join(root, '*.csv')):
                try:
                    # For each CSV file, read it with Pandas
                    df = pd.read_csv(file)
                    # Write the dataframe to the output file
                    # If it's the first file, write headers, otherwise skip headers
                    df.to_csv(f_out, index=False, header=first_file, mode='a')
                    first_file = False  # Set flag to False after the first file is processed
                except pd.errors.EmptyDataError:
                    # If an EmptyDataError occurs, print a message and continue with the next file
                    print(f'Empty or malformed file skipped: {file}')
                    continue
                
                counter += 1  # Increment the counter
                print(f'Processing file #{counter}: {file}')  # Print the progress
                
    print(f'Combined CSV file created at {output_file} with {counter} files combined.')

# Specify the root directory of your dataset and the output file
root_directory = './WFDBRecords/01'
output_csv_file = './WFDBRecords/01combined_records.csv'

# Call the function to combine all CSV files into a single CSV file incrementally
combine_csv_files_incrementally(root_directory, output_csv_file)
