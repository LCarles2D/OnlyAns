
import cmath
import math
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
import funciones_herramientas 
from funciones_herramientas import *


def verificador_error(Error):
    if not (Error == None or Error == ""):
        messagebox.showerror("¡ ERROR CRITICO !", message = Error)
    else:
        pass

generales_Ferrari = funciones_herramientas.Transportador()
raices_reales_ferrari = funciones_herramientas.Transportador()
raices_imaginarias_ferrari = funciones_herramientas.Transportador()


def Metodo_Ferrari(expresion):
    print("entra al metodo")
    Mensaje, Error = "", ""
    raices_reales, raices_imaginarias = [], []
    
    #24*x**4 - 3*x**3 + 2*x**2 + x - 2 = 0
    funcion, dicc, Error = funciones_herramientas.validar_funcion(expresion)
    verificador_error(Error)
    print("funcion: ",funcion)
    coeficientes = []
    coeficientes, Error = funciones_herramientas.obtener_coeficientes(expresion)
    verificador_error(Error)

    print("coeficientes: ", coeficientes)
    grado, Error = funciones_herramientas.obtener_grado(expresion, 4)
    verificador_error(Error)
    #print(grado, "type: ",type(grado))
    f, a, b, c, d = coeficientes
    print(f"f, a, b, c, d : {f}, {a} ,{b}, {c}, {d}")
    
    try:
        f, a, b, c, d = coeficientes
    except ValueError as Er:
        Error = "Ha ocurrido un problema al asignar los coeficientes"
        verificador_error(Error)

    #1. calculamos p, q, R
    P = ((8*b)-(3*a**2))/8
    Q = ((8*c) - (4*a*b) + (a**3))/8
    R = ((256*d) - (64*a*c) + (16*a**2*b) - (3*a**4))/256
    
    #2. Reescribimos  la expresion a una cubica
    U = sp.symbols("U")
    expresion_v = U**3 - P/2*U**2 - R*U + ((4*P*R) - (Q**2))/8
    funcion_v = sp.simplify(expresion_v)
    polinomio_u = sp.Poly(expresion_v)
    print("polinomio: ", polinomio_u)
    coeficientes_u, Error = funciones_herramientas.obtener_coeficientes(expresion_v)
    verificador_error(Error)


    """REVISAR
    (U**3) - ((-11/8/2)*U**2) - (-275/256*U) + (((4*-11/8*-275/256) - (5/8**2))/8) type:  <class 'str'>
    U**3 + 11*U**2/16 + 275*U/256 + 2985/4096 type:  <class 'sympy.core.add.Add'>
    (U**3 + 11*U**2/16 + 275*U/256 + 2985/4096,) type:  <class 'tuple'>"""

    print("coeficiente cant: ",len(coeficientes_u))    
    fU, aU, bU, cU = coeficientes_u

    try:
        fU, aU, bU, cU = coeficientes_u
    except ValueError as Er:
        Error = "Ha ocurrido un problema al asignar los coeficientes"
        verificador_error(Error)
    print(f"fu, au, bu, cu : {fU}, {aU} ,{bU}, {cU}")

    #3. realizamos el metodo de tartaglia para encontrar U
        #calculamos la p y q
    p_t = (3*bU - aU**2)/3 
    q_t = (2*aU**3 - 9*aU*bU + 27*cU)/27

        #calculamos el discriminante
    D = (q_t/2)**2 + (p_t/3)**3
    U_= None
    
    #metodo tartaglia
    if D == 0: #si el discriminante es igual a cero
        p_q = p_t*q_t #multiplico p * q
        if p_t == 0 and q_t == 0: #Si p y q son iguales a cero
            raiz_triple =- (aU/3) # tiene una raiz triple

            raiz_triple, Error = funciones_herramientas.convertir_float(raiz_triple)
            U_ = raiz_triple

            Mensaje = f"Metodo Ferrari:\nExpresion: {expresion},  P = {P} , Q = {Q} , R = {R}\n"
            Mensaje = Mensaje + f"Elementos metodo ferrari: p = {p_t} , q = {q_t}\n"
            Mensaje = Mensaje + f"Discriminate Δ: {D}, con un valor de U: {U}\n"


        elif p_t*q_t != 0: #Si la multiplicacion de p * q es diferente de cero
            raiz_doble = -((3*q_t)/(2*p_t)) - (aU/3)#Se encuentra la raiz doble
            raiz = -((4*p_t**2)/(9*q_t)) - (aU/3) 
            U_ = raiz
            
            raiz_doble = funciones_herramientas.convertir_float(raiz_doble)
            raiz = funciones_herramientas.convertir_float(raiz)

            Mensaje = f"Metodo Ferrari:\nExpresion: {expresion},  P = {P} , Q = {Q} , R = {R}\n"
            Mensaje = Mensaje + f"Elementos metodo ferrari: p = {p_t} , q = {q_t}\n"
            Mensaje = Mensaje + f"Discriminate Δ: {D}, con un valor de U: {U}\n"

    elif D > 0: #Si el discriminante es mayor a cero
        #Calculamos U y V
        U = math.cbrt((-q_t/2) + math.sqrt(D))#Con la raiz cubica a todo
        V = math.cbrt((-q_t/2) - math.sqrt(D)) #con la raiz cubica a todo
        U_ = U
        print(f"Δ = {D}")
        print(f"U = {U_}")
        
        #Calculamos la raiz real
        raiz_real = (U + V) - (aU/3)
        raiz_real = funciones_herramientas.convertir_float(raiz_real)

        #Calculamos la raiz imaginaria
        raiz_imaginaria_uno =  (-((U + V ) / 2 )) - (aU/3) + complex( (((math.sqrt(3))/2) * (U - V)) )# i 
        raiz_imaginaria_dos =  (-((U + V ) / 2 )) - (aU/3) - complex( (((math.sqrt(3))/2) * (U - V)) )# i 

        Mensaje = f"Metodo Ferrari:\nExpresion: {expresion},  P = {P} , Q = {Q} , R = {R}\n"
        Mensaje = Mensaje + f"Elementos metodo ferrari: p = {p_t} , q = {q_t}\n"
        Mensaje = Mensaje + f"Discriminate Δ: {D}, con un valor de U: {U}\n"

    elif D < 0: #Si el discriminante es menor a cero
        #Calculamos el angulo Cos θ
        angulo = math.acos( (-(q_t/2)) / (math.sqrt((-((p_t/3)**3)))) )
        #Utilizamos un valor de K=0,1,2
        K = 0
        if 0 < angulo < math.pi:
            raiz = 2 * math.sqrt(-(p_t/3)) * math.cos( (angulo + 2*K*math.pi) / (3) ) - (aU/3) # Se calcula la raiz
            U_ = raiz
            
            raiz = funciones_herramientas.convertir_float(raiz)
            
            Mensaje = f"Metodo Ferrari:\nExpresion: {expresion},  P = {P} , Q = {Q} , R = {R}\n"
            Mensaje = Mensaje + f"Elementos metodo ferrari: p = {p_t} , q = {q_t}\n"
            Mensaje = Mensaje + f"Discriminate Δ: {D}, con un valor de U: {U} , con un θ = {angulo}\n"

            print(f"Δ = {D}")
            print(f"θ = {angulo}")
            print(f"U = {U_}")
        else:
            Error = "Error: M_Ferrari: D < 0: calculo raiz"

    #terminar metodo Ferrari: se necesita U_, P, Q, a:
    VV, Error = funciones_herramientas.calcular_raiz_cuadrada(2*U_-P)
    verificador_error(Error)

    WW = -(Q/2*VV)

    Mensaje = Mensaje + f"Con V = {VV}  y  W = {WW}\n"

    #calcular raices
    x1 = ((VV + cmath.sqrt((VV)*2 -4*(U_ - WW)))/2) -(a/4)
    x_reales, x_imaginarias = funciones_herramientas.validar_raices(x1)
    print("1. x reales, imaginarios: ",x_reales,", ",x_imaginarias)
    print("1. x reales, imaginarios: ",x_reales,", ",x_imaginarias[0])
    x_reales, x_imaginarias, Error = funciones_herramientas.validar_CamR_I(x_reales, x_imaginarias)    
    print("1. x reales, imaginarios: ",x_reales,", ",x_imaginarias,"\n")
    raices_reales.extend(x_reales)
    raices_imaginarias.extend(x_imaginarias)
    print("VERIFICACION: reales, imaginarias: ",raices_reales,":",raices_imaginarias)
    
    x2 = ((VV - cmath.sqrt((VV)*2 -4*(U_ - WW)))/2) -(a/4)
    x_reales, x_imaginarias = funciones_herramientas.validar_raices(x2)
    print("2. x reales, imaginarios: ",x_reales,", ",x_imaginarias)
    print("2. x reales, imaginarios: ",x_reales,", ",x_imaginarias[0])
    x_reales, x_imaginarias, Error = funciones_herramientas.validar_CamR_I(x_reales, x_imaginarias)
    print("2. x reales, imaginarios: ",x_reales,", ",x_imaginarias,"\n")
    raices_reales.extend(x_reales)
    raices_imaginarias.extend(x_imaginarias)
    print("VERIFICACION: reales, imaginarias: ",raices_reales,":",raices_imaginarias)

    x3 = ((-VV + cmath.sqrt(VV**2 - 4*(U_ + WW))) / 2) - (a / 4)
    x_reales, x_imaginarias = funciones_herramientas.validar_raices(x3)
    print("3. x reales, imaginarios: ",x_reales,", ",x_imaginarias)
    print("3. x reales, imaginarios: ",x_reales,", ",x_imaginarias[0])
    x_reales, x_imaginarias, Error = funciones_herramientas.validar_CamR_I(x_reales, x_imaginarias)
    print("3. x reales, imaginarios: ",x_reales,", ",x_imaginarias,"\n")
    raices_reales.extend(x_reales)
    raices_imaginarias.extend(x_imaginarias)
    print("VERIFICACION: reales, imaginarias: ",raices_reales,":",raices_imaginarias)

    x4 = ((-VV - cmath.sqrt(VV**2 - 4*(U_ + WW))) / 2) - (a / 4)
    x_reales, x_imaginarias = funciones_herramientas.validar_raices(x4)
    print("4. x reales, imaginarios: ",x_reales,", ",x_imaginarias)
    print("4. x reales, imaginarios: ",x_reales,", ",x_imaginarias[0])
    x_reales, x_imaginarias, Error = funciones_herramientas.validar_CamR_I(x_reales, x_imaginarias)
    print("4. x reales, imaginarios: ",x_reales,", ",x_imaginarias)
    raices_reales.extend(x_reales)
    raices_imaginarias.extend(x_imaginarias)
    print("VERIFICACION: reales, imaginarias: ",raices_reales,":",raices_imaginarias)

    #f"Con 3 Raices reales:\nx1 = {raices_reales[0]} , x2 = {raices_reales[1]}\nx3 = {raices_reales[2]}\n1 Raiz imaginaria x4 = {raices_imaginarias[0]}"
    #f"Con 4 Raices imaginarias:\nx1 = {raices_imaginarias[0]} , x2 = {raices_imaginarias[1]}\nx3 = {raices_imaginarias[2]} , x4 = {raices_imaginarias[3]}
    #f"Los cuatro valores para x son: \nx1 = {x1} , x2 = {x2}\nx3 = {x3} , x4 = {x4}

    Mensaje = Mensaje + f"Raices Reales:  "
    for num in range(len(raices_reales)):
        Mensaje = Mensaje + f"x{num + 1} = {raices_reales[num]} , "
    Mensaje = Mensaje + "\n"   
    

    Mensaje = Mensaje + f"Raices Imaginarias:  "
    for num in range(len(raices_imaginarias)):
        Mensaje = Mensaje + f"x{num + 1} = {raices_imaginarias[num]} , "
    Mensaje = Mensaje + "\n"    

    if len(x_imaginarias) == 4:
        Mensaje = Mensaje + "\nNo hay raices reales, no es posible graficar"

    generales_Ferrari.set_transportador(expresion)
    generales_Ferrari.set_transportador(Mensaje)
    generales_Ferrari.set_transportador(Error)

    print("raices reales: ",raices_reales)
    print("raices imaginarias: ",raices_imaginarias)
    print(Mensaje)
    raices_reales_ferrari.set_transportador(raices_reales)
    raices_imaginarias_ferrari.set_transportador(raices_imaginarias)
 
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

def Ventana_Metodo_Ferrari(frame,ventana2,ventana):

    #disposicion de botones
    global marco_muestra_valores
    global canvas

    #botones globales
    global boton_limpiar,boton_resolver
    global tipo_tamaño_letra_ventana2,color_fondo_boton_ventana2,color_fondo_boton_ventana2
    global color_boton_pasar_mouse_ventana2,ancho_borde_ventana2,color_borde_ventana2
    global boton_limpiar,boton_resolver

    #declaracion marco superior
    marco_ingreso_valores = ctk.CTkFrame(frame, width=0, height=250, corner_radius=10)
    marco_ingreso_valores.pack(fill="x", expand=False, padx=10, pady=0)
    marco_ingreso_valores.grid_propagate(False)

    #declaracion marco inferior
    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=600,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)

        #declaracion label titulo
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores, text="Metodo Ferrari", font=("Arial Black", 16))
        #posicion
    label_ingrese_funcion.place(x=50,y=20)

        #declaracion label
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = "Ingrese una funcion",font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=50,y=50)

    #boton informacion
    def habilitar_boton_informacion():
        if label_informacion.winfo_ismapped():
            label_informacion.place_forget()
        else:
            label_informacion.place(x=350, y=50)

    label_informacion = ctk.CTkLabel(marco_ingreso_valores, text="El método de Ferrari es una técnica\nalgebraica utilizada para resolver\necuaciones polinómicas de cuarto\ngrado (cuárticas) de la forma:\nax**4 + bx**3 + cx**2 + dx + e = 0", font=tipo_tamaño_letra_ventana2)
    label_informacion.place_forget()

    #boton_informacion = ctk.CTkButton(marco_ingreso_valores, text="i", command=habilitar_boton_informacion,height = 20,width=20)
    #boton_informacion.place(x=300, y=50)

        #declaracion entry
    entry_ingrese_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    entry_ingrese_funcion.place(x=50,y=80)

    #::validaciones::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #habilitacion de botones globales
    global boton_limpiar,boton_resolver,mostrar

    def Validacion():
        expresion_recib = entry_ingrese_funcion.get()

        #Vacio
        if expresion_recib == "" or expresion_recib == None:
            messagebox.showerror("¡ ERROR CRITICO !", message = f"Parece que el campo: Ingrese funcion, esta vacio\n{expresion_recib}")
        else:
            #Caracteres permitidos
            expresion_carac, Error = funciones_herramientas.validar_caracteres(expresion_recib)
            verificador_error(Error)

            #Apertura y cierre de signos de agrupacion
            expresion_carac, Error = funciones_herramientas.validar_PCL(expresion_carac)
            verificador_error(Error)

            #multiplicacion implicita
            expresion_valid, Error = funciones_herramientas.validar_multiplicacion_implicita(expresion_carac)
            verificador_error(Error)

            #crear los espacios donde se estableceran los resultados, indicanto el marcos
            muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

            #Ecuaciones_Cuadraticas(funcion, destinos) 
            Metodo_Ferrari(expresion_valid) 
            
            #traer valores a mostrar de Ecuaciones_Cuadraticas
            #transport_valores.get_transportador() -> muetra_valores -> marco_muestra_valores
            muestra_valores.configure(text = generales_Ferrari.get_transportador(1),anchor='w', justify='left')

            #impresion del grafico
            # Crear y mostrar el gráfico
            num_reales = []
            num_reales = raices_reales_ferrari.get_transportador()
            print("fuera del metodo: grafico: [0, 'expresion']",generales_Ferrari.get_transportador(0))
            print("fuera del metodo: grafico: [1, 'puntos']",num_reales)
            print("raices reales: ",raices_reales_ferrari.get_transportador())
            fig = Grafico(generales_Ferrari.get_transportador(0), num_reales)

            canvas = FigureCanvasTkAgg(fig, master = muestra_grafica)
            #grafico(funcion, x_valores)
            #indice = 0:mensaje, 1:funcion, 2:list_reales, 3:list_imaginarios

            canvas.draw()
            widget_grafico = canvas.get_tk_widget()
            widget_grafico.pack(fill="both", expand=True)
                
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
            entry_ingrese_funcion.delete(0, END)
        
   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=125)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=125)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=125)


