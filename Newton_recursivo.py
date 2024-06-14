#!/usr/bin/env python3

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

import sympy as sp

b_array = []

def Newton_recursivo(x_array, y_array=None, ecuacion = None, x_inter=None):
#Puntos a cambiar
    if y_array == None and ecuacion == None:
        raise ValueError(f'{Color.RED}ERROR | Debe de ingresar un array de "Y" o una ecuacion')
    if ecuacion != None and y_array != None:
        raise ValueError(f'{Color.RED}ERROR | Ingresas el array o ingresas la ecuacion, no se puede ambos')

    x = sp.symbols("x")
    ecuacion = sp.log(x)
    fx_array = y_array or [ecuacion.subs(x,xi).evalf() for xi in x_array]
    grado = len(x_array) - 1

    b0 = fx_array[0]
    global b_array
    b_array = [] 

    recursiva(x_array, fx_array, grado, 0)
    
#Inicializamos el array donde guardare los factores, los incializare con 1 para poder multiplicarlo con el anterior (Nose si esta sea la mejor opcion, porque si directamente los agrego no podria luego meterlos en orden)
    factor = [1 for i in range(0, grado)]


    Px = b0
    for i in range(1, grado+1):
        for j in range(0,i):
            factor[i-1] = (factor[i-1] * (x - x_array[j]))
        Px +=  b_array[i] * factor[i-1]

    Px = sp.expand(Px)
    Px = sp.simplify(Px)
    if x_inter == None:
        return Px
    raiz = Px.subs(x,x_inter).evalf()
    return [Px, raiz]




def recursiva(x_array, fx_array,grado, i=0):
    global b_array
    if grado+1 == i:
        return
    if i == 0:
        b_array.append(fx_array[0])
        recursiva(x_array, fx_array,grado, 1)
        return
    elif i == 1:
        b_array.append((fx_array[i] - b_array[i-1])/(x_array[i]- x_array[0]))
        recursiva(x_array, fx_array, grado, 2)
        return
    b_array.append((((fx_array[i] - fx_array[i-1])/(x_array[i] - x_array[i-1])) - b_array[i-1])/(x_array[i] - x_array[0]))
    recursiva(x_array, fx_array, grado, i+1)


x= sp.symbols('x')
x_a = [1,2,3,4]
y = [2,3,4,5]
Px, raiz= Newton_recursivo(x_a, y, None, 1)
print(Px, raiz)
