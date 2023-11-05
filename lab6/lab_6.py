import math
from abc import ABC, abstractmethod


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


quadratic_eq = QuadraticEquation(2, 3, 1)
result = quadratic_eq.value(4)
derivative_result = quadratic_eq.derivative(4)
print(result)
print(derivative_result)


class SinEquation(Equation):
    def __init__(self, a):
        self.a = a

    def value(self, x):
        return math.sin(self.a * x) / x

    def derivative(self, x):
        return (self.a * x * math.cos(self.a * x) - math.sin(self.a * x)) / x ** 2


sin_equation = SinEquation(5)
sin_result = sin_equation.value(6)
derivative_sin_result = sin_equation.derivative(6)
print(sin_result)
print(derivative_sin_result)
