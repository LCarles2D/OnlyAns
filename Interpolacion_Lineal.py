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



def interpolacion_Lineal(xk,yk, inter_point, ecuacion = None):

    
    x = sp.symbols("x")
    if ecuacion != None:
        yk = [ecuacion.subs(x, xi).evalf() for xi in xk]

  
    fx = yk
    
    Px = ((fx[1] - fx[0])/(xk[1] - xk[0])) * (x - xk[0]) + fx[0]
    Px = sp.simplify(Px)

    valor_aprox = Px.subs(x, inter_point).evalf()
    return Px, valor_aprox

color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2



def Ventana_Interpolacion_Lineal(frame, ventana2, ventana):
    global marco_muestra_valores
    global canvas

    global boton_limpiar,boton_resolver
    global tipo_tamaño_letra_ventana2,color_fondo_boton_ventana2,color_fondo_boton_ventana2
    global color_boton_pasar_mouse_ventana2,ancho_borde_ventana2,color_borde_ventana2
    global boton_limpiar,boton_resolver

    marco_height = 300
    marco_ingreso_valores = ctk.CTkFrame(frame, width=0, height=marco_height, corner_radius=10)
    marco_ingreso_valores.pack(fill="x", expand=False, padx=10, pady=0)
    marco_ingreso_valores.grid_propagate(False)

    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=600,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)

    etiqueta_ingreso_valor_inicial = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese los valores de x",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_inicial.place(x=40,y=20)

    etiqueta_ingreso_valor_final = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese los valores de y",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_final.place(x=320,y=20)

    etiqueta_ingreso_valor_real = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el punto de interpolacion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_real.place(x=565,y=20)

    etiqueta_ingreso_valor = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor real",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor.place(x=875,y=20)

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=1140,y=20)

    necesarios = [marco_ingreso_valores, tipo_tamaño_letra_ventana2, color_texto_ventana2]

    ingresos_x0 =IngresarEnCadena(*necesarios, 100, 60, 2)
    ingresos_x1 = IngresarEnCadena(*necesarios, 325, 60, 2)
    



    ingreso_cifras_significativas = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_cifras_significativas.place(x=600,y=60)

    ingreso_valor_real = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_real.place(x=880,y=60)

    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=1100,y=60)

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

    def Validacion():
        global boton_limpiar,boton_resolver,mostrar
        #Se valida el ingreso de datos
        valor_inicial = ingreso_valor_inicial.get()
        valor_final = ingreso_valor_final.get()
        cifras_significativas = ingreso_cifras_significativas.get()
        valor_real = ingreso_valor_real.get()
        funcion = ingreso_funcion.get()

        #Si estan vacios todos
        if valor_inicial == "" and valor_final == "" and cifras_significativas == "" and valor_real == "" and funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
        #SI uno o varios estan vacios
        elif valor_inicial == "" or valor_final == "" or cifras_significativas == "" or valor_real == "" or funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
            #si todos estan llenados   
        else:
            
            if numero_valido(valor_inicial) and numero_valido(valor_final) and numero_valido(cifras_significativas) and numero_valido(valor_real) :
                if Validacion_Funcion(funcion) == True and Convertir_Funcion(funcion) == True:

                    valor_inicial = float(valor_inicial)
                    valor_final = float(valor_final)
                    cifras_significativas = float(cifras_significativas)
                    valor_real = float(valor_real)

                    muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
                    

                    muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
                    

                    muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
                    

                    muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)
                    

                    Metodo_Biseccion(funcion,valor_inicial,valor_final,cifras_significativas,valor_real,muestra_valores,muestra_tabla,muestra_raiz,muestra_grafica)

                    if mostrar == True:
                        muestra_valores.place(x=10,y=20)
                        muestra_tabla.place(x=0,y=130)
                        muestra_raiz.place(x=10,y=400)
                        muestra_grafica.place(x=700,y=20)



                    #Se desactiva el botón de Resolver
                    boton_resolver.configure(state=DISABLED)
                    #Se activa el botón de Limpiar
                    boton_limpiar.configure(state=NORMAL)
                    
                    
                    #Se limpia los entry cuando ya se resulve por el metodo
                    ingreso_valor_inicial.delete(0, END)
                    ingreso_valor_final.delete(0, END)
                    ingreso_cifras_significativas.delete(0, END)
                    ingreso_valor_real.delete(0, END)
                    ingreso_funcion.delete(0, END)

                else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Ingrese la funcion en terminos 'x' y sin dejar espacios ")
                    
            else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Solo debe ingresar valores numericos en los 4 primeros campos")
            
    
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
x_array = [2,3]
y_array = [67, 91]

x = sp.symbols("x")
Px, valor =interpolacion_Lineal(x_array, None, -1, sp.log(x))
print(Px, ' ', valor)'''
