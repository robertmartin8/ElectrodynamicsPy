from point_charges_2D import Charge


def straight_line_charge(start, end, res=40, Q=10):
    """
    A straight line of charge
    :param start: the coordinates (as a tuple/list) for the starting point of the line
    :param end: the coordinates (as a tuple/list) for the end point of the line 
    :param res: number of point charges per unit length
    :param Q: total charge on the line
    """
    length = ((end[1] - start[1])**2 + (end[0] - start[0])**2)**0.5
    gradient = (end[1] - start[1]) / (end[0] - start[0])
    intercept = start[1] - gradient * start[0]

    lambd = Q / length
    for i in range(int((end[0] - start[0])*res)):
        Charge(lambd, [i/res + start[0], gradient * (i/res) + intercept])


def line_charge(parametric_x, parametric_y, trange, res, Q):
    """
    Any line of charge, where the line is specified by parametric equations in t. 
    :param parametric_x: x(t)
    :param parametric_y: y(t)
    :param trange: the range of t values
    :param res: how many point charges should be plotted per unit t
    :param Q: the total charge of the line
    """
    for t in range(int(trange * res)):
        Charge(Q/res, [parametric_x(t/res), parametric_y(t/res)])

# Example
"""
import numpy as np

Charge.reset()
xs = ys = [-2, 2]

line_charge(parametric_x=lambda t: np.cos(t), parametric_y=lambda t: np.sin(t), trange=2*np.pi, res=100, Q=10 )
Charge.plot_field(xs, ys)
"""


def rectangle_charge(dim, corner, res, Q):
    """
    A rectangle of charge
    :param dim: the dimensions of the rectangle, as a tuple or list. 
    :param corner: the coordinates of the lower left corner of the rectangle
    :param res: number of point charges per unit length
    :param Q: the total charge of the rectangle
    """
    sigma = Q / (dim[0] * dim[1] * res**2)
    for i in range(int(dim[0] * res)):
        for j in range(int(dim[1] * res)):
            Charge(sigma, [i/res + corner[0], j/res + corner[1]])

# Example
"""
Charge.reset()
xs = ys = [-2, 2]

rectangle_charge([1, 1], [-0.5, -0.5], res=80, Q=100)
Charge.plot_field(xs, ys)
"""
