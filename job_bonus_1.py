import numpy as np
import matplotlib.pyplot as plt

param = 2
sample_size = 1000
sample_number = 1000

means = []
for _ in range(sample_number):
    sample = np.random.exponential(scale=1/param, size=sample_size)
    sample_mean = np.mean(sample)
    means.append(sample_mean)

plt.hist(means, bins=30, density=True, color="lightgrey", edgecolor='black')

theoretical_mean = 1/param
theoretical_standard_deviation = 1/np.sqrt(param)
x = np.linspace(0, 3, 1000)
y = (1 / (theoretical_standard_deviation * np.sqrt(2 * np.pi))) * np.exp(-(x - theoretical_mean)**2 / (2 * theoretical_standard_deviation**2))
plt.plot(x, y, color='red')

plt.title('Théorème Central Limit - Simulation')
plt.xlabel('Moyenne des échantillons')
plt.ylabel('Densité de probabilité')
plt.show()
