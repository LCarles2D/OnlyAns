from typing import Union
import sympy as sp
import pandas as pd
import funciones_herramientas
from funciones_herramientas import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

def verificador_error(Error):
    if not (Error == None or Error == ""):
        messagebox.showerror("¡ ERROR CRITICO !", message = Error)
    else:
        pass

def Metodo_Trapecio_Simple(expresion : str = None, A : Union[int, float] = None , B : Union[int, float] = None, list_a : list = None, list_b : list = None):

    if expresion is not None and list_a is None and list_b is None:
        # Modo función: requiere funcion, A y B
        
        print("Modo función")
        x = sp.symbols('x')
        
        try:
            funcion, Error = funciones_herramientas.validar_funcion_x(expresion)
            if Error:
                verificador_error(Error)
                return

            funcion_A = funcion.subs(x, A)
            print(f"f({A}) = {funcion_A}")
            funcion_B = funcion.subs(x, B)
            print(f"f({B}) = {funcion_B}")

            integral_approx = (B - A) * (funcion_A + funcion_B) / 2
            print(f"[TS: función] La integral aproximada es: {integral_approx}") 
            
        except Exception as e:
            Error = f"Error al evaluar la función, Metodo Trapecio Simple {e}"
            print(f"Error al evaluar la función: {e}")
            verificador_error(Error)

    elif expresion is None and A is None and B is None and list_a is not None and list_b is not None:
        # Modo tabla: requiere lista x y lista y
    
        try:    
            lista_x = list_a
            lista_y = list_b
                            #(b - a)                     #(fa + fb)
            integral_approx = (lista_x[-1] - lista_x[0]) * (lista_y[0] + lista_y[-1]) / 2
            print(f"[TS: modo tabla] La integral aproximada es: {integral_approx}") 
        except Exception as e:
            Error = f"Error: Metodo Trapecio Compuesto {e}"
            print(f"Error: Metodo Trapecio Compuesto {e}")
            verificador_error(Error)

 
def Metodo_Trapecio_Compuesto(grado_integral : int,  n : int, expresion : str = None, A : Union[int, float] = None , B : Union[int, float] = None, list_a : list = None, list_b : list = None):
    
    Error = ""

    if grado_integral == 1:

        if expresion is not None and n is not None and A is not None and B is not None and list_a is None and list_b is None:
            # Modo función: requiere funcion, A, B y n
            x, y, z = sp.symbols('x y z')
            lista_valiables = []

            funcion, lista_variables, Error = funciones_herramientas.validar_funcion_xyz(expresion)
            if Error:
                print(Error)
                return

            if n < 2:
                Error = "El numero de intervalos debe ser mayor o igual que 2"
                verificador_error(Error)

            # Convertir A, B y n a números flotantes e enteros respectivamente
            
            h = (B - A) / n
            
            # Lista para almacenar los puntos desde A hasta B con paso h
            valores_x = [A + i * h for i in range(n + 1)]

            # Lista para almacenar los valores de la función evaluada en esos puntos
            
            valores_funcion = [funcion.subs(x, valor) for valor in valores_x]

            print("Puntos de evaluación x:")
            print(valores_x)
            print("Valores de la función evaluada en esos puntos:")
            print(valores_funcion)

            # Suma desde la segunda posición hasta la penúltima posición
            suma_interior = sum(valores_funcion[1:-2])

            # Fórmula del trapecio compuesto
            integral_aprox = (h * (valores_funcion[0] + 2 * suma_interior + valores_funcion[-1])) / 2
            integral_aprox = float(integral_aprox)

            print(f"[TC: modo funcion] La integral aproximada es: {integral_aprox}")

        elif list_a is not None and list_b is not None and n is not None and expresion is None and A is None and B is None:
            # Modo tabla: requiere lista_x, lista_y, y n

            if n < 2:
                Error = "El numero de intervalos debe ser mayor o igual que 2"
                verificador_error(Error)

            try:    
                lista_x = list_a
                valores_funcion = list_b

                h = (lista_y[1] - lista_y[0]) / n
                
                # Suma desde la segunda posición hasta la penúltima posición
                suma_interior = sum(valores_funcion[1:-2])

                print("Puntos de evaluación x:")
                print(lista_x)
                print("Valores de la función evaluada en esos puntos:")
                print(valores_funcion)
                    
                # Fórmula del trapecio compuesto
                integral_aprox = (h * (valores_funcion[0] + 2 * suma_interior + valores_funcion[-1])) / 2
                integral_aprox = float(integral_aprox)

                print(f"[TC: modo tabla] La integral aproximada es: {integral_aprox}")

            except Exception as e:
                Error = f"Error: Metodo Trapecio Compuesto {e}"
                print(f"Error: Metodo Trapecio Compuesto {e}")

    elif grado_integral >=2:    

        if expresion is not None and n is not None and A is not None and B is not None and list_a is None and list_b is None:
            # Modo función: requiere funcion, A, B y n
            x, y, z = sp.symbols('x y z')

            funcion, Error = funciones_herramientas.validar_funcion_x(expresion)
            if Error:
                print(Error)
                return

            if n < 2:
                Error = "El numero de intervalos debe ser mayor o igual que 2"
                verificador_error(Error)

            # Convertir A, B y n a números flotantes e enteros respectivamente
            
            h = (B - A) / n
            
            # Lista para almacenar los puntos desde A hasta B con paso h
            valores_x = [A + i * h for i in range(n + 1)]

            # Lista para almacenar los valores de la función evaluada en esos puntos
            valores_funcion = [funcion.subs(x, valor) for valor in valores_x]

            print("Puntos de evaluación x:")
            print(valores_x)
            print("Valores de la función evaluada en esos puntos:")
            print(valores_funcion)

            # Suma desde la segunda posición hasta la penúltima posición
            suma_interior = sum(valores_funcion[1:-2])

            # Fórmula del trapecio compuesto
            integral_aprox = (h * (valores_funcion[0] + 2 * suma_interior + valores_funcion[-1])) / 2
            integral_aprox = float(integral_aprox)

            print(f"[TC: modo funcion] La integral aproximada es: {integral_aprox}")

    
print("Primera forma:")
Metodo_Trapecio_Simple(expresion="x**2 - 2*x", A=3, B=5, )

print("\nSegunda forma:")
listx = [3, 5]
listy = [3, 15]
Metodo_Trapecio_Simple(list_a = listx, list_b = listy)    
    
print("\n")

print("primera forma")
Metodo_Trapecio_Compuesto(grado_integral=1, n=4, expresion="2*x**2 + 32", A=-1, B=1)   

lista_x = [-1.0, -0.5, 0.0, 0.5, 1.0]
lista_y = [34, 32.5, 32, 32.5, 34]
print("segunda forma")
Metodo_Trapecio_Compuesto(grado_integral=1, n=4, list_a=lista_x, list_b=lista_y)

#Cosas a verificar
"""
B > A
cant list_a = cant list_b
"""

#UFFFFF
"""print("validar y conversion de funcion")
# Ejemplo adicional de uso con y
expresion_y = "y**2 + 3*y + 2"
funcion_y, mensaje_y = validar_funcion_xyz(expresion_y)
print(mensaje_y)

if funcion_y:
    # Evaluar la función en algunos valores de y
    puntos_y = [1.0, 2.0, 3.0]
    for punto in puntos_y:
        try:
            valor_evaluado_y = evaluar_funcion(funcion_y, {sp.Symbol('y'): punto})
            print(f"y = {punto}, f(y) = {valor_evaluado_y.evalf()}")
        except Exception as e:
            print(f"Error al evaluar en y = {punto}: {e}")"""

#
#
#
#
#
#
#
#
#
#
#  

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

def Ventana_Metodo_Integracion(frame,ventana2,ventana):

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


    """# Primer marco dentro del marco superior izquierda
    marco_izquierdo = ctk.CTkFrame(marco_ingreso_valores, width=375, height=250, corner_radius=10)
    marco_izquierdo.grid(row=0, column=0, padx=10, pady=20)  # Ajustar pady a 20 para espacio arriba

    # Segundo marco dentro del marco superior derecha
    marco_derecho = ctk.CTkFrame(marco_ingreso_valores, width=375, height=250, corner_radius=10)
    marco_derecho.grid(row=0, column=1, padx=10, pady=20)  # Ajustar pady a 20 para espacio arriba


    """

    # Variables de control
    menu_bloqueado = False  # Inicialmente el menú no está bloqueado
    grado_seleccionado = None  # Variable para almacenar el grado de integración seleccionado

    # Funciones para ocultar todos los labels de opciones
    def ocultar_labels():
        for label in [label_opcion1, label_opcion2, label_opcion3, label_opcion4, label_opcion5]:
            label.place_forget()

    def ocultar_labels_grado():
        for label in [grado1, grado2, grado3]:
            label.place_forget()

    # Funciones para los comandos del menú principal
    def opcion_trapecio_simple():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels()
        ocultar_labels_grado()
        label_opcion1.place(x=50, y=80)
        grado1.place(x=50, y=140)  # Mostrar label de Grado 1
        menu_bloqueado = True  # Bloquear menú de grado
        grado_seleccionado = grado1  # Almacenar grado seleccionado
        boton_menu_grado.config(state=tk.DISABLED)  # Deshabilitar botón de grado

    def opcion_trapecio_compuesto():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels()
        ocultar_labels_grado()
        label_opcion2.place(x=50, y=80)
        menu_bloqueado = False  # Desbloquear menú de grado
        boton_menu_grado.config(state=tk.NORMAL)  # Habilitar botón de grado

    def opcion_simpson_13():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels()
        ocultar_labels_grado()
        label_opcion3.place(x=50, y=80)
        menu_bloqueado = False  # Desbloquear menú de grado
        boton_menu_grado.config(state=tk.NORMAL)  # Habilitar botón de grado

    def opcion_simpson_38():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels()
        ocultar_labels_grado()
        label_opcion4.place(x=50, y=80)
        menu_bloqueado = False  # Desbloquear menú de grado
        boton_menu_grado.config(state=tk.NORMAL)  # Habilitar botón de grado

    def opcion_trapecio_simpson():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels()
        ocultar_labels_grado()
        label_opcion5.place(x=50, y=80)
        menu_bloqueado = False  # Desbloquear menú de grado
        boton_menu_grado.config(state=tk.NORMAL)  # Habilitar botón de grado

    # Crear el menú desplegable principal
    menu_desplegable = Menu(ventana, tearoff=0)
    menu_desplegable.add_command(label="Trapecio Simple", command=opcion_trapecio_simple)
    menu_desplegable.add_command(label="Trapecio Compuesto", command=opcion_trapecio_compuesto)
    menu_desplegable.add_command(label="Simpson 1/3", command=opcion_simpson_13)
    menu_desplegable.add_command(label="Simpson 3/8", command=opcion_simpson_38)
    menu_desplegable.add_command(label="Trapecio Simpson", command=opcion_trapecio_simpson)


    # Función para mostrar o esconder el menú principal en una ubicación específica
    def mostrar_menu(event):
        global menu_bloqueado
        ocultar_labels()
        ocultar_labels_grado()
        boton_menu.update_idletasks()
        x = boton_menu.winfo_rootx()
        y = boton_menu.winfo_rooty() + boton_menu.winfo_height()
        menu_desplegable.tk_popup(x, y)

    # Crear un botón para desplegar el menú principal
    boton_menu = ctk.CTkButton(marco_ingreso_valores, text="Opciones de Integración")
    boton_menu.place(x=50, y=50)
    boton_menu.bind("<Button-1>", mostrar_menu)

    # Labels para las opciones del menú principal (inicialmente ocultos)
    label_opcion1 = ctk.CTkLabel(marco_ingreso_valores, text="[Trapecio Simple]", font=("Arial", 12))
    label_opcion2 = ctk.CTkLabel(marco_ingreso_valores, text="[Trapecio Compuesto]", font=("Arial", 12))
    label_opcion3 = ctk.CTkLabel(marco_ingreso_valores, text="[Simpson 1/3]", font=("Arial", 12))
    label_opcion4 = ctk.CTkLabel(marco_ingreso_valores, text="[Simpson 3/8]", font=("Arial", 12))
    label_opcion5 = ctk.CTkLabel(marco_ingreso_valores, text="[Trapecio Simpson]", font=("Arial", 12))

    #GRADO DE INTEGRACION ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    

    # Funciones para los comandos del menú de grado
    def grado1():
        ocultar_labels_grado()
        grado1.place(x=50, y=140)
        print("Grado Integración: 1")

    def grado2():
        ocultar_labels_grado()
        grado2.place(x=50, y=140)
        print("Grado Integración: 2")

    def grado3():
        ocultar_labels_grado()
        grado3.place(x=50, y=140)
        print("Grado Integración: 3")

    # Crear el menú desplegable de grado
    menu_grado = Menu(ventana, tearoff=0)
    menu_grado.add_command(label="Grado Integración: 1", command=grado1)
    menu_grado.add_command(label="Grado Integración: 2", command=grado2)
    menu_grado.add_command(label="Grado Integración: 3", command=grado3)

    # Función para mostrar o esconder el menú de grado en una ubicación específica
    def mostrar_menu_grado(event):
        global menu_bloqueado
        ocultar_labels_grado()
        if not menu_bloqueado:
            boton_menu_grado.update_idletasks()
            x = boton_menu_grado.winfo_rootx()
            y = boton_menu_grado.winfo_rooty() + boton_menu_grado.winfo_height()
            menu_grado.tk_popup(x, y)

    # Crear un botón para desplegar el menú de grado
    boton_menu_grado = ctk.CTkButton(marco_ingreso_valores, text="Grado de Integración")
    boton_menu_grado.place(x=50, y=110)
    boton_menu_grado.bind("<Button-1>", mostrar_menu_grado)

    # Labels para las opciones del menú de grado (inicialmente ocultos)
    grado1 = ctk.CTkLabel(marco_ingreso_valores, text="[Grado de Integración: 1]", font=("Arial", 12))
    grado2 = ctk.CTkLabel(marco_ingreso_valores, text="[Grado de Integración: 2]", font=("Arial", 12))
    grado3 = ctk.CTkLabel(marco_ingreso_valores, text="[Grado de Integración: 3]", font=("Arial", 12))

    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


        #label funcion
    _func = "Ingrese una funcion"    
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = _func,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=410,y=80)
        #entry funcion
    e_ingrese_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_funcion.place(x=400,y=110)

    #pares de A-B segun opcion grado integral
    
    #label A-B grado1
    _B1 = "B1"
    label_ingrese_B1 = ctk.CTkLabel(marco_ingreso_valores,text = _B1,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_B1.place(x=370,y=40)
        #entry Cs
    e_ingrese_B1 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_B1.place(x=360,y=70)

    _A1 = "A1"
    label_ingrese_A1 = ctk.CTkLabel(marco_ingreso_valores,text = _A1,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_A1.place(x=370,y=180)
        #entry Cs
    e_ingrese_A1 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_A1.place(x=360,y=150)

    #label A-B grado2
    _B2 = "B2"
    label_ingrese_B2 = ctk.CTkLabel(marco_ingreso_valores,text = _B2,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_B2.place(x=330,y=40)
        #entry Cs
    e_ingrese_B2 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_B2.place(x=320,y=70)

    _A2 = "A2"
    label_ingrese_A2 = ctk.CTkLabel(marco_ingreso_valores,text = _A2,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_A2.place(x=330,y=180)
        #entry Cs
    e_ingrese_A2 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_A2.place(x=320,y=150)

    #label A-B grado3
    _B3 = "B3"
    label_ingrese_B3 = ctk.CTkLabel(marco_ingreso_valores,text = _B3,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_B3.place(x=290,y=40)
        #entry Cs
    e_ingrese_B3 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_B3.place(x=280,y=70)

    _A1 = "A3"
    label_ingrese_A1 = ctk.CTkLabel(marco_ingreso_valores,text = _A1,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_A1.place(x=290,y=180)
        #entry Cs
    e_ingrese_A1 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_A1.place(x=280,y=150)

"""

"""#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

#--------------------- Variables globales---------------------------------------------------------------------
# Inicializacion de Labels y Entrys
# Inicialización de variables
label_ingrese_A1 = None
label_ingrese_A2 = None
label_ingrese_A3 = None
label_ingrese_B1 = None
label_ingrese_B2 = None
label_ingrese_B3 = None

e_ingrese_A1 = None
e_ingrese_A2 = None
e_ingrese_A3 = None
e_ingrese_B1 = None
e_ingrese_B2 = None
e_ingrese_B3 = None
 

def Ventana_Metodo_Integracion(frame,ventana2,ventana):

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
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores, text="Metodo de Integracion", font=("Arial Black", 16))
        #posicion
    label_ingrese_funcion.place(x=50,y=20)
    #MENU TIPO DE INTEGRACION::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    # Variables de control
    menu_bloqueado = False  # Inicialmente el menú no está bloqueado
    grado_seleccionado = None  # Variable para almacenar el grado de integración seleccionado

    

    def ocultar_labels():
        for label in [label_opcion1, label_opcion2, label_opcion3, label_opcion4, label_opcion5]:
            label.place_forget()

    def ocultar_labels_grado():
        for label in [grado1, grado2, grado3]:
            label.place_forget()

    # Función para ocultar todos los labels y entries
    def ocultar_labels_y_entries():
        for label, entry in [
            (label_ingrese_A1, e_ingrese_A1),
            (label_ingrese_A2, e_ingrese_A2),
            (label_ingrese_A3, e_ingrese_A3),
            (label_ingrese_B1, e_ingrese_B1),
            (label_ingrese_B2, e_ingrese_B2),
            (label_ingrese_B3, e_ingrese_B3),
        ]:
            label.place_forget()
            entry.place_forget()

    def ocultar_variables():
        for label in [
            (label_ingrese_dx),
            (label_ingrese_dy),
            (label_ingrese_dz),
        ]:
            label.place_forget()

    def ocultar_variables2():
        for label in [
            (label_ingrese_dx2),
            (label_ingrese_dy2),
            (label_ingrese_dz2),
        ]:
            label.place_forget()

    def ocultar_variables3():
        for label in [
            (label_ingrese_dx3),
            (label_ingrese_dy3),
            (label_ingrese_dz3),
        ]:
            label.place_forget()        
            

    # Funciones para los comandos del menú principal
    def opcion_trapecio_simple():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels_y_entries()
        ocultar_labels()
        mostrar_labels_entries_grado1()
        label_opcion1.place(x=50, y=80)
        grado1.place(x=50, y=140)  # Mostrar label de Grado 1
        menu_bloqueado = True  # Bloquear menú de grado
        grado_seleccionado = grado1  # Almacenar grado seleccionado
        boton_menu_grado.config(state=tk.DISABLED)  # Deshabilitar botón de grado
        
        

    def opcion_trapecio_compuesto():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels_y_entries()
        ocultar_labels_grado()
        ocultar_labels()
        mostrar_labels_entries_grado1()
        label_opcion2.place(x=50, y=80)
        grado1.place(x=50, y=140)
        menu_bloqueado = False  # Desbloquear menú de grado
        boton_menu_grado.config(state=tk.NORMAL)  # Habilitar botón de grado

    def opcion_simpson_13():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels_y_entries()
        ocultar_labels_grado()
        ocultar_labels()
        mostrar_labels_entries_grado1()
        label_opcion3.place(x=50, y=80)
        mostrar_labels_entries_grado1()
        grado1.place(x=50, y=140)
        menu_bloqueado = False  # Desbloquear menú de grado
        boton_menu_grado.config(state=tk.NORMAL)  # Habilitar botón de grado

    def opcion_simpson_38():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels_y_entries()
        ocultar_labels_grado()
        ocultar_labels()
        mostrar_labels_entries_grado1()
        label_opcion4.place(x=50, y=80)
        mostrar_labels_entries_grado1()
        grado1.place(x=50, y=140)
        menu_bloqueado = False  # Desbloquear menú de grado
        boton_menu_grado.config(state=tk.NORMAL)  # Habilitar botón de grado

    def opcion_trapecio_simpson():
        global menu_bloqueado, grado_seleccionado
        ocultar_labels_y_entries()
        ocultar_labels_grado()
        ocultar_labels()
        mostrar_labels_entries_grado1()
        label_opcion5.place(x=50, y=80)
        grado1.place(x=50, y=140)
        menu_bloqueado = False  # Desbloquear menú de grado
        boton_menu_grado.config(state=tk.NORMAL)  # Habilitar botón de grado

    # Crear el menú desplegable principal
    menu_desplegable = Menu(ventana, tearoff=0)
    menu_desplegable.add_command(label="Trapecio Simple", command=opcion_trapecio_simple)
    menu_desplegable.add_command(label="Trapecio Compuesto", command=opcion_trapecio_compuesto)
    menu_desplegable.add_command(label="Simpson 1/3", command=opcion_simpson_13)
    menu_desplegable.add_command(label="Simpson 3/8", command=opcion_simpson_38)
    menu_desplegable.add_command(label="Trapecio Simpson", command=opcion_trapecio_simpson)

    # Función para mostrar o esconder el menú principal en una ubicación específica
    def mostrar_menu(event):
        global menu_bloqueado
        #ocultar_labels_y_entries()
        ocultar_labels_grado()
        #mostrar_labels_entries_grado1()
        boton_menu.update_idletasks()
        x = boton_menu.winfo_rootx()
        y = boton_menu.winfo_rooty() + boton_menu.winfo_height()
        menu_desplegable.tk_popup(x, y)
        

    # Crear un botón para desplegar el menú principal
    boton_menu = ctk.CTkButton(marco_ingreso_valores, text="Opciones de Integración")
    boton_menu.place(x=50, y=50)
    boton_menu.bind("<Button-1>", mostrar_menu)

    # Labels para las opciones del menú principal (inicialmente ocultos)
    label_opcion1 = ctk.CTkLabel(marco_ingreso_valores, text="[Trapecio Simple]", font=("Arial", 12))
    label_opcion2 = ctk.CTkLabel(marco_ingreso_valores, text="[Trapecio Compuesto]", font=("Arial", 12))
    label_opcion3 = ctk.CTkLabel(marco_ingreso_valores, text="[Simpson 1/3]", font=("Arial", 12))
    label_opcion4 = ctk.CTkLabel(marco_ingreso_valores, text="[Simpson 3/8]", font=("Arial", 12))
    label_opcion5 = ctk.CTkLabel(marco_ingreso_valores, text="[Trapecio Simpson]", font=("Arial", 12))

    # Funciones para los comandos del menú de grado
    def grado1():
        ocultar_labels_grado()
        ocultar_labels_y_entries()
        grado1.place(x=50, y=140)
        mostrar_labels_entries_grado1()
        print("Grado Integración: 1")

        mostrar_v1()

    def grado2():
        ocultar_labels_grado()
        ocultar_labels_y_entries()
        grado2.place(x=50, y=140)
        mostrar_labels_entries_grado2()
        print("Grado Integración: 2")

        mostrar_v2()

    def grado3():
        ocultar_labels_grado()
        ocultar_labels_y_entries()
        grado3.place(x=50, y=140)
        mostrar_labels_entries_grado3()
        print("Grado Integración: 3")

        mostrar_v3()

    # Crear el menú desplegable de grado
    menu_grado = Menu(ventana, tearoff=0)
    menu_grado.add_command(label="Grado Integración: 1", command=grado1)
    menu_grado.add_command(label="Grado Integración: 2", command=grado2)
    menu_grado.add_command(label="Grado Integración: 3", command=grado3)

    # Función para mostrar o esconder el menú de grado en una ubicación específica
    def mostrar_menu_grado(event):
        global menu_bloqueado
        if not menu_bloqueado:
            boton_menu_grado.update_idletasks()
            x = boton_menu_grado.winfo_rootx()
            y = boton_menu_grado.winfo_rooty() + boton_menu_grado.winfo_height()
            menu_grado.tk_popup(x, y)

    # Crear un botón para desplegar el menú de grado
    boton_menu_grado = ctk.CTkButton(marco_ingreso_valores, text="Grado de Integración")
    boton_menu_grado.place(x=50, y=110)
    boton_menu_grado.bind("<Button-1>", mostrar_menu_grado)

    # Labels para las opciones del menú de grado (inicialmente ocultos)
    grado1 = ctk.CTkLabel(marco_ingreso_valores, text="[Grado de Integración: 1]", font=("Arial", 12))
    grado2 = ctk.CTkLabel(marco_ingreso_valores, text="[Grado de Integración: 2]", font=("Arial", 12))
    grado3 = ctk.CTkLabel(marco_ingreso_valores, text="[Grado de Integración: 3]", font=("Arial", 12))

    
    # Funciones para mostrar los labels y entries correspondientes al grado seleccionado
    def mostrar_labels_entries_grado1():
        
        label_ingrese_B1.place(x=370, y=40)
        e_ingrese_B1.place(x=360, y=70)
        label_ingrese_A1.place(x=370, y=180)
        e_ingrese_A1.place(x=360, y=150)

        mostrar_v1()

    def mostrar_labels_entries_grado2():
        
        label_ingrese_B2.place(x=330, y=40)
        e_ingrese_B2.place(x=320, y=70)
        label_ingrese_A2.place(x=330, y=180)
        e_ingrese_A2.place(x=320, y=150)
        
        label_ingrese_B1.place(x=370, y=40)
        e_ingrese_B1.place(x=360, y=70)
        label_ingrese_A1.place(x=370, y=180)
        e_ingrese_A1.place(x=360, y=150)

        mostrar_v1()
        mostrar_v2()
        

    def mostrar_labels_entries_grado3():
        
        label_ingrese_B3.place(x=290, y=40)
        e_ingrese_B3.place(x=280, y=70)
        label_ingrese_A3.place(x=290, y=180)
        e_ingrese_A3.place(x=280, y=150)

        label_ingrese_B2.place(x=330, y=40)
        e_ingrese_B2.place(x=320, y=70)
        label_ingrese_A2.place(x=330, y=180)
        e_ingrese_A2.place(x=320, y=150)

        label_ingrese_B1.place(x=370, y=40)
        e_ingrese_B1.place(x=360, y=70)
        label_ingrese_A1.place(x=370, y=180)
        e_ingrese_A1.place(x=360, y=150)

        mostrar_v1()
        mostrar_v2()
        mostrar_v3()
        
        
        #label funcion
    _func = "Ingrese una funcion"    
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = _func,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=410,y=80)
        #entry funcion
    e_ingrese_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_funcion.place(x=400,y=110)

        
    #label A-B grado1
    _B1 = "B1"
    label_ingrese_B1 = ctk.CTkLabel(marco_ingreso_valores,text = _B1,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_B1.place(x=370,y=40)
        #entry Cs
    e_ingrese_B1 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_B1.place(x=360,y=70)

    _A1 = "A1"
    label_ingrese_A1 = ctk.CTkLabel(marco_ingreso_valores,text = _A1,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_A1.place(x=370,y=180)
        #entry Cs
    e_ingrese_A1 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_A1.place(x=360,y=150)

    #label A-B grado2
    _B2 = "B2"
    label_ingrese_B2 = ctk.CTkLabel(marco_ingreso_valores,text = _B2,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_B2.place(x=330,y=40)
        #entry Cs
    e_ingrese_B2 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_B2.place(x=320,y=70)

    label_ingrese_B2.place_forget()
    e_ingrese_B2.place_forget()

    _A2 = "A2"
    label_ingrese_A2 = ctk.CTkLabel(marco_ingreso_valores,text = _A2,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_A2.place(x=330,y=180)
        #entry Cs
    e_ingrese_A2 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_A2.place(x=320,y=150)

    label_ingrese_A2.place_forget()
    e_ingrese_A2.place_forget()

    #label A-B grado3
    _B3 = "B3"
    label_ingrese_B3 = ctk.CTkLabel(marco_ingreso_valores,text = _B3,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_B3.place(x=290,y=40)
        #entry Cs
    e_ingrese_B3 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_B3.place(x=280,y=70)

    label_ingrese_B3.place_forget()
    e_ingrese_B3.place_forget()

    _A3 = "A3"
    label_ingrese_A3 = ctk.CTkLabel(marco_ingreso_valores,text = _A3,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_A3.place(x=290,y=180)
        #entry Cs
    e_ingrese_A3 = ctk.CTkEntry(marco_ingreso_valores,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_A3.place(x=280,y=150)

    label_ingrese_A3.place_forget()
    e_ingrese_A3.place_forget()


    """:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
    def opcion_dx():
        ocultar_variables()
        label_ingrese_dx.place(x=635,y=110)
        if menu_grado == grado2:
            label_ingrese_dy2.place(x=735,y=110)
        #menu_desplegable_variable_2.add_command(label="dx", command=opcion_dx_2)
            

    def opcion_dy():
        ocultar_variables()
        label_ingrese_dy.place(x=635,y=110)
        if menu_grado == grado2:    
            label_ingrese_dx2.place(x=735,y=110)

    def opcion_dz():
        ocultar_variables()
        label_ingrese_dz.place(x=635,y=110)
        if boton_menu_grado == grado2:
            grado1()

    # Crear el menú desplegable principal
    menu_desplegable_variable = Menu(ventana, tearoff=0)
    menu_desplegable_variable.add_command(label="dx", command=opcion_dx)
    menu_desplegable_variable.add_command(label="dy", command=opcion_dy)
    menu_desplegable_variable.add_command(label="dz", command=opcion_dz)
    
    def mostrar_menu_variable(event):
        global menu_bloqueado
        #ocultar_labels_y_entries()
        #ocultar_labels_grado()
        #mostrar_labels_entries_grado1()
        boton_menu_v.update_idletasks()
        x = boton_menu_v.winfo_rootx()
        y = boton_menu_v.winfo_rooty() + boton_menu_v.winfo_height()
        menu_desplegable_variable.tk_popup(x, y)


    # Labels para las opciones del menú principal (inicialmente ocultos)
    opcion_dx = ctk.CTkLabel(marco_ingreso_valores, text="dx", font=("Arial", 14))
    opcion_dy = ctk.CTkLabel(marco_ingreso_valores, text="dy", font=("Arial", 14))
    opcion_dz = ctk.CTkLabel(marco_ingreso_valores, text="dz", font=("Arial", 14))
    

    def mostrar_v1():
        ocultar_variables()
        ocultar_variables2()
        ocultar_variables3()
        boton_menu_v.place_forget()
        boton_menu_v2.place_forget()
        boton_menu_v3.place_forget()

        boton_menu_v.place(x=600, y=65)
        label_ingrese_dx.place(x=635,y=110)

    def mostrar_v2():
        ocultar_variables()
        ocultar_variables2()
        ocultar_variables3()
        boton_menu_v.place_forget()
        boton_menu_v2.place_forget()
        boton_menu_v3.place_forget()
        
        boton_menu_v.place(x=600, y=65)
        boton_menu_v2.place(x=700, y=65)
        label_ingrese_dx.place(x=635,y=110)
        label_ingrese_dy2.place(x=735,y=110)
        
        
    def mostrar_v3():
        ocultar_variables()
        ocultar_variables2()
        ocultar_variables3()
        boton_menu_v.place_forget()
        boton_menu_v2.place_forget()
        boton_menu_v3.place_forget()
        
        boton_menu_v.place(x=600, y=65)
        boton_menu_v2.place(x=700, y=65)
        boton_menu_v3.place(x=800, y=65)
        label_ingrese_dx.place(x=635,y=110)
        label_ingrese_dy2.place(x=735,y=110)
        label_ingrese_dz3.place(x=835,y=110)

    #label opcion variable:
    _dx = "dx"
    label_ingrese_dx = ctk.CTkLabel(marco_ingreso_valores,text = _dx,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dx.place(x=635,y=110)
        
    _dy = "dy"
    label_ingrese_dy = ctk.CTkLabel(marco_ingreso_valores,text = _dy,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dy.place(x=635,y=110)
    label_ingrese_dy.place_forget()

    _dz = "dz"
    label_ingrese_dz = ctk.CTkLabel(marco_ingreso_valores,text = _dz,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dz.place(x=635,y=110)
    label_ingrese_dz.place_forget()
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def opcion_dx_2():
        ocultar_variables()
        ocultar_variables2()
        label_ingrese_dx2.place(x=735,y=110)
        label_ingrese_dy.place(x=635,y=110)
        

    def opcion_dy_2():
        ocultar_variables()
        ocultar_variables2()
        label_ingrese_dy2.place(x=735,y=110)
        label_ingrese_dx.place(x=635,y=110)
    

    def opcion_dz_2():
        ocultar_variables()
        ocultar_variables2()
        label_ingrese_dz2.place(x=735,y=110)

    def opcion_dx_3():
        ocultar_variables()
        ocultar_variables3()
        label_ingrese_dx2.place(x=835,y=110)

    def opcion_dy_3():
        ocultar_variables()
        ocultar_variables2()
        ocultar_variables3()
        label_ingrese_dy2.place(x=835,y=110)

    def opcion_dz_3():
        ocultar_variables()
        ocultar_variables2()
        ocultar_variables3()
        label_ingrese_dz2.place(x=835,y=110)    

    # Crear el menú desplegable principal
    menu_desplegable_variable_2 = Menu(ventana, tearoff=0)
    menu_desplegable_variable_2.add_command(label="dx", command=opcion_dx_2)
    menu_desplegable_variable_2.add_command(label="dy", command=opcion_dy_2)
    menu_desplegable_variable_2.add_command(label="dz", command=opcion_dz_2)
    menu_desplegable_variable_2.place_forget()

    menu_desplegable_variable_3 = Menu(ventana, tearoff=0)
    menu_desplegable_variable_3.add_command(label="dx", command=opcion_dx_3)
    menu_desplegable_variable_3.add_command(label="dy", command=opcion_dy_3)
    menu_desplegable_variable_3.add_command(label="dz", command=opcion_dz_3)
    menu_desplegable_variable_3.place_forget()

############################################################################################################
    def integral1_cambiado(valor):
        derivadas_array = list(derivada_respecto)
        derivadas_array.remove(valor)
        print(derivadas_array)
        menu_variable2.set(derivadas_array[0])
        menu_variable3.set(derivadas_array[1])

    def integral2_cambiado(valor):
        derivadas_array = list(derivada_respecto)
        print('holaa', valor)
        print('holaa2', derivada_respecto)
        derivadas_array.remove(valor)
        print(derivadas_array)
        menu_variable1.set(derivadas_array[0])
        menu_variable3.set(derivadas_array[1])

    def integral3_cambiado(valor):
        derivadas_array = list(derivada_respecto)
        derivadas_array.remove(valor)
        print(derivadas_array)
        menu_variable1.set(derivadas_array[0])
        menu_variable2.set(derivadas_array[1])

    # Lista de opciones
    derivada_respecto = ("dx", "dy", "dz")
    width_menu = 100

    # Menu 1
    menu_variable1 = StringVar(marco_ingreso_valores)
    menu_variable1.set("dx")
    boton_menu_v1 = ctk.CTkOptionMenu(marco_ingreso_valores, variable=menu_variable1, values=derivada_respecto, command=lambda valor: integral1_cambiado(valor))
    boton_menu_v1.configure(width=width_menu)
    boton_menu_v1.place(x=700, y=60)

    # Menu 2
    menu_variable2 = StringVar(marco_ingreso_valores)
    menu_variable2.set("dy")
    boton_menu_v2 = ctk.CTkOptionMenu(marco_ingreso_valores, variable=menu_variable2, values=derivada_respecto, command=lambda valor: integral2_cambiado(valor))
    boton_menu_v2.configure(width=width_menu)
    boton_menu_v2.place(x=700, y=120)

    # Menu 3
    menu_variable3 = StringVar(marco_ingreso_valores)
    menu_variable3.set("dz")
    boton_menu_v3 = ctk.CTkOptionMenu(marco_ingreso_valores, variable=menu_variable3, values=derivada_respecto, command=lambda valor: integral3_cambiado(valor))
    boton_menu_v3.configure(width=width_menu)
    boton_menu_v3.place(x=700, y=180)

####################################################################################################################################################################

    

    def mostrar_menu_variable2(event):
        global menu_bloqueado
        #ocultar_labels_y_entries()
        #ocultar_labels_grado()
        #mostrar_labels_entries_grado1()
        boton_menu_v2.update_idletasks()
        x = boton_menu_v2.winfo_rootx()
        y = boton_menu_v2.winfo_rooty() + boton_menu_v2.winfo_height()
        menu_desplegable_variable_2.tk_popup(x, y)

    def mostrar_menu_variable3(event):
        global menu_bloqueado
        #ocultar_labels_y_entries()
        #ocultar_labels_grado()
        #mostrar_labels_entries_grado1()
        boton_menu_v3.update_idletasks()
        x = boton_menu_v3.winfo_rootx()
        y = boton_menu_v3.winfo_rooty() + boton_menu_v3.winfo_height()
        menu_desplegable_variable_3.tk_popup(x, y)    

# Crear un botón para desplegar el menú para seleccion de integral
    boton_menu_v2 = ctk.CTkButton(marco_ingreso_valores, text="2° Integral", width=80)
    boton_menu_v2.place(x=700, y=65)
    boton_menu_v2.place_forget()

    boton_menu_v3 = ctk.CTkButton(marco_ingreso_valores, text="3° Integral", width=80)
    boton_menu_v3.place(x=800, y=65)
    boton_menu_v3.place_forget()

    boton_menu_v2.bind("<Button-1>", mostrar_menu_variable2)

    boton_menu_v3.bind("<Button-1>", mostrar_menu_variable3)

    # Labels para las opciones del menú principal (inicialmente ocultos)
    opcion_dx_2 = ctk.CTkLabel(marco_ingreso_valores, text="dx", font=("Arial", 14))
    opcion_dy_2 = ctk.CTkLabel(marco_ingreso_valores, text="dy", font=("Arial", 14))
    opcion_dz_2 = ctk.CTkLabel(marco_ingreso_valores, text="dz", font=("Arial", 14))

    opcion_dx_3 = ctk.CTkLabel(marco_ingreso_valores, text="dx", font=("Arial", 14))
    opcion_dy_3 = ctk.CTkLabel(marco_ingreso_valores, text="dy", font=("Arial", 14))
    opcion_dz_3 = ctk.CTkLabel(marco_ingreso_valores, text="dz", font=("Arial", 14))
    
    #label opcion variable: 2
    _dx = "dx"
    label_ingrese_dx2 = ctk.CTkLabel(marco_ingreso_valores,text = _dx,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dx2.place(x=735,y=110)
    label_ingrese_dx2.place_forget()
        
    _dy = "dy"
    label_ingrese_dy2 = ctk.CTkLabel(marco_ingreso_valores,text = _dy,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dy2.place(x=735,y=110)
    label_ingrese_dy2.place_forget()

    _dz = "dz"
    label_ingrese_dz2 = ctk.CTkLabel(marco_ingreso_valores,text = _dz,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dz2.place(x=735,y=110)
    label_ingrese_dz2.place_forget()

    #label opcion variable: 3
    _dx = "dx"
    label_ingrese_dx3 = ctk.CTkLabel(marco_ingreso_valores,text = _dx,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dx3.place(x=835,y=110)
    label_ingrese_dx3.place_forget()
        
    _dy = "dy"
    label_ingrese_dy3 = ctk.CTkLabel(marco_ingreso_valores,text = _dy,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dy3.place(x=835,y=110)
    label_ingrese_dy3.place_forget()

    _dz = "dz"
    label_ingrese_dz3 = ctk.CTkLabel(marco_ingreso_valores,text = _dz,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_dz3.place(x=835,y=110)
    label_ingrese_dz3.place_forget()

"""
    #::validaciones::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #habilitacion de botones globales
    global boton_limpiar,boton_resolver,mostrar


    def Validacion():
        

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

                #Validar igualdad
            expresion, Error = funciones_herramientas.validar_igualdad(expresion)
            verificador_error(Error)


            #validar implicita
            expresion_valid, Error = funciones_herramientas.validar_multiplicacion_implicita(expresion)
            verificador_error(Error)

    
            muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

            #Ecuaciones_Cuadraticas(funcion, destinos) 
#            Metodo_Muller(expresion_valid, x0, x1, x2, cs) 
        
            #impresion de datos
#            muestra_valores.configure(text = generales_Muller.get_transportador(1), anchor='w', justify='left')

            #impresion del grafico
#            fig = Grafico(generales_Muller.get_transportador(0), raices_reales_Muller.get_transportador())
#            canvas = FigureCanvasTkAgg(fig, master = muestra_grafica)

#            canvas.draw()
#            widget_grafico = canvas.get_tk_widget()
#            widget_grafico.pack(fill="both", expand=True)
            
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

# Función para ocultar todos los labels y entries+
"""