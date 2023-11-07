import pytest
import math
from lab6.lab_6 import RectangleIntegrator, TrapezoidIntegrator, QuadraticEquation


# Импортирование классов из лабораторной работы 6

class TestRectangleIntegrator:
    def test_integration(self):
        equation = QuadraticEquation(2, 3, 1)
        rect_integrator = RectangleIntegrator(equation, 0, 4, h=0.1)
        result = rect_integrator.integrate()
        assert math.isclose(result, 68.48000000000005, abs_tol=0.01)  # abs_tol=0.01 - заданная погрешность


class TestTrapezoidIntegrator:
    def test_integration(self):
        equation = QuadraticEquation(2, 3, 1)
        trap_integrator = TrapezoidIntegrator(equation, 0, 4, N=100)
        result = trap_integrator.integrate()
        assert math.isclose(result, 70.66880000000006, abs_tol=0.01)


if __name__ == '__main__':
    pytest.main()
