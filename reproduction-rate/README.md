# Reproduction Rate Model – Green Sea Turtles

This Python script simulates and visualizes the estimated annual reproduction rates of green sea turtles in Thailand, Australia, and Costa Rica by modeling variability in eggs laid, clutches per year, and survival rates over 100 years using stochastic sampling.

##  Features

- Simulates yearly reproduction rates with natural variability  
- Models eggs per clutch, clutch frequency, and hatchling survival rate with Gaussian noise  
- Uses realistic biological parameter ranges with clipping to ensure plausible values  
- Compares reproduction trends across three distinct geographic populations  
- Visualizes results in a clear multi-line plot with markers and labeled axes  

##  Visualization

The output consists of a line graph showing:

- Estimated adult turtle reproduction rate over 100 years  
- Comparison between **Thailand**, **Australia**, and **Costa Rica**  
- Yearly data points with markers for clarity  
- Axes customized with proper ranges and intervals  

##  Calculation Logic

The model estimates the annual number of adult turtles produced by combining three stochastic components sampled from normal distributions, constrained within biologically reasonable ranges:

```
Reproduction Rate = (Eggs per Clutch) × (Clutches per Year) × (Survival Rate)
```

Where each component is sampled annually as:

- Eggs per clutch vary around the average value (e) with some natural variation, but always stay between 80 and 200 eggs.

- Clutches per year vary around the average number (c) with some variation, clipped between 2 and 7 clutches.

- Survival rate varies around the average rate (se) with small fluctuations, constrained between 0.005 (0.5%) and 0.02 (2%).

Parameters per country:

| Country     | Eggs per Clutch (e) | SD (eggs) | Clutches per Year (c) | SD (clutches) | Survival Rate (se) | SD (survival) |
|-------------|---------------------|-----------|-----------------------|---------------|--------------------|---------------|
| Thailand    | 142.5               | 10        | 4                     | 0.3           | 0.01               | 0.001         |
| Australia   | 100                 | 8         | 4.5                   | 0.2           | 0.015              | 0.0015        |
| Costa Rica  | 110                 | 12        | 6                     | 0.3           | 0.012              | 0.001         |

## 🛠 Requirements

- Python 3.x  
- numpy  
- matplotlib  

Install the required packages:

```bash
pip install numpy matplotlib
