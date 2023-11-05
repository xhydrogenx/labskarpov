import math
from abc import ABC, abstractmethod

import numpy as np
from matplotlib import pyplot as plt


class Equation(ABC):
    @abstractmethod
    def value(self, x):
        pass

    @abstractmethod
    def derivative(self, x):
        pass


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def derivative(self, x):
        return 2 * self.a * x + self.b


class SinEquation(Equation):
    def __init__(self, a):
        self.a = a

    def value(self, x):
        return math.sin(self.a * x) / x

    def derivative(self, x):
        return (self.a * x * math.cos(self.a * x) - math.sin(self.a * x)) / x ** 2


def plot_equation(equation, x1, x2, num_points=1000):
    x_values = np.linspace(x1, x2, num_points)
    y_values = [equation.value(x) for x in x_values]

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.grid()
    plt.show()


quadratic_eq = QuadraticEquation(2, 3, 1)
plot_equation(quadratic_eq, -5, 5)

sine_over_x_eq = SinEquation(2)
plot_equation(sine_over_x_eq, 0.01, 5)
