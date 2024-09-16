from ad import *


def relu(u):
    return max(dual(0, 0), u)


def convnet(x):

    if len(x) > 5:
        raise Exception

    # Weights (w, v)
    w = [dual(1.2, 1), dual(-0.2, 0)]
    v = [dual(-0.3, 0), dual(0.6, 0), dual(1.3, 0), dual(-1.5, 0)]

    # Hidden Neurones (z)
    z = []
    for i in range(len(x)-1):
        d1 = dual(x[i], 0)
        d2 = dual(x[i+1], 0)
        z.append(relu(w[0]*d1 + w[1]*d2))

    # Model Output (y)
    y = relu(v[0]*z[0] + v[1]*z[1] + v[2]*z[2] + v[3]*z[3])

    return y, z
