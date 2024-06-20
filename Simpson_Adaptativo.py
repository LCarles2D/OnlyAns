"""Aproximar la siguiente integral por Simpson Adaptativo a = 1 , b = 2  x**3 /  1 + x*1/2 
con una tolerancia de e= 10−3"""

import numpy as np
import sympy as sp
import funciones_herramientas
from funciones_herramientas import *


def integracion_simpson_adaptativo(funcion, a, b, error):
    x = sp.symbols("x")
    f = sp.lambdify(x, funcion)

    def simpson_compuesto(f, a, b):

        h = (b - a) / 2
        return (h / 3) * (f(a) + 4 * f((a + b) / 2) + f(b))
    
    def integral_adaptativa(f, a, b, error, I_total):

        I1 = simpson_compuesto(f, a, b)
        I2 = simpson_compuesto(f, a, (a + b) / 2)
        I3 = simpson_compuesto(f, (a + b) / 2, b) 

        error_estimado = abs(I1 - I2 - I3)
        
        if error_estimado < 15 * error:
            return I2 + I3 + (I2 + I3 - I1) / 15
        
        else:
            I_left = integral_adaptativa(f, a, (a + b) / 2, error / 2, I2)
            I_right = integral_adaptativa(f, (a + b) / 2, b, error / 2, I3)
            return I_left + I_right
    
    resultado = integral_adaptativa(f, a, b, error, simpson_compuesto(f, a, b))
    
    print(f"funcion = {funcion}\na = {a}\nb = {b}\ne = {error}\n")
    print(f"El resultado de la integración adaptativa de Simpson es: {resultado:.8f}")


x = sp.symbols("x")
funcion = (x**3) / (1 + x**1/2)
a = 1
b = 2
error = 1e-3  

integracion_simpson_adaptativo(funcion, a, b, error)

def Metodo_Trapecio(expresion, a, b, n):
    x, y = sp.symbols("x y")
    funcion, dicc, Error = validar_funcion(expresion)
    h = 0
    if n < 2 and n > 0:
        

    

