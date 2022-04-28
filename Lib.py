from sympy import sympify, var, solve
import matplotlib.pyplot as plt
import numpy as np

class MathMaker:
    #variables = var('a, b, c, d, e, w, x, y, z')

    def __init__(self, _a, _b, _dx, _nt, _nd):
        self.a = _a
        self.b = _b
        self.dx = _dx
        self.nt = _nt
        self.nd = _nd

    def convertToFunction(self):
        exp = sympify(self.dx)

        return exp