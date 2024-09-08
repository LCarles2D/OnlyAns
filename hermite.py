#!/usr/bin/env python3

import sympy as sp
import math
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

mostrar= False 
cantidad_derivadas = 1


def derivate(ecuacion,valor,n,x_array, derivates):
    if ecuacion == None:
        funcion = dict(zip(x_array,derivates))
        return (funcion[valor][n-1])/math.factorial(n)

    x = sp.symbols("x")
    derivada = ecuacion
    for _ in range(0, n):
        derivada = sp.diff(derivada)
    return derivada.subs(x, valor).evalf()

def hermite(x_array, y_array=None, ecuacion=None,inter_point=None, derivates=None, derivates_array = []):
    global mostrar
    if y_array == None and ecuacion == None:
        raise ValueError(f'{Color.RED}ERROR | Debe de ingresar un array de "Y" o una ecuacion')
    if ecuacion != None and y_array != None:
        raise ValueError(f'{Color.RED}ERROR | Ingresas el array o ingresas la ecuacion, no se puede ambos')

    x= sp.symbols("x")
    fx_array = y_array
    dx_array = derivates_array or []
    print('holad',dx_array)
    if y_array == None:
        fx_array = [ecuacion.subs(x,xi).evalf() for xi in x_array]
        if derivates != None:
            for xi in x_array:
                dx_array.append([derivate(ecuacion, xi, orden, x_array, None) for orden in range(1, derivates+1)])
    print('deri', dx_array)
    contador = [0 for _ in range(len(dx_array))]
    print(f"derivadas: {dx_array}")
    for i in range(len(dx_array)):
        for j in range(len(dx_array[i])):
            if dx_array[i][j] != None:
                contador[i] += 1
    x_nodos = []
    fx_nodos = []
    suma = 1 if (ecuacion == None) else 0
    for i in range(0,len(x_array)):
        for j in range(contador[i]):
            x_nodos.append(x_array[i])
            fx_nodos.append(fx_array[i])

    grado = 2*len(x_array) + 1
    nivel = [fx_nodos] + [[] for i in range(len(x_nodos)-1)]
#Conseguir las constantes b
    for i in range(1, len(x_nodos)):
        for j in range(1, (len(x_nodos)+1)-i):
            b = (nivel[i-1][j] - nivel[i-1][j-1])/(x_nodos[j+(i-1)] - x_nodos[(j+(i-1)) - i]) if (x_nodos[j+(i-1)] - x_nodos[j-1]) != 0 else (derivate(ecuacion, x_nodos[j+(i-1)], i,x_array, dx_array))
            nivel[i].append(b)

    b_array = [nivel[i][0] for i in range(0,len(nivel))]
    factor = [1 for i in range(0, grado)]


    Px = b_array[0]
    for i in range(1, len(x_nodos)):
        for j in range(0,i):
            factor[i-1] = (factor[i-1] * (x - x_nodos[j]))
        Px +=  b_array[i] * factor[i-1]

    Px = sp.expand(Px)
    Px = sp.simplify(Px)

    mostrar = True
    valor_aprox = Px.subs(x, inter_point).evalf()
    if ecuacion == None:
        return Px, valor_aprox, ''
    valor_verdadero = ecuacion.subs(x, inter_point).evalf()

    Ea = ((valor_verdadero - valor_aprox)/(valor_verdadero))*100


    return Px, valor_verdadero, f'\n\nError porcentual: {Ea}'

color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2
toggle = False
mostrar_y = True




def Ventana_Hermite(frame, ventana2, ventana):
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

    etiqueta_puntos = ctk.CTkLabel(marco_ingreso_valores, text = 'Puntos', font=tipo_tamaño_letra_ventana2)
    etiqueta_puntos.place(x=530, y=375)

    etiqueta_numero_derivadas = ctk.CTkLabel(marco_ingreso_valores, text=cantidad_derivadas, font=tipo_tamaño_letra_ventana2)
    etiqueta_numero_derivadas.place(x=665, y= 350)
    etiqueta_der = ctk.CTkLabel(marco_ingreso_valores, text = 'Derivadas', font=tipo_tamaño_letra_ventana2)
    etiqueta_der.place(x=640, y=375)


    necesarios = [marco_ingreso_valores, tipo_tamaño_letra_ventana2, color_texto_ventana2]
    
    ############# ingresos_y de valores
    ingresos_x0 =IngresarEnCadena(*necesarios, 100, 60, 2)
    ingresos_y = IngresarEnCadena(*necesarios, 325, 60, 2)
    PlaceArray(ingresos_x0, 100, 60)
    PlaceArray(ingresos_y, 325, 60)
    ingresos_derivadas = [[IngresarEnCadena(*necesarios, 825, 60, 2), ctk.CTkLabel(marco_ingreso_valores, text = "f'(x)", font=tipo_tamaño_letra_ventana2), True]]
    PlaceArray(ingresos_derivadas[0][0], 825, 60)
    ingresos_derivadas[0][1].place(x=850, y=20)

    ingreso_interpolacion = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_interpolacion.place(x=600,y=60)
    d_x, d_y = 825, 60
    t_x, t_y = 850, 20
    for i in range(1, 4):
        n_derivada = ""
        for _ in range(i+1):
            n_derivada += "'" 
        ingresos_derivadas.append([IngresarEnCadena(*necesarios, d_x+(150*i), d_y, 2), ctk.CTkLabel(marco_ingreso_valores, text = f"f{n_derivada}(x)", font=tipo_tamaño_letra_ventana2), False])

    
    def agregar_ingresos_ys():
        global mostrar_y
        if len(ingresos_x0) > 7:
            return
        x_x0 = ingresos_x0[-1].winfo_x()
        y_x0 = ingresos_x0[-1].winfo_y()
        x_y0 = ingresos_y[-1].winfo_x()
        y_y0 = ingresos_y[-1].winfo_y()
        ingresos_x0.append(ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = necesarios[1],text_color=necesarios[2]))
        ingresos_x0[-1].place(x=x_x0,y=(y_x0 + 40))
        ingresos_y.append(ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = necesarios[1],text_color=necesarios[2]))
        if mostrar_y == True:
            ingresos_y[-1].place(x=x_y0,y=(y_y0 + 40))
        for i in range(len(ingresos_derivadas)):
            xi = ingresos_derivadas[i][0][-1].winfo_x()
            yi = ingresos_derivadas[i][0][-1].winfo_y()
            ingresos_derivadas[i][0].append(ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = necesarios[1],text_color=necesarios[2]))
            print(i,': ',ingresos_derivadas[i][2])
            if mostrar_y == True and ingresos_derivadas[i][2] == True:
                ingresos_derivadas[i][0][-1].place(x=xi, y=yi+40)

    def eliminar_ingresos_ys():
        if len(ingresos_x0) <= 2:
            return
        ingresos_x0[-1].place_forget()
        ingresos_x0.pop()
        ingresos_y[-1].delete(0, END) 
        ingresos_y[-1].place_forget()
        ingresos_y.pop()
        for i in range(len(ingresos_derivadas)):
            ingresos_derivadas[i][0][-1].place_forget()
            ingresos_derivadas[i][0][-1].delete(0, END)
            ingresos_derivadas[i][0].pop()

    def agregar_derivadas():
        global cantidad_derivadas
        global mostrar_y
   

        if cantidad_derivadas > 1:
            return
        etiqueta_numero_derivadas.configure(text=cantidad_derivadas+1)  
        if mostrar_y == False:
            ingresos_derivadas[cantidad_derivadas][2] = True
            cantidad_derivadas += 1 
            return

        d_x, d_y = 825, 60
        t_x, t_y = 850, 20
        for i in range(len(ingresos_derivadas)):
            PlaceArray(ingresos_derivadas[cantidad_derivadas][0], d_x+(150*cantidad_derivadas), d_y)
            ingresos_derivadas[cantidad_derivadas][1].place(x= t_x + (150*cantidad_derivadas), y=t_y)
            ingresos_derivadas[cantidad_derivadas][2] = True

        cantidad_derivadas += 1

    
    def eliminar_derivadas():
        global cantidad_derivadas
        if cantidad_derivadas <= 1:
            return
        UnPlaceArray(ingresos_derivadas[cantidad_derivadas-1][0])
        ingresos_derivadas[cantidad_derivadas-1][1].place_forget()
        ingresos_derivadas[cantidad_derivadas-1][2] = False
        cantidad_derivadas = cantidad_derivadas - 1
        etiqueta_numero_derivadas.configure(text=cantidad_derivadas)

    btn_x = 500
    btn_y = 400
    boton_eliminar = ctk.CTkButton(marco_ingreso_valores,text ="-",command=eliminar_ingresos_ys,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_eliminar.place(x=btn_x,y=btn_y)
    boton_agregar = ctk.CTkButton(marco_ingreso_valores,text ="+",command=agregar_ingresos_ys,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_agregar.place(x=btn_x+55,y=btn_y)

    derivada_boton_eliminar = ctk.CTkButton(marco_ingreso_valores,text ="-",command=eliminar_derivadas,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    derivada_boton_eliminar.place(x=btn_x+120,y=btn_y)
    derivada_boton_agregar = ctk.CTkButton(marco_ingreso_valores,text ="+",command=agregar_derivadas,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    derivada_boton_agregar.place(x=btn_x+175,y=btn_y)

    


    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)


    ########### Alternar entre funcion y valores de y 
    def Alternar_visibilidad():
        global toggle
        global mostrar_y
        global cantidad_derivadas
        if toggle == False:
            boton_funcion_valores.configure(text="Valores de y")
            etiqueta_ingreso_valores_y.configure(text='Funcion')
            toggle = True
            ingreso_funcion.place(x=325,y=60)
            mostrar_y = False

            for ingreso in ingresos_y:
                ingreso.delete(0, END)
                ingreso.place_forget()
            for i in range(len(ingresos_derivadas)):
                ingresos_derivadas[i][1].place_forget()
                for j in range(len(ingresos_y)):
                    ingresos_derivadas[i][0][j].delete(0, END)
                    ingresos_derivadas[i][0][j].place_forget()
        else:
            boton_funcion_valores.configure(text='Funcion')
            etiqueta_ingreso_valores_y.configure(text='Valores de y')
            toggle= False
            ingreso_funcion.delete(0, END)
            ingreso_funcion.place_forget()
            mostrar_y = True
            
            for i in range(0,len(ingresos_y)):        ################ CAMBIAR ENTRY POR BOTON
                ingresos_y[i].place(x=325,y=(60 + 30*i + 10*i))
            for i in range(len(ingresos_derivadas)):
                if ingresos_derivadas[i][2] == True:
                    ingresos_derivadas[i][1].place(x= 850 + (150*i), y=t_y)
                    for j in range(len(ingresos_y)):
                            ingresos_derivadas[i][0][j].place(x=825+(150*i),y=60+30*j + 10*j)


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
        valores_derivada = [[ingreso.get() for ingreso in ingresos_derivadas[i][0]] for i in range(len(ingresos_derivadas))]
        print('DERIVADAS',valores_derivada)
        interpolacion = ingreso_interpolacion.get()
        funcion = ingreso_funcion.get()
        derivadas = cantidad_derivadas
        x_llenados = False
        y_llenados = False
        derivada_llenado = False
        for i in range(len(valores_x)):
            print(valores_y[i])
            if (valores_x[i] == '' or numero_valido(valores_x[i]) == False):
                x_llenados = True
            if (valores_y[i] == '' or numero_valido(valores_y[i]) == False):
                y_llenados = True
                print('y_llenados de manera inccorrecta')
        for i in range(0,cantidad_derivadas):
            for j in range(len(valores_x)):
                if valores_derivada[i][j] == '' or numero_valido(valores_derivada[i][j]) == False:
                    derivada_llenado = True
        
            
   
# Limitar el número de sub-arrays a procesar
        valores_derivada = valores_derivada[:cantidad_derivadas]

# Convertir elementos a float y reemplazar '' con None
        derivadas_convertidas = [
        [float(elem) if elem.strip() != '' else None for elem in subarray]
        for subarray in valores_derivada        ]

# Eliminar sub-arrays vacíos (todos None)
        derivadas_convertidas = [subarray for subarray in derivadas_convertidas if any(elem is not None for elem in subarray)]

# Utiliza zip para intercalar los elementos y luego convierte el resultado en una lista
        valores_derivada = [list(x) for x in zip(*derivadas_convertidas)]
        
        print(valores_derivada, cantidad_derivadas) 

        #Si estan vacios todos
        if (x_llenados == True or interpolacion == '') or ((y_llenados == True or derivada_llenado == True) and funcion == '') :
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos de forma correcta")
        else:
             
            if numero_valido(valores_x[0]) and numero_valido(valores_x[1]) and numero_valido(interpolacion):

                if funcion == '':    
                    valores_y = [float(valores) for valores in valores_y]
                    funcion = None
                    derivadas = None
                    
                else:
                    booleano, funcion = Validar_y_Reemplazar_funcion(funcion)
                    valores_y = None
                    valores_derivada = None
                    if booleano == False:
                        messagebox.showerror('ERROR', message='Ingrese una funcion valida')
                        return

                print("DERIVADAAAAAAS", derivadas)
                valores_x = [float(valor) for valor in valores_x]
                print(valores_derivada)
                interpolacion = float(interpolacion)

                muestra_valores = ctk.CTkLabel(marco_muestra_valores,font= ("Currier",15,"bold"), justify= 'left', anchor='w', wraplength=1000)
                
                Px, valor_aprox, new_y = hermite(valores_x, valores_y, funcion, interpolacion, cantidad_derivadas, valores_derivada)
#def hermite(x_array, y_array=None, ecuacion=None,inter_point=None, derivates=None, derivates_array = []):
                result = 'Resultado de la interpolacion:\n\n'
                for i, (val_x, val_y) in enumerate(zip(valores_x, new_y), start=1):
                    result += f"x{i} = {val_x}, y{i} = {val_y}\n"

                if valores_y == None:
                    muestra_valores.configure(text=result+f'evaluados en f(x) = {funcion}\n\n Con un polinomio interpolador de Px = {Px} con un valor aproximado de {valor_aprox}')
                else:
                    muestra_valores.configure(text=result+f'\nCon un polinomio interpolador de Px = {Px} con un valor aproximado de {valor_aprox}')

                print(mostrar)
                if mostrar == True:
                    print(mostrar)
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
                [[ingresos[0][i].delete(0, END) for ingresos in ingresos_derivadas] for i in range(len(ingresos_x0))]

            else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Asegurate de ingresar valores numericos en los campos correspondientes")
            
    
    y_pos = 400
   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=y_pos)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=y_pos)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=y_pos)
    

def Volver(ventana2,ventana):
    cantidad_derivadas = 1
    print('volver', cantidad_derivadas)
    ventana2.destroy()
    ventana.deiconify()


def IngresarEnCadena(marco, fuente, color, x, y, cantidad):
    ingresos = []
    for i in range(0, cantidad):
        ingresos.append(ctk.CTkEntry(marco,width=100,height=30,corner_radius=10,font = fuente,text_color=color))
    return ingresos

def PlaceArray(array, x, y):
    cantidad = len(array)
    for i in range(cantidad):
        array[i].place(x=x,y=(y + 30*i + 10*i))
def UnPlaceArray(array):
    cantidad = len(array)
    for i in range(cantidad):
        array[i].place_forget()
        array[i].delete(0, END)


def Limpiar():
    global marco_muestra_valores
    global canvas
    global boton_resolver,boton_limpiar 

    boton_resolver.configure(state=NORMAL)
    boton_limpiar.configure(state=DISABLED)

    # Iterar sobre los widgets y destruirlos uno por uno
    for widget in marco_muestra_valores.winfo_children():
        widget.destroy()


