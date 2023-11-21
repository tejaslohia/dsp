'''
1. Vary the standard deviation.

For example, I can change the values of standard deviation such as [0.1,0.2,0.3] to represent different level of noises.

The Python code would be:   
'''
# x is my training data
# mu is the mean
# std is the standard deviation
mu=0.0
std = 0.1
def gaussian_noise(x,mu,std):
    noise = np.random.normal(mu, std, size = x.shape)
    x_noisy = x + noise
    return x_noisy 

'''
2. change the percentage of Gaussian noise added to data.
For example, I add 5% of gaussian noise to my data then change it to 10% etc. 
In this case, the Python code would look like:
'''
mu=0.0
std = 0.05 * np.std(x) # for %5 Gaussian noise
def gaussian_noise(x,mu,std):
    noise = np.random.normal(mu, std, size = x.shape)
    x_noisy = x + noise
    return x_noisy