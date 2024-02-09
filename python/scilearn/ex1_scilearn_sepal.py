from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

iris = datasets.load_iris()
x=iris.data[:,0] # First column width of Sepal
y=iris.data[:,1] # Second column height of Sepal
species=iris.target
x_min,x_max = np.min(x) - 0.5, np.max(x) + 0.5
y_min,y_max = np.min(y) - 0.5, np.max(y) + 0.5

#scalter plot
plt.figure()
plt.title('Iris Dataset - Classification By Sepal Sizes')
plt.scatter(x,y,c=species)
plt.xlabel("Sepal Width")
plt.ylabel("Sepal Height")
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.xticks(())
plt.yticks(())
plt.show()

