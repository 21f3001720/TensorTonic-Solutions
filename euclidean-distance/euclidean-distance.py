import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    if x.shape[0] == y.shape[0] :
        diff_vec = x-y
        return np.sqrt(sum(diff_vec*diff_vec))
    else:
        raise ValueError("Input arrays must have the same length")
    pass