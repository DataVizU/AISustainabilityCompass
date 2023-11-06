import numpy as np


def cal_x(h: float, l: float):
    n = 0.63
    k = (n - 1) / n

    return (h**k + l**k) ** (1 / k)


def ces(h: float, l: float, a: float):
    x = cal_x(h, l)
    return a * x


def ces_diff_h(h: float, l: float, a: float):
    n = 0.63
    k = (n - 1) / n

    return k * h ** (k - 1) * (a * k * (h**k + l**k) ** (k - 1))


def ces_diff_l(h: float, l: float, a: float):
    n = 0.63
    k = (n - 1) / n

    return k * k * a * l ** (k - 1) * (h**k + l**k) ** (k - 1)
