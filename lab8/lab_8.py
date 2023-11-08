import math
from abc import ABC, abstractmethod

import numpy as np
from matplotlib import pyplot as plt


# Важная особенность - в Python нет обработчиков событий в чистом виде, так как код выполняется по порядку и без
# использования асинхронных фуункций подобного функционала не добиться


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


class Integrator(ABC):
    def __init__(self, equation, a, b, h=None, N=None):
        self.equation = equation
        self.a = a
        self.b = b

        if h is not None:
            self.h = h
            self.N = None
        elif N is not None:
            self.h = (b - a) / N
            self.N = N
        else:
            raise ValueError("Нужно указать h или N")

    @abstractmethod
    def integrate(self):
        pass

    @abstractmethod
    def get_method_name(self):
        pass


class RectangleIntegrator(Integrator):
    def integrate(self):
        result = 0
        x = self.a
        integration_result = ""
        with open('rect_integration_results.txt', 'w') as f:
            f.truncate(0)
            while x < self.b:
                result += self.equation.value(x) * self.h
                f.write(f"x = {x:.4f}, y = {result:.4f}\n")
                integration_result += f"x = {x:.4f}, y = {result:.4f}\n"
                x += self.h
        print(f"Метод прямоугольников: {integration_result}")
        return result, integration_result

    def get_method_name(self):
        return "Метод прямоугольников"


class TrapezoidIntegrator(Integrator):
    def integrate(self):
        result = 0
        x = self.a
        integration_result = ""
        with open('trapezoid_integration_results.txt', 'w') as f:
            # truncate позволяет очищать файл перед тем как записывать новые значения
            f.truncate(0)
            while x < self.b:
                result += (self.equation.value(x) + self.equation.value(x + self.h)) * self.h / 2
                f.write(f"x = {x:.4f}, y = {result:.4f}\n")
                integration_result += f"x = {x:.4f}, y = {result:.4f}\n"
                x += self.h
        print(f"Метод трапеций: {integration_result}")
        return result, integration_result

    def get_method_name(self):
        return "Метод трапеции"


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

quadratic_eq = QuadraticEquation(2, 3, 1)

rect_integrator = RectangleIntegrator(quadratic_eq, 0, 4, h=0.1)
result_rect = rect_integrator.integrate()
print("Результат интегрирования методом прямоугольников:", result_rect[0])

trapezoid_integrator = TrapezoidIntegrator(quadratic_eq, 0, 4, N=100)
result_trap = trapezoid_integrator.integrate()
print("Результат интегрирования методом трапеций:", result_trap[0])
