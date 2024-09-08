import sympy as sp
import pandas as pd
from sympy import symbols, sympify, parse_expr
from sympy.parsing.sympy_parser import parse_expr
from sympy import Poly
from sympy.parsing.sympy_parser import transformations,_T,standard_transformations,implicit_multiplication,convert_xor,implicit_application,function_exponentiation,implicit_multiplication_application,auto_symbol,auto_number,split_symbols
from sympy import Eq, solve
import funciones_herramientas
from funciones_herramientas import * 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
import ctypes

#generales_Honer(expresion, Mensaje, Error)
generales_Honer = funciones_herramientas.Transportador()
#raices_reales(lista de raices reales)
raices_reales_horner = funciones_herramientas.Transportador()


def verificador_error(Error):
    if not (Error == None or Error == ""):
        messagebox.showerror("¡ ERROR CRITICO !", message = Error)
    else:
        pass

#   x**4-7*x**3+13*x**2+23*x-78    1 + 3*x + 5*x**2 + 6*x**3

#Metodo Horner:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def Metodo_Horner(expresion, x0, cifras_significativas):
    Mensaje, Error = "", ""
    x = sp.symbols("x")
    raices_reales = []
    funcion, dicc, Error = validar_funcion(expresion)
    Xo = x0
    Es, Error = calcular_Es(cifras_significativas)
    print("Es: ", Es, "%")
    
    coeficientes, Error = obtener_coeficientes(expresion)
    verificador_error(Error)
    print("coeficientes: ", coeficientes)

    division_sintetica_R, Error = division_sintetica(coeficientes, Xo)
    verificador_error(Error)
    R = division_sintetica_R[-1]
    print("lista R: ", division_sintetica_R)
    print(f"R: {R}")

    lista_2 = [valor for indice, valor in enumerate(division_sintetica_R) if indice != len(division_sintetica_R) - 1]
    print("lista 2: ", lista_2)
    division_sintetica_S, Error = division_sintetica(lista_2, Xo)
    verificador_error(Error)
    S = division_sintetica_S[-1]
    print("lista S: ", division_sintetica_S)
    print(f"S: {S}")

    df = pd.DataFrame(columns=["Iteracion", "Xi", "Ea %"])
    contador = 1

    Xi = Xo - (R / S)
    x_reales, x_imaginarias = funciones_herramientas.validar_raices(Xi)
    raices_reales.extend(x_reales)

    print("xo: ", Xo)
    print("xi: ", Xi)
    Ea, Error = calcular_Ea(Xi, Xo)
    verificador_error(Error)
    print("Ea: ", Ea, "%")
    print("Es: ", Es, "%")

    df.loc[contador - 1] = [contador, Xi, Ea] 

    Mensaje = f"Metodo de Horner:\nDatos ingresados: Expresion: {expresion} , Xo = {Xo} y Cifras Significativas: {cifras_significativas}\n"
    Mensaje = Mensaje + f"Calculos previos:  Error de Aproximacion permitido Ea: {Ea}%\n"
    Mensaje = Mensaje + f"Tabla de resultados:\n"
    
    while Ea >= Es:
        Xo = Xi

        division_sintetica_R, Error = division_sintetica(coeficientes, Xo)
        verificador_error(Error)
        R = division_sintetica_R[-1]
        print("lista R: ", division_sintetica_R)
        print(f"R: {R}")

        lista_2 = [valor for indice, valor in enumerate(division_sintetica_R) if indice != len(division_sintetica_R) - 1]
        print("lista 2: ", lista_2)
        division_sintetica_S, Error = division_sintetica(lista_2, Xo)
        verificador_error(Error)
        S = division_sintetica_S[-1]
        print("lista S: ", division_sintetica_S)
        print(f"S: {S}")

        Xi = Xo - (R / S)
        x_reales, x_imaginarias = funciones_herramientas.validar_raices(Xi)
        raices_reales.extend(x_reales)

        Ea, Error = calcular_Ea(Xi, Xo)
        verificador_error(Error)
        print("Ea: ", Ea, "%")

        df.loc[contador] = [contador, Xi, Ea] 

        contador += 1

    Mensaje = Mensaje + f"{df.to_string(index=False)}\n"
    Mensaje = Mensaje + f"La raiz aproximada es {Xi} con un error de {Ea} % en la {contador} iteracion\n"

    generales_Honer.set_transportador(expresion)
    generales_Honer.set_transportador(Mensaje)
    generales_Honer.set_transportador(Error)
    raices_reales_horner.set_transportador(raices_reales)
    
"""x = sp.symbols("x")
#x**4-7*x**3+13*x**2+23*x-78
funtion = "1 + 3*x + 5*x**2 + 6*x**3"
horner_method(funtion, -0.45, 3) """

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

def Ventana_Metodo_Horner(frame,ventana2,ventana):

    #disposicion de botones
    global marco_muestra_valores
    global canvas

    #botones globales
    global boton_limpiar,boton_resolver
    global tipo_tamaño_letra_ventana2,color_fondo_boton_ventana2,color_fondo_boton_ventana2
    global color_boton_pasar_mouse_ventana2,ancho_borde_ventana2,color_borde_ventana2
    global boton_limpiar,boton_resolver

    #declaracion marco superior
    marco_ingreso_valores = ctk.CTkFrame(frame, width=0, height=300, corner_radius=10)
    marco_ingreso_valores.pack(fill="x", expand=False, padx=10, pady=0)
    marco_ingreso_valores.grid_propagate(False)

    #declaracion marco inferior
    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=550,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)


        #Label titulo
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores, text="Metodo de Horner", font=("Arial Black", 16))
        #posicion
    label_ingrese_funcion.place(x=50,y=20)

        #label funcion
    _func = "Ingrese una funcion"    
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = _func,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=50,y=50)

    #boton informacion funcion
    def habilitar_boton_informacion():
        if label_informacion.winfo_ismapped():
            label_informacion.place_forget()
        else:
            label_informacion.place(x=75,y=135)

    label_informacion = ctk.CTkLabel(marco_ingreso_valores, text="El método de Horner es una\ntécnica eficiente para evaluar\npolinomios y encontrar sus raíces.", font=tipo_tamaño_letra_ventana2)
    label_informacion.place_forget()

    #boton_informacion = ctk.CTkButton(marco_ingreso_valores, text="i", command=habilitar_boton_informacion,height = 20,width=20)
    #boton_informacion.place(x=300, y=50)

        #entry funcion
    e_ingrese_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_funcion.place(x=50,y=80)

    #label Xo
    _xo = "Ingrese Xo"
    label_ingrese_xo = ctk.CTkLabel(marco_ingreso_valores,text = _xo,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_xo.place(x=500,y=50)
        #entry Xo
    e_ingrese_xo = ctk.CTkEntry(marco_ingreso_valores,width=150,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_xo.place(x=500,y=80)

    #label CS
    _cs = "Ingrese cantidad de cifras significativas"
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = _cs,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=500,y=125)
        #entry Cs
    e_ingrese_cs = ctk.CTkEntry(marco_ingreso_valores,width=150,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_cs.place(x=500,y=155)
    

    #::validaciones::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #habilitacion de botones globales
    global boton_limpiar,boton_resolver,mostrar

    def Validacion():
        expresion = e_ingrese_funcion.get()
        xo = e_ingrese_xo.get()
        cs = e_ingrese_cs.get()

        #Vacio
        lista_param = {_func:expresion, _xo:xo, _cs:cs}

        if not validar_vacio(expresion) or not validar_vacio(xo) or not validar_vacio(cs):
            mens = validar_vacio_g(lista_param)
            verificador_error(mens)
        else:
            #Caracteres permitidos
            expresion, Error = funciones_herramientas.validar_caracteres(expresion)
            verificador_error(Error)
            xo, Error = funciones_herramientas.validar_numeros(xo)
            verificador_error(Error)
            cs, Error = funciones_herramientas.validar_numeros(cs, "int")
            verificador_error(Error)


            #validar cs
            if cs < 0 and not isinstance(cs, (int)):
                Error = "El valor de las cifras significativas debe ser positivo y ser un numero entero"
                verificador_error(Error)
            if cs < 0:
                Error = "El valor de las cifras significativas deben ser un numero positivo"    
                verificador_error(Error)
            if not isinstance(cs, (int)):
                Error = "El valor de las cifras significativas debe ser un numero entero"
                verificador_error(Error)

            #Apertura y cierre de signos de agrupacion
            expresion, Error = funciones_herramientas.validar_PCL(expresion)
            verificador_error(Error)

            #Validar igualdad
            expresion, Error = funciones_herramientas.validar_igualdad(expresion)
            verificador_error(Error)

            expresion_valid, Error = funciones_herramientas.validar_multiplicacion_implicita(expresion)
            verificador_error(Error)
    
            muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

            #Ecuaciones_Cuadraticas(funcion, destinos) 
            Metodo_Horner(expresion_valid, xo, cs) 
        
            #impresion de datos
            muestra_valores.configure(text = generales_Honer.get_transportador(1), anchor='w', justify='left')

            #impresion del grafico
            fig = Grafico(generales_Honer.get_transportador(0), raices_reales_horner.get_transportador())
            canvas = FigureCanvasTkAgg(fig, master = muestra_grafica)

            canvas.draw()
            widget_grafico = canvas.get_tk_widget()
            widget_grafico.pack(fill="both", expand=True)
            
            #mostar
            mostrar =True

            #establece donde se generaran los gidgets
            if mostrar == True:
                muestra_valores.place(x=10,y=20)
                #muestra_tabla.place(x=0,y=130)
                #muestra_raiz.place(x=10,y=400)
                muestra_grafica.place(x=700,y=20)

            #Se desactiva el botón de Resolver
            boton_resolver.configure(state=DISABLED)
            #Se activa el botón de Limpiar
            boton_limpiar.configure(state=NORMAL)
                        
                        
            #Se limpia los entry cuando ya se resulve por el metodo
            e_ingrese_funcion.delete(0, END)
            e_ingrese_xo.delete(0, END)
            e_ingrese_cs.delete(0, END)
        
   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=225)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=225)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=225)
