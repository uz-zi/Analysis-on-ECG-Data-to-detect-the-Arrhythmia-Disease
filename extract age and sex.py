import os
import glob
import pandas as pd

def read_condition_names(file_path):
    # Read the condition names from the CSV and return a dictionary mapping Snomed_CT to Full Name
    condition_df = pd.read_csv(file_path)
    condition_map = dict(zip(condition_df['Snomed_CT'].astype(str), condition_df['Full Name']))
    return condition_map

def extract_age_sex_dx_from_hea(file_path):
    age, sex, dx_values = None, None, []  # Default values
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.lower().startswith("#age"):
                age = line.split(":")[1].strip()
            elif line.lower().startswith("#sex"):
                sex = line.split(":")[1].strip()
            elif line.lower().startswith("#dx"):
                dx_values = line.split(":")[1].strip().split(',')
    return age, sex, dx_values

def process_hea_files(start_path, condition_map):
    age_sex_dx_data = []
    counter = 0
    for root, dirs, files in os.walk(start_path):
        for file in glob.glob(os.path.join(root, '*.hea')):
            age, sex, dx_values = extract_age_sex_dx_from_hea(file)
            dx_full_names = [condition_map[dx] for dx in dx_values if dx in condition_map]
            # Use file path as ID
            file_id = os.path.relpath(file, start=start_path)
            age_sex_dx_data.append([file_id, age, sex, '; '.join(dx_full_names)])
            counter += 1
            print(f"Processed {counter} files: {file_id}")
    return age_sex_dx_data

def save_to_csv(data, headers, file_path):
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(file_path, index=False)

header = ['ID', 'Age', 'Sex', 'Arrhythmias']
root_directory = './WFDBRecords'
new_dataset_directory = './NewDataset'
condition_names_file_path = './ConditionNames_SNOMED-CT.csv'  # Update this path if needed

# Ensure the new dataset directory exists
os.makedirs(new_dataset_directory, exist_ok=True)

# Read condition names mapping
condition_map = read_condition_names(condition_names_file_path)

# Process .hea files
age_sex_dx_data = process_hea_files(root_directory, condition_map)

# Save to CSV
save_to_csv(age_sex_dx_data, header, os.path.join(new_dataset_directory, 'age_sex_dx_data.csv'))

print(f"Total files processed: {len(age_sex_dx_data)}")
