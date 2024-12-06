import sympy as sp
import herr_polinomios
from herr_polinomios import validar_funcion, validar_expresion, obtener_grado, obtener_coeficientes

x = sp.simplify("x")
expresion = "x**2 + 4*x +3"
funcion = sp.sympify(expresion)
funcion_validada = validar_funcion(funcion)
print("funcion validada: ",funcion_validada)
expresion_evaluada = validar_expresion(expresion)
print("la expresion es valida: ",expresion_evaluada)
grado = obtener_grado(funcion)
print("grado: ",grado)

a = -3
b = 2
c = 1
d = -2

p = ((8*b)-(3*a**2))/8
q = ((8*c) - (4*a*b) + (a**3))/8
R = ((256*d) - (64*a*c) + (16*a**2*b) - (3*a**4))/256
U = sp.symbols("U")
expresion_u = f"(U**3) - (({p}/2)*U**2) - ({R}*U) + (((4*{p}*{R}) - ({q}**2))/8)"
print(expresion_u, "type: ",type(expresion_u))
funcion_u = validar_funcion(expresion_u)
print(funcion_u, "type: ",type(funcion_u))
coeficientes_u = obtener_coeficientes(funcion_u)
grado_ = obtener_grado(funcion_u)
print("grado: ",grado_)