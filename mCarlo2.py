import numpy as np


def f_MonteC(f, a, b, n,min,max):
    """
           :param f: funkcja
           :param a: dolny przedział całkowania
           :param b: górny przedział całkowania
           :param n: ilość losowych punktow
           :param min: minimalna wartość funkcji
           :param max: maksymalna wartość funkcji
           :return: przybliżona wartość całki
           """
    minY = min
    maxY = max

    # losowanie n dowolnych punktów z przedziału <a,b>
    X = np.random.uniform(a, b, n)

    Y = []
    # wartości funkcji w węzłach kwadratury
    for i in range(0, n):
        Y.append(f(X[i]))

    # n losowych wartości z przedziału <0, maxY>
    Yi = np.random.uniform(minY, maxY, n)  ##To są losowe Y dla losowych X
    # obliczenie ułamka prawdopodobieństwa, że losowan punkt znajduje się pod wykresem funkcji f(x)
    k = 0
    for i in range(0, n):
        if (Yi[i] > 0) and (Yi[i] <= Y[i]):
            k += 1
        elif (Yi[i] < 0) and (Yi[i] >= Y[i]):
            k -= 1
    # wartość przybliżona całki. k/n procent punktów znajdujących się w kwadracie (b-a)*maxY
    P = np.abs(b - a) * np.abs(maxY - minY)
    I = k / n * P
    return I
