import numpy as np
import matplotlib.pyplot as plt

## Logistic Growth Function
def logistic_growth (t, P0, K, r):
    A = (K - P0) / P0
    return K / (1 + A * np.exp(-r * t))

## Parameters
years = 100

## Thailand
i1 = 1000
k1 = 2000
r1 = 0.005

## Australia
i2 = 35000
k2 = 60000
r2 = 0.005

## Costa Rica
i3 = 18000
k3 = 100000
r3 = 0.04

# Time array
t = np.arange(0, years + 1, 1)

## Calculation
p1 = logistic_growth(t, i1, k1, r1)
p2 = logistic_growth(t, i2, k2, r2)
p3 = logistic_growth(t, i3, k3, r3)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, p1, label="Thailand", marker='o')
plt.plot(t, p2, label="Australia", marker='o')
plt.plot(t, p3, label="Costa Rica", marker='o')

# Title and labels
plt.title("Logistic Population Growth Model - Green Sea Turtle")
plt.xlabel("Time (years)")
plt.ylabel("Population (Estimated Nest Count)")

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
