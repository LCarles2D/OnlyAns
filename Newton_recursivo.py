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
from herramientas import *


b_array = []
mostrar =False

def Newton_recursivo(x_array, y_array=None, ecuacion = None, x_inter=None):
    global mostrar
#Puntos a cambiar
    if y_array == None and ecuacion == None:
        raise ValueError(f'{Color.RED}ERROR | Debe de ingresar un array de "Y" o una ecuacion')
    if ecuacion != None and y_array != None:
        raise ValueError(f'{Color.RED}ERROR | Ingresas el array o ingresas la ecuacion, no se puede ambos')
    if not has_unique_values(x_array):
        mostrar = False
        messagebox.showerror("¡ ERROR CRITICO !", message="Asegurate de ingresar valores no repetidos")
        return
    x = sp.symbols("x")
    ecuacion = sp.log(x)
    fx_array = y_array or [ecuacion.subs(x,xi).evalf() for xi in x_array]
    grado = len(x_array) - 1

    b0 = fx_array[0]
    global b_array
    b_array = [] 

    recursiva(x_array, fx_array, grado, 0)
    
#Inicializamos el array donde guardare los factores, los incializare con 1 para poder multiplicarlo con el anterior (Nose si esta sea la mejor opcion, porque si directamente los agrego no podria luego meterlos en orden)
    factor = [1 for i in range(0, grado)]


    Px = b0
    for i in range(1, grado+1):
        for j in range(0,i):
            factor[i-1] = (factor[i-1] * (x - x_array[j]))
        Px +=  b_array[i] * factor[i-1]

    Px = sp.expand(Px)
    Px = sp.simplify(Px)
    if x_inter == None:
        return Px
    raiz = Px.subs(x,x_inter).evalf()
    mostrar = True
    return Px, raiz, fx_array




def recursiva(x_array, fx_array,grado, i=0):
    global b_array
    if grado+1 == i:
        return
    if i == 0:
        b_array.append(fx_array[0])
        recursiva(x_array, fx_array,grado, 1)
        return
    elif i == 1:
        b_array.append((fx_array[i] - b_array[i-1])/(x_array[i]- x_array[0]))
        recursiva(x_array, fx_array, grado, 2)
        return
    b_array.append((((fx_array[i] - fx_array[i-1])/(x_array[i] - x_array[i-1])) - b_array[i-1])/(x_array[i] - x_array[0]))
    recursiva(x_array, fx_array, grado, i+1)

color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2
toggle = False
mostrar_y = True


def Ventana_Newton_Recursivo(frame, ventana2, ventana):
    global toggle
    global marco_muestra_valores
    global canvas

    global boton_limpiar,boton_resolver
    global tipo_tamaño_letra_ventana2,color_fondo_boton_ventana2,color_fondo_boton_ventana2
    global color_boton_pasar_mouse_ventana2,ancho_borde_ventana2,color_borde_ventana2
    global boton_limpiar,boton_resolver

    ########### Marcos
    marco_height = 460
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
    
    ############# ingresos_y de valores
    ingresos_x0 =IngresarEnCadena(*necesarios, 100, 60, 2)
    ingresos_y = IngresarEnCadena(*necesarios, 325, 60, 2)

    ingreso_interpolacion = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_interpolacion.place(x=600,y=60)

    
    def agregar_ingresos_ys():
        global mostrar_y
        if len(ingresos_x0) > 7:
            return
        x_x0 = ingresos_x0[-1].winfo_x()
        y_x0 = ingresos_x0[-1].winfo_y()
        ingresos_x0.append(ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = necesarios[1],text_color=necesarios[2]))
        ingresos_x0[-1].place(x=x_x0,y=(y_x0 + 40))
        if mostrar_y == True:
            x_y0 = ingresos_y[-1].winfo_x()
            y_y0 = ingresos_y[-1].winfo_y()
            ingresos_y.append(ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = necesarios[1],text_color=necesarios[2]))
            ingresos_y[-1].place(x=x_y0,y=(y_y0 + 40))
        else:
            x_y0 = ingresos_y[-1].winfo_x()
            y_y0 = ingresos_y[-1].winfo_y()
            ingresos_y.append(ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = necesarios[1],text_color=necesarios[2]))




    def eliminar_ingresos_ys():
        if len(ingresos_x0) <= 2:
            return
        ingresos_x0[-1].delete(0, END) 
        ingresos_x0[-1].place_forget()
        ingresos_x0.pop()
        ingresos_y[-1].delete(0, END) 
        ingresos_y[-1].place_forget()
        ingresos_y.pop()

                

    boton_agregar = ctk.CTkButton(marco_ingreso_valores,text ="-",command=eliminar_ingresos_ys,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_agregar.place(x=500,y=400)
    boton_eliminar = ctk.CTkButton(marco_ingreso_valores,text ="+",command=agregar_ingresos_ys,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_eliminar.place(x=555,y=400)



    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)


    ########### Alternar entre funcion y valores de y 
    def Alternar_visibilidad():
        global toggle
        global mostrar_y
        if toggle == False:
            boton_funcion_valores.configure(text="Valores de y")
            etiqueta_ingreso_valores_y.configure(text='Funcion')
            toggle = True
            ingreso_funcion.place(x=325,y=60)
            mostrar_y = False

            for ingreso in ingresos_y:
                ingreso.delete(0, END)
                ingreso.place_forget()
        else:
            boton_funcion_valores.configure(text='Funcion')
            etiqueta_ingreso_valores_y.configure(text='Valores de y')
            toggle= False
            ingreso_funcion.delete(0, END)
            ingreso_funcion.place_forget()
            mostrar_y = True
            
            for i in range(0,len(ingresos_y)):        ################ CAMBIAR ENTRY POR BOTON
                ingresos_y[i].place(x=325,y=(60 + 30*i + 10*i))

    boton_funcion_valores = ctk.CTkButton(marco_ingreso_valores,text ="Funcion",command=Alternar_visibilidad,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_funcion_valores.place(x=350 , y=400)


    def numero_valido(texto):
        return re.match(r"^-?\d*\.?\d*$", texto) is not None

    def Validacion_Funcion(funcion):
        patron = r'^(\s*\d+|\+|\-|\*{1,2}|/|\(|\)|x|e|sin\(x\)|cos\(x\)|tan\(x\)|asin\(x\)|acos\(x\)|atan\(x\)|log\(x\)|ln\(x\)|sqrt\(x\)|sqrt\d*\(x\))*\s*$'
        return re.match(patron, funcion) is not None
    
    def Convertir_Funcion(funcion):
        try:
            #Intenta convertir la ingresos_y en una expresion simbolica
            sp.sympify(funcion)
            return True
        except (sp.SympifyError, TypeError,SyntaxError):
            #Si hay un error en la sintaxis la ingresos_y no es valida
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
        x_llenados = False
        y_llenados = False
        derivada_llenado = False
        for i in range(len(valores_x)):
            if (valores_x[i] == '' or numero_valido(valores_x[i]) == False):
                x_llenados = True
            if (valores_y[i] == '' or numero_valido(valores_y[i]) == False):
                y_llenados = True
       #Si estan vacios todos
        if (x_llenados == True or interpolacion == '') or (y_llenados == True and funcion == '') :
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos de forma correcta")
        else:
            if not numero_valido(interpolacion):
                messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos de forma correcta")
                return 

            if funcion == '':    
                valores_y = [float(valores) for valores in valores_y]
                funcion = None
            else:
                booleano, funcion = Validar_y_Reemplazar_funcion(funcion)
                valores_y = None
                if booleano == False:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Ingrese una  funcion valida")
                    return

            valores_x = [float(valor) for valor in valores_x]
            interpolacion = float(interpolacion)

            muestra_valores = ctk.CTkLabel(marco_muestra_valores,font= ("Currier",15,"bold"), justify= 'left', anchor='w')
            
            Px, valor_aprox, new_y = Newton_recursivo(valores_x,valores_y,funcion, interpolacion) #def Newton_recursivo(x_array, y_array=None, ecuacion = None, x_inter=Non:
            result = ''
            for i, (val_x, val_y) in enumerate(zip(valores_x, new_y), start=1):
                result += f"x{i} = {val_x}, y{i} = {val_y}\n"

            if valores_y == None:
                muestra_valores.configure(text=result+f'evaluados en f(x) = {funcion}\n\n Con un polinomio interpolador de Px = {Px} con un valor aproximado de {valor_aprox}')
            else:
                muestra_valores.configure(text=result+f'\nCon un polinomio interpolador de Px = {Px} con un valor aproximado de {valor_aprox}')

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

            
    
    y_pos = 400
   
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


