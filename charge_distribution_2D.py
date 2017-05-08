from point_charges_2D import Charge


def line_charge(start, end, res, Q):
    """
    A line of charge
    :param start: the coordinates (as a tuple/list) for the starting point of the line
    :param end: the coordinates (as a tuple/list) for the end point of the line 
    :param res: number of point charges per unit length
    :param Q: total charge on the line
    """
    length = ((end[1] - start[1])**2 + (end[0] - start[0])**2)**0.5
    gradient = (end[1] - start[1]) / (end[0] - start[0])
    intercept = start[1] - gradient * start[0]

    lambd = Q / length
    for i in range((end[0]-start[0])*res):
        Charge(lambd, [i/res + start[0], gradient * (i/res) + intercept])


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
            Charge(sigma, [i/res - corner[0], j/res - corner[1]])
