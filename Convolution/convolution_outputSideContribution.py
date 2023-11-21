'''
Reference Book  : The Scientist and Engineer's Guide to  Digital Signal Processing
                    By Steven W. Smith, Ph.D.
Chapter 6       : Convolution
Paragraph       : Output Side Algorithm
              

This module demonstrates Outside contribution Algorithm of convolution

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

#lengh of xn, hn and yn
hn_len=len(hn)
xn_len=len(xn)
yn_len=hn_len+xn_len-1

#number of columns in plot
subplot_cols=3

#number of row in plot : Calcultion
subplot_rows=(yn_len/subplot_cols)
temp=int(subplot_rows)
if subplot_rows > temp:
    subplot_rows=temp+1
subplot_rows=int(subplot_rows)

#figure (Matplotlib.pyplot)
fig2=plt.figure("Convolution : Input Contribution for Each Ouput ")
#adjust space between subplots
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9, 
                    wspace=0.4,hspace=0.4)

#Calculation for each output and plot on graph
for index in range(yn_len):
    #finding out valid xn and hn
    if index < (hn_len):
        xn_i=0
        xn_c=xn[0:index+1]
        hn_c=hn[0:index+1]
    elif index > (xn_len-1):
        xn_i=index-(hn_len-1)
        j=hn_len-1
        xn_c=xn[xn_i:xn_i+j]
        hn_c=hn[index-xn_len+1:hn_len]
    else:
        xn_i=index-(hn_len-1)
        xn_c=xn[xn_i:xn_i+hn_len]
        hn_c=hn
    #calculate xn_c length    
    len_xn_c=len(xn_c)

    #flip hn and calculate yn
    yn_c=xn_c*np.array(hn_c)

    titleStr=f"Yn[{index}] = Xn[{xn_i}:{xn_i+len_xn_c-1}]"
    #subplot
    plt.subplot(subplot_rows,subplot_cols,index+1)
    #generate x and plot yn_c
    x=np.arange(xn_i,xn_i+len_xn_c,1)
    plt.plot(x,yn_c,'ro')
   
    #Set X and Y Limit,grid and legend
    plt.xlim(-1,xn_len)
    plt.ylim(yn_min,yn_max)
    plt.xticks(np.arange(-1,xn_len+1,1))
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.title(titleStr)
   # plt.title(f"Yn[{index}]")
   # plt.legend()
    
plt.show()    

