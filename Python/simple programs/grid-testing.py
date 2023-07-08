import numpy as np
import matplotlib.pyplot as plt

x = np.array([i for i in range(10)])
y = np.array([i for i in range(10)])

plt.title("Cluedo")
plt.xlabel("Minutes playing")
plt.ylabel("Boredom")

plt.plot(x, y)

plt.grid()

plt.show()
