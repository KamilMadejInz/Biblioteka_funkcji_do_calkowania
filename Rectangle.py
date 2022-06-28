import numpy as np

def f_rectI(f,a,b,n):
    """
    :param fun: funkcja
    :param a: dolny przedział całkowania
    :param b: górny przedział całkowania
    :param n: ilość podprzedziałów, na które dzielimy odcinek <a,b>
    :return: przybliżona wartość całki
    """

    # szerokość pojedynczego przedziału
    h = (b - a) / n

    # zwraca n równo rozmieszczonych punktów z przedziału <a,b>
    X = np.linspace(a + 0.5 * h, b - 0.5 * h, num=n)

    # Lista wartości funkcji w punktach Xi
    Y = []
    for i in range(0, n):
        Y.append(f(X[i]))

    # konwertowanie listy na Listę NumPy, którą da się przemnożyć przez liczbę
    Y = np.array(Y)

    # wartość przybliżona całki
    I = h * Y
    I = np.sum(I)
    return I







