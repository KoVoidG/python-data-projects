import matplotlib.pyplot as plt

# Monthly rainfall data (in mm)
rainfall = [97, 99, 123, 141, 76, 28, 10, 22, 42, 51, 103, 97]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Rainfall sensitivity: 1 mm drop = 0.7 km of migration
sensitivity = 0.7

# Calculate migration distances
migration = [0.1]  # First month default small movement
for i in range(1, len(rainfall)):
    delta_rain = rainfall[i] - rainfall[i - 1]
    if delta_rain < 0:
        distance = -sensitivity * delta_rain  # more movement during dry spells
    else:
        distance = 0.1  # minimal movement if rainfall increases
    migration.append(round(distance, 1))

# Plotting the graphs
plt.figure(figsize=(12, 6))

# Plot 1: Rainfall per month
plt.subplot(2, 1, 1)
plt.plot(months, rainfall, marker='o', color='blue', label="Rainfall (mm)")
plt.title("Monthly Rainfall in Serengeti")
plt.ylabel("Rainfall (mm)")
plt.grid(True)
plt.legend()

# Plot 2: Migration distance per month
plt.subplot(2, 1, 2)
plt.plot(months, migration, marker='o', color='green', label="Migration Distance (km)")
plt.fill_between(months, 0, migration, color='green', alpha=0.3)
plt.title("Estimated Wildebeest Migration per Month")
plt.xlabel("Month")
plt.ylabel("Migration Distance (km)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
