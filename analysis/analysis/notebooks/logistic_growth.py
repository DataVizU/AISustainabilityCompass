import numpy as np


def logistic_growth(t, K, r, x0):
    return K / (1 + ((K - x0) / x0) * np.exp(-r * t))
