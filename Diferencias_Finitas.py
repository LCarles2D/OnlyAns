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
from sympy import E as e

def Diferencias_Finitas(funcion,punto,h,hacia_atras,hacia_adelante,centrales,tres_puntos,cinco_puntos,primera_derivada,segunda_derivada,tercera_drivada,cuarta_derivada,muestra_titulo,muestra_primer_formula,muestra_segunda_formula,muestra_valores):
    global mostrar

    valores_mostrar = ""
    titulo_mostrar = ""
    primera_formula_mostrar = ""
    segunda_formula_mostrar = ""


    #funcion_ = parse_expr(funcion)
    x = sp.symbols("x")  
    f = sp.lambdify(x,funcion)
    
    #Evaluo la funcion en el punto
    punto_evaluado = f(punto)

    valores_x = []
    valores_y = []

    #Genero tres restando el valor de h
    for i in range(5, 0, -1):
        valores_x.append(punto- i * h)


    valores_x.append(punto) # Agregar el punto inicial

    #Generar los puntos sumando 0.15
    for i in range(1, 6):
        valores_x.append(punto + i * h)


    #Ahora evaluo la funcion y guardo los valores
    for i in valores_x:
        valor = f(i)
        valores_y.append(valor)

    

    #Guardo el indice del punto en los valores de y
    encontrado = valores_y.index(punto_evaluado)
    #Calculamos el valor verdadero
    d_f  = sp.diff(funcion,x)
    d = sp.lambdify(x,d_f)
    Vv = d(punto)


    valores_mostrar = f"Funcion : {funcion}\n\n\nPunto : {punto}\n\n\nh : {h}\n\n\nx --> {valores_x}\n\n"

    try:
    
        if hacia_atras == True:

            titulo_mostrar = "DIFERENCIAS DIVIDIDAS FINITAS HACIA ATRÁS\n"

            if primera_derivada  == True:

                formula_uno = (valores_y[encontrado] - valores_y[encontrado - 1]) / (h)
                formula_dos = ((3 * valores_y[encontrado]) - (4 * valores_y[encontrado - 1]) + (valores_y[encontrado - 2])) / (2 * h)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"PRIMERA DERIVADA\n\n\n\nPrimer Formula \n\nf'(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf'(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"


            elif segunda_derivada == True:

                formula_uno = ((valores_y[encontrado]) - (2 * valores_y[encontrado - 1]) + (valores_y[encontrado - 2])) / (h**2)
                formula_dos = ((2* valores_y[encontrado]) - (5 * valores_y[encontrado - 1]) + (4 * valores_y[encontrado - 2]) - (valores_y[encontrado - 3])) / (h**2)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100


                primera_formula_mostrar = f"SEGUNDA DERIVADA\n\n\n\nPrimer Formula \n\nf''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"


            elif tercera_drivada == True:

                formula_uno = ((valores_y[encontrado]) - (3 * valores_y[encontrado - 1]) + (3 * valores_y[encontrado - 2]) - (valores_y[encontrado - 3])) / (h**3)
                formula_dos = ((5 * valores_y[encontrado]) - (18 * valores_y[encontrado - 1]) + (24 * valores_y[encontrado - 2]) - (14 * valores_y[encontrado - 3]) + (3 * valores_y[encontrado - 4]) ) / (2 * h**3)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"TERCER DERIVADA\n\n\n\nPrimer Formula \n\nf'''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf'''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"


            elif cuarta_derivada == True:

                formula_uno = ((valores_y[encontrado]) - (4 * valores_y[encontrado - 1]) + (6 * valores_y[encontrado - 2]) -(4 * valores_y[encontrado - 3]) + (valores_y[encontrado - 4])) / (h**4)
                formula_dos = ((3 * valores_y[encontrado]) - (14 * valores_y[encontrado - 1]) + (26 * valores_y[encontrado - 2]) - (24 * valores_y[encontrado - 3]) + (11 * valores_y[encontrado - 4]) - (2 * valores_y[encontrado - 5])) / (h**4)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"CUARTA DERIVADA\n\n\n\nPrimer Formula \n\nf''''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf''''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"


        elif hacia_adelante == True:

            titulo_mostrar = "DIFERENCIAS DIVIDIDAS FINITAS HACIA ADELANTE\n"

            if primera_derivada  == True:

                formula_uno = ( (valores_y[encontrado + 1]) - (valores_y[encontrado]) ) / (h) 
                formula_dos = ( (-(valores_y[encontrado + 2])) + (4 * (valores_y[encontrado + 1])) - (3 * (valores_y[encontrado]))   ) / (2 * h)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"PRIMERA DERIVADA\n\n\n\nPrimer Formula \n\nf'(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf'(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"



            elif segunda_derivada == True:

                formula_uno = ((valores_y[encontrado + 2]) - (2 * valores_y[encontrado + 1]) + (valores_y[encontrado])) / (h**2)
                formula_dos = ((-valores_y[encontrado + 3]) + (4 * valores_y[encontrado + 2]) - (5 * valores_y[encontrado + 1]) + (2 * valores_y[encontrado])) / (h**2)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"SEGUNDA DERIVADA\n\n\n\nPrimer Formula \n\nf''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"



            elif tercera_drivada == True:

                formula_uno = ((valores_y[encontrado + 3]) - (3 * valores_y[encontrado + 2]) + (3 * valores_y[encontrado + 1]) - (valores_y[encontrado])) / (h**3)
                formula_dos = ((- (3 * valores_y[encontrado + 4])) + (14 * valores_y[encontrado + 3]) - (24 * valores_y[encontrado + 2]) + (18 * valores_y[encontrado + 1])) - (5 * valores_y[encontrado]) / (2 * h**3)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"TERCER DERIVADA\n\n\n\nPrimer Formula \n\nf'''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf'''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"



            elif cuarta_derivada == True:

                formula_uno = ((valores_y[encontrado + 4]) - (4 * valores_y[encontrado + 3]) + (6 * valores_y[encontrado + 2]) - (4 * valores_y[encontrado + 1]) + (valores_y[encontrado])) / (h**4)
                formula_dos = ((-(2 * valores_y[encontrado + 5])) + (11 * valores_y[encontrado + 4]) - (24 * valores_y[encontrado + 3]) + (26 *valores_y[encontrado + 2]) - (14 * valores_y[encontrado + 1]) + (3 * valores_y[encontrado])) / (h**4) 

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"CUARTA DERIVADA\n\n\n\nPrimer Formula \n\nf''''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf''''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"



        elif centrales == True:
            titulo_mostrar = "DIFERENCIAS FINITAS CENTRALES\n"

            if primera_derivada  == True:

                formula_uno = ((valores_y[encontrado + 1]) - (valores_y[encontrado - 1])) / (2 * h)
                formula_dos = ((-(valores_y[encontrado + 2])) + (8 * valores_y[encontrado + 1]) - (8 * valores_y[encontrado - 1]) + (valores_y[encontrado - 2])) / (12 * h)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"PRIMERA DERIVADA\n\n\n\nPrimer Formula \n\nf'(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf'(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"

    
            elif segunda_derivada == True:

                formula_uno = ((valores_y[encontrado + 1]) - (2 * valores_y[encontrado]) + (valores_y[encontrado - 1])) / (h**2)
                formula_dos = ((-(valores_y[encontrado + 2])) + (16 * valores_y[encontrado + 1]) - (30 * valores_y[encontrado]) + (16 * valores_y[encontrado - 1]) - (valores_y[encontrado - 2])) / (12 * h**2)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"SEGUNDA DERIVADA\n\n\n\nPrimer Formula \n\nf''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"


                

            elif tercera_drivada == True:

                formula_uno = ((valores_y[encontrado +2]) - (2 * valores_y[encontrado + 1]) + (2 * valores_y[encontrado - 1]) - (valores_y[encontrado - 2])) / (2 * h**3)
                formula_dos = ((-(valores_y[encontrado + 3])) + (8 * valores_y[encontrado + 2]) - (13 * valores_y[encontrado + 1]) + (13 * valores_y[encontrado - 1]) - (8 * valores_y[encontrado - 2]) + (valores_y[encontrado - 3])) / (8 * h**3)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"TERCER DERIVADA\n\n\n\nPrimer Formula \n\nf'''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf'''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"


            elif cuarta_derivada == True:

                formula_uno = ((valores_y[encontrado + 2]) - (4 *valores_y[encontrado + 1]) + (6 * valores_y[encontrado]) - (4 * valores_y[encontrado - 1]) + (valores_y[encontrado - 2])) / (h**4)
                formula_dos = ((-(valores_y[encontrado + 3])) + (12 * valores_y[encontrado + 2]) + (39 * valores_y[encontrado + 1]) + (56 * valores_y[encontrado]) - (39 * valores_y[encontrado - 1]) + (12 * valores_y[encontrado - 2]) + (valores_y[encontrado - 3])) / (6 * h**4)

                Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
                Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

                primera_formula_mostrar = f"CUARTA DERIVADA\n\n\n\nPrimer Formula \n\nf''''(x) :{formula_uno}\nEa :{Error_porcentual_formula_uno} %"
                segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf''''(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"


        elif tres_puntos == True:
            titulo_mostrar = "FORMULA DE LOS TRES PUNTOS\n"

            formula_uno = ((valores_y[encontrado + 1]) - (valores_y[encontrado - 1])) / (2 * h) #centrada de orden dos
            formula_dos = ((-(3 * valores_y[encontrado])) + (4 * valores_y[encontrado + 1]) - (valores_y[encontrado +2])) / (2 * h)

            Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
            Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100

            primera_formula_mostrar = f"Primer Formula \n\nf'(x) :{formula_uno} ; centrada de orden dos\nEa :{Error_porcentual_formula_uno} %"
            segunda_formula_mostrar = f"\n\nSegunda Formula \n\nf'(x) :{formula_dos}\nEa :{Error_porcentual_formula_dos} %"


        elif cinco_puntos == True:
            titulo_mostrar = "FORMULA DE LOS CINCO PUNTOS\n"
            
            formula_uno = (1/12 * h) * ((-(25 * valores_y[encontrado])) + (48 * valores_y[encontrado + 1]) - (36 * valores_y[encontrado + 2]) + (16 * valores_y[encontrado + 3]) - (3 * valores_y[encontrado + 4]))
            formula_dos = (1/12 * h) * ((-(3 * valores_y[encontrado - 1])) - (10 * valores_y[encontrado]) + (18 * valores_y[encontrado + 1]) - (6 * valores_y[encontrado + 2]) + (valores_y[encontrado + 3]))
            formula_tres =  (1/12 * h) * ((valores_y[encontrado - 2]) - (8 * valores_y[encontrado - 1]) + (8 * valores_y[encontrado + 1]) - (valores_y[encontrado + 2]))
            formula_cuatro = (1/12 * h) * ((4 * valores_y[encontrado - 3]) + (6 * valores_y[encontrado - 2]) - (8 * valores_y[encontrado - 1]) + (34 * valores_y[encontrado]) + (3 * valores_y[encontrado + 1]) + (34 * valores_y[encontrado + 2]))
            formula_cinco = (1/12 * h) * ((valores_y[encontrado - 4]) - (3 * valores_y[encontrado - 3]) + (4 * valores_y[encontrado - 2]) - (36 * valores_y[encontrado - 1]) + (25 * valores_y[encontrado]))


            Error_porcentual_formula_uno  = abs((Vv - formula_uno) / (Vv)) * 100
            Error_porcentual_formula_dos  = abs((Vv - formula_dos) / (Vv)) * 100
            Error_porcentual_formula_tres  = abs((Vv - formula_tres) / (Vv)) * 100
            Error_porcentual_formula_cuatro  = abs((Vv - formula_cuatro) / (Vv)) * 100
            Error_porcentual_formula_cinco  = abs((Vv - formula_cinco) / (Vv)) * 100

            P_f = f"Primer Formula \t\tSegunda formula \nf'(x) :{formula_uno}\t\tf'(x) :{formula_dos}\nEa :{Error_porcentual_formula_uno} %\t\tEa :{Error_porcentual_formula_dos} %"
            S_f = f"Tercera Formula \t\tCuarta Formula \nf'(x) :{formula_tres}\t\tf'(x) :{formula_cuatro}\nEa :{Error_porcentual_formula_tres} %\t\tEa :{Error_porcentual_formula_cuatro} %\n\n\nQuinta Formula \nf'(x) :{formula_cinco}\nEa :{Error_porcentual_formula_cinco} %"
            primera_formula_mostrar = P_f
            segunda_formula_mostrar = S_f

        muestra_titulo.configure(text =titulo_mostrar)
        muestra_valores.configure(text =valores_mostrar)
        muestra_primer_formula.configure(text= primera_formula_mostrar)
        muestra_segunda_formula.configure(text =segunda_formula_mostrar)
        mostrar = True


    except ZeroDivisionError:
        messagebox.showerror("¡ ERROR CRITICO !","Se ha producido una división por cero")
        mostrar = False

    




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



def Ventana_Diferencias_Finitas(frame,ventana2,ventana):

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
    etiqueta_formulas.place(x=100,y=20)

    etiqueta_derivada = ctk.CTkLabel(marco_ingreso_valores,text = "Elija la derivada",font=tipo_tamaño_letra_ventana2)
    etiqueta_derivada.place(x=350,y=20)

    etiqueta_ingreso_punto = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el punto",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_punto.place(x=600,y=20)

    etiqueta_ingreso_valor_h = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor de h",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_h.place(x=800,y=20)

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=1050,y=20)


    #lista para las formulas
    lista_valores_formulas = StringVar(marco_ingreso_valores)
    #dejamo fijo un valor
    lista_valores_formulas.set("")
    #lo que llevara la lista
    todas_formulas = ["Formulas hacia atras","Formulas hacia adelante","Formulas centrales","Formulas de tres puntos","Formulas de cinco puntos"]
    #Cramos el menu
    opcion_formulas = ctk.CTkOptionMenu(marco_ingreso_valores,variable=lista_valores_formulas, values=todas_formulas)
    opcion_formulas.configure(width=200)
    opcion_formulas.place(x=50,y=60)

    
    #lista para las derivadas
    lista_derivadas = StringVar(marco_ingreso_valores)
    #dejamo fijo un valor
    lista_derivadas.set("")
    #lo que llevara la lista
    todas_derivadas = ["Primera derivada","Segunda derivada","Tercera derivada","Cuarta derivada"]
    #Cramos el menu
    opcion_derivadas = ctk.CTkOptionMenu(marco_ingreso_valores,variable=lista_derivadas, values=todas_derivadas)
    opcion_derivadas.configure(width=200)
    opcion_derivadas.place(x=300,y=60)


    ingreso_punto = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_punto.place(x=600,y=60)

    ingreso_valor_h = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_h.place(x=800,y=60)

    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=1000,y=60)


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
        
        
        seleccion_formula = lista_valores_formulas.get()
        seleccion_derivada = lista_derivadas.get()
        valor_h = ingreso_valor_h.get()
        punto = ingreso_punto.get()
        funcion = ingreso_funcion.get()

        if seleccion_formula == "" and seleccion_derivada == "" and valor_h == "" and punto == "" and funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")

        elif seleccion_formula == "" or seleccion_derivada == "" or valor_h == "" or punto == "" or funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")

        else:
            valida,funcion_str = Validar_y_Reemplazar_funcion(funcion)
            if numero_valido(punto) and numero_valido(valor_h):
                if valida == True:

                    h_ = float(valor_h)
                    punto_v = float(punto) 
                    funcion = funcion_str
                                     

                    #valido la derivada para cada formula
                    if seleccion_formula == "Formulas hacia atras":
                        formula_hacia_atras = True 
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
                        elif seleccion_derivada == "Segunda derivada":
                            segunda_deriv = True
                        elif seleccion_derivada == "Tercera derivada":
                            tercera_deriv = True
                        elif seleccion_derivada == "Cuarta derivada":
                            cuarta_deriv = True


                    elif seleccion_formula == "Formulas hacia adelante":
                        formula_hacia_adelante = True 
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
                        elif seleccion_derivada == "Segunda derivada":
                            segunda_deriv = True
                        elif seleccion_derivada == "Tercera derivada":
                            tercera_deriv = True
                        elif seleccion_derivada == "Cuarta derivada":
                            cuarta_deriv = True
                        

                    elif seleccion_formula == "Formulas centrales":
                        formulas_centrales = True 
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
                        elif seleccion_derivada == "Segunda derivada":
                            segunda_deriv = True
                        elif seleccion_derivada == "Tercera derivada":
                            tercera_deriv = True
                        elif seleccion_derivada == "Cuarta derivada":
                            cuarta_deriv = True
                        

                    elif seleccion_formula == "Formulas de tres puntos":
                        formulas_tres_puntos = True
                        if seleccion_derivada == "Primera derivada":
                            primera_deriv = True
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
                        elif seleccion_derivada == "Segunda derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de cinco puntos solo posee la primer derivada")
                        elif seleccion_derivada == "Tercera derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de cinco puntos solo posee la primer derivada")
                        elif seleccion_derivada == "Cuarta derivada":
                            messagebox.showerror("¡ ERROR CRITICO !",message="Las formulas de cinco puntos solo posee la primer derivada")


                    muestra_titulo = ctk.CTkLabel(marco_muestra_valores,font=("Currier",20,"bold"),anchor="w", justify="left")
                    muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=("Currier",15,"bold"),anchor="w", justify="left")
                    muestra_primer_formula = ctk.CTkLabel(marco_muestra_valores,font=("Currier",15,"bold"),anchor="w", justify="left")
                    muestra_segunda_formula = ctk.CTkLabel(marco_muestra_valores,font=("Currier",15,"bold"),anchor="w", justify="left")
                    


    
                    Diferencias_Finitas(funcion,punto_v,h_,formula_hacia_atras,formula_hacia_adelante,formulas_centrales,formulas_tres_puntos,formulas_cinco_puntos,primera_deriv,segunda_deriv,tercera_deriv,cuarta_deriv,muestra_titulo,muestra_primer_formula,muestra_segunda_formula,muestra_valores)

                    if mostrar == True:
                        muestra_titulo.place(x=450,y=10)
                        muestra_valores.place(x=60,y=200)
                        muestra_primer_formula.place(x=875,y=100)
                        muestra_segunda_formula.place(x=875,y=250)

                        #Se desactiva el botón de Resolver
                        boton_resolver.configure(state=DISABLED)
                        #Se activa el botón de Limpiar
                        boton_limpiar.configure(state=NORMAL)
                    
                    
                    #Se limpia los entry cuando ya se resulve por el metodo
                    ingreso_punto.delete(0, END)
                    ingreso_valor_h.delete(0, END)
                    ingreso_funcion.delete(0, END)
                    lista_valores_formulas.set("")
                    lista_derivadas.set("")





                else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Error al ingresar la funcion")
            else:
                messagebox.showerror("¡ ERROR CRITICO !",message="Solo debe ingresar valores numericos en el campo del valor de h y el punto")
           


    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=125)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=125)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=125)



"""
x = sp.symbols("x") 
funcion  = sp.exp(x) 
punto = 3
h = 0.15

hacia_atras = False 
hacia_adelante = False   
centrales = False    
tres_puntos = False
cinco_puntos = True

primera_derivada = False
segunda_derivada = False
tercera_derivada = False
cuarta_derivada = False

Diferencias_Finitas(funcion,punto,h,hacia_atras,hacia_adelante,centrales,tres_puntos,cinco_puntos,primera_derivada,segunda_derivada,tercera_derivada,cuarta_derivada) """

