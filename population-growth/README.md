# Logistic Population Growth Model – Green Sea Turtles

This Python script models the estimated population growth of green sea turtles in Thailand, Australia, and Costa Rica using a logistic growth function. The model visualizes the long-term population trajectory under resource limitations and carrying capacity.

##  Features

- Simulates turtle population growth across three regions
- Uses a logistic growth function to model realistic environmental limits
- Clearly labeled multi-line graph for comparison
- Adjustable parameters for growth rate, initial population, and carrying capacity

## Visualization

The output consists of a single line graph showing:

- Population estimates over 100 years
- Comparison across **Thailand**, **Australia**, and **Costa Rica**
- Smooth population curves that approach each region’s carrying capacity

##  Calculation Logic

The model uses the **logistic growth function**:

```bash
P(t) = K / (1 + A · e^(–r·t))
where A = (K – P₀) / P₀
```

Where:  
- **P₀** = initial population  
- **K** = carrying capacity  
- **r** = growth rate  
- **t** = time in years  

Each country has its own set of parameters:
- Thailand: P₀ = 1000, K = 2000, r = 0.005  
- Australia: P₀ = 35,000, K = 60,000, r = 0.005  
- Costa Rica: P₀ = 18,000, K = 100,000, r = 0.04  

## 🛠 Requirements

- Python 3.x  
- numpy  
- matplotlib

Install the required packages:
```bash
pip install numpy matplotlib
