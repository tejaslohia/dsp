import numpy as np
import matplotlib.pyplot as plt

np.linspace(0,10,7)
np.random.random((2,3))

a=np.arange(4,8)
print(a)
a *= 2
print(a)

a += 10
print(a)
a -= 5
print(a)

b=np.arange(10,14)
a+b
a-b
a*b

a=np.linspace(0,np.pi/2,5)
b=10*np.sin(a)

a=np.arange(0,9).reshape(3,3)
print(a)
b=np.ones((3,3))
print(b)
c=np.dot(a,b)
print(c)

a=np.arange(1,5)
print(a)
b=np.sqrt(a)
print(b)
b=np.log(a)
print(b)
b=np.sin(a)
print(b)


a=np.arange(1,5)
print(a)
b=np.sum(a)
print(b)
b=np.min(a)
print(b)
b=np.max(a)
print(b)

$$c = \sqrt{a^2 + b^2}$$

c=a*b
print(c)


#interation
a=np.arange(1,4)
for i in a:
    print(i)

a=np.arange(1,10).reshape(3,3)
for raw in a:
    print(raw)

a=np.arange(1,5).reshape(2,2)
for item in a.flat:
    print(item)

a=np.arange(1,10).reshape(3,3)
a
b=np.apply_along_axis(np.mean,axis=0,arr=a)
b   

a=np.arange(1,10).reshape(3,3)
a
b=np.apply_along_axis(np.mean,axis=1,arr=a)
b 

def foo(x):
    return(x/2)

a=np.arange(1,10).reshape(3,3)
a
b=np.apply_along_axis(foo,axis=1,arr=a)
b 

###############
a = np.random.random((3, 3))
a
a>0.5

a[a>0.5]

a=np.arange(1,10)
a.shape=(3,3)
a
b=a.transpose()
b

a=np.ones((2,2))
a
b=np.zeros((2,2))
b
c=np.hstack((a,b))
c

#plot sin(x)/x

x=np.arange(-2*np.pi,2*np.pi,0.1)
y1=np.sin(3*x)/x
y2=np.sin(2*x)/x
y3=np.sin(1*x)/x

plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.grid(True)
plt.show()


np.random.seed(0)
i = np.random.permutation(10)




