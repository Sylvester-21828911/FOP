#
# growthplot.py - simulation of unconstrained growth (now with plots!)
#
import numpy as np
import matplotlib.pyplot as plt

print("\nSIMULATION - Unconstrained Growth\n")
length = 100
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step
pop_plot = []
#times = np.array([])
print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (sim length * time step per hour): ",
num_iter)
print("Growth step (growth rate per time step): ",
growth_step)
print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)
for i in range(1, int(num_iter) + 1 ):
    growth = growth_step * population
    population = population + growth
    time = i * time_step
    print("Time: ", time, " \tGrowth: ", growth, "\tPopulation: ", population)
    pop_plot.append(population)
print("\nPROCESSING COMPLETE.\n")
times = range(1, len(pop_plot)+1)
pop_plot = np.array(pop_plot)
plt.plot(times, pop_plot, 'r^')
plt.title('Prac 3.1: Unconstrained Growth')
plt.xlabel('Time')
plt.ylabel('Population')
plt.show()
