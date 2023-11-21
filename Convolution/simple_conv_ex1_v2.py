'''

Reference Book  : The Scientist and Engineer's Guide to  Digital Signal Processing
                    By Steven W. Smith, Ph.D.
Chapter 6       : Convolution
Paragraph       : Input Side Algorithm
              

This module demonstrates contrition of each input on output of convolution

__author__ = "Tejas Lohia IIT Gandhinagar"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Tejas Lohia"
__email__ = "tejaslohia@gmail.com"
'''
#import libraries
import numpy as np
import matplotlib.pyplot as plt

#Input
xn=np.array([0, -1, -1.2, 2, 1.3, 1.3, 0.8, 0, 0.7])

#Impulse Response
hn=np.array([1, 0.6, 0.5, 0])

#Convolution
yn=np.convolve(xn,hn)

#Min Max value for ploting
yn_max=np.max(yn)
yn_min=np.min(yn)

#lengh of xn and hn
hn_len=len(hn)
xn_len=len(xn)
total_len=hn_len+xn_len-1

#number of columns in plot
subplot_cols=3

#number of row in plot : Calcultion
subplot_rows=(xn_len/subplot_cols)
temp=int(subplot_rows)
if subplot_rows > temp:
    subplot_rows=temp+1
subplot_rows=int(subplot_rows)

#figure (Matplotlib.pyplot)
fig2=plt.figure("Convolution : Contribution from Each Input on different Output ")
#adjust space between subplots
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9, 
                    wspace=0.2,hspace=0.2)

#Calculation for each input and plot on graph
for index in range(xn_len):
    #calculating output for each input
    i_yn=hn*(xn[index])

    #plot cross mark and dot for each input
    titlestring=f"x[{index}]* h[n-{index}]]"
    l_append=np.zeros(index)
    r_append=np.zeros(total_len - index - hn_len)

    #Subplot
    plt.subplot(subplot_rows,subplot_cols,index+1)
    #Plot cross and dot for valid input
    x=np.arange(0,index,1)
    plt.plot(x,l_append,'rx')
    x=np.arange(index,index+hn_len,1)
    plt.plot(x,i_yn,'go',label=titlestring)
    x=np.arange(index+hn_len,total_len,1)
    plt.plot(x,r_append,'rx')
    #Set X and Y Limit,grid and legend
    plt.xlim(-1,total_len)
    plt.xticks(np.arange(-1,total_len+1,1))
    plt.ylim(yn_min,yn_max)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.legend()

plt.show()

