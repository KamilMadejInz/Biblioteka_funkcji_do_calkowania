from SimpleTrap import  f_trapI
def f_adapt(f,a,b,tol):
    """
            :param fun: funkcja
            :param a: dolny przedział całkowania
            :param b: górny przedział całkowania
            :param tol: tolerancja
            :return: przybliżona wartość całki
    """
    m = (a+b)/2.0
    P1 = f_trapI(f,a,b)
    P2 = f_trapI(f,a,m) + f_trapI(f,m,b)
    if abs(P1 - P2 ) < 3 * tol:
        return P2
    else:
        return f_adapt(f,a,m,tol) + f_adapt(f,m,b,tol)
