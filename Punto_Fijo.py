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

def Grafico(funcion,X_r):

    x = sp.symbols("x")
   # Definir el rango de valores de x para graficar
    valores_x = np.linspace(X_r - 5, X_r + 5, 1000)
    
    # Convertir la expresión simbólica en una función numérica
    funcion_numerica = sp.lambdify(x, funcion)
    
    # Calcular los valores de y correspondientes
    valores_y = funcion_numerica(valores_x)

    # Crear la figura y el eje
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Graficar la función y la raíz encontrada por el método de la secante
    ax.plot(valores_x, valores_y, label=str(funcion), color="blue")
    ax.scatter(X_r, funcion_numerica(X_r), color="red", label=f"Raíz: {X_r}")
    
    # Agregar líneas de referencia y etiquetas
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Grafico')
    ax.legend()
    ax.grid(True)

    return fig




def Punto_Fijo(funcion,despejo_x,X_i,cifras_significativas,muestra_valores,muestra_tabla,muestra_raiz,muestra_grafica):
    global mostrar
    valores_mostrar = ""
    tabla_resultados = ""
    valor_raiz = ""
    mensaje_ = ""

    x=sp.symbols("x")
    derivada_despejo_x = sp.diff(despejo_x,x) #derivdo lo despejado
    
    deriv = sp.lambdify(x,derivada_despejo_x) #Preparo para evaluar en la derivada
    resultado_derivada = deriv(X_i) #Evaluo en la derivada
    g=sp.lambdify(x,despejo_x) # se va a evaluar en la funcion despejada
    f=sp.lambdify(x,funcion)  #se va a evaluar la funcion

    try:

        if resultado_derivada < 1: #Convergue

            i=1 # iniciar el contador
            Ea=0 # iniciar la variable de error
            valor_anterior=0 # iniciar la variable de x anterior
            Es=(0.5*10**(2-cifras_significativas))
            valores_mostrar = f"Funcion : {funcion}\n\nValor inicial : {X_i}\tfuncion x = : {despejo_x}\n\nCifras significativas : {cifras_significativas}\tNivel de tolerancia : {Es} %\n"
        #imprimir encabezado de la tabla
            df=pd.DataFrame(columns=["Iteracion","X","g(x)","Ea"])
            while True:
                deriv=g(X_i)
                Ea=abs(((deriv-X_i)/deriv)*100) #encontramos el error aproximado
                df.loc[i-1]=[i,X_i,deriv,Ea]
                if Ea<Es: #si el error aproximado es menor que el nivel de tolerancia
                    break
                
                #se hacen los cambios
                X_i=deriv
                i+=1

            tabla_resultados = df.to_string()+ "\n"
            valor_raiz = f"\nEl valor de la raiz es {(X_i)} con un error de {(Ea)} % en la iteracion {i}"
            
            muestra_valores.configure(text =valores_mostrar)
            muestra_tabla.configure(text  =tabla_resultados)
            muestra_raiz.configure(text =valor_raiz)

            fig = Grafico(funcion,X_i)

            canvas = FigureCanvasTkAgg(fig, master=muestra_grafica)
            canvas.draw()
            widget_grafico = canvas.get_tk_widget()
            widget_grafico.pack(fill="both", expand=True)

            mostrar = True

        else:
            mensaje_  = "Diverge, de modo que las iteraciones tenderan a alejarse de la solucion"
            messagebox.showerror("¡ ERROR CRITICO !",message=mensaje_)

            mostrar = False
    except ZeroDivisionError:
        messagebox.showerror("¡ ERROR CRITICO !","Se ha producido una división por cero")
        mostrar = False






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


def Ventana_Punto_Fijo(frame,ventana2,ventana):

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

    etiqueta_ingreso_valor_inicial = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor inicial",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_inicial.place(x=40,y=20)

    #etiqueta_ingreso_valor_final = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor final",font=tipo_tamaño_letra_ventana2)
    #etiqueta_ingreso_valor_final.place(x=320,y=20)

    etiqueta_ingreso_cifras_significativas = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese las cifras significativas",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_cifras_significativas.place(x=365,y=20)

    etiqueta_ingreso_valor_real = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_real.place(x=725,y=20)

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion despejada x\nx =",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=1000,y=20)


    ingreso_valor_inicial = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_inicial.place(x=50,y=60)

    #ingreso_valor_final  = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    #ingreso_valor_final.place(x=325,y=60)

    ingreso_cifras_significativas = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_cifras_significativas.place(x=400,y=60)

    #ingreso la funcion y =
    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=675,y=60)

    #ingreso la funcion g(x)
    ingreso_g_x= ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_g_x.place(x=1000,y=60)

    def numero_valido(texto):
        return re.match(r"^-?\d*\.?\d*$", texto) is not None

    def Validar_y_Reemplazar_funcion(funcion_str):
        x = sp.symbols('x')
        
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
        valor_inicial = ingreso_valor_inicial.get()
        #valor_final = ingreso_valor_final.get()
        cifras_significativas = ingreso_cifras_significativas.get()
        funcion = ingreso_funcion.get()
        g_x = ingreso_g_x.get()
        

        #Si estan vacios todos
        if valor_inicial == "" and  cifras_significativas == "" and g_x == "" and funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
        #SI uno o varios estan vacios
        elif valor_inicial == ""  or cifras_significativas == "" or g_x == "" or funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
            #si todos estan llenados   
        else:
            valida_y,funcion_str = Validar_y_Reemplazar_funcion(funcion)
            valida_g_x,funcion_str_g_x = Validar_y_Reemplazar_funcion(g_x)
            
            
            if numero_valido(valor_inicial)  and numero_valido(cifras_significativas)  :
                if valida_y == True and valida_g_x == True:

                    valor_inicial = float(valor_inicial)
                    cifras_significativas = float(cifras_significativas)
                    g_x =funcion_str_g_x
                    funcion = funcion_str


                    muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")
                    
                    muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")
                    
                    muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2,anchor="w", justify="left")
                    
                    muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)
                    

                    Punto_Fijo(funcion,g_x,valor_inicial,cifras_significativas,muestra_valores,muestra_tabla,muestra_raiz,muestra_grafica)

                    if mostrar == True:
                        muestra_valores.place(x=10,y=20)
                        muestra_tabla.place(x=10,y=130)
                        muestra_raiz.place(x=10,y=400)
                        muestra_grafica.place(x=700,y=20)

                        #Se desactiva el botón de Resolver
                        boton_resolver.configure(state=DISABLED)
                        #Se activa el botón de Limpiar
                        boton_limpiar.configure(state=NORMAL)
                    
                    
                    #Se limpia los entry cuando ya se resulve por el metodo
                    ingreso_valor_inicial.delete(0, END)
                    #ingreso_valor_final.delete(0, END)
                    ingreso_cifras_significativas.delete(0, END)
                    ingreso_g_x.delete(0, END)
                    ingreso_funcion.delete(0, END)


                    

                else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Error al ingresar las funciones")
                    
            else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Solo debe ingresar valores numericos en los 4 primeros campos")
            

    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=125)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=125)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=125)



