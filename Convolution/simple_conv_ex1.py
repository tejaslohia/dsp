import numpy as np
import matplotlib.pyplot as plt

xn=np.array([0, -1, -1.2, 2, 1.3, 1.3, 0.8, 0, 0.7])
hn=np.array([1, 0.6, 0.5, 0])
yn=np.convolve(xn,hn)

hn_len=len(hn)
xn_len=len(xn)

index=1

subplot_cols=3

subplot_rows=(xn_len/subplot_cols)
temp=int(subplot_rows)
if subplot_rows > temp:
    subplot_rows=temp+1
print(subplot_rows)


#for index in range(xn_len)



total_len=hn_len+xn_len-1

i_yn=np.convolve(xn[index],hn)
a=hn*(xn[index])
l_append=np.zeros(index)
r_append=np.zeros(total_len - index - hn_len)


fig2=plt.figure("Signal and Convolution")
plt.xlim(-1,total_len)
plt.xticks(np.arange(-1,total_len+1,1))

x=np.arange(0,index,1)
plt.plot(x,l_append,'rx')
x=np.arange(index,index+hn_len,1)
plt.plot(x,i_yn,'ro')
x=np.arange(index+hn_len,total_len,1)
plt.plot(x,r_append,'rx')

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

#ploting waveforms and FFT
fig1=plt.figure("Signal and Convolution")
#plot Singal 1      
plt.subplot(3,1,1)
#plt.xlim(signal_xmin,signal_xmax)
#plt.xticks(np.arange(signal_xmin,signal_xmax, 10.0))
plt.plot(xn,'ro')
plt.grid()

plt.subplot(3,1,2)
#plt.xlim(signal_xmin,signal_xmax)
#plt.xticks(np.arange(signal_xmin,signal_xmax, 10.0))
plt.plot(hn,'ro')
plt.grid()

plt.subplot(3,1,3)
#plt.xlim(signal_xmin,signal_xmax)
#plt.xticks(np.arange(signal_xmin,signal_xmax, 10.0))
plt.plot(yn,'ro')
plt.grid()

plt.show()

