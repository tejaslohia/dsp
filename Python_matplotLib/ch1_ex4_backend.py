import numpy as np
import matplotlib
matplotlib.use("PDF")
import matplotlib.pyplot as plt

print(matplotlib.get_backend())

plt.ion()
plt.plot(range(10))
plt.show()
plt.ioff()
plt.savefig("test.pdf")