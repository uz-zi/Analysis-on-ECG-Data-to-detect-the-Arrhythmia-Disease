import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('./NewDataset/01_010_JS00001_cleaned_data.csv')

time = df['time']
lead_I = df['I']
lead_II = df['II']
lead_III = df['III']
lead_AVF = df['aVF']
lead_AVL = df['aVL']
lead_AVR = df['aVR']
lead_V1 = df['V1']
lead_V2 = df['V2']
lead_V3 = df['V3']
lead_V4 = df['V4']
lead_V5 = df['V5']
lead_V6 = df['V6']


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time, lead_I, label='Lead I')
plt.plot(time, lead_II, label='Lead II')
plt.plot(time, lead_III, label='Lead III')
plt.plot(time, lead_AVF, label='Lead AVF')
plt.plot(time, lead_AVL, label='Lead AVL')
plt.plot(time, lead_AVR, label='Lead AVR')
plt.plot(time, lead_V1, label='Lead V1')
plt.plot(time, lead_V2, label='Lead V2')
plt.plot(time, lead_V3, label='Lead V3')
plt.plot(time, lead_V4, label='Lead V4')
plt.plot(time, lead_V5, label='Lead V5')
plt.plot(time, lead_V6, label='Lead V6')


# Customize the plot
plt.xlabel('Time')
plt.ylabel('Voltage (mV)')
plt.title('ECG')
plt.legend()


plt.show()



# Define the leads to plot
leads = ['I', 'II', 'III', 'aVF', 'aVL', 'aVR', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']

# Create subplots for each lead
fig, axs = plt.subplots(len(leads), 1, figsize=(10, 6*len(leads)), sharex=True)

# Plot each lead's signal
for i, lead in enumerate(leads):
    axs[i].plot(df['time'], df[lead])
    axs[i].set_ylabel(f'Lead {lead}', rotation=0, ha='right') 
    axs[i].grid(True)

# Add x-axis label, title, and adjust subplot spacing
plt.xlabel('Time (s)')
plt.suptitle('ECG Measurements')
plt.subplots_adjust(hspace=0.1)  # Adjust the vertical spacing between subplots
plt.xticks(rotation=0)  # Rotate x-axis labels for better visibility if needed

# Show the plot
plt.show()