# Rainfall & Wildebeest Migration Estimator

This Python script models the seasonal movement of wildebeests in the Serengeti based on monthly rainfall data. It estimates the distance of migration using a simple sensitivity model, where reduced rainfall prompts greater movement.

##  Features

- Monthly rainfall data visualization
- Estimated migration distance per month based on rainfall drop
- Dual subplots for clear comparison
- Smooth and readable data plotting with `matplotlib`

##  Visualization

The program generates two subplots:

1. **Monthly Rainfall Chart**  
   - Displays rainfall levels from January to December  
   - Visualized using a blue line graph with markers

2. **Migration Distance Chart**  
   - Shows the estimated distance wildebeests travel each month  
   - Represented with a green line and filled area to show impact intensity

##  Calculation Logic

- A rainfall drop from one month to the next increases migration.
- Sensitivity value used: **0.7 km per 1 mm decrease** in rainfall.
- If rainfall increases, a minimal movement of **0.1 km** is assumed.
- The first month starts with a default distance of 0.1 km.

## 🛠 Requirements

- Python 3.x
- matplotlib

To install the required package:
```bash
pip install matplotlib
