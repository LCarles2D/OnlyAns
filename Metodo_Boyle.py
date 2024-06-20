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

def Metodo_Boyle(funcion,a,b,muestra_valores,muestra_raiz):
    global mostrar
    x = sp.symbols("x")
    f = sp.lambdify(x,funcion)

    #Encontramos el vlaor de h
    h = ( b - a ) / 4

    valores_mostrar  = f"Funcion : {funcion}\na  = {a}\nb = {b}\nh = {h}"

    puntos_consecutivos = []

    puntos_consecutivos.append(a)

    for i in range(5):
        a += h
        puntos_consecutivos.append(a)

    formula = ((2 * h)/(45)) * ( (7 * f(puntos_consecutivos[0])) + (32 * f(puntos_consecutivos[1])) + (12 * f(puntos_consecutivos[2])) + (32 * f(puntos_consecutivos[3])) + (7 * f(puntos_consecutivos[4])) )

    respuesta = f"∫ {funcion} dx = {formula}"

    muestra_valores.configure(text =valores_mostrar)
    muestra_raiz.configure(text =respuesta)

    mostrar = True
    

"""
x = sp.symbols("x")
funcion = (x ** 2) * sp.log(x)
a = 1
b = 1.5

Metodo_Boyle(funcion,a,b)
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



def Ventana_Metodo_Boyle(frame,ventana2,ventana):

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

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=1000,y=20)

    
    ingreso_valor_a = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_a.place(x=50,y=60)

    ingreso_valor_b = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_b.place(x=400,y=60)

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
        funcion = ingreso_funcion.get()

        #Si estan vacios todos
        if a == "" and b == ""  and funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
        #SI uno o varios estan vacios
        elif a == "" or b == ""  or funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
            #si todos estan llenados   
        else:

            valida,funcion_str = Validar_y_Reemplazar_funcion(funcion)
            if numero_valido(a) and numero_valido(b) :
                if valida == True :

                    a = float(a)
                    b = float(b)
                    funcion = funcion_str

                    muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")
                                      

                    muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")

                    

                    Metodo_Boyle(funcion,a,b,muestra_valores,muestra_raiz)
                
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