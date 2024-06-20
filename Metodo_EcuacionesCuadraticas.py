# Metodo_EcuacionesCuadraticas.py
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
import funciones_herramientas 
from funciones_herramientas import *

#funcion complementarias:    
def impr_error(Error):
    if not (Error == None or Error == ""):
        messagebox.showerror("¡ ERROR CRITICO !", message = Error)
    else:
        pass   
#iniciar transportadores:
general_ECuadratica = funciones_herramientas.Transportador()
raices_reales_ECuadratica = funciones_herramientas.Transportador()
raices_imaginarias_ECuadratica = funciones_herramientas.Transportador()

#Recibe funcion, ver_valores: widget ver_grafico:  widget
def Ecuaciones_Cuadraticas(expresion):
    print("Entra al metodo")
    Error = ""                      
    x = sp.symbols("x")
    igualdad_cero, Error = funciones_herramientas.validar_igualdad(expresion)
    impr_error(Error)
    impr_error(Error)
    funcion, dicc, Error = funciones_herramientas.validar_funcion(expresion)

    impr_error(Error)
    coeficientes, Error = funciones_herramientas.obtener_coeficientes(expresion)
    impr_error(Error)
    """coe = sp.Poly(expresion)
    coef = coe.all_coeffs()
    print("coeficientes: ",coef)"""

    grado, Error = funciones_herramientas.obtener_grado(funcion, 2)
    impr_error(Error)

    # Validar grado de la funcion
    if grado != 2:  # El grado de la funcion es distinta de 2
        Error = "Error: grado invalido: el grado de la funcion es distinta de 2"
        impr_error(Error)
        

    # Guardar valores
    A, B, C = None, None, None
    try:
        A, B, C = coeficientes
    except ValueError as err: 
        Error = "Ha ocurrido un error a la hora de optener los coeficientes"
        impr_error(Error)   

    # Resolver la ecuación
    x1 = sp.simplify((-B + sp.sqrt(B**2 - 4*A*C)) / (2*A))
    x2 = sp.simplify((-B - sp.sqrt(B**2 - 4*A*C)) / (2*A))

    x_reales, x_imaginarios = [], []
    raices_reales, raices_imaginarias = [], []
    Mensaje = ""

    x1_exacto = sp.N(x1, 5)
    x2_exacto = sp.N(x2, 5)

    # Convertir los resultados a flotantes si es posible
    
    try:
        x1_exacto = float(x1_exacto)
    except ValueError as Err:
        Error = "Ha habido un error en la conversion de a tipo flotante de x1"
        impr_error(Error)
    try:
        x2_exacto = float(x2_exacto)
    except ValueError as Err:
        Error = "Ha habido un error en la conversion de a tipo flotante de x2"
        impr_error(Error)
    

    x_reales, x_imaginarios = validar_raices(x1_exacto)
    raices_reales.extend(x_reales)
    raices_imaginarias.extend(x_imaginarios)

    x_reales, x_imaginarios = validar_raices(x2_exacto)
    raices_reales.extend(x_reales)
    raices_imaginarias.extend(x_imaginarios)

    # Enviar mostrar resultado a ver_valores
    Mensaje = "Metodo Ecuaciones cuadradas\n"
    if len(raices_imaginarias) == 0:
        Mensaje = Mensaje + f"Expresion ingresada: {funcion}\n\nGrado de la expresion: {grado}\n\nRaices Reales: {len(raices_reales)}: 1[{x1_exacto}] , 2[{x2_exacto}]"
        print(Mensaje)
    elif len(raices_imaginarias) == 0:
        Mensaje = Mensaje + f"Expresion ingresada: {funcion}\n\nGrado de la expresion: {grado}\n\nRaices Reales: {len(raices_imaginarias)}: 1[{x1_exacto}] , 2[{x2_exacto}]"
        print(Mensaje)
    else:    
        Mensaje = Mensaje + f"Expresion ingresada: {funcion}\n\nGrado de la expresion: {grado}\n\nRaices: ({len(raices_reales) + len(raices_imaginarias)})\n\nReales: {raices_reales}\n\nImaginarias: {raices_imaginarias}"
        print(Mensaje)
    
    general_ECuadratica.set_transportador(expresion)
    general_ECuadratica.set_transportador(Mensaje)
    general_ECuadratica.set_transportador(Error)
    print("general_Ecuadratica 1: ",general_ECuadratica.get_transportador(0))
    print("general_Ecuadratica 2: ",general_ECuadratica.get_transportador(1))
    print("general_Ecuadratica 3: ",general_ECuadratica.get_transportador(2))
    raices_reales_ECuadratica.set_transportador(raices_reales)
    raices_imaginarias_ECuadratica.set_transportador(raices_imaginarias)
    
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

def Ventana_Ecuaciones_Cuadraticas(frame,ventana2,ventana):

    #disposicion de botones
    global marco_muestra_valores
    global canvas

    #botones globales
    global boton_limpiar,boton_resolver
    global tipo_tamaño_letra_ventana2,color_fondo_boton_ventana2,color_fondo_boton_ventana2
    global color_boton_pasar_mouse_ventana2,ancho_borde_ventana2,color_borde_ventana2
    global boton_limpiar,boton_resolver

    #declaracion marco superior
    marco_ingreso_valores = ctk.CTkFrame(frame, width=0, height=250, corner_radius=10)
    marco_ingreso_valores.pack(fill="x", expand=False, padx=10, pady=0)
    marco_ingreso_valores.grid_propagate(False)

    #declaracion marco inferior
    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=600,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)

        #declaracion label titulo
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores, text="Metodo Ecuaciones Cuadraticas", font=("Arial Black", 16))
        #posicion
    label_ingrese_funcion.place(x=50,y=20)

        #declaracion label
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese una funcion",font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=50,y=50)

    #boton informacion
    def habilitar_boton_informacion():
        if label_informacion.winfo_ismapped():
            label_informacion.place_forget()
        else:
            label_informacion.place(x=350, y=50)

    label_informacion = ctk.CTkLabel(marco_ingreso_valores, text="El método de Ecuaciones Cuadraticas\nsirve para resolver ecuaciones\ncuadráticas consiste en encontrar\nlas soluciones de una ecuación\nde la forma: ax**2 + bx + c = 0", font=tipo_tamaño_letra_ventana2)
    label_informacion.place_forget()

    boton_informacion = ctk.CTkButton(marco_ingreso_valores, text="i", command=habilitar_boton_informacion,height = 20,width=20)
    boton_informacion.place(x=300, y=50)

        #declaracion entry
    entry_ingrese_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    entry_ingrese_funcion.place(x=50,y=80)

    #::validaciones::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #habilitacion de botones globales
    global boton_limpiar,boton_resolver,mostrar

    def Validacion():
        expresion_recib = entry_ingrese_funcion.get()

        #Vacio
        if expresion_recib == "" or expresion_recib == None:
            messagebox.showerror("¡ ERROR CRITICO !", message = f"Parece que el campo: Ingrese funcion, esta vacio")
        else:
            #Caracteres permitidos
            expresion_carac, Error = funciones_herramientas.validar_caracteres(expresion_recib)
            impr_error(Error)

            #Apertura y cierre de signos de agrupacion
            expresion_carac, Error = funciones_herramientas.validar_PCL(expresion_carac)
            impr_error(Error)

            #Multiplicacion implicita
            expresion_valid, Error = funciones_herramientas.validar_multiplicacion_implicita(expresion_carac)    
            impr_error(Error)

            #crear los espacios donde se estableceran los resultados, indicanto el marcos
            muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

            #Ecuaciones_Cuadraticas(funcion, destinos) 
            Ecuaciones_Cuadraticas(expresion_valid) 
            
            #traer valores a mostrar de Ecuaciones_Cuadraticas
            #transport_valores.get_transportador() -> muetra_valores -> marco_muestra_valores
            muestra_valores.configure(text = general_ECuadratica.get_transportador(1), anchor='w', justify='left')
            print("\nFuera del metodo: valores: ",general_ECuadratica.get_transportador(1))

            #impresion del grafico
            # Crear y mostrar el gráfico
            #print("fuera del metodo: grafico: [0]",transport_graf_ECuadraticas.get_transportador(0))
            #print("fuera del metodo: grafico: [1]",transport_graf_ECuadraticas.get_transportador(1))
            fig = Grafico(general_ECuadratica.get_transportador(0), raices_reales_ECuadratica.get_transportador())
            canvas = FigureCanvasTkAgg(fig, master = muestra_grafica)
            #grafico(funcion, x_valores)
            #indice = 0:mensaje, 1:funcion, 2:list_reales, 3:list_imaginarios

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
            entry_ingrese_funcion.delete(0, END)
        
   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=125)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=125)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=125)
