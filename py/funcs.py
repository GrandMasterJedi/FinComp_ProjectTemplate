import numpy as np

def cont_return(price):
    ret = np.log(price / price.shift(periods=1))
    return ret