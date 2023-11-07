import pytest
import math


def solve_quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент a должен быть не равен 0")

    D = b * b - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return [x1, x2]
    elif D == 0:
        return [-b / (2 * a)]
    else:
        return [None]


class TestSolveQuadraticEquation(object):

    def test_positive(self):
        assert solve_quadratic_equation(1, 2, 1) == [-1]

    def test_negative(self):
        assert solve_quadratic_equation(-1, 2, 1) == [1, 1]

    def test_zero(self):
        assert solve_quadratic_equation(0, 2, 1) == [None]


if __name__ == "__main__":
    pytest.main()
