import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [23, 45, 56, 78, 213, 45, 67, 89, 56, 34, 23, 45, 67, 89, 45, 67, 89, 100]

# Create a figure and a set of subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Line Chart
# For line chart, we'll use the indices of the data as the x-axis
x = np.arange(len(data))
axs[0].plot(x, data, marker='o', color='blue', linestyle='-', linewidth=2, markersize=6)
axs[0].set_title('Line Chart')
axs[0].set_xlabel('Index')
axs[0].set_ylabel('Value')

# Bar Chart
# For bar chart, we'll use the indices of the data as the x-axis
axs[1].bar(x, data, color='green')
axs[1].set_title('Bar Chart')
axs[1].set_xlabel('Index')
axs[1].set_ylabel('Value')

# Histogram
# Histogram for the same data, bins can be adjusted as needed
axs[2].hist(data, bins=8, color='purple', edgecolor='black')
axs[2].set_title('Histogram')
axs[2].set_xlabel('Value')
axs[2].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
