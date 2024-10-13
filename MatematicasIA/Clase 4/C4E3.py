import sympy as sp
from scipy.optimize import linprog


C = [-10, -15]

A = [[2,1], [1,2]]

B= [20, 15]

x0_borde = (0, None)
x1_borde = (0,None)

result = linprog(C, A_ub=A , b_ub=B, bounds=[x0_borde, x1_borde], method = "highs")

print(-result.fun)