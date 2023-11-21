import numpy as np
import matplotlib.pyplot as plt

xn=np.array([0, -1, -1.2, 2, 1.3, 1.4, 0.8, 0, 0.7])
hn=np.array([1, 0.6, 0.5, 0])
yn=np.convolve(xn,hn)
yn_max=np.max(yn)
yn_min=np.min(yn)
print(yn)

hn_len=len(hn)
xn_len=len(xn)
yn_len=hn_len+xn_len-1

print(hn_len)
print(xn_len)
print(yn_len)

subplot_cols=3
subplot_rows=(yn_len/subplot_cols)
temp=int(subplot_rows)
if subplot_rows > temp:
    subplot_rows=temp+1
#print(subplot_rows)
subplot_rows=int(subplot_rows)

fig2=plt.figure("Convolution : Input Contribution for Each Ouput ")
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9, 
                    wspace=0.2,hspace=0.2)


for index in range(yn_len):
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
    input_len=len(xn_c)

    yn_c=xn_c*np.array(hn_c)
    plt.subplot(subplot_rows,subplot_cols,index+1)
    plt.xlim(-1,xn_len)
    plt.ylim(yn_min,yn_max)
    plt.xticks(np.arange(-1,xn_len+1,1))
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
  
   # x=np.arange(0,input_len,1)
    titleStr=f"Yn[{index}]"
    plt.title(titleStr)
    x=np.arange(xn_i,xn_i+input_len,1)
    lblStr=f"Yn[{index}] = Xn[{xn_i}:{xn_i+input_len-1}]"
    print(x)
    print(yn_c)
    plt.plot(x,yn_c,'go',label=lblStr)
    plt.legend()
    
plt.show()    

'''
    titlestring=f"x[{index}]* h[n-{index}]]"
    #plt.title("hi")
    l_append=np.zeros(index)
    r_append=np.zeros(total_len - index - hn_len)

    plt.subplot(subplot_rows,subplot_cols,index+1)
    plt.xlim(-1,total_len)
    plt.xticks(np.arange(-1,total_len+1,1))

    x=np.arange(0,index,1)
    plt.plot(x,l_append,'rx')
    x=np.arange(index,index+hn_len,1)
    plt.plot(x,i_yn,'go',label=titlestring)
    x=np.arange(index+hn_len,total_len,1)
    plt.plot(x,r_append,'rx')

    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.legend()
    '''


