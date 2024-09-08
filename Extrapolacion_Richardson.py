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


 

def Extrapolacion_Richardson(funcion,punto,h,hacia_atras,hacia_adelante,centrales,tres_puntos,cinco_puntos,primera_derivada,segunda_derivada,tercera_drivada,cuarta_derivada,nivel,formula_uno,formula_dos,formula_tres,formula_cuatro,formula_cinco,muestra_valores,muestra_niveles):
    resultado = ""
    valores = ""
    global mostrar

    x = sp.symbols("x") 
    f = sp.lambdify(x,funcion)

    #Calcular los h de acuerdo al nivel 
    h_valor_dic = {f'h{i + 1}': h / (2 ** i) for i in range(nivel)}
    h_valor_list = [h / (2 ** i) for i in range(nivel)]
    valores = f"Funcion : {funcion}\nPunto : {punto}\nh : {h}\nNivel : {nivel}\n\nValores de h utilizados:\n\n"
    for key,value in h_valor_dic.items():
        valores += f"{key}: {value}\n"


    

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


    resultado = f"\nResultados de la extrapolación de Richardson hasta el nivel {nivel}:\n\n"
    resultado += f"Nivel 1: {nivel_1}\n"
    for i, res in enumerate(D):
        resultado += f"Nivel {i + 2}: {res}\n"

    
    muestra_valores.configure(text= valores)
    muestra_niveles.configure(text=resultado)
    mostrar = True
    




"""#----------------------------------------------------------------------------

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
"""






"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
mostrar = False

boton_resolver = None
boton_limpiar = None
canvas = None


#------------Funciones para los botones de la segunda interfaz-----------------------------------

def Volver(ventana2,ventana):
    ventana2.destroy()
    ventana.deiconify()


def Limpiar():
    global marco_muestra_valores
    global canvas
    global boton_resolver,boton_limpiar 

    boton_resolver.configure(state=NORMAL)
    boton_limpiar.configure(state=DISABLED)

    # Iterar sobre los widgets y destruirlos uno por uno
    for widget in marco_muestra_valores.winfo_children():
        widget.destroy()



#--------------------- Ventana Secundaria---------------------------------------------------------------------
color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2



def Ventana_Extrapolacion_Richardson(frame,ventana2,ventana):
    global marco_muestra_valores
    global canvas
    global boton_limpiar,boton_resolver
    global tipo_tamaño_letra_ventana2,color_fondo_boton_ventana2,color_fondo_boton_ventana2
    global color_boton_pasar_mouse_ventana2,ancho_borde_ventana2,color_borde_ventana2
    global boton_limpiar,boton_resolver


    marco_ingreso_valores = ctk.CTkFrame(frame, width=0, height=200, corner_radius=10)
    marco_ingreso_valores.pack(fill="x", expand=False, padx=10, pady=0)
    marco_ingreso_valores.grid_propagate(False)

    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=600,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)

    etiqueta_formulas = ctk.CTkLabel(marco_ingreso_valores,text = "Elija la formula",font=tipo_tamaño_letra_ventana2)
    etiqueta_formulas.place(x=50,y=20)

    etiqueta_derivada = ctk.CTkLabel(marco_ingreso_valores,text = "Elija la derivada",font=tipo_tamaño_letra_ventana2)
    etiqueta_derivada.place(x=250,y=20)

    etiqueta_derivada = ctk.CTkLabel(marco_ingreso_valores,text = "Elija cual formula ocupará",font=tipo_tamaño_letra_ventana2)
    etiqueta_derivada.place(x=450,y=20)

    etiqueta_ingreso_punto = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el punto",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_punto.place(x=675,y=20)

    etiqueta_ingreso_valor_h = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor de h",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_h.place(x=815,y=20)

    etiqueta_ingreso_nivel = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el nivel",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_nivel.place(x=975,y=20)

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=1100,y=20)

    #lista para las formulas
    lista_valores_formulas = StringVar(marco_ingreso_valores)
    #dejamo fijo un valor
    lista_valores_formulas.set("")
    #lo que llevara la lista
    todas_formulas = ["Formulas hacia atras","Formulas hacia adelante","Formulas centrales","Formulas de tres puntos","Formulas de cinco puntos"]
    #Cramos el menu
    opcion_formulas = ctk.CTkOptionMenu(marco_ingreso_valores,variable=lista_valores_formulas, values=todas_formulas)
    opcion_formulas.configure(width=200)
    opcion_formulas.place(x=10,y=60)

    
    #lista para las derivadas
    lista_derivadas = StringVar(marco_ingreso_valores)
    #dejamo fijo un valor
    lista_derivadas.set("")
    #lo que llevara la lista
    todas_derivadas = ["Primera derivada","Segunda derivada","Tercera derivada","Cuarta derivada"]
    #Cramos el menu
    opcion_derivadas = ctk.CTkOptionMenu(marco_ingreso_valores,variable=lista_derivadas, values=todas_derivadas)
    opcion_derivadas.configure(width=200)
    opcion_derivadas.place(x=225,y=60)

    #lista para cual formula
    lista_cual_formula = StringVar(marco_ingreso_valores)
    #dejamo fijo un valor
    lista_cual_formula.set("")
    #lo que llevara la lista
    todas_cual_formula = ["Formula uno","Formula dos","Formula tres","Formula cuatro"]
    #Cramos el menu
    opcion_cual_formula = ctk.CTkOptionMenu(marco_ingreso_valores,variable=lista_cual_formula, values=todas_cual_formula)
    opcion_cual_formula.configure(width=200)
    opcion_cual_formula.place(x=445,y=60)




    ingreso_punto = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_punto.place(x=675,y=60)

    ingreso_valor_h = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_h.place(x=820,y=60)

    ingreso_nivel = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_nivel.place(x=975,y=60)

    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=1100,y=60)

    def numero_valido(texto):
        return re.match(r"^-?\d*\.?\d*$", texto) is not None

    def Validar_y_Reemplazar_funcion(funcion_str):
        x = sp.symbols('x')
        
        # Reemplazar 'e**' por 'exp(' y agregar ')' después del término completo
        def replacer(match):
            return f"exp({match.group(1)})"
        
        # Primero, reemplazar 'ln' por 'log'
        funcion_str = funcion_str.replace('ln', 'log')
        
        # Luego, reemplazar 'e**...' por 'exp(...)'
        funcion_str = re.sub(r'e\*\*(\S+)', replacer, funcion_str)
        
        # Finalmente, reemplazar 'e' por 'exp(1)' cuando no está seguido por '**'
        funcion_str = re.sub(r'\be\b(?![\*\w])', 'exp(1)', funcion_str)

        try:
            # Intenta convertir la función ingresada en una expresión sympy
            expr = sp.sympify(funcion_str)
            
            # Verifica si la expresión contiene solo la variable 'x'
            if expr.free_symbols <= {x, sp.exp(1)}:  # Permitir x y la constante e
                return True, funcion_str
            else:
                return False, None
        except Exception as e:
            #messagebox.showerror("Error de validación", f"La función ingresada no es válida")
            return False, None
    

    def Validacion():

        formula_hacia_atras = False
        formula_hacia_adelante = False
        formulas_centrales = False
        formulas_cinco_puntos = False
        formulas_tres_puntos = False

        primera_deriv = False
        segunda_deriv = False
        tercera_deriv = False
        cuarta_deriv = False

        formula_uno = False
        formula_dos  = False
        formula_tres = False
        formula_cuatro  = False
        formula_cinco = False
        
        
        seleccion_formula = lista_valores_formulas.get()
        seleccion_derivada = lista_derivadas.get()
        seleccion_cual_formula  = lista_cual_formula.get()
        valor_h = ingreso_valor_h.get()
        punto = ingreso_punto.get()
        nivel = ingreso_nivel.get()
        funcion = ingreso_funcion.get()

        if seleccion_formula == "" and seleccion_derivada == "" and seleccion_cual_formula == "" and valor_h == "" and nivel == "" and punto == "" and funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")

        elif seleccion_formula == "" or seleccion_derivada == "" or seleccion_cual_formula == "" or valor_h == "" or punto == ""or nivel == "" or funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")

        else:
            valida,funcion_str = Validar_y_Reemplazar_funcion(funcion)

            if numero_valido(punto) and numero_valido(valor_h) and numero_valido(nivel):
                if valida == True:

                    h_ = float(valor_h)
                    punto_v = float(punto) 
                    nivel =int(nivel)

                    funcion  = funcion_str
                                     

                    #valido la derivada para cada formula
                    if seleccion_formula == "Formulas hacia atras":
                        formula_hacia_atras = True 
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cinco":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                return True


                        elif seleccion_derivada == "Segunda derivada":
                            segunda_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                 return True
                            
                        elif seleccion_derivada == "Tercera derivada":
                            tercera_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                 return True
                            
                        elif seleccion_derivada == "Cuarta derivada":
                            cuarta_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                 return True


                    elif seleccion_formula == "Formulas hacia adelante":
                        formula_hacia_adelante = True 
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas hacia atras solo poseen dos formulas diferentes")
                                 return True
                        elif seleccion_derivada == "Segunda derivada":
                            segunda_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                 return True
                        elif seleccion_derivada == "Tercera derivada":
                            tercera_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cinco":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                return True
                        elif seleccion_derivada == "Cuarta derivada":
                            cuarta_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas hacia adelante solo poseen dos formulas diferentes")
                                 return True
                        

                    elif seleccion_formula == "Formulas centrales":
                        formulas_centrales = True 
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas centrales solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas centrales solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la primer derivada de las formulas centrales solo poseen dos formulas diferentes")
                                 return True
                        elif seleccion_derivada == "Segunda derivada":
                            segunda_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas centrales solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas centrales solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la segunda derivada de las formulas centrales solo poseen dos formulas diferentes")
                                 return True
                        elif seleccion_derivada == "Tercera derivada":
                            tercera_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas centrales solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas centrales solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la tercera derivada de las formulas centrales solo poseen dos formulas diferentes")
                                 return True
                        elif seleccion_derivada == "Cuarta derivada":
                            cuarta_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas centrales solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas centrales solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En la cuarta derivada de las formulas centrales solo poseen dos formulas diferentes")
                                 return True
                        

                    elif seleccion_formula == "Formulas de tres puntos":
                        formulas_tres_puntos = True
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                messagebox.showerror("¡ ERROR CRITICO !",message="En las formulas de tres puntos solo poseen dos formulas diferentes")
                                return True
                            elif seleccion_cual_formula == "Formula cuatro":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En las formulas de tres puntos solo poseen dos formulas diferentes")
                                 return True
                            elif seleccion_cual_formula == "Formula cinco":
                                 messagebox.showerror("¡ ERROR CRITICO !",message="En las formulas de tres puntos solo poseen dos formulas diferentes")
                                 return True
                        elif seleccion_derivada == "Segunda derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de tres puntos solo posee la primer derivada")
                        elif seleccion_derivada == "Tercera derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de tres puntos solo posee la primer derivada")
                        elif seleccion_derivada == "Cuarta derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de tres puntos solo posee la primer derivada")
                        

                    elif seleccion_formula == "Formulas de cinco puntos":
                        formulas_cinco_puntos = True
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
                            if seleccion_cual_formula == "Formula uno":
                                formula_uno = True
                            elif seleccion_cual_formula == "Formula dos":
                                formula_dos = True
                            elif seleccion_cual_formula == "Formula tres":
                                formula_tres = True
                            elif seleccion_cual_formula == "Formula cuatro":
                                formula_cuatro = True
                            elif seleccion_cual_formula == "Formula cuatro":
                                formula_cinco = True
                            
                        elif seleccion_derivada == "Segunda derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de cinco puntos solo posee la primer derivada")
                        elif seleccion_derivada == "Tercera derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de cinco puntos solo posee la primer derivada")
                        elif seleccion_derivada == "Cuarta derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de cinco puntos solo posee la primer derivada")



    
                    muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=("Currier",15,"bold"),anchor="w", justify="left")
                    muestra_niveles = ctk.CTkLabel(marco_muestra_valores,font=("Currier",15,"bold"),anchor="w", justify="left")
                    

                    Extrapolacion_Richardson(funcion,punto_v,h_,formula_hacia_atras,formula_hacia_adelante,formulas_centrales,formulas_tres_puntos,formulas_cinco_puntos,primera_deriv,segunda_deriv,tercera_deriv,cuarta_deriv,nivel,formula_uno,formula_dos,formula_tres,formula_cuatro,formula_cinco,muestra_valores,muestra_niveles)


                    if mostrar == True:
                        muestra_valores.place(x=60,y=100)
                        muestra_niveles.place(x=300,y=100)

                        #Se desactiva el botón de Resolver
                        boton_resolver.configure(state=DISABLED)
                        #Se activa el botón de Limpiar
                        boton_limpiar.configure(state=NORMAL)
                        
                    
                    #Se limpia los entry cuando ya se resulve por el metodo
                    ingreso_punto.delete(0, END)
                    ingreso_valor_h.delete(0, END)
                    ingreso_funcion.delete(0, END)
                    ingreso_nivel.delete(0,END)
                    lista_valores_formulas.set("")
                    lista_derivadas.set("")
                    lista_cual_formula.set("")





                else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Ingrese la funcion en terminos 'x' y sin dejar espacios ")
            else:
                messagebox.showerror("¡ ERROR CRITICO !",message="Solo debe ingresar valores numericos en el campo del valor de h y el punto")
           


    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=125)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=125)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=125)
