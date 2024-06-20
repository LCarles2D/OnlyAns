
import sympy as sp
from sympy import symbols, sqrt, Poly, div , root , acos
import pandas as pd
import numpy as np
import funciones_herramientas
from funciones_herramientas import *
import math as math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
import ctypes

def verificador_error(Error):
    if not (Error == None or Error == ""):
        messagebox.showerror("¡ ERROR CRITICO !", message = Error)
    else:
        pass

#iniciar transportadores:
#trnasporte_val_tartaglia(0:funcion ,1:p 2:q, 3:D ,4:Mensaje)
generales_Tartaglia = funciones_herramientas.Transportador()
raices_reales_Tartaglia = funciones_herramientas.Transportador()
raices_imaginarias_Tartaglia = funciones_herramientas.Transportador()


#transport_val_ECuadraticas = funciones_herramientas.Transportador()
#transport_graf_ECuadraticas = funciones_herramientas.Transportador()

def Metodo_Tartaglia(expresion):
    print("Entra a metodo")
    x=sp.symbols("x")
    print("ingresa a funcion")
    #expresion_valida = validar_expresion(expresion)
    igualdad_cero, Error = funciones_herramientas.validar_igualdad(expresion)
    verificador_error(Error)
    funcion, dicc, Error = funciones_herramientas.validar_funcion(igualdad_cero)
    verificador_error(Error)
    coeficientes, Error = funciones_herramientas.obtener_coeficientes(expresion)
    print("coeficientes: ",coeficientes)
    print(coeficientes)
    grado, Error = funciones_herramientas.obtener_grado(expresion, 3)
    if not grado == 3:
        Error = "Error: grado invalido: el grado de la funcion es distinta de segunda grado"
        verificador_error(Error)
        
    if coeficientes[0] != 1:# Si el primer coeficiente es diferente de 1
        primer_coeficiente = coeficientes[0]
        #impr("primer coeficiente",coeficientes[0])
        nuevo_coeficientes = [coef / primer_coeficiente for coef in coeficientes]
        #impr("nuevo_coeficientes", nuevo_coeficientes)
        coeficientes = nuevo_coeficientes
        #impr("nuevos coeficientes",coeficientes)
        
    f, a, b, c = coeficientes # Guardamos los coeficientes en distintas varibles
    print(f"f: {f}, a: {a}, b: {b}, c: {c}")

    #1. calcular p y q
    p = (3*b - a**2)/3 
    q = (2*a**3 - 9*a*b + 27*c)/27

    #2. calculamos el discriminante
    D = (q/2)**2 + (p/3)**3
    
    print("p: ",p)
    print("q: ",q)
    print("determinante: ",D)

    raices_reales, raices_imaginarias = [], []
    x_reales, x_imaginarias = [], []
    Mensaje = ""
    Error = ""    

    #Condiciones
    if D == 0: #Si el discriminante es igual a cero
        print("D=0")
        p_q = p*q #multiplico p * q
        if p == 0 and q == 0: #Si p y q son iguales a cero
            print("p, q = 0")
            raiz_triple = -(a/3) # tiene una raiz triple
            raiz_triple = float(raiz_triple)
            
            Mensaje = f"Metodo de Targtaglia:\nCon un discriminante: {D}, p = {p} y q = {q}\nSe tiene las raices:"
            Mensaje = Mensaje + f"Raiz Triple: [{raiz_triple}]"

            x_reales, x_imaginarias = validar_raices(raiz_triple)
            
        elif p_q != 0: #Si la multiplicacion de p * q es diferente de cero
            print("pq != 0")
            raiz_doble = -((3*q)/(2*p)) - (a/3)#Se encuentra la raiz doble
            raiz = -((4*p**2)/(9*q)) - (a/3) 

            raiz_doble = float(raiz_doble)
            raiz = float(raiz)

            Mensaje = f"Metodo de Targtaglia:\nCon un discriminante: {D}, p = {p} y q = {q}\nSe tiene las raices:"
            Mensaje = Mensaje + f"    3 Raices Reales: 1.[{raiz}] y Raiz Doble: 2.[{raiz_doble}] , 3.[{raiz_doble}]"

            print("raiz: ",raiz)
            x_reales, x_imaginarias =  funciones_herramientas.validar_raices(raiz)
            raices_reales.append(x_reales)
            raices_imaginarias.append(x_imaginarias)
            x_reales, x_imaginarias =  funciones_herramientas.validar_raices(raiz_doble)
            raices_reales.append(x_reales)
            raices_reales.append(x_reales)
            raices_imaginarias.append(x_reales)
            raices_imaginarias.append(x_reales)

    elif D>0: #Si el discriminante es mayor a cero
        print("D>0")
        #Calculamos U y V
        U = math.cbrt((-q/2) + sp.sqrt(D))#Con la raiz cubica a todo
        V = math.cbrt((-q/2) - sp.sqrt(D)) #con la raiz cubica a todo

        #Calculamos la raiz real

        raiz_real = (( sp.root((-(q/2)) + sqrt(D),3) ) + (sp.root( (-(q/2)) - sp.sqrt(D),3) ) )- (a/3) 
        raiz_real = (U + V) - (a/3)
        raiz_real = float(raiz_real)
        #impr_grafico(expresion, funcion, raices_validadas)

        #Calculamos la raiz imaginaria
        raiz_imaginaria_uno =  (-((U + V ) / 2 )) - (a/3) + complex( (((sqrt(3))/2) * (U - V)) )# i 
        raiz_imaginaria_dos =  (-((U + V ) / 2 )) - (a/3) - complex( (((sqrt(3))/2) * (U - V)) )# i 

        raiz_imaginaria_uno = float(raiz_imaginaria_uno)
        raiz_imaginaria_dos = float(raiz_imaginaria_dos)

        Mensaje = f"Metodo de Targtaglia:\nCon un discriminante: {D}, p = {p} y q = {q}\nSe tiene las raices:"
        Mensaje = Mensaje + f"    1 Raiz Real: 1. [{raiz_real}]\n    2 Raices Imaginarias: 2.[{raiz_imaginaria_uno}]i , 3.[{raiz_imaginaria_dos}]i"

        x_reales.append(raiz_real)
        raices_reales.extend(x_reales)
        
        x_imaginarias.append(raiz_imaginaria_uno)
        x_imaginarias.append(raiz_imaginaria_dos)
        raices_imaginarias.extend(x_imaginarias)


    elif D<0: #Si el discriminante es menor a cero
        #Calculamos el angulo Cos θ
        angulo = sp.acos( (-(q/2)) / (sp.sqrt((-((p/3)**3)))) )
        #Utilizamos un valor de K=0,1,2
        
        if 0 < angulo < sp.pi:
            print("D<0")
            K1 = 0
            raiz1 = 2 * (sp.sqrt(-(p/3))) * sp.cos( (angulo + 2*K1*sp.pi) / (3) ) - (a/3) # Se calcula la raiz
            K2 = 1
            raiz2 = 2 * (sp.sqrt(-(p/3))) * sp.cos( (angulo + 2*K2*sp.pi) / (3) ) - (a/3) # Se calcula la raiz
            K3 = 2
            raiz3 = 2 * (sp.sqrt(-(p/3))) * sp.cos( (angulo + 2*K3*sp.pi) / (3) ) - (a/3) # Se calcula la raiz
            
            Mensaje = f"Metodo de Targtaglia:\nCon un discriminante: {D}, p = {p} y q = {q}\nSe tiene las raices:"
            Mensaje = Mensaje + f"    3 Raices Reales: 1.[{raiz1}, con K = {K1}] 2.[{raiz2}, con K = {K2}] \n3.[{raiz3}, con K = {K3}]"

            x_reales, x_imaginarias = funciones_herramientas.validar_raices(raiz1)
            raices_reales.append(x_reales)
            raices_imaginarias.append(x_imaginarias)

            x_reales, x_imaginarias = funciones_herramientas.validar_raices(raiz2)
            raices_reales.append(x_reales)
            raices_imaginarias.append(x_imaginarias)

            x_reales, x_imaginarias = funciones_herramientas.validar_raices(raiz3)
            raices_reales.append(x_reales)
            raices_imaginarias.append(x_imaginarias)

        else:
            Error = f"Error: Se encontro que el discriminante es :{D}\np = {p} y q = {q}\nEl angulo es :{angulo} este no se encuentra entre 0 y pi"

    #generales_Tartaglia.set_transportador (1:expresion, 2:Mensaje, 3:Error)
    #raices_Tartaglia.set_transportador (1:raices_reales, 2:raices_imaginarias)
    
    generales_Tartaglia.set_transportador(expresion)
    generales_Tartaglia.set_transportador(Mensaje)
    generales_Tartaglia.set_transportador(Error)
    
    raices_reales_Tartaglia.set_transportador(raices_reales)
    raices_imaginarias_Tartaglia.set_transportador(raices_imaginarias)

    if raices_imaginarias_Tartaglia.set_transportador == 0: 
        print("list reales: ",raices_reales_Tartaglia.get_transportador())
    else:
        print("list reales: ",raices_reales_Tartaglia.get_transportador())
        print("list imaginarias: ",raices_imaginarias_Tartaglia.get_transportador())
    
    print("para grafico: ",raices_reales_Tartaglia.get_transportador())

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

def Ventana_Metodo_Tartaglia(frame,ventana2,ventana):

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

    #mostrar opciones texto:::::::::::::::::::::::::::::::::::::::::

        #declaracion label titulo
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores, text="Metodo  Tartaglia", font=("Arial Black", 18))
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

    label_informacion = ctk.CTkLabel(marco_ingreso_valores, text="El método de Tartaglia, también conocido\ncomo el método de Cardano-Tartaglia, es una\ntécnica utilizada para resolver ecuaciones\ncúbicas (ecuaciones de tercer grado)", font=tipo_tamaño_letra_ventana2)
    label_informacion.place_forget()

    boton_informacion = ctk.CTkButton(marco_ingreso_valores, text="i", command=habilitar_boton_informacion,height = 20,width=20)
    boton_informacion.place(x=300, y=50)

    #declara informacion:::::::::::::::::::::::::::::::::::::::::

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
            messagebox.showerror("¡ ERROR CRITICO !", message = f"Parece que el campo: Ingrese funcion, esta vacio\n{expresion_recib}")
        else:
            #Caracteres permitidos
            expresion_carac, Error = funciones_herramientas.validar_caracteres(expresion_recib)
            verificador_error(Error)

            #Apertura y cierre de signos de agrupacion
            expresion_carac, Error = funciones_herramientas.validar_PCL(expresion_carac)
            verificador_error(Error)

            expresion_valid, Error = funciones_herramientas.validar_multiplicacion_implicita(expresion_carac)
            verificador_error(Error)

        #crear los espacios donde se estableceran los resultados, indicanto el marcos
            muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

        #Ecuaciones_Cuadraticas(funcion, destinos) 
            Metodo_Tartaglia(expresion_valid) 
            #generales_Tartaglia.set_transportador (0:expresion, 1:Mensaje, 2:Error)
            #raices_Tartaglia.set_transportador (0:raices_reales, 1:raices_imaginarias)


        #traer valores a mostrar de Metodo_Tartaglia
            #transport_valores.get_transportador() -> muetra_valores -> marco_muestra_valores
            muestra_valores.configure(text = generales_Tartaglia.get_transportador(1), anchor='w', justify='left')
            print("\nFuera del metodo: valores: ",generales_Tartaglia.get_transportador())

        #impresion del grafico
            # Crear y mostrar el gráfico
            print("grafico: ", raices_reales_Tartaglia.get_transportador())
            fig = Grafico(generales_Tartaglia.get_transportador(0), raices_reales_Tartaglia.get_transportador())
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
            entry_ingrese_funcion.delete(0, END)
        
   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=125)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=125)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=125)