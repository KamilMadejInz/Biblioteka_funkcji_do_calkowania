import numpy as np

def f_gauss_legrande(f,a,b,n):
    """
          :param fun: funkcja
          :param a: dolny przedział całkowania
          :param b: górny przedział całkowania
          :param n: ilość podprzedziałów, na które dzielimy odcinek <a,b>
          :return: przybliżona wartość całki
          """

    half = float(b-a)/2
    mid = (a+b)/2
    [t,w] = np.polynomial.legendre.leggauss(n)

    I = 0
    for i in range(n):
        I += w[i] * f(mid+half*t[i])

    I *= half

    return I
