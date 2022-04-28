import Lib
from sympy import sympify, var

class UserGUI:
	variables = var('a, b, w, x, y, z')
	math = Lib.MathMaker

	def user_input():
		try:
			a = float(input("Digite o valor de A: "))
			b = float(input("Digite o valor de B: "))
			dx = input("Digite a funcao: ")
			nt = int(input("Digite o numero de trapezios: "))
			nd = int(input("Digite o numero limite de casas decimais: "))
		except ValueError:
			print("Numero invalido.\n")
		
		return dx
		#return [a, b, dx, nt, nd]