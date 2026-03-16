def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    step = 0
    while step < steps :
        xnew = x0 - lr*(2*a*x0 + b)
        x0 = xnew
        step = step + 1
    return x0
    
    pass