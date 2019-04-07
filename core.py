import matplotlib.pyplot as plt
import math
import random


def f(x, y):
    return y


def g(x, y):
    return -x - y * y * y


if __name__ == '__main__':
    Y = []
    X = []

    for i in range(0, 150):
        Xo = random.randint(-15, 15)
        Yo = random.randint(-15, 15)
        _X, _Y = [], []
        _X.append(Xo)
        _Y.append(Yo)

        h = 0.001
        for i in range(0, 10000):
            k1 = h * f(Xo, Yo)
            q1 = h * g(Xo, Yo)

            k2 = f(Xo + k1 * h / 2.0, Yo + q1 * h / 2.0)
            q2 = g(Xo + k1 * h / 2.0, Yo + q1 * h / 2.0)

            k3 = f(Xo + k2 * h / 2.0, Yo + q2 * h / 2.0)
            q3 = g(Xo + k2 * h / 2.0, Yo + q2 * h / 2.0)

            k4 = f(Xo + h * k3, Yo + h * q3)
            q4 = g(Xo + h * k3, Yo + h *q3)

            Xo = Xo + h * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
            Yo = Yo + h * (q1 + 2.0 * q2 + 2.0 * q3 + q4) / 6.0

            _X.append(Xo)
            _Y.append(Yo)
        X.append(_X)
        Y.append(_Y)

    #print(X, Y)
    for i in range(len(X)):
        plt.plot(X[i], Y[i], color='blue')
    plt.show()
