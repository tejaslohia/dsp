import numpy as np
import matplotlib.pyplot as plt


print("c:\ajay")

M=30
n=np.arange(0,M,1)
h=0.54-0.4*np.cos(2*np.pi*n/M)
k=np.sum(h)
h=h/k


xticks=['2^6','2^7','2^8','2^9','2^10','2^12']


fig = plt.figure()

x_values = [2**6,2**7,2**8,2**9,2**10,2**12]
y_values_ST = [7.3,15,29,58,117,468]
y_values_S3 = [2.3,4.6,9.1,19,39,156]
xticks=['2^6','2^7','2^8','2^9','2^10','2^12']

ax = plt.gca()
ax.set_xscale('log')
plt.plot(x_values, y_values_ST,'-gv')
plt.plot(x_values, y_values_S3,'-r+')
plt.legend(['ST','S^3'], loc='upper left')
plt.xticks(x_values,xticks)

fig.suptitle('Encrypted Query Size Overhead')
plt.xlabel('Query size')
plt.ylabel('Size in KB')

plt.autoscale(enable=True, axis='x', tight=True)#plt.axis('tight')
plt.grid()
fig.savefig('token_size_plot.pdf')
plt.show()