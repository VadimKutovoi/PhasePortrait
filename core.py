import matplotlib.pyplot as plt
import math
import random


def f(x, y):
    return -x * (1 + x * y) - 2 * y


def g(x, y):
    return x + y


if __name__ == '__main__':
    for i in range(0, 150):
        Xo = random.randint(-15, 15)
        Yo = random.randint(-15, 15)
        Y = []
        X = []
        h = 0.001
        for i in range(0, 100):
            k1 = h * f(Xo, Yo)
            q1 = h * g(Xo, Yo)

            k2 = h * f(Xo + k1 / 2.0, Yo + q1 / 2.0)
            q2 = h * g(Xo + k1 / 2.0, Yo + q1 / 2.0)

            k3 = h * f(Xo + k2 / 2.0, Yo + q2 / 2.0)
            q3 = h * g(Xo + k2 / 2.0, Yo + q2 / 2.0)

            k4 = h * f(Xo + k3, Yo + q3)
            q4 = h * g(Xo + k3, Yo + q3)

            Xo = Xo + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
            Yo = Yo + (q1 + 2.0 * q2 + 2.0 * q3 + q4) / 6.0

            X.append(Xo)
            Y.append(Yo)


        plt.plot(X, Y)

    plt.show()
