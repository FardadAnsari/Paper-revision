import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace this with your actual data)
num_parameters = [1.054, 1.054, 1.054, 1.059, 1.073, 1.24, 1.32]
nmse_values = [-12.70, -15.34, -16.01, -17, -18.29, -22.13, -22.91]

# Architecture names corresponding to the data points
architectures = ['CSINet', 'ACRNet1X', 'CRNet', 'DS-NLCsiNet', 'CsiNetPlus', 'Deep Decoder', 'TransNet']

# Define colors and markers for different data points
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black']
markers = ['o', 's', '^', 'v', 'x', 'p', '*']

# Plotting the figure
plt.figure(figsize=(10, 6))

# Plot the main line with data points
plt.plot(np.array(num_parameters), nmse_values, marker='o', linestyle='-', color='black', label='Overall Trend')

# Add individual points with specific markers and colors
for i, (x, y, arch) in enumerate(zip(num_parameters, nmse_values, architectures)):
    plt.plot(x, y, marker=markers[i], markersize=9, linestyle='None', color=colors[i], label=arch)
    # plt.text(x, y, arch, fontsize=17, ha='right', va='bottom')  # Commented out to remove text labels

# Update font properties
plt.xlabel('Number of Parameters (1M)', fontsize=20,  fontname='Arial')
plt.ylabel('NMSE (dB)', fontsize=20,  fontname='Arial')
plt.title('NMSE vs Number of Parameters', fontsize=20, fontname='Arial')

# Customize grid and axes
plt.grid(True, linestyle='--', linewidth=0.5, color='grey')
plt.ylim(-40, -1)  # Set y-axis limit from -40 to -1
plt.xticks(fontsize=25, fontname='Arial')
plt.yticks(fontsize=25, fontname='Arial')

# Add a vertical red line from NMSE = -10 to NMSE = -20 for architectures with low number of parameters
low_param_x = 1.1  # Define the x-coordinate for the low number of parameters
plt.plot([low_param_x, low_param_x], [-10, -20], color='red', linestyle='--', linewidth=1, label='Low Parameter Range')

# Add legend with bold labels
plt.legend(fontsize=20, loc='upper right')  # Bold legend labels

# Adjust the layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()
