import sympy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sympy import *
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
import ctypes

def Cuadratura_Gaussiana(funcion,a,b,puntos,muestra_valores,muestra_raiz):
    global mostrar
    x = sp.symbols("x")
    f = sp.lambdify(x,funcion)

    valores_mostrar = f"Funcion : {funcion}\na = {a}\nb = {b}\nPuntos = {puntos}"

    h = (b - a)

    if puntos == 1:
        w0 = 2

        t0 = 0

        I = (h / 2) * ( ( w0 * f( (h * t0 + h) / (2) ) ) )

        respuesta = f"∫ {funcion} = {I}"

        muestra_valores.configure(text =valores_mostrar)
        muestra_raiz.configure(text =respuesta)

        mostrar = True

        

    elif puntos == 2:
        w0 = 1
        w1 = 1

        t0 = -0.577350269
        t1 = 0.577350269

        I = (h / 2) * ( ( w0 * f( (h * t0 + h) / (2) ) ) + ( w1 * f( (h * t1 + h) / (2) ) ) )

    
        respuesta = f"∫ {funcion} = {I}"

        muestra_valores.configure(text =valores_mostrar)
        muestra_raiz.configure(text =respuesta)

        mostrar = True

    elif puntos == 3:
        w0 = 0.55555555
        w1 = 0.88888888
        w2 = 0.55555555

        t0 = -0.774596669
        t1 = 0
        t2 = 0.774596669

        I = (h / 2) * ( ( w0 * f( (h * t0 + h) / (2) ) ) + ( w1 * f( (h * t1 + h) / (2) ) ) + ( w2 * f( (h * t2 + h) / (2) ) ))

    
        respuesta = f"∫ {funcion} = {I}"

        muestra_valores.configure(text =valores_mostrar)
        muestra_raiz.configure(text =respuesta)

        mostrar = True

    elif puntos == 4:
        w0 = 0.3478548
        w1 = 0.6521452
        w2 = 0.6521452
        w3 = 0.3478548

        t0 = -0.861136312
        t1 = -0.339981044
        t2 = 0.339981044
        t3 = 0.861136312

        I = (h / 2) * ( ( w0 * f( (h * t0 + h) / (2) ) ) + ( w1 * f( (h * t1 + h) / (2) ) ) + ( w2 * f( (h * t2 + h) / (2) ) ) + ( w3 * f( (h * t3 + h) / (2) ) ))

    
        respuesta = f"∫ {funcion} = {I}"

        muestra_valores.configure(text =valores_mostrar)
        muestra_raiz.configure(text =respuesta)

        mostrar = True


    elif puntos == 5:
        w0 = 0.2369269
        w1 = 0.4786287
        w2 = 0.5688889
        w3 = 0.4786287
        w4 = 0.2369269

        t0 = -0.906179846
        t1 = -0.538469310
        t2 = 0
        t3 = 0.538469310
        t4 = 0.906179846

        I = (h / 2) * ( ( w0 * f( (h * t0 + h) / (2) ) ) + ( w1 * f( (h * t1 + h) / (2) ) ) + ( w2 * f( (h * t2 + h) / (2) ) ) + ( w3 * f( (h * t3 + h) / (2) ) ) + ( w4 * f( (h * t4 + h) / (2) ) ))

    
        respuesta = f"∫ {funcion} = {I}"

        muestra_valores.configure(text =valores_mostrar)
        muestra_raiz.configure(text =respuesta)

        mostrar = True


    elif puntos == 6:
        w0 = 0.1713245
        w1 = 0.3607616
        w2 = 0.4679139
        w3 = 0.4679139
        w4 = 0.3607616
        w5 = 0.1713245

        t0 = -0.932469514
        t1 = -0.661209386
        t2 = -0.238619186
        t3 = 0.238619186
        t4 = 0.661209386
        t5 = 0.932469514

        I = (h / 2) * ( ( w0 * f( (h * t0 + h) / (2) ) ) + ( w1 * f( (h * t1 + h) / (2) ) ) + ( w2 * f( (h * t2 + h) / (2) ) ) + ( w3 * f( (h * t3 + h) / (2) ) ) + ( w4 * f( (h * t4 + h) / (2) ) ) +  ( w5 * f( (h * t5 + h) / (2) ) ))

    
        respuesta = f"∫ {funcion} = {I}"

        muestra_valores.configure(text =valores_mostrar)
        muestra_raiz.configure(text =respuesta)

        mostrar = True


1

"""x = sp.symbols("x")
funcion = sp.sin(sp.pi * x)
a = -2
b = -1

puntos = 6

Cuadratura_Gaussiana(funcion,a,b,puntos)"""


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



def Ventana_Cuadratura_Gaussiana(frame,ventana2,ventana):

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

    etiqueta_ingreso_valor_a= ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor de a",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_a.place(x=40,y=20)

    etiqueta_ingreso_valor_b = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor de b",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_b.place(x=400,y=20)

    etiqueta_ingreso_puntos = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el punto",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_puntos.place(x=675,y=20)

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=1000,y=20)

    
    ingreso_valor_a = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_a.place(x=50,y=60)

    ingreso_valor_b = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_b.place(x=400,y=60)

    ingreso_puntos = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_puntos.place(x=675,y=60)

    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=1000,y=60)

    def numero_valido(texto):
        return re.match(r"^-?\d*\.?\d*$", texto) is not None

    def Validar_y_Reemplazar_funcion(funcion_str):
        x= sp.symbols('x')
        
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
        global boton_limpiar,boton_resolver,mostrar
        #Se valida el ingreso de datos
        a= ingreso_valor_a.get()
        b = ingreso_valor_b.get()
        puntos = ingreso_puntos.get()
        funcion = ingreso_funcion.get()

        #Si estan vacios todos
        if a == "" and b == "" and puntos == "" and funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
        #SI uno o varios estan vacios
        elif a == "" or b == "" or  puntos == "" or funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
            #si todos estan llenados   
        else:

            valida,funcion_str = Validar_y_Reemplazar_funcion(funcion)
            if numero_valido(a) and numero_valido(b) and  numero_valido(puntos) :
                if valida == True :

                    a = float(a)
                    b = float(b)
                    puntos = float(puntos)
                    funcion = funcion_str

                    muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")
                                      

                    muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")

                    

                    Cuadratura_Gaussiana(funcion,a,b,puntos,muestra_valores,muestra_raiz)
                
                    if mostrar == True:
                        
                        muestra_valores.place(x=50,y=50)
                        muestra_raiz.place(x=50,y=200)

                        #Se desactiva el botón de Resolver
                        boton_resolver.configure(state=DISABLED)
                        #Se activa el botón de Limpiar
                        boton_limpiar.configure(state=NORMAL)
                    
                    
                    #Se limpia los entry cuando ya se resulve por el metodo
                    ingreso_valor_a.delete(0, END)
                    ingreso_valor_b.delete(0, END)
                    ingreso_puntos.delete(0, END)
                    ingreso_funcion.delete(0, END)

                else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Error al ingresar la funcion")
                    
            else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Solo debe ingresar valores numericos en los 4 primeros campos")
            

   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=125)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=125)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=125)

