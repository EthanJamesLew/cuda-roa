import matplotlib.pyplot as plt
import numpy as np

# Read binary files
with open('initial_states.bin', 'rb') as file:
    initial_states = np.fromfile(file, dtype=np.float64).reshape((-1, 2))
with open('final_states.bin', 'rb') as file:
    final_states = np.fromfile(file, dtype=np.float64).reshape((-1, 2))

# Determine which simulations ended in a stable state
stable = np.logical_and(np.abs(final_states[:, 0]) < 0.5, np.abs(final_states[:, 1]) < 1.0)

# Create scatter plot of final states
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(final_states[:, 0], final_states[:, 1], s=1)
plt.title('Final States')
plt.xlabel('Final Theta')
plt.ylabel('Final Omega')

# Create scatter plot of initial states that led to stability
plt.subplot(1, 2, 2)
plt.scatter(initial_states[stable, 0], initial_states[stable, 1], s=1, color='blue', label='Stable')
plt.scatter(initial_states[~stable, 0], initial_states[~stable, 1], s=1, color='red', label='Unstable')
plt.title('Region of Attraction')
plt.xlabel('Initial Theta')
plt.ylabel('Initial Omega')
#plt.legend()

plt.tight_layout()
plt.show()

