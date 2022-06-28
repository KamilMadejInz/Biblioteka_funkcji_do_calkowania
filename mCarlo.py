import numpy as np
def f_crudeMonteC(f,a,b,n):
    """
          :param fun: funkcja
          :param a: dolny przedział całkowania
          :param b: górny przedział całkowania
          :param n: ilość losowych punktow
          :return: przybliżona wartość całki
          """
    # szerokość pojedynczego przedziału
    h = (b - a) / n

    #Results are from the “continuous uniform” distribution over the stated interval.
    # To sample  multiply the output of random_sample by (b-a) and add a:
    # losowanie n dowolnych punktów z przedziału <a,b>
    X = (b-a)*np.random.random_sample(n)+a
    Y = []

    # wartości funkcji w węzłach kwadratury
    for i in range(0, n):
        Y.append(f(X[i]))

    # konwertowanie tablicy Y na tablicę NumPy, którą da się przemnożyć przez liczbę
    Y = np.array(Y)

    # wartość przybliżona całki
    I = h*Y
    I = np.sum(I)
    return I
