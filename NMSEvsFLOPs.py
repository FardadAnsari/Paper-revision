import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace this with your actual data)
architectures = ['CSINet', 'ACRNet1X', 'CRNet', 'DS-NLCsiNet', 'CsiNetPlus', 'Deep Decoder', 'TransNet']
nmse_values = [-12.70, -15.34, -16.01, -17, -18.29, -22.91, -22.13]
num_flops = [4.37, 3.6, 4.07, 10.25, 23.52, 34, 55.9]  # Replace with your actual FLOP values

# Define adjusted colors for bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Define font properties for IEEE style
font_properties = {
    'family': 'sans-serif',
    #'weight': 'bold',
    'size': 20,
}

# Plotting as a bar chart with adjusted colors
plt.figure(figsize=(10, 6))  # Adjusted figure size for better spacing
bars = plt.barh(np.arange(len(architectures)), nmse_values, color=colors)

# Adding number of FLOPs as annotations on the bars with larger font size
for i, nmse in enumerate(nmse_values):
    plt.text(nmse - 2, i, f'{num_flops[i]}M', ha='right', va='center', color='black', fontsize=15)  # Increased fontsize to 12

# Adding labels and title
plt.xlabel('NMSE (dB)', fontsize=20, fontname='Arial')
plt.ylabel('', fontsize=20, fontname='Arial')
plt.title('FLOPs for Different Architectures', fontsize=20, fontname='Arial')

# Adjust x-axis limits for better readability of annotations
plt.xlim(-25, 0)

# Adding legend with custom labels in lower left corner
plt.legend(bars, architectures, title='Architectures', title_fontsize='large', loc='lower left',fontsize=20)

# Adding grid
plt.grid(True, axis='x')

# Apply font settings to tick labels
plt.xticks(fontsize=25, fontname='Arial')
plt.yticks(np.arange(len(architectures)), [])  # Remove y-axis ticks

# Save the plot as an image file (optional)
plt.savefig('nmse_bar_chart_ieee.png', dpi=300, bbox_inches='tight')

# Show plot
plt.show()


