import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,8))
ax=plt.subplot(aspect=1)

ticklables=ax.get_xaxis().get_ticklabels()
for label in ticklables:
    label.set_fontweight("bold")

# Above for  lines in single line
#   for label in ax.get_xaxis().get_ticklabels()

ax.plot(range(10))
plt.show()