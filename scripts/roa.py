import matplotlib.pyplot as plt
import numpy as np

# Read binary files
with open('initial_states.bin', 'rb') as file:
    initial_states = np.fromfile(file, dtype=np.float64).reshape((-1, 2))
with open('final_states.bin', 'rb') as file:
    final_states = np.fromfile(file, dtype=np.float64).reshape((-1, 2))

# Determine which simulations ended in a stable state
stable = np.logical_and(np.abs(final_states[:, 0]) < 0.1, np.abs(final_states[:, 1]) < 0.1)

# Create scatter plot of final states
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(final_states[:, 0], final_states[:, 1], s=1)
plt.title(f'Final States (Num Stable: {np.sum(stable)}, Total: {len(final_states)})')
plt.xlabel('Final Theta')
plt.ylabel('Final Omega')
plt.xlim(-np.pi, np.pi)
plt.ylim(-10, 10)

# Create scatter plot of initial states that led to stability
plt.subplot(1, 2, 2)
plt.scatter(initial_states[stable, 0], initial_states[stable, 1], s=1, color='blue', label='Stable', alpha=0.1)
plt.scatter(initial_states[~stable, 0], initial_states[~stable, 1], s=1, color='red', label='Unstable', alpha=0.1)
plt.title('Region of Attraction')
plt.xlabel('Initial Theta')
plt.ylabel('Initial Omega')

plt.tight_layout()
plt.savefig('img/roa.png')
plt.show()

