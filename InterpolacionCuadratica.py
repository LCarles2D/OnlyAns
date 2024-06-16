#!/usr/bin/env python3
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
from functools import partial

######## FUNCIONES PARA RESOLVER
def get_Bn(n1, n2, puntos, fx):
    return (fx[n2] - fx[n1])/(puntos[n2] - puntos[n1])


def interpolacionCuadratica(xk,yk, inter_point, ecuacion = None):

    
    x = sp.symbols("x")
    if ecuacion != None:
        yk = [ecuacion.subs(x, xi).evalf() for xi in xk]

  
    fx = yk
    b0 = fx[0]

    b1 = get_Bn(0, 1, xk, fx)
    b2 = (get_Bn(1,2, xk, fx) - b1) / (xk[2] - xk[0])
    Px = b0 + b1*(x - xk[0]) + b2*(x-xk[0])*(x-xk[1])
    Px = sp.simplify(Px)

    valor_aprox = Px.subs(x, inter_point).evalf()
    return Px, valor_aprox


######## INTERFAZ
#Variables
color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2
toggle = False

def Ventana_Interpolacion_Cuadratica(frame, ventana2, ventana):
    global toggle
    global marco_muestra_valores
    global canvas

    global boton_limpiar,boton_resolver
    global tipo_tamaño_letra_ventana2,color_fondo_boton_ventana2,color_fondo_boton_ventana2
    global color_boton_pasar_mouse_ventana2,ancho_borde_ventana2,color_borde_ventana2
    global boton_limpiar,boton_resolver

    ########### Marcos
    marco_height = 300
    marco_ingreso_valores = ctk.CTkFrame(frame, width=0, height=marco_height, corner_radius=10)
    marco_ingreso_valores.pack(fill="x", expand=False, padx=10, pady=0)
    marco_ingreso_valores.grid_propagate(False)

    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=600,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)

    ########### Etiquetas
    etiqueta_ingreso_valores_x = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese los valores de x",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valores_x.place(x=40,y=20)

    etiqueta_ingreso_valores_y = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese los valores de y",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valores_y.place(x=320,y=20)

    etiqueta_ingreso_interpolacion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el punto de interpolacion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_interpolacion.place(x=565,y=20)

    necesarios = [marco_ingreso_valores, tipo_tamaño_letra_ventana2, color_texto_ventana2]
    
    ############# Entrada de valores
    ingresos_x0 =IngresarEnCadena(*necesarios, 100, 60, 2)
    ingresos_y = IngresarEnCadena(*necesarios, 325, 60, 2)
    

    ingreso_interpolacion = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_interpolacion.place(x=600,y=60)


    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)


    ########### Alternar entre funcion y valores de y 
    def Alternar_visibilidad(entradas):
        global toggle
        if toggle == False:
            boton_funcion_valores.configure(text="Valores de y")
            etiqueta_ingreso_valores_y.configure(text='Funcion')
            toggle = True
            ingreso_funcion.place(x=325,y=60)

            for entrada in entradas:
                entrada.delete(0, END)
                entrada.place_forget()
        else:
            boton_funcion_valores.configure(text='Funcion')
            etiqueta_ingreso_valores_y.configure(text='Valores de y')
            toggle= False
            ingreso_funcion.delete(0, END)
            ingreso_funcion.place_forget()
            
            for i in range(0,len(entradas)):        
                entradas[i].place(x=325,y=(60 + 30*i + 10*i))

    boton_funcion_valores = ctk.CTkButton(marco_ingreso_valores,text ="Funcion",command=partial(Alternar_visibilidad, ingresos_y),fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_funcion_valores.place(x=350 , y=225)


    def numero_valido(texto):
        return re.match(r"^-?\d*\.?\d*$", texto) is not None

    def Validacion_Funcion(funcion):
        patron = r'^(\s*\d+|\+|\-|\*{1,2}|/|\(|\)|x|e|sin\(x\)|cos\(x\)|tan\(x\)|asin\(x\)|acos\(x\)|atan\(x\)|log\(x\)|ln\(x\)|sqrt\(x\)|sqrt\d*\(x\))*\s*$'
        return re.match(patron, funcion) is not None
    
    def Convertir_Funcion(funcion):
        try:
            #Intenta convertir la entrada en una expresion simbolica
            sp.sympify(funcion)
            return True
        except (sp.SympifyError, TypeError,SyntaxError):
            #Si hay un error en la sintaxis la entrada no es valida
            return False
    def Validar_y_Reemplazar_funcion(funcion_str):
        x= sp.symbols('x')
        
        # Reemplazar 'e**' por 'exp(' y agregar ')' después del término completo
        def replacer(match): 
            return f"exp({match.group(1)})"
        # Primero, reemplazar 'ln' por 'log'
        funcion_str = funcion_str.replace('ln', 'log')
        
        # Luego, reemplazar 'e**...' por 'exp(...)'
        funcion_str = re.sub(r'e\*\*\((.*?)\)', replacer, funcion_str)
        
        # Finalmente, reemplazar 'e' por 'exp(1)' cuando no está seguido por '**'
        funcion_str = re.sub(r'\be\b(?![\*\w])', 'exp(1)', funcion_str) 

        print('expresion', funcion_str)
        try:
            # Intenta convertir la función ingresada en una expresión sympy
            expr = sp.sympify(funcion_str)
            
            # Verifica si la expresión contiene solo la variable 'x'
            if expr.free_symbols <= {x, sp.exp(1)}:  # Permitir x y la constante e
                return True, expr
            else:
                return False, None
        except Exception as e:
            #messagebox.showerror("Error de validación", f"La función ingresada no es válida")
            return False, None

    def Validacion():
        global boton_limpiar,boton_resolver,mostrar
        #Se valida el ingreso de datos
        valores_x = [ingreso.get() for ingreso in ingresos_x0]
        valores_y = [ingreso.get() for ingreso in ingresos_y]
        interpolacion = ingreso_interpolacion.get()
        funcion = ingreso_funcion.get()

        #Si estan vacios todos
        if (valores_x[0] == '' or valores_x[1] == '' or interpolacion == '') or ((valores_y[0] == '' or valores_y[1] == '') and funcion == '') :
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos de forma correcta")
        else:
            
            if numero_valido(valores_x[0]) and numero_valido(valores_x[1]) and numero_valido(interpolacion):

                if funcion == '':    
                    valores_y = [float(valores) for valores in valores_y]
                    funcion = None
                else:
                    print('La funcion', funcion)
                    booleano, funcion = Validar_y_Reemplazar_funcion(funcion)
                    print(booleano, funcion)
                    valores_y = None
                """else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Ingrese una  funcion valida")
                    return"""

                valores_x = [float(valor) for valor in valores_x]
                interpolacion = float(interpolacion)

                muestra_valores = ctk.CTkLabel(marco_muestra_valores,font= ("Currier",15,"bold"), justify= 'left', anchor='w')
                
                Px, valor_aprox = interpolacion_Lineal(valores_x,valores_y,interpolacion,funcion)
                print(Px, valor_aprox)
                if valores_y == None:
                    muestra_valores.configure(text=f'x1 = {valores_x[0]}\n\nx2 = {valores_x[1]}\n\nevaluados en f(x) = {funcion}\n\n Con un polinomio interpolador de Px = {Px} con un valor aproximado de {valor_aprox} con un punto de interpolacion de {interpolacion}')
                else:
                    muestra_valores.configure(text=f'x1 = {valores_x[0]}\n\nx2 = {valores_x[1]}\n\ny1 = {valores_y[0]}\n\ny2 = {valores_y[1]}\n\nCon un polinomio interpolador de Px = {Px} con un valor aproximado de {valor_aprox}')



                if mostrar == True:
                    muestra_valores.place(x=10,y=20)

                #Se desactiva el botón de Resolver
                boton_resolver.configure(state=DISABLED)
                #Se activa el botón de Limpiar
                boton_limpiar.configure(state=NORMAL)
                
                
                #Se limpia los entry cuando ya se resulve por el metodo
                [ingresos.delete(0, END) for ingresos in ingresos_x0]
                [ingresos.delete(0, END) for ingresos in ingresos_y]
                ingreso_interpolacion.delete(0, END)
                ingreso_funcion.delete(0, END)

            else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Asegurate de ingresar valores numericos en los campos correspondientes")
            
    
    y_pos = 225
   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=y_pos)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=y_pos)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=y_pos)


def Volver(ventana2,ventana):
    ventana2.destroy()
    ventana.deiconify()


def IngresarEnCadena(marco, fuente, color, x, y, cantidad):
    ingresos = []
    for i in range(0, cantidad):
        ingresos.append(ctk.CTkEntry(marco,width=100,height=30,corner_radius=10,font = fuente,text_color=color))
        ingresos[i].place(x=x,y=(y + 30*i + 10*i))
    return ingresos

def Limpiar():
    global marco_muestra_valores
    global canvas
    global boton_resolver,boton_limpiar 

    boton_resolver.configure(state=NORMAL)
    boton_limpiar.configure(state=DISABLED)

    # Iterar sobre los widgets y destruirlos uno por uno
    for widget in marco_muestra_valores.winfo_children():
        widget.destroy()

    

