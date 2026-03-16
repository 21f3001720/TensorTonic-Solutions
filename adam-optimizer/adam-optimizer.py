import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    param = np.asarray(param)
    grad = np.asarray(grad)
    m=np.asarray(m)
    v = np.asarray(v)
    t = np.asarray(t)
    if (grad == np.zeros(grad.shape)).all() :
        return (param, m, v)
    else:
        m_new = beta1*m +(1-beta1)*grad
        v_new = beta2*v +(1-beta2)*(grad**2)
        bias_corrected_m = m_new/(1-beta1**t)
        bias_corrected_v = v_new/(1-beta2**t)
        param_new = param - lr*(bias_corrected_m)/(np.sqrt(bias_corrected_v)+eps)
        return (param_new, m_new, v_new)    # Write code here
    pass