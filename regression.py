import numpy as np

def myregression(y:np.array, x:np.array, constant=True):
    ''' Returns regression thetas'''
    if constant:
        ones = np.ones(x.shape[0]).reshape(x.shape[0], 1)
        x = np.hstack((ones, x))
    return np.linalg.inv((x.T.dot(x))).dot(x.T).dot(y)