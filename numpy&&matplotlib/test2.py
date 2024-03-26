import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,0.5)
y = np.sin(x)
#y = np.array(range(0,5))

plt.plot(y)
plt.show()

plt.plot(x,y)
plt.show()