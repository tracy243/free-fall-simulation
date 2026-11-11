import matplotlib.pyplot as plt
import numpy as np

def distance_chute(t):
    return 0.5 * 9.81 * t ** 2

print(distance_chute(2))

temps = np.linspace(0, 5, 100)                        #temps = [0, 1, 2, 3, 4, 5]
distances = [ ]
distances = distances_chutes(temps) 

#for t in temps:
      print(distance_chute(t))
      distances.append(distance_chute(t))

plt.plot(temps, distances)
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Free fall")
plt.show()