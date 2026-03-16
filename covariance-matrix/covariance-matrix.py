import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    
    X = np.asarray(X)
    N = X.shape[0] 
    
    if X.ndim <2:
        return None
    elif X.shape[0] <= 1:
        return None
    else :
        avg = X.mean(axis = 0)
        Xcnt = X - avg
        Cov = (Xcnt.T @ Xcnt)/(len(X) - 1)
        return Cov
    
    pass