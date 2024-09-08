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

mostrar = False

###################### SIMPSON SIMPLE ########################
def Simpson(a, b, fx):
    x = sp.symbols('x')
    c = (a + b)/2
    # Evaluamos los 3 puntos
    fa = fx.subs(x, a).evalf()
    fb = fx.subs(x, b).evalf()
    fc = fx.subs(x, c).evalf()

    valor = (b - a)*((fa + 4*fc + fb)/6)
    return valor



def Simpson_adaptativo(a, b, fx, tolerancia):
    global mostrar
    c  = (a + b)/2
    S  = Simpson(a, b, fx)
    S1 = Simpson(a, c, fx)
    S2 = Simpson(c, b, fx)

    if abs((S1 + S2 - S)/15) < tolerancia:
        return (16*(S1 + S2 - S)/15)
    else:
        nodo_superior = Simpson_adaptativo(a, c, fx, tolerancia)
        nodo_inferior  = Simpson_adaptativo(c, b, fx, tolerancia)
        
    return nodo_superior + nodo_inferior

color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2
toggle = False



def Ventana_Simpson_Adaptativo(frame, ventana2, ventana):
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
    etiqueta_ingreso_valores_x = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese los limites",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valores_x.place(x=40,y=20)


    etiqueta_ingreso_interpolacion = ctk.CTkLabel(marco_ingreso_valores,text = "Tolerancia",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_interpolacion.place(x=600,y=20)
    
    etiqueta_ingreso_valores_y = ctk.CTkLabel(marco_ingreso_valores,text = "funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valores_y.place(x=320,y=20)

    etiqueta_limite_a = ctk.CTkLabel(marco_ingreso_valores,text = "a",font=tipo_tamaño_letra_ventana2)
    etiqueta_limite_a.place(x=80, y=60)

    etiqueta_limite_b = ctk.CTkLabel(marco_ingreso_valores,text = "b",font=tipo_tamaño_letra_ventana2)
    etiqueta_limite_b.place(x=80, y=100)

    necesarios = [marco_ingreso_valores, tipo_tamaño_letra_ventana2, color_texto_ventana2]
    
    ############# Entrada de valores
    ingresos_x0 =IngresarEnCadena(*necesarios, 100, 60, 2)
    

    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=325,y=60)
    ingreso_interpolacion = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_interpolacion.place(x=600,y=60)



  
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
        Ea = ingreso_interpolacion.get()
        funcion = ingreso_funcion.get()

        #Si estan vacios todos
        if (valores_x[0] == '' or valores_x[1] == '' or Ea == '' or funcion == '') :
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos de forma correcta")
        else:
            
            if numero_valido(valores_x[0]) and numero_valido(valores_x[1]) and numero_valido(Ea):

                if funcion == '':    
                    valores_y = [float(valores) for valores in valores_y]
                    funcion = None
                else:
                    print('La funcion', funcion)
                    booleano, funcion = Validar_y_Reemplazar_funcion(funcion)
                    print(booleano, funcion)
                    valores_y = None
                    if booleano == False:
                        messagebox.showerror("¡ ERROR CRITICO !",message="Ingrese una  funcion valida")
                        return
                valores_x = [float(valor) for valor in valores_x]
                Ea = float(Ea)
                if Ea <= 0:
                    messagebox.showerror("¡ ERROR CRITICO !",message="La tolerancia debe de ser un valor mayor a 0 ")
                    return

                if valores_x[0] > valores_x[1]:
                        messagebox.showerror("¡ ERROR CRITICO !",message="El valor de 'b' debe de ser mayor que 'a' ")
                        return

                muestra_valores = ctk.CTkLabel(marco_muestra_valores,font= ("Currier",15,"bold"), justify= 'left', anchor='w')
                
                valor = Simpson_adaptativo(valores_x[0],valores_x[1],funcion, Ea)

                muestra_valores.configure(text=f'Funcion:{funcion}\na = {valores_x[0]}\nb = {valores_x[1]}\n\nEl valor aproximado de la integracion por el metodo de Simpson_adaptativo es {valor}')
                muestra_valores.place(x=10,y=20)

                #Se desactiva el botón de Resolver
                boton_resolver.configure(state=DISABLED)
                #Se activa el botón de Limpiar
                boton_limpiar.configure(state=NORMAL)
                
                
                #Se limpia los entry cuando ya se resulve por el metodo
                [ingresos.delete(0, END) for ingresos in ingresos_x0]
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





#x = sp.symbols('x')
#print('El valor aproximado de la integracion por el metodo de Simpson_adaptativo es',Simpson_adaptativo(1,2,(x**3)/(1+x**(1/2)), 10**(-3)))

