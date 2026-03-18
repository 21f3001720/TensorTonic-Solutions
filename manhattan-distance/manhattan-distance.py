import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)
    sum_abs_diff = sum(abs(x - y))
    return int(sum_abs_diff)
    pass
    