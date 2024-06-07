import math as math
import sympy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
import ctypes
from sympy.parsing.sympy_parser import parse_expr

def Diferencias_Finitas(funcion,punto,h,hacia_atras,hacia_adelante,centrales,tres_puntos,cinco_puntos,primera_derivada,segunda_derivada,tercera_drivada,cuarta_derivada,h_valor_list,formula_uno,formula_dos,formula_tres,formula_cuatro,formula_cinco):

    x = sp.symbols("x") 
    f = sp.lambdify(x,funcion)
    evaluado = []
    if hacia_atras == True:

        if primera_derivada  == True:
            if formula_uno:
                for h in h_valor_list:
                    formula = (f(punto) - f(punto - h)) / (h) 
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula = ((3 * f(punto)) - (4 * f(punto - h)) + (f(punto - 2*h))) / (2 * h)
                    evaluado.append(formula)
                return evaluado

        elif segunda_derivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = (f(punto) - (2 * f(punto - h)) + (f(punto - 2*h))) / (h**2)
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula = ((2* f(punto)) - (5 * f(punto - h)) + (4 * f(punto - 2 * h)) - (f(punto - 3* h))) / (h**2) 
                    evaluado.append(formula)
                return evaluado

        elif tercera_drivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = ((f(punto)) - (3 * f(punto - h)) + (3 * f(punto - 2*h)) - (f(punto - 3*h))) / (h**3)
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula = ((5 * f(punto)) - (18 * f(punto- h)) + (24 * f(punto - 2*h)) - (14 * f(punto - 3*h)) + (3 * f(punto- 4*h)) ) / (2 * h**3)
                    evaluado.append(formula)
                return evaluado
            

          
        elif cuarta_derivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = ((f(punto)) - (4 * f(punto - h)) + (6 * f(punto - 2*h)) -(4 * f(punto- 3*h)) + (f(punto - 4*h))) / (h**4) 
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula =  ((3 * f(punto)) - (14 * f(punto - h)) + (26 * f(punto- 2*h)) - (24 * f(punto- 3*h)) + (11 * f(punto - 4*h)) - (2 * f(punto - 5*h))) / (h**4)
                    evaluado.append(formula)
                return evaluado


    elif hacia_adelante == True:

        if primera_derivada  == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = ( (f(punto + h)) - (f(punto)) ) / (h) 
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula =  ( (-(f(punto + 2*h))) + (4 * (f(punto + h)) ) - (3 * (f(punto)) )) / (2 * h)
                    evaluado.append(formula)
                return evaluado


        elif segunda_derivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  =  ((f(punto + 2*h)) - (2 * f(punto + h)) + (f(punto))) / (h**2) 
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula =  ((- f(punto + 3*h)) + (4 * f(punto + 2*h)) - (5 * f(punto + h)) + (2 * f(punto))) / (h**2)
                    evaluado.append(formula)
                return evaluado
        
        elif tercera_drivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = ((f(punto + 3*h)) - (3 * f(punto + 2*h)) + (3 * f(punto + h)) - (f(punto))) / (h**3) 
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula =  ((- (3 * f(punto + 4*h))) + (14 * f(punto + 3*h)) - (24 * f(punto + 2*h)) + (18 * f(punto + h)) - (5 * f(punto)) )/ (2 * h**3)
                    evaluado.append(formula)
                return evaluado

        elif cuarta_derivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = ((f(punto + 4*h)) - (4 * f(punto + 3*h)) + (6 * f(punto + 2*h)) - (4 * f(punto+ h)) + (f(punto))) / (h**4) 
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula = ((-(2 * f(punto + 5*h))) + (11 * f(punto + 4*h)) - (24 * f(punto + 3*h)) + (26 * f(punto +2*h)) - (14 * f(punto + h)) + (3 * f(punto))) / (h**4) 
                    evaluado.append(formula)
                return evaluado

    elif centrales == True:

        if primera_derivada  == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = ((f(punto + h)) - (f(punto - h))) / (2 * h) 
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula = ((-(f(punto + 2*h))) + (8 * f(punto + h)) - (8 * f(punto - h)) + (f(punto - 2*h))) / (12 * h)

                    evaluado.append(formula)
                return evaluado

        elif segunda_derivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = ((f(punto + h)) - (2 * f(punto)) + (f(punto - h))) / (h**2)
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula = ((-(f(punto + 2*h))) + (16 * f(punto + h)) - (30 * f(punto)) + (16 * f(punto - h)) - (f(punto- 2*h))) / (12 * h**2)
                    evaluado.append(formula)
                return evaluado

        elif tercera_drivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  = ((f(punto + 2*h)) - (2 * f(punto + h)) + (2 * f(punto - h)) - (f(punto - 2*h))) / (2 * h**3) 
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula = ((-(f(punto + 3*h))) + (8 * f(punto + 2*h)) - (13 * f(punto + h)) + (13 * f(punto - h)) - (8 * f(punto - 2*h)) + (f(punto - 3*h))) / (8 * h**3)
                    evaluado.append(formula)
                return evaluado

        elif cuarta_derivada == True:
            if formula_uno:
                for h in h_valor_list:
                    formula  =  ((f(punto +2*h)) - (4 * f(punto + h)) + (6 * f(punto)) - (4 * f(punto - h)) + (f(punto- 2*h))) / (h**4)
                    evaluado.append(formula)
                return evaluado
            
            if formula_dos:
                for h in h_valor_list:
                    formula = ((-(f(punto + 3*h))) + (12 * f(punto + 2*h)) + (39 * f(punto + h)) + (56 * f(punto)) - (39 * f(punto - h)) + (12 * f(punto - 2*h)) + (f(punto -3*h))) / (6 * h**4)
                    evaluado.append(formula)
                return evaluado 

    elif tres_puntos == True:
        if formula_uno:
                for h in h_valor_list:
                    formula  = ((f(punto + h)) - (f(punto - h))) / (2 * h) 
                    evaluado.append(formula)
                return evaluado
            
        if formula_dos:
            for h in h_valor_list:
                formula = ((-(3 * f(punto))) + (4 * f(punto + h)) - (f(punto + 2*h))) / (2 * h)

                evaluado.append(formula)
            return evaluado

    elif cinco_puntos == True:   
        if formula_uno:
            for h in h_valor_list:
                formula = (1/12 * h) * ((-(25 * f(punto))) + (48 * f(punto + h)) - (36 * f(punto +2*h)) + (16 * f(punto +3*h)) - (3 * f(punto +4*h))) 
                evaluado.append(formula)
            return evaluado
        
        if formula_dos:
            for h in h_valor_list:
                formula =(1/12 * h) * ((-(3 * f(punto - h))) - (10 * f(punto)) + (18 * f(punto + h)) - (6 * f(punto + 2*h)) + (f(punto+ 3*h)))
                evaluado.append(formula)
            return evaluado        
        
        if formula_tres:
            for h in h_valor_list:
                formula =(1/12 * h) * ((f(punto - 2*h)) - (8 * f(punto - h)) + (8 * f(punto + h)) - (f(punto + 2*h))) 
                evaluado.append(formula)
            return evaluado
        
        if formula_cuatro:
            for h in h_valor_list:
                formula =(1/12 * h) * ((4 * f(punto - 3*h)) + (6 * f(punto - 2*h)) - (8 * f(punto - h)) + (34 * f(punto)) + (3 * f(punto + h)) + (34 * f(punto + 2*h))) 
                evaluado.append(formula)
            return evaluado
        
        if formula_cinco:
            for h in h_valor_list:
                formula = (1/12 * h) * ((f(punto - 4*h)) - (3 * f(punto - 3*h)) + (4 * f(punto - 2*h)) - (36 * f(punto - h)) + (25 * f(punto)))
                evaluado.append(formula)
            return evaluado


 

def Extrapolacion_Richardson(funcion,punto,h,hacia_atras,hacia_adelante,centrales,tres_puntos,cinco_puntos,primera_derivada,segunda_derivada,tercera_drivada,cuarta_derivada,nivel,formula_uno,formula_dos,formula_tres,formula_cuatro,formula_cinco):

    x = sp.symbols("x") 
    f = sp.lambdify(x,funcion)

    #Calcular los h de acuerdo al nivel 
    h_valor_dic = {f'h{i + 1}': h / (2 ** i) for i in range(nivel)}
    h_valor_list = [h / (2 ** i) for i in range(nivel)]
    print("Valores de h utilizados:")
    for key, value in h_valor_dic.items():
        print(f"{key}: {value}")

    #Sacamos el nivel 1
    nivel_1 = Diferencias_Finitas(funcion,punto,h,hacia_atras,hacia_adelante,centrales,tres_puntos,cinco_puntos,primera_derivada,segunda_derivada,tercera_drivada,cuarta_derivada,h_valor_list,formula_uno,formula_dos,formula_tres,formula_cuatro,formula_cinco)
    
    #Nivel 2
    nivel_2 = []
    for i in range(len(nivel_1) - 1):
        D = 4/3 * (nivel_1[i+1]) - 1/3 * (nivel_1[i])
        nivel_2.append(D)
    # Iniciar la lista D con los valores del nivel 2
    D = [nivel_2]

    # Realizar la extrapolación de Richardson desde el nivel 3 hasta el nivel n
    for k in range(3, nivel + 1):
        nivel_k = []
        for i in range(len(D[-1]) - 1):
            # Calcular Dk correctamente para cada nivel
            Dk = (4 ** (k-1) * D[-1][i+1] - D[-1][i]) / (4 ** (k-1) - 1)
            nivel_k.append(Dk)
        D.append(nivel_k)

    print(f"\nResultados de la extrapolación de Richardson hasta el nivel {nivel}:\n")
    print(f"Nivel 1: {nivel_1}")
    for i, res in enumerate(D):
        print(f"Nivel {i + 2}: {res}")




#----------------------------------------------------------------------------

x = sp.symbols("x") 
funcion  = sp.sin(x) * sp.cos(x)
punto = 3
h = 0.1
nivel = 4

hacia_atras = False
hacia_adelante = True 
centrales = False    
tres_puntos = False
cinco_puntos = False

primera_derivada = False
segunda_derivada = True
tercera_drivada = False
cuarta_derivada = False

formula_uno = True
formula_dos  = False
formula_tres = False
formula_cuatro  = False
formula_cinco = False



Extrapolacion_Richardson(funcion,punto,h,hacia_atras,hacia_adelante,centrales,tres_puntos,cinco_puntos,primera_derivada,segunda_derivada,tercera_drivada,cuarta_derivada,nivel,formula_uno,formula_dos,formula_tres,formula_cuatro,formula_cinco)
