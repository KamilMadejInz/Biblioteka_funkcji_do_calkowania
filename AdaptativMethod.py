from SimpleTrap import  f_trapI
def f_adapt(f,a,b,tol,temp = "first"):
    """
            :param fun: funkcja
            :param a: dolny przedział całkowania
            :param b: górny przedział całkowania
            :param tol: tolerancja
            :return: przybliżona wartość całki
    """
    f_adapt.counter += 1

    print(f_adapt.counter)
    m = (a+b)/2.0
    P1 = f_trapI(f,a,b)
    P2 = f_trapI(f,a,m) + f_trapI(f,m,b)
    print(temp ,P1)
    print(temp,P2)
    if abs(P1 - P2 ) < 3 * tol:
        return P2
    else:
        return f_adapt(f,a,m,tol,temp = "LL") + f_adapt(f,m,b,tol,temp = "PP")

f_adapt.counter = 0