import matplotlib.pyplot as plt
import numpy as np

# Data setup
models = ['ASTRODF', 'GPT 4o', 'o1', 'o3-mini', 'Claude 3.5 Sonnet', 'DeepSeek R1']
means = [0.4472, 0.0 ,0.5009, 0.5218, 0.4897, 0.4659]
errors = [0.0657, 0.0 , 0.0850, 0.0897, 0.0597, 0.1146] * 2
colors = ['#ff9999', '#99ff99', '#9999ff', '#ffcc99', '#cc99ff', '#99ccff']
patterns = ['', '', '', '', '', '']

# Create figure
plt.figure(figsize=(10, 6))
bars = []

# Plot bars with error caps
for i, (mean, error) in enumerate(zip(means, errors)):
    bar = plt.bar(i, mean, 
                 color=colors[i],
                 edgecolor='black',
                 linewidth=1,
                 yerr=error,
                 capsize=5,
                 error_kw={'ecolor': 'black', 'capsize': 5})

    # Add pattern to last bar
    if patterns[i]:
        bar[0].set_hatch(patterns[i])
        bar[0].set_edgecolor('black')
    bars.append(bar)

# Customize axes and labels
plt.xticks(range(len(models)), models, rotation=45, ha='right', fontsize = 16)
plt.xlabel('Methods', fontsize=16)
plt.ylabel('Optimal Profit (Maximization)', fontsize=16)
plt.yticks(fontsize=16)
plt.ylim(0, max(means) + 5 *  max(errors))

# Remove top and right spines
for spine in ['top', 'right']:
    plt.gca().spines[spine].set_visible(False)

# Add grid
plt.grid(axis='y', alpha=0.3)

# Adjust layout and show
plt.tight_layout()
plt.show()