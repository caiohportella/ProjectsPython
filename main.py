import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import quad
import numpy as np
import UserGUI, Lib

user = UserGUI.UserGUI
math = Lib.MathMaker

def main():
	def f(x):
		return x**2 + 9

	x = sp.Symbol('x')
	q = user.user_input()

	math(q[0], q[1], q[2], q[3], q[4])
	print(q)
	print(quad(f, 1, 3))




	#print(integrate(1/sqrt(3 - x), (x, 0, 3)))

if __name__ == '__main__':
	main()

"""
x = np.linspace(0, 2, 1000)
plt.plot(x, f(x))
plt.fill_between(x, f(x), where=[(x > 0) and (x < 2) for x in x])
plt.show()
"""