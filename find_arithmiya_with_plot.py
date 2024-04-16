
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./NewDataset/age_sex_dx_data.csv')

# Now using the correct column name 'Arrhythmias', let's find rows with missing values
missing_arrhythmias = df['Arrhythmias'].isna()

# Find the IDs of rows with missing values in the "Arrhythmias" column
missing_ids = df[missing_arrhythmias]['ID'].tolist()
missing_ids_df = pd.DataFrame(missing_ids, columns=['Missing Arrhythmias IDs'])
print(missing_ids_df)




has_arrhythmia = df['Arrhythmias'].notna().sum()
no_arrhythmia = df['Arrhythmias'].isna().sum()

# Data to plot
labels = 'Has Arrhythmia', 'No Arrhythmia'
sizes = [has_arrhythmia, no_arrhythmia]
 
# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Entries with and without Arrhythmia')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the plot
plt.show()

male_with_arrhythmia = df[(df['Sex'] == 'Male') & df['Arrhythmias'].notna()].shape[0]
male_without_arrhythmia = df[(df['Sex'] == 'Male') & df['Arrhythmias'].isna()].shape[0]

# Analysis 2: Female patients with and without arrhythmias
female_with_arrhythmia = df[(df['Sex'] == 'Female') & df['Arrhythmias'].notna()].shape[0]
female_without_arrhythmia = df[(df['Sex'] == 'Female') & df['Arrhythmias'].isna()].shape[0]

# Analysis 3: Distribution of arrhythmias between males and females
total_with_arrhythmia = df['Arrhythmias'].notna().sum()
male_percentage_with_arrhythmia = (male_with_arrhythmia / total_with_arrhythmia) * 100
female_percentage_with_arrhythmia = (female_with_arrhythmia / total_with_arrhythmia) * 100

labels_gender = ['Males with Arrhythmia', 'Males without Arrhythmia', 'Females with Arrhythmia', 'Females without Arrhythmia']
sizes_gender = [male_with_arrhythmia, male_without_arrhythmia, female_with_arrhythmia, female_without_arrhythmia]
colors_gender = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Labels for the distribution
labels_distribution = ['Males', 'Females']
sizes_distribution = [male_percentage_with_arrhythmia, female_percentage_with_arrhythmia]
colors_distribution = ['#66b3ff','#99ff99']

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Gender Analysis Pie Chart
axs[0].pie(sizes_gender, labels=labels_gender, colors=colors_gender, autopct='%1.1f%%', startangle=140)
axs[0].set_title('Arrhythmia Analysis by Gender')

# Distribution of Arrhythmias between Genders
axs[1].pie(sizes_distribution, labels=labels_distribution, colors=colors_distribution, autopct='%1.1f%%', startangle=140)
axs[1].set_title('Distribution of Arrhythmias Between Genders')

plt.tight_layout()
plt.show()