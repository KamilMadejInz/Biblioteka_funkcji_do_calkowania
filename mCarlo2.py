import numpy as np

def f_MonteC(f, a, b, n, *args):
    """
           :param f: funkcja
           :param a: dolny przedział całkowania
           :param b: górny przedział całkowania
           :param n: ilość losowych punktow
           :param *args: opcjonalne argumenty min, max
           :return: przybliżona wartość całki
           """

    # losowanie n dowolnych punktów z przedziału <a,b>
    X = np.random.uniform(a, b, n)

    Y = []
    # wartości funkcji w węzłach kwadratury
    for i in range(0, n):
        Y.append(f(X[i]))

    if len(args) == 0:
        minY = np.min(Y)
        maxY = np.max(Y)
    else:
        minY = args[0]
        maxY = args[1]

    # n losowych wartości z przedziału <0, maxY>
    Yi = np.random.uniform(minY, maxY, n)  ##To są losowe Y dla losowych X
    # obliczenie ułamka prawdopodobieństwa, że losowan punkt znajduje się pod wykresem funkcji f(x)
    k = 0

    #obliczanie punktów leżących nad osią OX i lęzących pod wykresem funkcji oraz obliczanie punktów znajdujących
    #się poniżej osi OX i lezących nad krzywą
    pos = np.where(np.logical_and(Yi > 0, Yi <= Y))
    neg = np.where(np.logical_and(Yi < 0, Yi >= Y))

    # zliczanie dodatnich punktów leżących nad krzywą
    k += np.count_nonzero(pos)
    k += np.count_nonzero(pos == 0)

    # zliczanie ujemnych punktów leżących nad krzywą
    k -= np.count_nonzero(neg)
    k +=  np.count_nonzero(neg == 0)

    # wartość przybliżona całki. k/n procent punktów znajdujących się w kwadracie (b-a)*maxY
    P = np.abs(b - a) * np.abs(maxY - minY)
    I = k / n * P
    return I
