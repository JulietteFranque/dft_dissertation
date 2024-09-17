import matplotlib.pyplot as plt
from matplotlib import rc

# Enable LaTeX text rendering
rc('text', usetex=True)

# Set the color cycle for axes
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.tab20.colors)

# Update various rcParams to customize the plot appearance
plt.rcParams.update({
    'axes.labelsize': 16,
    'axes.titlesize': 16,
    'legend.fontsize': 16,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'lines.linewidth': 4,
    'grid.color': 'gray',
    'grid.linestyle': ':',
    'grid.linewidth': 0.5,
    'axes.grid': True
})