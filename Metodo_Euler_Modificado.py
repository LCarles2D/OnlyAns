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
import tkinter.simpledialog as simpledialog

def Grafico(funcion,X_r):

    x, y = sp.symbols("x y")  # Agregar y como símbolo

    # Definir el rango de valores de x para graficar
    valores_x = np.linspace(X_r - 5, X_r + 5, 1000)

    # Convertir la expresión simbólica en una función numérica
    funcion_numerica = sp.lambdify((x, y), funcion)

    # Calcular los valores de y correspondientes
    valores_y = funcion_numerica(valores_x, 0)  # Pasa y=0 para graficar en función de x solamente

    # Crear la figura y el eje
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Graficar la función y la raíz encontrada por el método de la secante
    ax.plot(valores_x, valores_y, label=str(funcion), color="blue")
    ax.scatter(X_r, funcion_numerica(X_r, 0), color="red", label=f"Raíz: {X_r}")

    # Agregar líneas de referencia y etiquetas
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Gráfico')
    ax.legend()
    ax.grid(True)
    return fig

def Metodo_Euler_Mejorado(funcion,x0,y0,h,valor_final,muestra_valores,muestra_tabla,muestra_raiz,muestra_grafica):
    global mostrar
    x = sp.symbols("x")
    y = sp.symbols("y")

    f = sp.lambdify((x, y), funcion)


    valores_mostrar = f"f(x,y) = {funcion}\nX0 = {x0}\t\tY0 = {y0}\nh = {h}\nX final = {valor_final}"
    i = 1

    df=pd.DataFrame(columns=["n","Xn","Yn"])

    while x0 < valor_final:
        x1 = x0 + h
        y1 = y0 + h * f(x0, y0)
        formula = y0 + h *(( (f(x0,y0)) + (f(x1,y1)) )/ (2) )
        
        df.loc[i-1] = [i,x0, y0]
        y0 = formula
        x0 = x1

        
        i+=1

    df.loc[i-1] = [i,x0, y0]


    respuesta = f"Respuesta //  y({valor_final}) = {formula}"

    fig = Grafico(funcion,valor_final)

    canvas = FigureCanvasTkAgg(fig, master=muestra_grafica)
    canvas.draw()
    widget_grafico = canvas.get_tk_widget()
    widget_grafico.pack(fill="both", expand=True)

    tabla_resultados = df.to_string(index=False,col_space=10) + "\n"
    muestra_valores.configure(text =valores_mostrar)
    muestra_tabla.configure(text  =tabla_resultados)
    muestra_raiz.configure(text =respuesta)

    mostrar = True


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

def Ventana_Metodo_Euler_Modificado(frame,ventana2,ventana):
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

    etiqueta_ingreso_valor_inicial_x = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese x0",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_inicial_x.place(x=40,y=20)

    etiqueta_ingreso_valor_inicial_y = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese y0",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_inicial_y.place(x=320,y=20)

    etiqueta_ingreso_valor_h = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor de h",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_h.place(x=565,y=20)

    etiqueta_ingreso_valor_final = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor final",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_final.place(x=875,y=20)

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=1140,y=20)

    
    ingreso_valor_inicial_x = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_inicial_x.place(x=50,y=60)

    ingreso_valor_inicial_y  = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_inicial_y.place(x=325,y=60)

    ingreso_valor_h = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_h.place(x=600,y=60)

    ingreso_valor_final = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_final.place(x=880,y=60)

    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=1100,y=60)

    def numero_valido(texto):
        return re.match(r"^-?\d*\.?\d*$", texto) is not None

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
                return True, funcion_str
            else:
                messagebox.showerror("¡ ERROR CRITICO !",message="La función contiene variables no permitidas.")
        except Exception as e:
            #messagebox.showerror("Error de validación", f"La función ingresada no es válida")
            return False, None
        
    def Validacion():
        global boton_limpiar,boton_resolver,mostrar
        #Se valida el ingreso de datos
        x0 = ingreso_valor_inicial_x.get()
        y0 = ingreso_valor_inicial_y.get()
        h = ingreso_valor_h.get()
        valor_final = ingreso_valor_final.get()
        funcion = ingreso_funcion.get()

        #Si estan vacios todos
        if x0 == "" and y0 == "" and h == "" and valor_final == "" and funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
        #SI uno o varios estan vacios
        elif x0 == "" or y0 == "" or h == "" or valor_final == "" or funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
            #si todos estan llenados   
        else:

            valida,funcion_str = Validar_y_Reemplazar_funcion(funcion)
            if numero_valido(x0) and numero_valido(y0) and numero_valido(h) and numero_valido(valor_final) :
                if valida == True :

                    x0 = float(x0)
                    y0 = float(y0)
                    h = float(h)
                    valor_final = float(valor_final)
                    funcion = funcion_str

                    muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")
                    

                    muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")
                    

                    muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")
                    

                    muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

                    Metodo_Euler_Mejorado(funcion,x0,y0,h,valor_final,muestra_valores,muestra_tabla,muestra_raiz,muestra_grafica)
                    
                    

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
                    ingreso_valor_inicial_x .delete(0, END)
                    ingreso_valor_inicial_y.delete(0, END)
                    ingreso_valor_h.delete(0, END)
                    ingreso_valor_final.delete(0, END)
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