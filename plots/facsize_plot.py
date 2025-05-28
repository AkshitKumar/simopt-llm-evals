import matplotlib.pyplot as plt
import numpy as np

# Data setup
models = ['RNDSRCH', 'GPT 4o', 'o1', 'o3-mini', 'Claude 3.5 Sonnet', 'DeepSeek R1']
means = [576.4132, 601.1536819 , 580, 574.36, 576.71, 575.2576803]
errors = [0.0, 0.0 ,0.0 , 0.0, 0.0, 0.0] * 2
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
plt.ylabel('Total Cost (Minimization)', fontsize=16)
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