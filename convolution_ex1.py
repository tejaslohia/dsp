import matplotlib.pyplot as plt
import numpy as np

sig1=[1, 2, 3, 4, 3, 2, 1]  # 7 Points
sig2=[5, 6, 7] # 3 Points

conv_full=np.convolve(sig1,sig2,mode="full") 
conv_same=np.convolve(sig1,sig2,mode="same")
conv_valid=np.convolve(sig1,sig2,mode="valid")

plt.figure("Convolution Example")
plt.subplot(5,1,1)
plt.plot(sig1,'ro')
plt.grid()
plt.title("signle 1")


plt.subplot(5,1,2)
plt.plot(sig2,'ro')
plt.grid()
plt.title("signle 2")

fig=plt.figure("Convolution Example")
fig.tight_layout()

plt.subplot(5,1,3)
plt.plot(conv_full,'ro')
plt.grid()
plt.title("Convolution Full")

plt.subplot(5,1,4)
plt.plot(conv_same,'ro')
plt.grid()
plt.title("Convolution Same")

plt.subplot(5,1,5)
plt.plot(conv_valid,'ro')
plt.grid()
plt.title("Convolution Valid")

plt.show()

