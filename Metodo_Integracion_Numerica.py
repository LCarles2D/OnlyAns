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
        return
    else:
        pass

metodo_funcion_tabla = funciones_herramientas.Transportador()
grado_integracion_1 = funciones_herramientas.Transportador()
grado_integracion_2 = funciones_herramientas.Transportador()
opcion_modo_5 = funciones_herramientas.Transportador()
nivel_grado = funciones_herramientas.Transportador()
cant_intervalos = funciones_herramientas.Transportador()

Mensaje = ""
    
#####################################################################
#                 TRAPECIO SIMPLE: fUNCION/TABLA                    #
#####################################################################
def Metodo_Trapecio_Simple(expresion=None, A=None, B=None, list_a=None, list_b=None):
    if expresion is not None and list_a is None and list_b is None:
        # Modo función: requiere función, A y B
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
            Error = f"Error al evaluar la función, Método Trapecio Simple: {e}"
            print(f"Error al evaluar la función: {e}")
            verificador_error(Error)
            
    elif expresion is None and A is None and B is None and list_a is not None and list_b is not None:
        # Modo tabla: requiere lista x y lista y
        if len(list_a) != 2 or len(list_b) != 2:
            verificador_error("Las listas deben contener exactamente dos elementos.")
            return

        try:
            A = list_a[0]
            B = list_a[1]
            funcion_A = list_b[0]
            funcion_B = list_b[1]

            integral_approx = (B - A) * (funcion_A + funcion_B) / 2
            print("sumatoria: ",integral_approx)
            print(f"[TS: modo tabla] La integral aproximada es: {integral_approx}") 

        except Exception as e:
            Error = f"Error: Método Trapecio Simple {e}"
            print(f"Error: Método Trapecio Simple {e}")
            verificador_error(Error)

 
######################################################################
#                 TRAPECIO COMPUESTO: fUNCION/TABLA                  #
######################################################################
def Metodo_Trapecio_Compuesto(grado_integral: int, n: int, expresion: str = None, A: Union[int, float] = None, B: Union[int, float] = None, list_a: list = None, list_b: list = None):
    
    Error = ""

    if grado_integral == 1:
            

        if expresion is not None and n is not None and A is not None and B is not None and list_a is None and list_b is None:
            # Modo función: requiere función, A, B y n
            x = sp.symbols('x')

            try:
                funcion, lista_variables, Error = funciones_herramientas.validar_funcion_xyz(expresion)
                if Error:
                    print(Error)
                    return

                if n < 2:
                    Error = "El número de intervalos debe ser mayor o igual que 2"
                    verificador_error(Error)

                # Convertir A, B y n a números flotantes e enteros respectivamente
                h = (B - A) / n
                print("h:",h)

                # Lista para almacenar los puntos desde A hasta B con paso h
                valores_x = [A + i * h for i in range(n + 1)]

                # Lista para almacenar los valores de la función evaluada en esos puntos
                valores_funcion = [funcion.subs(x, valor) for valor in valores_x]

                print("Puntos de evaluación x:")
                print(valores_x)
                print("Valores de la función evaluada en esos puntos:")
                print(valores_funcion)

                # Suma desde la segunda posición hasta la penúltima posición
                suma_interior = sum(valores_funcion[1:-1])

                # Fórmula del trapecio compuesto
                integral_aprox = (h * (valores_funcion[0] + 2 * suma_interior + valores_funcion[-1])) / 2
                integral_aprox = float(integral_aprox)
                print("sumatoria: ",integral_aprox)

                print(f"[TC: modo función] La integral aproximada es: {integral_aprox}")

            except Exception as e:
                Error = f"Error: Método Trapecio Compuesto {e}"
                print(f"Error: Método Trapecio Compuesto {e}")

            

        elif list_a is not None and list_b is not None and n is not None and expresion is None and A is None and B is None:
            # Modo tabla: requiere lista_x, lista_y, y n

            if n < 2:
                Error = "El número de intervalos debe ser mayor o igual que 2"
                verificador_error(Error)

            try:
                lista_x = list_a
                valores_funcion = list_b

                h = (lista_x[-1] - lista_x[0]) / n

                # Suma desde la segunda posición hasta la penúltima posición
                suma_interior = sum(valores_funcion[1:-1])

                print("Puntos de evaluación x:")
                print(lista_x)
                print("Valores de la función evaluada en esos puntos:")
                print(valores_funcion)

                # Fórmula del trapecio compuesto
                integral_aprox = (h * (valores_funcion[0] + 2 * suma_interior + valores_funcion[-1])) / 2
                integral_aprox = float(integral_aprox)

                print(f"[TC: modo tabla] La integral aproximada es: {integral_aprox}")

            except Exception as e:
                Error = f"Error: Método Trapecio Compuesto {e}"
                print(f"Error: Método Trapecio Compuesto {e}")

    elif grado_integral >= 2:

        if expresion is not None and n is not None and A is not None and B is not None and list_a is None and list_b is None:
            # Modo función: requiere función, A, B y n
            x = sp.symbols('x')

            try:
                funcion, Error = funciones_herramientas.validar_funcion_x(expresion)
                if Error:
                    print(Error)
                    return

                if n < 2:
                    Error = "El número de intervalos debe ser mayor o igual que 2"
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
                suma_interior = sum(valores_funcion[1:-1])

                # Fórmula del trapecio compuesto
                integral_aprox = (h * (valores_funcion[0] + 2 * suma_interior + valores_funcion[-1])) / 2
                integral_aprox = float(integral_aprox)

                print(f"[TC: modo función] La integral aproximada es: {integral_aprox}")

            except Exception as e:
                Error = f"Error: Método Trapecio Compuesto {e}"
                print(f"Error: Método Trapecio Compuesto {e}")
######################################################################
#                     SIMPSON 1/3: fUNCION/TABLA                     #
######################################################################
def Metodo_Simpson_13(grado_integral: int, n: int, expresion: str = None, A: Union[int, float] = None, B: Union[int, float] = None, list_a: list = None, list_b: list = None):

    Error = ""

    if grado_integral == 1:
        
        if expresion is not None and n is not None and A is not None and B is not None and list_a is None and list_b is None:
            # Modo función: requiere función, A, B y n
            x = sp.symbols('x')

            try:
                funcion, Error = validar_funcion_x(expresion)
                if Error:
                    print(Error)
                    return

                if n < 2 or n % 2 != 0:
                    Error = "El número de intervalos debe ser un número par mayor o igual que 2."
                    verificador_error(Error)
                    return

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

                # Sumas para los términos pares e impares
                suma_pares = sum(valores_funcion[2:-2:2])
                suma_impares = sum(valores_funcion[1:-1:2])

                # Fórmula de Simpson 1/3 compuesto
                integral_aprox = (h / 3) * (valores_funcion[0] + 4 * suma_impares + 2 * suma_pares + valores_funcion[-1])
                integral_aprox = float(integral_aprox)

                print(f"[Simpson 1/3: modo función] La integral aproximada es: {integral_aprox}")

            except Exception as e:
                Error = f"Error: Método Simpson 1/3 Compuesto {e}"
                print(f"Error: Método Simpson 1/3 Compuesto {e}")

        elif list_a is not None and list_b is not None and n is not None and expresion is None and A is None and B is None:
            # Modo tabla: requiere lista_x, lista_y, y n

            if n < 2 or n % 2 != 0:
                Error = "El número de intervalos debe ser un número par mayor o igual que 2."
                verificador_error(Error)
                return

            try:
                lista_x = list_a
                valores_funcion = list_b

                h = (lista_x[-1] - lista_x[0]) / n

                # Sumas para los términos pares e impares
                suma_pares = sum(valores_funcion[2:-2:2])
                suma_impares = sum(valores_funcion[1:-1:2])

                print("Puntos de evaluación x:")
                print(lista_x)
                print("Valores de la función evaluada en esos puntos:")
                print(valores_funcion)

                # Fórmula de Simpson 1/3 compuesto
                integral_aprox = (h / 3) * (valores_funcion[0] + 4 * suma_impares + 2 * suma_pares + valores_funcion[-1])
                integral_aprox = float(integral_aprox)

                print(f"[Simpson 1/3: modo tabla] La integral aproximada es: {integral_aprox}")

            except Exception as e:
                Error = f"Error: Método Simpson 1/3 Compuesto {e}"
                print(f"Error: Método Simpson 1/3 Compuesto {e}")

######################################################################
#                     SIMPSON 3/8: fUNCION/TABLA                     #
######################################################################
def Metodo_Simpson_38(grado_integral: int, n: int, expresion: str = None, A: Union[int, float] = None, B: Union[int, float] = None, list_a: list = None, list_b: list = None):

    Error = ""

    if grado_integral == 1:
        
        if expresion is not None and n is not None and A is not None and B is not None and list_a is None and list_b is None:
            # Modo función: requiere función, A, B y n
            x = sp.symbols('x')

            try:
                funcion, Error = validar_funcion_x(expresion)
                if Error:
                    print(Error)
                    return

                if n < 3 or n % 3 != 0:
                    Error = "El número de subintervalos debe ser un múltiplo de 3 y mayor o igual que 3."
                    verificador_error(Error)
                    return

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

                # Sumas para los términos pares e impares
                suma_pares = sum(valores_funcion[2:-1:3])
                suma_impares = sum(valores_funcion[1:-1:3])
                suma_resto = sum(valores_funcion[3:-1:3])

                # Fórmula de Simpson 3/8 compuesto
                integral_aprox = (3 * h / 8) * (valores_funcion[0] + 3 * suma_impares + 3 * suma_pares + 2 * suma_resto + valores_funcion[-1])
                integral_aprox = float(integral_aprox)

                print(f"[Simpson 3/8: modo función] La integral aproximada es: {integral_aprox}")

            except Exception as e:
                Error = f"Error: Método Simpson 3/8 Compuesto {e}"
                print(f"Error: Método Simpson 3/8 Compuesto {e}")

        elif list_a is not None and list_b is not None and n is not None and expresion is None and A is None and B is None:
            # Modo tabla: requiere lista_x, lista_y, y n

            if n < 3 or n % 3 != 0:
                Error = "El número de subintervalos debe ser un múltiplo de 3 y mayor o igual que 3."
                verificador_error(Error)
                return

            try:
                lista_x = list_a
                valores_funcion = list_b

                h = (lista_x[-1] - lista_x[0]) / n

                # Sumas para los términos pares e impares
                suma_pares = sum(valores_funcion[2:-1:3])
                suma_impares = sum(valores_funcion[1:-1:3])
                suma_resto = sum(valores_funcion[3:-1:3])

                print("Puntos de evaluación x:")
                print(lista_x)
                print("Valores de la función evaluada en esos puntos:")
                print(valores_funcion)

                # Fórmula de Simpson 3/8 compuesto
                integral_aprox = (3 * h / 8) * (valores_funcion[0] + 3 * suma_impares + 3 * suma_pares + 2 * suma_resto + valores_funcion[-1])
                integral_aprox = float(integral_aprox)

                print(f"[Simpson 3/8: modo tabla] La integral aproximada es: {integral_aprox}")

            except Exception as e:
                Error = f"Error: Método Simpson 3/8 Compuesto {e}"
                print(f"Error: Método Simpson 3/8 Compuesto {e}")

######################################################################
 #                 TRAPECIO/SIMPSON: fUNCION/TABLA                   #
#####################################################################
def Metodo_Trapecio_Simpson(expresion=None, A=None, B=None, list_x=None, list_y=None):
    if expresion is not None and A is not None and B is not None and list_x is None and list_y is None:
        # Modo función
        x = sp.symbols('x')
        funcion, error = validar_funcion_x(expresion)
        if error:
            verificador_error(error)
            return
        
        # Determinar el método
        h = (B - A) / 2
        if h == (B - A):
            Metodo_Trapecio_Simple(expresion=expresion, A=A, B=B)
        elif (B - A) % 2 == 0:
            Metodo_Simpson_13(grado_integral=1, n=2, expresion=expresion, A=A, B=B)
        elif (B - A) % 3 == 0:
            Metodo_Simpson_38(grado_integral=1, n=3, expresion=expresion, A=A, B=B)
        else:
            verificador_error("No se encontró un método adecuado para los intervalos dados.")

    elif list_x is not None and list_y is not None and expresion is None and A is None and B is None:
        # Modo tabla
        n = len(list_x) - 1
        
        if n == 1:
            Metodo_Trapecio_Simple(list_a=list_x, list_b=list_y)
        elif n % 2 == 0:
            Metodo_Simpson_13(grado_integral=1, n=n, list_a=list_x, list_b=list_y)
        elif n % 3 == 0:
            Metodo_Simpson_38(grado_integral=1, n=n, list_a=list_x, list_b=list_y)
        else:
            verificador_error("No se encontró un método adecuado para los intervalos dados.")
    else:
        verificador_error("Parámetros insuficientes o incorrectos.")

"""
print("-----trapcio simple: funcion------")   
print("forma simple")
print("Primera forma:")
Metodo_Trapecio_Simple(expresion="x**2 - 2*x", A=3, B=5)
"""
print("-----trapcio simple: tablas------")   
print("\nSegunda forma:")
listx = [3, 5]
listy = [3, 15]
Metodo_Trapecio_Simple(list_a = listx, list_b = listy)    
    
print("\n")
print("-----trapcio compuesto: funcion------")   
print("trapecio compuesto")
print("primera forma")
Metodo_Trapecio_Compuesto(grado_integral=1, n=4, expresion="2*x**2 + 32", A=-1, B=1)   
"""
print("\n-----trapcio compuesto: tablas------")   
lista_x = [-1.0, -0.5, 0.0, 0.5, 1.0]
lista_y = [34, 32.5, 32, 32.5, 34]
print("segunda forma")
Metodo_Trapecio_Compuesto(grado_integral=1, n=4, list_a=lista_x, list_b=lista_y)

print("\n-----simpson 1/3:funcion------")   
Metodo_Simpson_13(grado_integral=1, n=4, expresion='x**2', A=0, B=2)

print("\n-----simpson 1/3:tabla------")   
lista_x = [0, 0.5, 1, 1.5, 2]
valores_funcion = [0, 0.25, 1, 2.25, 4]
Metodo_Simpson_13(grado_integral=1, n=4, list_a=lista_x, list_b=valores_funcion)

print("\n-----simpson 3/8:funcion------")   
Metodo_Simpson_38(grado_integral=1, n=6, expresion='x**2', A=0, B=2.5)

print("\n-----simpson 3/8:funcion------")   
lista_x = [0, 0.5, 1, 1.5, 2, 2.5]
valores_funcion = [0, 0.25, 1, 2.25, 4, 6.25]
Metodo_Simpson_38(grado_integral=1, n=6, list_a=lista_x, list_b=valores_funcion)
"""
   

#print(integrar_funcion_auto(expresion='x**2', A=0, B=1))  # Usará trapecio simple
#print(integrar_funcion_auto(list_x=[0, 0.5, 1], list_y=[0, 0.25, 1]))  # Usará trapecio compuesto
#print(integrar_funcion_auto(expresion='x**3', A=0, B=1))  # Usará Simpson 1/3 compuesto
#print(integrar_funcion_auto(list_x=[0, 0.2, 0.4, 0.6, 0.8, 1], list_y=[0, 0.008, 0.064, 0.216, 0.512, 1]))  # Usará Simpson 3/8 compuesto




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

    metodo = None
    opcion_metodo = None
    opcion_grado = None

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

    #habilitar y desabilitar marcos

    def deshabilitar_marco(marco):
        for widget in marco.winfo_children():
            try:
                widget.configure(state=ctk.DISABLED)
            except:
                pass 
        if marco == marco_modo_funcion:#habilitando marco tabla
            metodo_funcion_tabla.set_transportador(1)
            """label_habf.place_forget()
            label_habt.place_forget()
            label_habt.place(x=875, y=30)
            label_habf.place(x=625, y=30)"""
            habilitar_marco(marco_modo_tabla)
            boton_resolver_1.configure(state=ACTIVE)
            boton_resolver_2.configure(state=DISABLED)

            
            

        elif marco == marco_modo_tabla:#habilitando marco funcion
            metodo_funcion_tabla.set_transportador(0)
            """label_habt.place_forget()
            label_habf.place_forget()
            label_habf.place(x=625, y=30)
            label_habt.place(x=875, y=30)"""  
            habilitar_marco(marco_modo_funcion)  
            boton_resolver_1.configure(state=DISABLED)
            boton_resolver_2.configure(state=ACTIVE)
            


    def habilitar_marco(marco):
        for widget in marco.winfo_children():
            try:
                widget.configure(state=ctk.NORMAL)
            except:
                pass        
                

    #MARCO IZQUIERDA
    marco_meth_grad = ctk.CTkFrame(marco_ingreso_valores, width=260, height=250, corner_radius=10)
    marco_meth_grad.grid(row=0, column=0, padx=7.5, pady=20)  # Ajustar pady a 20 para espacio arriba
    
        #label titulo
    label_ingrese_funcion = ctk.CTkLabel(marco_meth_grad, text="Metodo de Integracion", font=("Arial Black", 16))
    label_ingrese_funcion.place(x=25,y=12.5)


    #MARCO CENTRO
    marco_modo_funcion = ctk.CTkFrame(marco_ingreso_valores, width=520, height=250, corner_radius=10)
    marco_modo_funcion.grid(row=0, column=1, padx=7.5, pady=20)  

    """label_habf = ctk.CTkLabel(marco_ingreso_valores, text=" ✅ [En uso]", font=("Arial Black", 16))
    label_habf.place(x=600, y=40)
    label_desf = ctk.CTkLabel(marco_ingreso_valores, text=" 🔙 [Habilitar]", font=("Arial Black", 16))
    #label_desf.place(x=600, y=40)"""

    #MARCO DERECHA
    marco_modo_tabla = ctk.CTkFrame(marco_ingreso_valores, width=520, height=250, corner_radius=10)
    marco_modo_tabla.grid(row=0, column=2, padx=7.5, pady=20)  # Ajustar pady a 20 para espacio arriba

    """label_habt = ctk.CTkLabel(marco_ingreso_valores, text=" ✅ [En uso]", font=("Arial Black", 16))
    #label_habt.place(x=800, y=40)
    label_dest = ctk.CTkLabel(marco_ingreso_valores, text=" 🔙 [Habilitar]", font=("Arial Black", 16))
    label_dest.place(x=875, y=40)"""

    boton_modo_tabla = ctk.CTkButton(marco_ingreso_valores, text="Modo Tabla", command=lambda: deshabilitar_marco(marco_modo_funcion))
    boton_modo_tabla.pack(pady=20)
    boton_modo_tabla.place(x=835, y=35)

    boton_modo_funcion = ctk.CTkButton(marco_ingreso_valores, text="Modo Funcion", command=lambda: deshabilitar_marco(marco_modo_tabla))
    boton_modo_funcion.pack(pady=20)
    boton_modo_funcion.place(x=300, y=35)


    #declaracion marco inferior
    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=550,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)


    #MENU TIPO DE INTEGRACION::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    # Variables de control
    menu_bloqueado = False  # Inicialmente el menú no está bloqueado
    grado_seleccionado = None  # Variable para almacenar el grado de integración seleccionado
    valor_metodo_integral=0
    valor_grado_integral=0

    

    #FUNCIONES OCULTAL LABELS
    def ocultar_labes_M1():
        #ocultar metodos de integracion
        for label in [label_opcion1_M1, label_opcion2_M1, label_opcion3_M1, label_opcion4_M1, label_opcion5_M1]:
            label.place_forget()

    def ocultar_labes_M2():
        #ocultar grado de integracion
        for label in [label_grado1_M2,label_grado2_M2]:
            label.place_forget()

    def ocultar_labels_A1B1A2B2A3B3():
        #oculta los labels y los entrys de todos los grados
        for label, entry in [
            (label_ingrese_A1, e_ingrese_A1),
            (label_ingrese_A2, e_ingrese_A2),
            (label_ingrese_B1, e_ingrese_B1),
            (label_ingrese_B2, e_ingrese_B2),
        ]:
            label.place_forget()
            entry.place_forget()

    def ocultar_labels_M3():
        for label in [
            (label_dx_M3),
            (label_dy_M3),
        ]:
            label.place_forget()   

    def ocultar_labels_M4():
        for label in [
            (label_dx_M4),
            (label_dy_M4),
        ]:
            label.place_forget()          
         
    
    #FUNCIONES DE POSICIONES DE LABELS Y ENTRYS
    #funciones pares AB:
    def pares_grado1():
        ocultar_labels_A1B1A2B2A3B3()
        label_ingrese_B1.place(x=87.5,y=genBy)    
        e_ingrese_B1.place(x=80,y=70)
        label_ingrese_A1.place(x=87.5,y=geneAy)
        e_ingrese_A1.place(x=80,y=150)

    def pares_grado2():
        pares_grado1()
        label_ingrese_B2.place(x=42.5,y=genBy)
        e_ingrese_B2.place(x=35,y=70)
        label_ingrese_A2.place(x=42.5,y=geneAy)
        e_ingrese_A2.place(x=35,y=150)

    #funciones mostrar labels menus
    def op1_M1():
        ocultar_labes_M1()
        label_opcion1_M1.place(x=72.5, y=pry)
    def op2_M1():
        ocultar_labes_M1()  
        label_opcion2_M1.place(x=65, y=pry)
    def op3_M1():
        ocultar_labes_M1()
        label_opcion3_M1.place(x=85, y=pry)
    def op4_M1():
        ocultar_labes_M1()
        label_opcion4_M1.place(x=85, y=pry)
    def op5_M1():
        ocultar_labes_M1()    
        label_opcion5_M1.place(x=70, y=pry)

    def op1_M2():
        ocultar_labes_M2()  
        ocultar_labels_M4()
        label_grado1_M2.place(x=57.5,y=150)
        boton_integracion_2.place_forget()
    def op2_M2():
        ocultar_labes_M2() 
        ocultar_labels_M4()       
        label_dx_M4.place(x=452.5,y=110)
        label_grado2_M2.place(x=57.5,y=150)
        boton_integracion_2.place_forget()
        boton_integracion_2.place(x=420, y=65)
        

    def opcion_dx_M3():
        grado_integracion_1.set_transportador(1)
        ocultar_labels_M3()
        label_dx_M3.place(x=360,y=110)
    def opcion_dy_M3():
        grado_integracion_1.set_transportador(2)
        ocultar_labels_M3()
        label_dy_M3.place(x=360,y=110)

    def opcion_dx_M4():
        grado_integracion_2.set_transportador(1)
        ocultar_labels_M4()
        label_dx_M4.place(x=452.5,y=110)
    def opcion_dy_M4():
        grado_integracion_2.set_transportador(2)
        ocultar_labels_M4()
        label_dy_M4.place(x=452.5,y=110)


    #MENU: SELECCION METODO DE INTEGRACION:       
    #funciones opciones menu: Metodo de integracion
    prx, pry = 70, 90
    def opcion_trapecio_simple():
        boton_grado_de_integracion.configure(state=DISABLED)
        boton_grado_de_integracion.configure(state="disabled")
        metodo_funcion_tabla.set_transportador(1)
        opcion_grado_1()
        op1_M1()
        op1_M2()
        
    def opcion_trapecio_compuesto():
        boton_grado_de_integracion.configure(state="normal")
        metodo_funcion_tabla.set_transportador(2)
        opcion_grado_1()
        op2_M1()       
        
    def opcion_simpson_13():
        boton_grado_de_integracion.configure(state="normal")
        metodo_funcion_tabla.set_transportador(3)
        opcion_grado_1()
        op3_M1()

    def opcion_simpson_38():
        boton_grado_de_integracion.configure(state="normal")
        metodo_funcion_tabla.set_transportador(4)
        opcion_grado_1()                  
        op4_M1()

    def opcion_trapecio_simpson():
        boton_grado_de_integracion.configure(state="normal")
        metodo_funcion_tabla.set_transportador(5)
        opcion_grado_1()
        op5_M1()
        
    #MENU: SELECCION GRADO DE INTERGRACION:
    #funciones opciones menu: Grado de integracion

    def opcion_grado_1():
        nivel_grado.set_transportador(1) 
        pares_grado1()
        op1_M2()
        
    def opcion_grado_2():    
        nivel_grado.set_transportador(2) 
        pares_grado2()
        op2_M2()




    ###################################################################################################################
    #MENU METODO DE INTEGRACION↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    menu_metodo_de_integracion_M1 = Menu(ventana, tearoff=0)
    menu_metodo_de_integracion_M1.add_command(label="Trapecio Simple", command=opcion_trapecio_simple)
    menu_metodo_de_integracion_M1.add_command(label="Trapecio Compuesto", command=opcion_trapecio_compuesto)
    menu_metodo_de_integracion_M1.add_command(label="Simpson 1/3", command=opcion_simpson_13)
    menu_metodo_de_integracion_M1.add_command(label="Simpson 3/8", command=opcion_simpson_38)
    menu_metodo_de_integracion_M1.add_command(label="Trapecio Simpson", command=opcion_trapecio_simpson)

    # Función para mostrar o esconder el menú principal en una ubicación específica
    def mostrar_menu(event):
        global menu_bloqueado
        #ocultar_labels_y_entries()
        ocultar_labes_M2()
        #mostrar_labels_entries_grado1()
        boton_metodo_de_integracion.update_idletasks()
        x = boton_metodo_de_integracion.winfo_rootx()
        y = boton_metodo_de_integracion.winfo_rooty() + boton_metodo_de_integracion.winfo_height()
        menu_metodo_de_integracion_M1.tk_popup(x, y)

    # Crear un botón para desplegar el menú principal
    boton_metodo_de_integracion = ctk.CTkButton(marco_meth_grad, text="Opciones de Integración")
    boton_metodo_de_integracion.place(x=50, y=60)
    boton_metodo_de_integracion.bind("<Button-1>", mostrar_menu)

    # Labels para las opciones del menú principal (inicialmente ocultos)
    label_opcion1_M1 = ctk.CTkLabel(marco_meth_grad, text="[Trapecio Simple]", font=("Arial", 12))
    label_opcion2_M1 = ctk.CTkLabel(marco_meth_grad, text="[Trapecio Compuesto]", font=("Arial", 12))
    label_opcion3_M1 = ctk.CTkLabel(marco_meth_grad, text="[Simpson 1/3]", font=("Arial", 12))
    label_opcion4_M1 = ctk.CTkLabel(marco_meth_grad, text="[Simpson 3/8]", font=("Arial", 12))
    label_opcion5_M1 = ctk.CTkLabel(marco_meth_grad, text="[Trapecio Simpson]", font=("Arial", 12))

    #MENU METODO DE INTEGRACION↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    ###################################################################################################################
    #MENU GRADO DE INTEGRACION↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    menu_grado_de_integracion_M2 = Menu(ventana, tearoff=0)
    menu_grado_de_integracion_M2.add_command(label="Grado Integración: 1", command=opcion_grado_1)
    menu_grado_de_integracion_M2.add_command(label="Grado Integración: 2", command=opcion_grado_2)

    # Función para mostrar o esconder el menú de grado en una ubicación específica
    def mostrar_menu_grado(event):
        boton_grado_de_integracion.update_idletasks()
        x = boton_grado_de_integracion.winfo_rootx()
        y = boton_grado_de_integracion.winfo_rooty() + boton_grado_de_integracion.winfo_height()
        menu_grado_de_integracion_M2.tk_popup(x, y)

    # Crear un botón para desplegar el menú de grado
    boton_grado_de_integracion = ctk.CTkButton(marco_meth_grad, text="Grado de Integración")
    boton_grado_de_integracion.place(x=55, y=120)
    boton_grado_de_integracion.bind("<Button-1>", mostrar_menu_grado)

    # Labels para las opciones del menú de grado (inicialmente ocultos)
    label_grado1_M2 = ctk.CTkLabel(marco_meth_grad, text="[Grado de Integración: 1]", font=("Arial", 12))
    label_grado2_M2 = ctk.CTkLabel(marco_meth_grad, text="[Grado de Integración: 2]", font=("Arial", 12))

    #MENU GRADO DE INTEGRACION↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    ###################################################################################################################
    #MENU INTEGRACION 1 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    menu_integracion_1 = Menu(ventana, tearoff=0)
    menu_integracion_1.add_command(label="dx", command=opcion_dx_M3)
    menu_integracion_1.add_command(label="dy", command=opcion_dy_M3)
    
    def mostrar_menu_variable(event):
        global menu_bloqueado
        boton_integracion_1.update_idletasks()
        x = boton_integracion_1.winfo_rootx()
        y = boton_integracion_1.winfo_rooty() + boton_integracion_1.winfo_height()
        menu_integracion_1.tk_popup(x, y)

    # Crear un botón para desplegar el menú para seleccion de integral
    boton_integracion_1 = ctk.CTkButton(marco_modo_funcion, text="1° Integral", width=60)
    boton_integracion_1.place(x=330, y=65)
    
    boton_integracion_1.bind("<Button-1>", mostrar_menu_variable)

    """
    # Labels para las opciones del menú principal (inicialmente ocultos)
    opcion_dx_M3 = ctk.CTkLabel(marco_modo_funcion, text="dx", font=("Arial", 14))
    opcion_dy_M3 = ctk.CTkLabel(marco_modo_funcion, text="dy", font=("Arial", 14))
    """
    #MENU INTEGRACION 1 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    ###################################################################################################################
    #MENU INTEGRACION 2 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    menu_integracion_2 = Menu(ventana, tearoff=0)
    menu_integracion_2.add_command(label="dx", command=opcion_dx_M4)
    menu_integracion_2.add_command(label="dy", command=opcion_dy_M4)
    menu_integracion_2.place_forget()#aparece invisible

    #creamos boton
    def mostrar_menu_variable2(event):
        global menu_bloqueado
        boton_integracion_2.update_idletasks()
        x = boton_integracion_2.winfo_rootx()
        y = boton_integracion_2.winfo_rooty() + boton_integracion_2.winfo_height()
        menu_integracion_2.tk_popup(x, y)

    boton_integracion_2 = ctk.CTkButton(marco_modo_funcion, text="2° Integral", width=60)
    #boton_integracion_2.place(x=450, y=65)
    boton_integracion_2.place_forget()    
    boton_integracion_2.bind("<Button-1>", mostrar_menu_variable2)

    """
    # Labels para las opciones del menú principal (inicialmente ocultos)
    opcion_dx_M4 = ctk.CTkLabel(marco_modo_funcion, text="dx", font=("Arial", 14))
    opcion_dy_M4 = ctk.CTkLabel(marco_modo_funcion, text="dy", font=("Arial", 14))
    """
    #MENU INTEGRACION 2 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    ###################################################################################################################

    #################################################################################################################################################################
    ################################################################# LABELS Y ENTRYS GENERALES #####################################################################
    #################################################################################################################################################################
    
    #label y entry funcion
    
    geneAy, genBy,  = 180, 45

    _func = "Ingrese una funcion"    
    label_ingrese_funcion = ctk.CTkLabel(marco_modo_funcion,text = _func,font=tipo_tamaño_letra_ventana2)
    label_ingrese_funcion.place(x=130,y=80)
    e_ingrese_funcion = ctk.CTkEntry(marco_modo_funcion,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_funcion.place(x=120,y=110)


    #LABEL Y ENTRY GRADO 1
    _B1 = "B1"
    label_ingrese_B1 = ctk.CTkLabel(marco_modo_funcion,text = _B1,font=tipo_tamaño_letra_ventana2)
    e_ingrese_B1 = ctk.CTkEntry(marco_modo_funcion,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)

    _A1 = "A1"
    label_ingrese_A1 = ctk.CTkLabel(marco_modo_funcion,text = _A1,font=tipo_tamaño_letra_ventana2)
    e_ingrese_A1 = ctk.CTkEntry(marco_modo_funcion,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)

    label_ingrese_B1.place(x=87.5,y=genBy)    
    e_ingrese_B1.place(x=80,y=70)
    label_ingrese_A1.place(x=87.5,y=geneAy)
    e_ingrese_A1.place(x=80,y=150)
    
    #LABEL Y ENTRY GRADO 2
    _B2 = "B2"
    label_ingrese_B2 = ctk.CTkLabel(marco_modo_funcion,text = _B2,font=tipo_tamaño_letra_ventana2)
    label_ingrese_B2.place(x=62.5,y=genBy)
    e_ingrese_B2 = ctk.CTkEntry(marco_modo_funcion,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_B2.place(x=55,y=70)

    _A2 = "A2"
    label_ingrese_A2 = ctk.CTkLabel(marco_modo_funcion,text = _A2,font=tipo_tamaño_letra_ventana2)
    label_ingrese_A2.place(x=62.5,y=geneAy)
    e_ingrese_A2 = ctk.CTkEntry(marco_modo_funcion,width=30,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_A2.place(x=55,y=150)

    #aparecen ocultos al inicio
    label_ingrese_B2.place_forget()
    e_ingrese_B2.place_forget()

    label_ingrese_A2.place_forget()
    e_ingrese_A2.place_forget()



    #LABEL INTEGRACION 1:
    _dx, _dy, _dz = "dx", "dy", "dz"
    label_dx_M3 = ctk.CTkLabel(marco_modo_funcion,text = _dx,font=tipo_tamaño_letra_ventana2)
    label_dx_M3.place(x=362.5,y=110)
        
    label_dy_M3 = ctk.CTkLabel(marco_modo_funcion,text = _dy,font=tipo_tamaño_letra_ventana2)
    #label_dy_M3.place(x=362.5,y=110)
    #aparece oculto al inicio
    #label_dy_M3.place_forget()


    #LABEL INTEGRACION 2:
    label_dx_M4 = ctk.CTkLabel(marco_modo_funcion,text = _dx,font=tipo_tamaño_letra_ventana2)
    #label_dx_M4.place(x=445,y=110)
    #aparece oculto al inicio
    #label_dx_M4.place_forget()
        
    label_dy_M4 = ctk.CTkLabel(marco_modo_funcion,text = _dy,font=tipo_tamaño_letra_ventana2)
    #label_dy_M4.place(x=362.5,y=110)
    #aparece oculto al inicio
    #label_dy_M4.place_forget()

    #INGRESE INTERVALOS
    label_numero_intervalos = ctk.CTkLabel(marco_modo_funcion,text = "Cantidad Intervalos",font=tipo_tamaño_letra_ventana2)
    label_numero_intervalos.place(x=330,y=20)
    e_ingreso_numero_intervalos = ctk.CTkEntry(marco_modo_funcion,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingreso_numero_intervalos.place(x=450,y=20)
    #cant_intervalos.set_transportador()
    

    ###CUADRO DERECHA:

    _x1 = "Valores x:   "
    label_x1 = ctk.CTkLabel(marco_modo_tabla,text = _x1,font=tipo_tamaño_letra_ventana2)
    label_x1.place(x=40,y=90)    

    e_ingrese_x1 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_x2 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_x1.place(x=120,y=90)
    e_ingrese_x2.place(x=170,y=90)
    
    e_ingrese_x3 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_x4 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_x5 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)

    _y1 = "Valores f(x):"
    label_y1 = ctk.CTkLabel(marco_modo_tabla,text = _y1,font=tipo_tamaño_letra_ventana2)
    label_y1.place(x=40,y=130)    
    e_ingrese_y1 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_y2 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_y1.place(x=120,y=130)
    e_ingrese_y2.place(x=170,y=130)

    e_ingrese_y3 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_y4 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    e_ingrese_y5 = ctk.CTkEntry(marco_modo_tabla,width=40,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)

    e_ingrese_x3.place(x=220,y=90)
    e_ingrese_y3.place(x=220,y=130)             
    e_ingrese_x4.place(x=270,y=90)
    e_ingrese_y4.place(x=270,y=130)        
    e_ingrese_x5.place(x=320,y=90)
    e_ingrese_y5.place(x=320,y=130)

    e_ingrese_x3.place_forget()
    e_ingrese_y3.place_forget()
    e_ingrese_x4.place_forget()
    e_ingrese_y4.place_forget()
    e_ingrese_x5.place_forget()
    e_ingrese_y5.place_forget()

    def validar_numeros(cadena):
        if cadena.isdigit():  # Verifica si la cadena contiene solo dígitos
            numero = int(cadena)
        else:
            numero = None

        return numero

    _cv = "Cantidad de parejas (min: 2, max: 5):"
    label_cv = ctk.CTkLabel(marco_modo_tabla,text = _cv ,font=tipo_tamaño_letra_ventana2)
    label_cv.place(x=40,y=50)

    def limpiar():
        for entry in [
            (e_ingrese_x3),(e_ingrese_y3),
            (e_ingrese_x4),(e_ingrese_y4),
            (e_ingrese_x5),(e_ingrese_y5)
        ]:
            entry.place_forget()
    
    def opcion_2():
        limpiar()
        e_ingrese_x1.place(x=120,y=90)
        e_ingrese_x2.place(x=170,y=90)
        boton_cant_vari.place_forget()
        boton_cant_vari.place(x=275, y=50)
        boton_cant_vari.configure(text="Cantidad de pares: 2")
    def opcion_3():
        limpiar()
        e_ingrese_x3.place(x=220,y=90)
        e_ingrese_y3.place(x=220,y=130)
        boton_cant_vari.place_forget()
        boton_cant_vari.place(x=275, y=50)
        boton_cant_vari.configure(text="Cantidad de pares: 3")
    def opcion_4():
        limpiar()
        e_ingrese_x3.place(x=220,y=90)
        e_ingrese_y3.place(x=220,y=130)             
        e_ingrese_x4.place(x=270,y=90)
        e_ingrese_y4.place(x=270,y=130)
        boton_cant_vari.place_forget()
        boton_cant_vari.place(x=275, y=50)
        boton_cant_vari.configure(text="Cantidad de pares: 4")
    def opcion_5():
        limpiar()
        e_ingrese_x3.place(x=220,y=90)
        e_ingrese_y3.place(x=220,y=130)             
        e_ingrese_x4.place(x=270,y=90)
        e_ingrese_y4.place(x=270,y=130)        
        e_ingrese_x5.place(x=320,y=90)
        e_ingrese_y5.place(x=320,y=130)
        boton_cant_vari.place_forget()
        boton_cant_vari.place(x=275, y=50)
        boton_cant_vari.configure(text="Cantidad de pares: 5")

    
    #menu cantidad pares variables
    menu_cant_pares = Menu(ventana, tearoff=0)
    menu_cant_pares.add_command(label="2 pares", command=opcion_2)
    menu_cant_pares.add_command(label="3 pares", command=opcion_3)
    menu_cant_pares.add_command(label="4 pares", command=opcion_4)
    menu_cant_pares.add_command(label="5 pares", command=opcion_5)

    #creamos boton
    def mostrar_menu_cant_vari(event):
        global menu_bloqueado
        boton_cant_vari.update_idletasks()
        x = boton_cant_vari.winfo_rootx()
        y = boton_cant_vari.winfo_rooty() + boton_cant_vari.winfo_height()
        menu_cant_pares.tk_popup(x, y)

    boton_cant_vari = ctk.CTkButton(marco_modo_tabla, text="Cantidad de pares", width=70)
    boton_cant_vari.bind("<Button-1>", mostrar_menu_cant_vari)
    boton_cant_vari.place(x=275, y=50)
    

    #################################################################################################################################################################
    #################################################################################################################################################################
    
    #::validaciones
    #habilitacion de botones globales
    global boton_limpiar,boton_resolver,mostrar
    """
    print("-----trapcio simple: funcion------")  
    Metodo_Trapecio_Simple(expresion="x**2 - 2*x", A=3, B=5)
    print("-----trapcio simple: tablas------")
    Metodo_Trapecio_Simple(list_a = listx, list_b = listy)
    print("-----trapcio compuesto: funcion------")
    Metodo_Trapecio_Compuesto(grado_integral=1, n=4, expresion="2*x**2 + 32", A=-1, B=1)
    print("\n-----trapcio compuesto: tablas------")
    Metodo_Trapecio_Compuesto(grado_integral=1, n=4, list_a=lista_x, list_b=lista_y)
    print("\n-----simpson 1/3:funcion------")
    Metodo_Simpson_13(grado_integral=1, n=4, expresion='x**2', A=0, B=2)
    print("\n-----simpson 1/3:tabla------")
    Metodo_Simpson_13(grado_integral=1, n=4, list_a=lista_x, list_b=valores_funcion)
    print("\n-----simpson 3/8:funcion------")
    Metodo_Simpson_38(grado_integral=1, n=6, expresion='x**2', A=0, B=2.5)
    print("\n-----simpson 3/8:funcion------")
    Metodo_Simpson_38(grado_integral=1, n=6, list_a=lista_x, list_b=valores_funcion)
    """

    def Validacion():
        #metodo: None, funcion 0, tabla 1
        #opcion metodo: None, trapecio simple 1, trapecio compusto 2, simpson 1/3 3, simpson 3/8, trapecion.simpson 5
        #opcion grado: None, grado de integracion 1 (1)(obligatorio para trapecio simple), grado de integracion 2 (2)

        def Metodo_Trapecio_Simple(expresion=None, A=None, B=None, list_a=None, list_b=None):
            modo = 'modo_funcion' if expresion is not None else 'modo_tabla'
            
            if not validar_entradas(modo, expresion, A, B, list_a, list_b):
                return
            
            if modo == 'modo_funcion':
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
                    Error = f"Error al evaluar la función, Método Trapecio Simple: {e}"
                    print(f"Error al evaluar la función: {e}")
                    verificador_error(Error)
                    
            elif modo == 'modo_tabla':
                if len(list_a) != 2 or len(list_b) != 2:
                    verificador_error("Las listas deben contener exactamente dos elementos.")
                    return

                try:
                    A = list_a[0]
                    B = list_a[1]
                    funcion_A = list_b[0]
                    funcion_B = list_b[1]

                    integral_approx = (B - A) * (funcion_A + funcion_B) / 2
                    print("sumatoria: ",integral_approx)
                    print(f"[TS: modo tabla] La integral aproximada es: {integral_approx}") 

                except Exception as e:
                    Error = f"Error: Método Trapecio Simple {e}"
                    print(f"Error: Método Trapecio Simple {e}")
                    verificador_error(Error)

            listmodo = metodo_funcion_tabla.get_transportador()
            modo = listmodo[-1]
            def validar_entradas(modo, expresion, A, B, list_a, list_b):
                if modo == 'modo_funcion':
                    if not expresion:
                        print("Error: La expresión no puede estar vacía.")
                        return False
                    if A is None or B is None:
                        print("Error: A y B no pueden estar vacíos.")
                        return False
                    return True
                
                elif modo == 'modo_tabla':
                    if not list_a or not list_b:
                        print("Error: Las listas no pueden estar vacías.")
                        return False
                    if len(list_a) != len(list_b):
                        print("Error: Las listas deben tener la misma longitud.")
                        return False
                    return True
                
                else:
                    print("Error: Modo desconocido.")
                    return False
        
        muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
        #muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
        #muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
        #muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

        #Metodo_Trapecio_Simple()
        #Metodo_Trapecio_Compuesto()
        #Metodo_Simpson_13()
        #Metodo_Simpson_38()
        #Metodo_Trapecio_Simpson
#             
    
        #impresion de datos
        muestra_valores.configure(text = Mensaje, anchor='w', justify='left')

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
            #muestra_grafica.place(x=700,y=20)

        #Se desactiva el botón de Resolver
        boton_resolver.configure(state=DISABLED)
        #Se activa el botón de Limpiar
        boton_limpiar.configure(state=NORMAL)
                    
                    
        #Se limpia los entry cuando ya se resulve por el metodo
        e_ingrese_funcion.delete(0, END)
        #e_ingrese_x0.delete(0, END)
        #e_ingrese_x1.delete(0, END)
        #e_ingrese_x2.delete(0, END)
        #e_ingrese_cs.delete(0, END)
        
   
    boton_resolver_1 = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=100,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver_1.place(x=1220,y=240)
    boton_resolver_1.configure(state=DISABLED)

    boton_resolver_2 = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=100,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver_2.place(x=680,y=240)
    boton_resolver_2.configure(state=DISABLED)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=100,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)    
    boton_limpiar.place(x=150,y=240)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=100,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=22.5,y=240)      

# Función para ocultar todos los labels y entries+
