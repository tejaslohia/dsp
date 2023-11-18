#https://scicoding.com/convolution-in-python-3-essential-packages/

import matplotlib.pyplot as plt
import numpy as np

def sig_square(x):
    if x < 3 or x > 5:
        return 0
    else:
        return 2
    
def sig_triangle(x):
    if x < 0 or x > 2:
        return 0   
    else:
        return x

sig1 = [sig_square(x/100) for x in range(1000)]
sig2 = [sig_triangle(x/100) for x in range(200)]
conv=np.convolve(sig1,sig2)

plt.figure("Convolution Example")
plt.subplot(3,1,1)
plt.plot(sig1)
plt.grid()

plt.subplot(3,1,2)
plt.plot(sig2)
plt.grid()

plt.subplot(3,1,3)
plt.plot(conv)
plt.grid()

plt.show()
