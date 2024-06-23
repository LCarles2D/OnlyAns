#!/usr/bin/env python3
import sympy as sp
import pandas as pd
from sympy import *
import pandas as pd
from sympy.core.numbers import *
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

def Metodo_Multipasos(edo, xi, yi, xf, h, paso):
    x,y=sp.symbols("x y")
    iteracion=0
    salida = ""  # Variable para almacenar todos los mensajes
    print('EDOOO:', edo)

    if paso != 2 and paso != 4:
        messagebox.showerror("ERROR",f"Error no se puede calcular el paso seleccionado\n")

    if xi >= xf:
        messagebox.showerror("ERROR", f"Error el X inicial debe de ser menor al X final\n")

    if h <= 0:
        messagebox.showerror("ERROR",f"Error el salto(h) debe de ser mayor a 0\n")

    if paso == 2 and (xi + 2*h) > xf:
        salida += f"Error el salto(h) no permite generar los valores (x) y (y) necesarios para el paso 2\n"

    if paso == 4 and (xi + 4*h) > xf:
        salida += f"Error el salto(h) no permite generar los valores (x) y (y) necesarios para el paso 4\n"

    if paso == 2:
        salida += f"Error el X inicial debe de ser menor al X iinal\n"
        tabla = [[], [], [], [], [], []]
        columnas = ["iteracion", "xi", "yi", "k1", "k2", "yi+1"]

        while xi + h < xf:
            tabla[0].append(iteracion)
            tabla[1].append(xi)
            tabla[2].append(yi)
            salida += f"{iteracion}\n"
            k_1 = N(edo, 8, subs={x: xi}).evalf(n=8)
            k1 = N(k_1, 8, subs={y: yi}).evalf(n=8)
            k_2 = N(edo, 8, subs={x: xi + h}).evalf(n=8)
            k2 = N(k_2, 8, subs={y: yi + k1 * h}).evalf(n=8)
            if k1.is_real == False:
                salida += "En el valor k1 se generaron numeros no reales\n"
                break
            elif k2.is_real == False:
                salida += "En el valor k2 se generaron numeros no reales\n"
                break
            else:
                yi_sig = N(yi + (1/2) * h * (k1 + k2), 8)
                tabla[3].append(k1)
                tabla[4].append(k2)
                tabla[5].append(yi_sig)
                iteracion = iteracion + 1
                xi = (xi + h)
                yi = yi_sig
        
        df = pd.DataFrame(tabla, columnas).T
        salida += f"{df}\n"
        y_predictor = tabla[5][len(tabla[5]) - 1] + (h / 2) * (3 * edo.subs({x: tabla[1][len(tabla[0]) - 1] + h, y: tabla[5][len(tabla[2]) - 1]}) - edo.subs({x: tabla[1][len(tabla[0]) - 1], y: tabla[2][len(tabla[0]) - 1]}))
        salida += f"{y_predictor}\n"
        y_corrector = tabla[5][len(tabla[5]) - 1] + (h / 2) * (edo.subs({x: tabla[1][len(tabla[0]) - 1] + 2 * h, y: y_predictor}) + edo.subs({x: tabla[1][len(tabla[0]) - 1] + h, y: tabla[1][len(tabla[0]) - 1]}))

    elif paso == 4:
        tabla = [[], [], [], [], [], [], [], []]
        columnas = ["iteracion", "xi", "yi", "k1", "k2", "k3", "k4", "yi+1"]

        while xi + h < xf:
            tabla[0].append(iteracion)
            tabla[1].append(xi)
            tabla[2].append(yi)
            salida += f"{iteracion}\n"
            k_1 = N(edo, 8, subs={x: xi}).evalf(n=8)
            k1 = N(k_1, 8, subs={y: yi}).evalf(n=6)
            k_2 = N(edo, 8, subs={x: xi + (h / 2)}).evalf(n=6)
            k2 = N(k_2, 8, subs={y: yi + (h / 2) * k1}).evalf(n=6)
            k_3 = N(edo, 8, subs={x: xi + (h / 2)}).evalf(n=6)
            k3 = N(k_3, 8, subs={y: yi + k2 * (h / 2)}).evalf(n=6)
            k_4 = N(edo, 8, subs={x: xi + h}).evalf(n=6)
            k4 = N(k_4, 8, subs={y: yi + k3 * h}).evalf(n=6)
            if k1.is_real == False:
                salida += "En el valor k1 se generaron numeros no reales\n"
                break
            elif k2.is_real == False:
                salida += "En el valor k2 se generaron numeros no reales\n"
                break
            elif k3.is_real == False:
                salida += "En el valor k3 se generaron numeros no reales\n"
                break
            elif k4.is_real == False:
                salida += "En el valor k4 se generaron numeros no reales\n"
                break
            else:
                yi_sig = N(yi + (1/6) * h * (k1 + 2 * k2 + 2 * k3 + k4), 8)
                tabla[3].append(k1)
                tabla[4].append(k2)
                tabla[5].append(k3)
                tabla[6].append(k4)
                tabla[7].append(yi_sig)
                iteracion = iteracion + 1
                xi = xi + h
                yi = yi_sig
        df = pd.DataFrame(tabla, columnas).T
        salida += f"{df}\n"
        salida += f"Respuesta {tabla[7][len(tabla[7]) - 1]}\n"
        eva1 = edo.subs({x: tabla[1][len(tabla[0]) - 1] + h, y: tabla[7][len(tabla[7]) - 1]})
        salida += f"{eva1}\n"
        eva2 = edo.subs({x: tabla[1][len(tabla[0]) - 1], y: tabla[2][len(tabla[7]) - 1]})
        salida += f"{eva2}\n"
        eva3 = edo.subs({x: tabla[1][len(tabla[0]) - 2], y: tabla[2][len(tabla[7]) - 2]})
        salida += f"{eva3}\n"
        eva4 = edo.subs({x: tabla[1][len(tabla[0]) - 3], y: tabla[2][len(tabla[7]) - 3]})
        salida += f"{eva4}\n"
        # predictor 
        y_predictor = tabla[7][len(tabla[7]) - 1] + (h / 24) * (55 * eva1 - 59 * eva2 + 37 * eva3 - 9 * eva4)
        salida += f"{y_predictor}\n"
        # corrector
        eva5 = edo.subs({x: tabla[1][len(tabla[0]) - 1] + 2 * h, y: y_predictor})
        salida += f"{eva5}\n"
        eva6 = edo.subs({x: tabla[1][len(tabla[0]) - 1] + h, y: tabla[7][len(tabla[7]) - 1]})
        salida += f"{eva6}\n"
        eva7 = edo.subs({x: tabla[1][len(tabla[0]) - 1], y: tabla[2][len(tabla[7]) - 1]})
        salida += f"{eva7}\n"
        eva8 = edo.subs({x: tabla[1][len(tabla[0]) - 2], y: tabla[2][len(tabla[7]) - 2]})
        salida += f"{eva8}\n"
        y_corrector = tabla[7][len(tabla[7]) - 1] + (h / 24) * (9 * eva5 + 19 * eva6 - 5 * eva7 + eva8)
        salida += f"{y_corrector}\n"
        # abc

    return salida  # Devolver la cadena con todos los mensajes

color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2
toggle = False
mostrar_y = True
orden = 2

def Ventana_Multipasos(frame, ventana2, ventana):
    global toggle
    global marco_muestra_valores
    global canvas, orden

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
    x_btn = 850
    y_btn = 60

    ########### Etiquetas
    etiqueta_ingreso_valores_x = ctk.CTkLabel(marco_ingreso_valores,text = "Valores de x",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valores_x.place(x=40,y=20)

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Valores de y",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=250, y=20)

    etiqueta_ingreso_interpolacion = ctk.CTkLabel(marco_ingreso_valores,text = "h",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_interpolacion.place(x=660,y=20)
    
    etiqueta_ingreso_valores_y = ctk.CTkLabel(marco_ingreso_valores,text = "funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valores_y.place(x=400,y=20)

    etiqueta_limite_a = ctk.CTkLabel(marco_ingreso_valores,text = "x1",font=tipo_tamaño_letra_ventana2)
    etiqueta_limite_a.place(x=80, y=60)

    etiqueta_limite_b = ctk.CTkLabel(marco_ingreso_valores,text = "x2",font=tipo_tamaño_letra_ventana2)
    etiqueta_limite_b.place(x=80, y=100)

    etiqueta_orden_text = ctk.CTkLabel(marco_ingreso_valores, text = "Orden:", font=tipo_tamaño_letra_ventana2)
    etiqueta_orden_text.place(x= 875, y= 105)

    etiqueta_orden = ctk.CTkLabel(marco_ingreso_valores, text = orden, font = tipo_tamaño_letra_ventana2)
    etiqueta_orden.place(x= 900, y= 125)

    necesarios = [marco_ingreso_valores, tipo_tamaño_letra_ventana2, color_texto_ventana2]
    
    ############# Entrada de valores
    ingresos_x0 =IngresarEnCadena(*necesarios, 100, 60, 2)
    ingreso_y1 = IngresarEnCadena(*necesarios, 250,60, 1)

    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=400,y=60)
    ingreso_interpolacion = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_interpolacion.place(x=660,y=60)
    
    def eliminar_orden():
        global orden
        if orden > 2:
            orden -= 1 
            etiqueta_orden.configure(text=orden)
    def agregar_orden():
        global orden
        if orden < 4:
            orden += 1
            etiqueta_orden.configure(text=orden)
    
    boton_agregar_grados = ctk.CTkButton(marco_ingreso_valores,text ="-",command=eliminar_orden,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_agregar_grados.place(x=x_btn,y=y_btn)
    boton_eliminar_grados = ctk.CTkButton(marco_ingreso_valores,text ="+",command=agregar_orden,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_eliminar_grados.place(x=x_btn+55,y=y_btn)
  
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
            x,y= sp.symbols('x y')
            
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
                if expr.free_symbols <= {x,y, sp.exp(1)}:  # Permitir x y la constante e
                    return True, expr
                else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="La función contiene variables no permitidas.")
            except Exception as e:
                #messagebox.showerror("Error de validación", f"La función ingresada no es válida")
                return False, None

    def Validacion():
        global boton_limpiar,boton_resolver,mostrar, orden, tabla, columnas
        #Se valida el ingreso de datos
        valores_x = [ingreso.get() for ingreso in ingresos_x0]
        valores_y = ingreso_y1[0].get()
        Ea = ingreso_interpolacion.get()
        funcion = ingreso_funcion.get()

        #Si estan vacios todos
        if (valores_x[0] == '' or valores_x[1] == '' or valores_y[0] == '' or Ea == '' or funcion == '') :
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos de forma correcta")
        else:
            
            if numero_valido(valores_x[0]) and numero_valido(valores_x[1]) and numero_valido(valores_y) and numero_valido(Ea):
                booleano, funcion = Validar_y_Reemplazar_funcion(funcion)
                print(type(funcion), funcion)
                if booleano == False:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Ingrese una  funcion valida")
                    return
                valores_x = [float(valor) for valor in valores_x]
                valores_y = float(valores_y)
                print(valores_y)
                Ea = float(Ea)

                if Ea <= 0:
                    messagebox.showerror("¡ ERROR CRITICO !",message="h debe ser mayor a 0")
                    return

                if valores_x[0] > valores_x[1]:
                        messagebox.showerror("¡ ERROR CRITICO !",message="El valor de 'x1' debe de ser mayor que 'x2' ")
                        return

                muestra_valores = ctk.CTkLabel(marco_muestra_valores,font= ("Currier",15,"bold"), justify= 'left', anchor='w')
                print(funcion, valores_x[0],valores_y,valores_x[1], Ea, orden)
                
                text = Metodo_Multipasos(funcion, valores_x[0],valores_y,valores_x[1], Ea, orden) #def Runge_Kutta(funcion, x1, y1, x2, h, grado):

                muestra_valores.configure(text=f'{df}\n\nFuncion:{funcion}\nx1 = {valores_x[0]}\nx2 = {valores_x[1]}\ny1 = {valores_y}\ny2 = ?\n\n {text}')
                if mostrar == False:
                    return
                
                muestra_valores.place(x=10,y=20)
                #Se desactiva el botón de Resolver
                boton_resolver.configure(state=DISABLED)
                #Se activa el botón de Limpiar
                boton_limpiar.configure(state=NORMAL)
                
                
                #Se limpia los entry cuando ya se resulve por el metodo
                [ingresos.delete(0, END) for ingresos in ingresos_x0]
                ingreso_interpolacion.delete(0, END)
                ingreso_funcion.delete(0, END)
                ingreso_y1[0].delete(0, END)

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



'''


x, y = sp.symbols("x y")

# ingresara el Xi
xi = 0
# ingresa Yi
yi = 1
# ingresa x final
xf = 0.75
# ingresar el paso que se calculara 2,4
paso = 4
# ingresar salto
h = 0.25
# ecuacion diferencial EDO

edo = x - y + 1

# Llamar a la función y obtener la salida
resultado = Metodo_Multipasos(edo, xi, yi, xf, h, paso) 
'''

