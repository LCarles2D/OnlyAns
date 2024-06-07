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



def Metodo_Secante(funcion,X_i,X_u,cifras_significativas,muestra_valores,muestra_tabla,muestra_raiz,muestra_grafica):
    global mostrar
    valores_mostrar = ""
    tabla_resultados = ""
    valor_raiz = ""
    mensaje_ = ""

    X_r=0 
    x=sp.symbols("x") #declaro la varaible simbolica
    f=sp.lambdify(x,funcion)  #se va a evaluar la funcion


    i=1 # iniciar el contador
    Ea=0 # iniciar la variable de error
    valor_anterior=0 # iniciar la variable de x anterior
    Es=(0.5*10**(2-cifras_significativas))

    if X_i == X_u:
        mensaje_  = "Los valores iniciales no pueden ser iguales"
        messagebox.showerror("¡ ERROR CRITICO !",message=mensaje_)
        mostrar = False
        return 
        

    valores_mostrar = f"Funcion : {funcion}\n\nValor inicial : {X_i}\tValor final : {X_u}\n\nCifras significativas : {cifras_significativas}\tNivel de tolerancia : {Es} %\n"
    #imprimir encabezado de la tabla
    df=pd.DataFrame(columns=["Iteracion","X_i-1","X_i","f(X_i)","f(X_i)","X_i+1","Ea"])
    while True:
        try:
            X_r=X_u-((f(X_u)*(X_i-X_u))/(f(X_i)-f(X_u)))# se hace la primera aproximacion
        except ZeroDivisionError:
            mensaje_ = "Se produjo una división por cero durante los cálculos"
            messagebox.showerror("¡ ERROR CRITICO !", message=mensaje_)
            mostrar = False
            return
        
        Ea=abs(((X_r-valor_anterior)/X_r)*100)  #encontramos el error aproximado
        df.loc[i-1]=[i,X_i,X_u,f(X_i),f(X_u),X_r,Ea]
        if Ea<Es: #si el error aproximado es menor que el nivel de tolerancia
            break
        
        #se hacen los cambios
        valor_anterior=X_r
        X_i=X_u 
        X_u=X_r
        i+=1

    tabla_resultados = df.to_string()+ "\n"
    valor_raiz = f"\nEl valor de la raiz es {(X_r)} con un error de {(Ea)} % en la iteracion {i}"
    
    muestra_valores.configure(text =valores_mostrar)
    muestra_tabla.configure(text  =tabla_resultados)
    muestra_raiz.configure(text =valor_raiz)

    fig = Grafico(funcion,X_r)

    canvas = FigureCanvasTkAgg(fig, master=muestra_grafica)
    canvas.draw()
    widget_grafico = canvas.get_tk_widget()
    widget_grafico.pack(fill="both", expand=True)

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




def Ventana_Secante(frame,ventana2,ventana):

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

    etiqueta_ingreso_valor_final = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor final",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_valor_final.place(x=320,y=20)

    etiqueta_ingreso_cifras_significativas = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese las cifras significativas",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_cifras_significativas.place(x=665,y=20)

    #etiqueta_ingreso_valor_real = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese el valor real",font=tipo_tamaño_letra_ventana2)
    #etiqueta_ingreso_valor_real.place(x=875,y=20)

    etiqueta_ingreso_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese la funcion",font=tipo_tamaño_letra_ventana2)
    etiqueta_ingreso_funcion.place(x=1050,y=20)

    ingreso_valor_inicial = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_inicial.place(x=50,y=60)

    ingreso_valor_final  = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_valor_final.place(x=325,y=60)

    ingreso_cifras_significativas = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_cifras_significativas.place(x=700,y=60)

    #ingreso_valor_real = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    #ingreso_valor_real.place(x=880,y=60)

    ingreso_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_funcion.place(x=1000,y=60)

    
    def Validacion():
        global boton_limpiar,boton_resolver,mostrar
        #Se valida el ingreso de datos
        valor_inicial = ingreso_valor_inicial.get()
        valor_final = ingreso_valor_final.get()
        cifras_significativas = ingreso_cifras_significativas.get()
        #valor_real = ingreso_valor_real.get()
        funcion = ingreso_funcion.get()

        #Si estan vacios todos
        if valor_inicial == "" and valor_final == "" and cifras_significativas == ""  and funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
        #SI uno o varios estan vacios
        elif valor_inicial == "" or valor_final == "" or cifras_significativas == ""  or funcion == "":
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos")
            #si todos estan llenados   
        else:
            def Validacion_Funcion(funcion):
                patron = r'^(\s*\d+|\+|\-|\*{1,2}|/|\(|\)|x|e|sin\(x\)|cos\(x\)|tan\(x\)|asin\(x\)|acos\(x\)|atan\(x\)|log\(x\)|ln\(x\)|sqrt\(x\)|sqrt\d*\(x\))*\s*$'
                return re.match(patron, funcion) is not None
            
            def numero_valido(texto):
                return re.match(r"^-?\d*\.?\d*$", texto) is not None
            
            if numero_valido(valor_inicial) and numero_valido(valor_final) and numero_valido(cifras_significativas)  :
                if Validacion_Funcion(funcion) == True:
                    valor_inicial = float(valor_inicial)
                    valor_final = float(valor_final)
                    cifras_significativas = float(cifras_significativas)
                    #valor_real = float(valor_real)

                    muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
                    

                    muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
                    

                    muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
                    

                    muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)
                    

                    Metodo_Secante(funcion,valor_inicial,valor_final,cifras_significativas,muestra_valores,muestra_tabla,muestra_raiz,muestra_grafica)

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
                    ingreso_valor_final.delete(0, END)
                    ingreso_cifras_significativas.delete(0, END)
                    #ingreso_valor_real.delete(0, END)
                    ingreso_funcion.delete(0, END)

                else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Ingrese la funcion en terminos 'x' y sin dejar espacios ")
                    
            else:
                    messagebox.showerror("¡ ERROR CRITICO !",message="Solo debe ingresar valores numericos en los 4 primeros campos")
            
    
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=125)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=125)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=125)


