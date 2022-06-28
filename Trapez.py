import numpy as np

def f_trapI(f, a, b, n):
    """
    :param fun: funkcja
    :param xa: dolny przedział całkowania
    :param xb: górny przedział całkowania
    :param n: ilość podprzedziałów, na które dzielimy odcinek <a,b>
    :return: przybliżona wartość całki
    """
    # szerokość pojedynczego przedziału
    h = (b - a) / n

    # linspace() zwraca n równo rozmieszczonych punktów z przedziału <a + 0.5 * h, b - 0.5 * h>
    X = np.linspace(a, b, num=n + 1)

    Y = []
    # umieszczenie w tablicy Y wartości funkcji dla każdego xi
    for i in range(0, n + 1):
        Y.append(f(X[i]))

    # konwertowanie tablicy Y na tablicę NumPy, którą da się przemnożyć przez liczbę
    Y = np.array(Y)

    # obliczenie przybliżonej wartości całki.
    I = []
    for i in range(0, n + 1):
        if i == 0 or i == n:
            I.append(h * Y[i] / 2)
        else:
            I.append(h * Y[i])

    I = np.sum(I)
    return I



