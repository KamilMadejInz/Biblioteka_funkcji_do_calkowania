def f_simp2I(f,a,b,n):
    """
        :param fun: funkcja
        :param xa: dolny przedział całkowania
        :param xb: górny przedział całkowania
        :param n: ilość podprzedziałów, na które dzielimy odcinek <a,b>
        :return: przybliżona wartość całki
        """
    # szerokość pojedynczego przedziału
    h = (b-a)/n

    # Przypisanie wartości funkcji pierwszego i ostatniego węzła
    I = f(a) + f(b)

    # obliczenie przybliżonej wartości całki.
    for i in range(1,n):
        if i%2==1:
            I += 4 * f(a + i*h)
        else:
            I += 2 * f(a +i*h)

    I = h/3 * I
    return I