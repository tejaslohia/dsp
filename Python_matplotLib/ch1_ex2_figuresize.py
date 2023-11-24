import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(6,6))
ax=plt.subplot(aspect=1)
# Above two lines in single line
# fig, ax = plt.subplots(figsize=(6,6),subplot_kw={"aspect"=1})
ax.plot(range(10))
plt.show()