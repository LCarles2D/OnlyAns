import sympy as sp
import herr_polinomios
from herr_polinomios import *
import pandas as pd

def Metodo_Trapecio_Compuesto(expresion, lim_a, lim_b, listx, listy):
    #resive expresion str y dos listas de float
    listax = []
    listay = []
    listax = listx
    listay = listy
    
    if not len(listax) == len(listay):
        impr("La cantidad de elemtos x, es diferente a la cantidad de elementos f(x)")
        exit()
    
    if len(listax) <= 2 and len(listay) <= 2:
        Metodo_Trapecio_Simple(expresion, lim_a, lim_b, x0 = listax[0], x1 = listax[1], y0 = listay[0], y1 = listay[1])    

    #   impr(f"lista x: con {len(listax)} elementos")
    #   impr(f"lista y: con {len(listay)} elementos")

    




def Metodo_Trapecio_Simple(expresion, lima, limb, x0 = None, x1 = None, y0 = None, y1 = None):
    x = sp.symbols("x")
    expresion_ig = validar_igualdad(expresion)
    funcion = validar_funcion(expresion_ig)
    eval_final = 0.0
    #Si viene desde trapecio complejo o desde simple 
    valores_eval = []
    funcion_eval = []
    if not (x0 or x1 or y0 or y1) == None:
        x_0 = validar_numero_float(x0, "Error: validar_numnero_float: No se puedo validar x0")
        x_1 = validar_numero_float(x1, "Error: validar_numnero_float: No se puedo validar x1")
        y_0 = validar_numero_float(y0, "Error: validar_numnero_float: No se puedo validar y0")
        y_1 = validar_numero_float(y1, "Error: validar_numnero_float: No se puedo validar y1")

        eval_final = (x_1 - x_0)*((y_0 + y_1)/2)
        data = {'Iter': [0, 1], 'X_n': [x_0, x_1], 'f(X_n)': [y_0, y_1]}
        df = pd.DataFrame(data)
        impr("Tabla de evaluación:")
        print(df.to_string(index=False))

    else: 
        lim_a, lim_b = validar_limites(lima, limb)
        
        # validar lim_a y lim_b
        if lim_a is None or lim_b is None:
            impr("Error: validar_limites: el limite inferior o superior")
            exit()
        
        # evaluar en funcion
        valores_eval = [lim_a, lim_b]
        funcion_eval = [funcion.subs(x, valor) for valor in valores_eval]
    
        eval1, eval2 = funcion_eval
        eval_final = (lim_b - lim_a)*((eval1 + eval2)/2)

        impr(f"funcion: {expresion_ig} evaluada desde {lim_a}, hasta {lim_b}: {eval_final}")

expresion = "E**x**4"
lim_a = -1
lim_b = 1
lista_x = 0, 3, 1
lista_y = 4, 7, 4
#   Metodo_Trapecio_Simple(expresion, lim_a, lim_b)
Metodo_Trapecio_Compuesto(expresion, lim_a, lim_b, lista_x, lista_y)

"""def Metodo_Trapeciosimple(expresion, lim_a, lim_b, grad):
    x = sp.symbols("x")
    grado = 0
    lim_A = 0
    lim_B = 0
    
    #validaciones
    expresion_val_igu = validar_igualdad(expresion)
    funcion = validar_funcion(expresion_val_igu)
    if isinstance(grad, int):
        grado = grad
    else:
        grado = validar_numero_int(grad, ":validacion de grado")

    lim_A, lim_B, error = validar_limites(lim_a, lim_b)
    if error:
        impr("Errror: validar_limites: ",error)

    impr("funcion: ", funcion)
    impr("grado: ", grado)
    impr("limite inferior: ", lim_A)
    impr("limite superior: ", lim_B)

    a = lim_A
    b = lim_B
    h = 
"""
