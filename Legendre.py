from math import factorial
import numpy as np


def pretty_polynomial(polynomial):
    """
    Takes a list of coefficients (must be in ascending powers of x) and produces a 'pretty' output. 
    :param polynomial: the list of coefficients of a polynomial
    :return: a string of the polynomial in a more readable format. 
    """
    s = ''
    for i in range(1, len(polynomial)):
        if polynomial[i] > 0:
            s += ' + ' + str(polynomial[i]) + 'x^' + str(i)
        elif polynomial[i] < 0:
            s += '  ' + str(polynomial[i]) + 'x^' + str(i)

    # If the constant is nonzero, prepend it to the string. Otherwise, get rid of the '+'.
    if polynomial[0]:
        s = str(polynomial[0]) + s
    else:
        s = s[2:]
    return s


def legendre_polynomial(n: int):
    """
    Calculate the coefficients of the nth order Legendre polynomial in x, using
    the Rodrigues formula: P_n(x) = 1/(2^n n!) (d/dx)^n [(x^2 - 1)^n].
    
    We will treat polynomials as lists in python, where the index in the list corresponds to the power 
    of x, so the element in the list contains the coefficient of x^i. Thus our polynomials will be 
    written in ascending powers of x, somewhat contrasting convention. All our operations will therefore
    be reduced to list methods. 
    
    :param n: the order of the Legendre polynomial whose coefficients are to be determined
    :return: a list of coefficients in ascending powers of x. 
    """
    # 1. Expand (x^2 - 1) ^ n with the binomial theorem.
    expansion = [None] * (n + 1)
    for i in range(len(expansion)):
        expansion[i] = (-1)**(n - i) * factorial(n) / (factorial(i) * factorial(n - i))

    # Because the brackets contain x^2, the expansion will only have even powers of x.
    # However, we need the odd powers too (which are all zero). 2n + 1 terms in total.
    coeffs = [None] * (2*n + 1)
    coeffs[::2] = expansion
    coeffs[1::2] = [0] * n

    # 2. Differentiate n times. Differentiating is the same as multiplying each element
    # by its index (remember this is the power of x), then deleting the first term in the list.
    for _ in range(n):
        coeffs = [i * coeffs[i] for i in range(1, len(coeffs))]

    # Don't forget the normalising constant in the Rodrigues formula.
    # The below code is the same as [x / (2**n * factorial(n)) for x in coeffs].
    return list(map(lambda x: x / (2**n * factorial(n)), coeffs))


def legendre_representation(poly):
    """
    Any polynomial can be written in terms of Legendre polynomials. 
    :param poly: A list or np array of coefficients of the polynomial
    :return: A list of coefficients of the Legendre polynomials, 
    e.g [3, 1, 0, 4] <=> 3P_0(x) + P_1(x) + 4P_3(x)
    """
    if not isinstance(poly, np.ndarray):
        poly = np.array(poly)
    n = len(poly) - 1
    legendre_coefficients = [0] * (n + 1)

    while n >= 0:
        Pn = legendre_polynomial(n)
        legendre_coefficients[n] = poly[n]/Pn[n]
        if n == len(poly) - 1:
            poly = poly - [legendre_coefficients[n] * x for x in Pn]
        else:
            poly[:n+1] = poly[:n+1] - [legendre_coefficients[n] * x for x in Pn]
        n -= 1

    return legendre_coefficients


