import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Simulation length
years = 100
t = np.arange(0, years + 1)

# Thailand Parameters
e1 = 142.5
c1 = 4
se1 = 0.01
e1_sd = 10
c1_sd = 0.3
se1_sd = 0.001

# Australia Parameters
e2 = 100
c2 = 4.5
se2 = 0.015
e2_sd = 8
c2_sd = 0.2
se2_sd = 0.0015

# Costa Rica Parameters
e3 = 110
c3 = 6
se3 = 0.012
e3_sd = 12
c3_sd = 0.3
se3_sd = 0.001

# Create the plot
plt.figure(figsize=(10, 6))

# Thailand Reproduction Rate Simulation
eggs_t1 = np.clip(np.random.normal(e1, e1_sd, size=len(t)), 80, 200)
clutches_t1 = np.clip(np.random.normal(c1, c1_sd, size=len(t)), 2, 7)
survival_t1 = np.clip(np.random.normal(se1, se1_sd, size=len(t)), 0.005, 0.02)
reproduction_t1 = eggs_t1 * clutches_t1 * survival_t1
plt.plot(t, reproduction_t1, label="Thailand", marker='o')

# Australia Reproduction Rate Simulation
eggs_t2 = np.clip(np.random.normal(e2, e2_sd, size=len(t)), 80, 200)
clutches_t2 = np.clip(np.random.normal(c2, c2_sd, size=len(t)), 2, 7)
survival_t2 = np.clip(np.random.normal(se2, se2_sd, size=len(t)), 0.005, 0.02)
reproduction_t2 = eggs_t2 * clutches_t2 * survival_t2
plt.plot(t, reproduction_t2, label="Australia", marker='o')

# Costa Rica Reproduction Rate Simulation
eggs_t3 = np.clip(np.random.normal(e3, e3_sd, size=len(t)), 80, 200)
clutches_t3 = np.clip(np.random.normal(c3, c3_sd, size=len(t)), 2, 7)
survival_t3 = np.clip(np.random.normal(se3, se3_sd, size=len(t)), 0.005, 0.02)
reproduction_t3 = eggs_t3 * clutches_t3 * survival_t3
plt.plot(t, reproduction_t3, label="Costa Rica", marker='o')

# Title and labels
plt.title("Reproduction Rate Model - Green Sea Turtles (Estimated Adults/Year)")
plt.xlabel("Time (Years)")
plt.ylabel("Estimated Adult Turtles")

# Grid and legend
plt.grid(True)
plt.legend()

# Force x-axis to tick every 10 years
plt.xticks(np.arange(0, years + 1, 10))

# Force y-axis to start from 0
plt.ylim(bottom=0)

# Force x-axis to start from 0
plt.xlim(left=0)

# Display the plot nicely
plt.tight_layout()
plt.show()
