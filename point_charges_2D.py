import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')


class Charge:
    # Registry will store the instances of Charge, i.e it will keep track of how many
    # charges we have created
    registry = []

    def __init__(self, q, pos):
        """
        Initialise the charge
        :param q: value of q 
        :param pos: position of source charge
        """
        self.q = q
        self.pos = pos
        self.registry.append(self)

    def field(self, x, y):
        """
        Calculates the electric field of the charge at point (x,y). 
        :param x: x coordinate in field
        :param y: y coordinate in field
        :return: Ex and Ey, the horizontal and vertical components of the field at (x,y).
        """
        Ex = self.q * (x - self.pos[0]) / ((x - self.pos[0])**2 + (y - self.pos[1])**2) ** 1.5
        Ey = self.q * (y - self.pos[1]) / ((x - self.pos[0])**2 + (y - self.pos[1])**2) ** 1.5

        return Ex, Ey

    def potential(self, x, y):
        """
        Calculates the electric potential of the charge at point (x,y). 
        :param x: x coordinate in field
        :param y: y coordinate in field
        :return: the value of the potential
        """
        V = self.q / np.sqrt((x - self.pos[0])**2 + (y - self.pos[1])**2)
        return V

    @staticmethod
    def E_total(x, y):
        """
        Calculates the total electric field at (x,y), by superposing the present fields. 
        :param x: x coordinate
        :param y: y coordinate
        :return: the x and y components of the total electric field 
        """
        Ex_total, Ey_total = 0, 0
        for C in Charge.registry:
            Ex_total += C.field(x, y)[0]
            Ey_total += C.field(x, y)[1]
        return [Ex_total, Ey_total]

    @staticmethod
    def V_total(x, y):
        """
        Calculates the total electric potential at (x,y), by superposing the present potential
        :param x: x coordinate
        :param y: y coordinate
        :return: the total potential at the point
        """
        V_total = 0
        for C in Charge.registry:
            V_total += C.potential(x, y)
        return V_total

    @staticmethod
    def reset():
        """
        :return: Empties the charge registry
        """
        Charge.registry = []

    @staticmethod
    def plot_field(xs, ys, show_charge=True, field=True, potential=False):
        """
        Creates very basic plots
        :param xs: 2d list/tuple of x plotting range
        :param ys: 2d list/tuple of y plotting range
        :param show_charge: Whether or not the point charges should be displayed
        :param field: If true, plots the field lines
        :param potential: If true, plots the equipotentials (this is far from perfect). 
        :return: A stream plot and/or contour plot. 
        """
        plt.figure()
        if show_charge:
            for C in Charge.registry:
                # The colour will depend on the charge, and the size will depend on the magnitude
                if C.q > 0:
                    plt.plot(C.pos[0], C.pos[1], 'bo', ms=6*np.sqrt(C.q))
                if C.q < 0:
                    plt.plot(C.pos[0], C.pos[1], 'ro', ms=6*np.sqrt(-C.q))

        x, y = np.meshgrid(np.linspace(xs[0], xs[1], 1000),
                           np.linspace(ys[0], ys[1], 1000))

        if field:
            Ex, Ey = Charge.E_total(x, y)
            plt.streamplot(x, y, Ex, Ey, color='g')
            plt.draw()
            plt.show()
        if potential:
            # I have to multiply by 100 to get the potentials visible.
            V = 100*(Charge.V_total(x, y))
            V[V > 10000] = 10000
            plt.contour(x, y, V, 10)


# Demonstration
Charge.reset()
A = Charge(1, [0, 0])
B = Charge(4, [1, 0])

xs = [-2, 2.5]
ys = xs
Charge.plot_field(xs, ys, show_charge=False, field=True, potential=True)


