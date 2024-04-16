import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('./NewDataset/age_sex_dx_data.csv')


# Count the number of males and females
male_count = df[df['Sex'] == 'Male'].shape[0]
female_count = df[df['Sex'] == 'Female'].shape[0]

# Calculate the percentage of males and females
total_count = len(df)
percent_male = (male_count / total_count) * 100
percent_female = (female_count / total_count) * 100

# Create a pie chart
plt.figure(figsize=(5, 5))
plt.pie([percent_male, percent_female], labels=['Male', 'Female'], autopct="%1.1f%%")
plt.title('Gender Distribution')
plt.show()

# Print the results (optional)
print("Percentage of Male:", percent_male, "%")
print("Percentage of Female:", percent_female, "%")



bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['1-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']
df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Count the number of occurrences in each bin
age_distribution = df['age_group'].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(age_distribution.index, age_distribution.values)

# Adding count above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')  # va='bottom' to make the text align above the bar

plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Age Distribution in Bins')
plt.show()


# Load the uploaded ECG data
ecg_data_path = './NewDataset/01_010_JS00001_cleaned_data.csv'
ecg_df = pd.read_csv(ecg_data_path)

# Drop the 'time' column for correlation analysis
ecg_df_no_time = ecg_df.drop(columns=['time'])

# Calculate the correlations between ECG leads
correlations = ecg_df_no_time.corr()

# Plotting the heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of ECG Leads')
plt.show()
