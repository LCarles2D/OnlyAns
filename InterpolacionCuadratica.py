#!/usr/bin/env python3

import sympy as sp

def get_Bn(n1, n2, puntos, fx):
    return (fx[n2] - fx[n1])/(puntos[n2] - puntos[n1])


def interpolacionCuadratica(xk,yk, inter_point, ecuacion = None):

    
    x = sp.symbols("x")
    if ecuacion != None:
        yk = [ecuacion.subs(x, xi).evalf() for xi in xk]

  
    fx = yk
    b0 = fx[0]

    b1 = get_Bn(0, 1, xk, fx)
    b2 = (get_Bn(1,2, xk, fx) - b1) / (xk[2] - xk[0])
    Px = b0 + b1*(x - xk[0]) + b2*(x-xk[0])*(x-xk[1])
    Px = sp.simplify(Px)

    valor_aprox = Px.subs(x, inter_point).evalf()
    return Px, valor_aprox


x_array = [2,3,4]
y_array = [67, 91, 135]

x = sp.symbols("x")
Px, valor =interpolacionCuadratica(x_array, None, -1, sp.log(x))
print(Px, valor)
