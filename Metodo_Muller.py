import sympy as sp
import pandas as pd
from sympy import symbols
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

#muller_method("x**3 - 13*x - 12", 4.5, 5.5, 5, 4)
generales_Muller = funciones_herramientas.Transportador()
raices_reales_Muller = funciones_herramientas.Transportador()


def verificador_error(Error):
    if not (Error == None or Error == ""):
        messagebox.showerror("¡ ERROR CRITICO !", message = Error)
    else:
        pass


def val_expr(expr):
    try:
        return sp.sympify(expr)
    except sp.SympifyError as e:
        raise ValueError(f"Error al convertir la expresión: {expr}. Detalles: {e}")

def Metodo_Muller(expresion, x_0, x_1, x_2, cifras_significativas):
    print("----------------------------Metodo Müller------------------------")
    x = symbols("x") 
    Error = ""
    #_expresion = expresion.lhs

    #funcion, dicc, Error = validar_funcion(expresion)
    #verificador_error(Error)
    print("expresion: ",expresion)
    print("expresion: ",type(expresion))
    
    funcion = sp.simplify(expresion)
    print("expresion: ",expresion)
    print("expresion: ",type(expresion))

    #Paso 1 --> inicializar las variables (no deben ser iguales)
    X0 = x_0
    X1 = x_1
    X2 = x_2
    Xr = 0
    print(f"Xo: {X0}\nX1: {X1}\nX2: {X2}")

    #Paso 2 --> Determinar Es
    Es, Error = funciones_herramientas.calcular_Es(cifras_significativas)
    verificador_error(Error)

    print("Cifras significativas: ",cifras_significativas)
    print("Nivel de tolerancia: ",Es, "%")

    #Paso 3 --> Calcular la funcion con los valores iniciales
    f = sp.lambdify(x, funcion,modules='sympy')  #--> Se va a evaluar la expresion
    #print(type(f))
    conteo = 1
    df = pd.DataFrame(columns=["Iteracion","Xi","Ea %"])

    Mensaje = "Metodo de Muller\n"
    Mensaje = Mensaje + f"Expresion ingresada: {expresion}, xo = {x_0}, x1 = {x_1}, x2 = {x_2}\n"
    Mensaje = Mensaje + f"Cifras significativas: {cifras_significativas} con un Nivel de tolerancia: Es = {Es}\n"


    while True:
        #se evalua en la funcion los valores iniciales
        f0 = f(X0) 
        f2 = f(X2)
        f1 = f(X1)
        print("tipos f")
        print(type(f(X0)))
        print(type(f(X1)))
        print(type(f(X2)))

        #Paso 4 --> Calcular ho y hi
        ho = X1 - X0
        if ho == 0:
            Error = "ho no debe ser cero"
            verificador_error(Error)
            break

        hi = X2 - X1
        if hi == 0:
            Error = "hi no debe ser cero"
            verificador_error(Error)
            break

        #Paso 5 --> Calcular S0 y S1
        S0 = (f1 - f0)/(ho)
        S1 = (f2 - f1)/(hi)

        #Paso 6 --> Calcular a,b,c
        a = (S1-S0)/(hi+ho)
        b = (a*hi) + S1
        c = f2

        #Paso 7 --> calcular el discriminante
        D = sp.sqrt((b**2)-(4*a*c))

        # Paso 8 -->Condicion
        if (abs(b + D))>(abs(b - D)):
            Xr = X2 + ((-2*c)/(b+D))
        else:
            Xr = X2 + ((-2*c)/(b-D))

        print("x2 = ",X2)
        print(type(f(X2)))

        print("xr = ",Xr)
        print(type(f(Xr)))
        #Paso 9 -->Calcular Ea
        Ea, Error = funciones_herramientas.calcular_Ea(Xr, X2)
        verificador_error(Error)

        #Tabla para mostrar datos y tener un control de las evaluaciones
        df.loc[conteo-1]=[conteo,Xr,Ea] 

        if Ea<Es:
            break

        X0 = X1
        X1 = X2
        X2 = Xr
        conteo += 1

    Mensaje = Mensaje + f"{df}\n"
    Mensaje = Mensaje + f"\nLa raiz aproximada es {Xr} con un error de {Ea} % en la {conteo} iteracion\n"
    print(df)
    print(f"\nLa raiz aproximada es {Xr} con un error de {Ea} % en la {conteo} iteracion\n")

    generales_Muller.set_transportador(expresion)
    generales_Muller.set_transportador(Mensaje)
    generales_Muller.set_transportador(Error)

    x_reales, x_imaginarias = funciones_herramientas.validar_raices(X1)
    x_reales, x_imaginarias, Error = funciones_herramientas.validar_CamR_I(x_reales, x_imaginarias)
    verificador_error(Error)

    raices_reales_Muller.set_transportador(x_reales)

    x_reales, x_imaginarias = funciones_herramientas.validar_raices(X2)
    x_reales, x_imaginarias, Error = funciones_herramientas.validar_CamR_I(x_reales, x_imaginarias)
    verificador_error(Error)

    raices_reales_Muller.set_transportador(x_reales)

    x_reales, x_imaginarias = funciones_herramientas.validar_raices(Xr)
    x_reales, x_imaginarias, Error = funciones_herramientas.validar_CamR_I(x_reales, x_imaginarias)
    verificador_error(Error)

    raices_reales_Muller.set_transportador(x_reales)

    print(f"Xr: {Xr}")
    print(f"Xr t: {type(Xr)}")
    print(f"Xr: {x_reales}")
    print(f"Xr t: {type(x_reales)}")
    print(f"Xr: {raices_reales_Muller.get_transportador(indice=0)}")

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

mostrar = False
boton_resolver = None
boton_limpiar = None
canvas = None

#----------------Funciones para los botones de la segunda interfaz---------------------------------

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

def Ventana_Metodo_Muller(frame,ventana2,ventana):

    #disposicion de botones
    global marco_muestra_valores
    global canvas

    #botones globales
    global boton_limpiar,boton_resolver
    global tipo_tamaño_letra_ventana2,color_fondo_boton_ventana2,color_fondo_boton_ventana2
    global color_boton_pasar_mouse_ventana2,ancho_borde_ventana2,color_borde_ventana2
    global boton_limpiar,boton_resolver

    #declaracion marco superior
    marco_ingreso_valores = ctk.CTkFrame(frame, width=0, height=260, corner_radius=10)
    marco_ingreso_valores.pack(fill="x", expand=False, padx=10, pady=0)
    marco_ingreso_valores.grid_propagate(False)

    #declaracion marco inferior
    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=590,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)


        #Label titulo
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores, text="Metodo de Muller", font=("Arial Black", 16))
        #posicion
    label_ingrese_funcion.place(x=50,y=20)

        #label funcion
    _func = "Ingrese una funcion"    
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = _func,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=50,y=50)
        #entry funcion
    e_ingrese_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_funcion.place(x=50,y=80)

    #label CS
    _cs = "Ingrese cifras significativas"
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = _cs,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=50,y=120)
        #entry Cs
    e_ingrese_cs = ctk.CTkEntry(marco_ingreso_valores,width=150,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_cs.place(x=50,y=150)

    #label xo
    _x0 = "Ingrese x0"
    label_ingrese_x0 = ctk.CTkLabel(marco_ingreso_valores,text = _x0,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_x0.place(x=500,y=50)
        #entry Xo
    e_ingrese_x0 = ctk.CTkEntry(marco_ingreso_valores,width=150,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_x0.place(x=500,y=80)

    #label x1
    _x1 = "Ingrese x1"
    label_ingrese_x1 = ctk.CTkLabel(marco_ingreso_valores,text = _x1,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_x1.place(x=670,y=50)
        #entry Xo
    e_ingrese_x1 = ctk.CTkEntry(marco_ingreso_valores,width=150,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_x1.place(x=670,y=80)
    
    #label x2
    _x2 = "Ingrese x2"
    label_ingrese_x2 = ctk.CTkLabel(marco_ingreso_valores,text = _x2,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_x2.place(x=500,y=120)
        #entry Xo
    e_ingrese_x2 = ctk.CTkEntry(marco_ingreso_valores,width=150,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_x2.place(x=500,y=150)

    #::validaciones::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #habilitacion de botones globales
    global boton_limpiar,boton_resolver,mostrar

    def Validacion():
        expresion = e_ingrese_funcion.get()
        x0 = e_ingrese_x0.get()
        x1 = e_ingrese_x1.get()
        x2 = e_ingrese_x2.get()
        cs = e_ingrese_cs.get()

        #Vacio
        lista_param = {_func:expresion, _x0:x0, _x1:x1, _x2:x2}

        if not validar_vacio(expresion) or not validar_vacio(x0) or not validar_vacio(x1) or not validar_vacio(x2) or not validar_vacio(cs):
            mens = validar_vacio_g(lista_param)
            verificador_error(mens)
        else:
            #Caracteres permitidos
            expresion, Error = funciones_herramientas.validar_caracteres(expresion)
            verificador_error(Error)
            x0, Error = funciones_herramientas.validar_numeros(x0)
            verificador_error(Error)
            x1, Error = funciones_herramientas.validar_numeros(x1)
            verificador_error(Error)
            x2, Error = funciones_herramientas.validar_numeros(x2)
            verificador_error(Error)
            cs, Error = funciones_herramientas.validar_numeros(cs, "int")
            verificador_error(Error)
            print("cs: ",cs)
            
            #validar x0, x1, x2
            if x0 == x1 and x0 == x2:
                Error = "x0, x1 y x2 no deben ser iguales"
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

            """#Validar igualdad
            expresion, Error = funciones_herramientas.validar_igualdad(expresion)
            verificador_error(Error)"""

            #validar implicita
            expresion_valid, Error = funciones_herramientas.validar_multiplicacion_implicita(expresion)
            verificador_error(Error)

    
            muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

            #Ecuaciones_Cuadraticas(funcion, destinos) 
            Metodo_Muller(expresion_valid, x0, x1, x2, cs) 
        
            #impresion de datos
            muestra_valores.configure(text = generales_Muller.get_transportador(1), anchor='w', justify='left')

            #impresion del grafico
            fig = Grafico(generales_Muller.get_transportador(0), raices_reales_Muller.get_transportador())
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
            e_ingrese_x0.delete(0, END)
            e_ingrese_x1.delete(0, END)
            e_ingrese_x2.delete(0, END)
            e_ingrese_cs.delete(0, END)
        
   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=200)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=200)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=200)


    