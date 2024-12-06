# Metodo_EcuacionesCuadraticas.py
import sympy as sp
from sympy import symbols, solve
import herr_polinomios 
from herr_polinomios import *

def Metodo_ECuadratica(expresion):
    x = symbols("x")
    print(f"expresion: {expresion}, type: {type(expresion)}")
    expresion_ig = validar_igualdad(expresion)
    funcion = validar_funcion(expresion_ig)
    print("funcion: ",funcion)
    coeficientes = obtener_coeficientes(funcion)
    print("coeficientes: ",coeficientes, "type: ",type(coeficientes))
        
    """else:
        print("Error: expresion no valida")    """

    grado = obtener_grado(funcion)
    print("grado: ",grado)
    #validar grado de la funcion
    if not grado == 2:  #el grado de la funcion es distinta de ^2
        print("Error: grado invalido: el grado de la funcion es distinta de ^2")
        exit()

    #guardar valores
    A, B, C = coeficientes

    # Resolver la ecuación
    x1 = sp.simplify((-B + sp.sqrt(B**2 - 4*A*C)) / (2*A))
    x2 = sp.simplify((-B - sp.sqrt(B**2 - 4*A*C)) / (2*A))

    x1_exacto = sp.N(x1, 5)
    x2_exacto = sp.N(x2, 5)
    
    print("funcion: ",expresion)
    print("Coefientes: ",coeficientes)
    print("grado: ",grado)
    print(f"x1 : {x1_exacto}")
    print(f"x2 : {x2_exacto}")
    
    valores_x = []
    valores_x.append(x1_exacto) 
    valores_x.append(x2_exacto)
    raices_validadas = validar_raices(valores_x)
    impr_grafico(expresion, funcion, raices_validadas)
    
    
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#Prueba
funcion = "x**2 + 2*x - 4"
Metodo_ECuadratica(funcion)
