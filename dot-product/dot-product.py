import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    if x.shape[0]==y.shape[0]:
        return np.dot(x,y)
    else:
        raise ValueError("Input arrays must have the same length")
    # Write code here
    pass