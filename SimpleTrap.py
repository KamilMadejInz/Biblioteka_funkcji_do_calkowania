def f_trapI(f,xa,xb):
    h = xb-xa
    I = h*(f(xa) + f(xb))/2
    return I