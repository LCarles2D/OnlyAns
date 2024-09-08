from sympy import parse_expr, symbols, Poly, div, sqrt, Eq, solve
import sympy as sp
import pandas as pd
from sympy.parsing.sympy_parser import transformations, T, standard_transformations, implicit_application, convert_xor, implicit_multiplication, function_exponentiation, implicit_multiplication_application, auto_symbol, auto_number, split_symbols
transformaciones = standard_transformations + (implicit_application, )
import funciones_herramientas
from funciones_herramientas import *
from IPython.display import display

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
import ctypes

#Metodo_bairstow("x**4-7x**3+13x**2+23x-78", 1.5, 1.5, 4)
def verificador_error(Error):
    if not (Error == None or Error == ""):
        messagebox.showerror("¡ ERROR CRITICO !", message = Error)
    else:
        pass

generales_Bairstow = funciones_herramientas.Transportador()
raices_reales = funciones_herramientas.Transportador()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def val_expr(expr):
    if isinstance(expr, sp.Basic) or isinstance(expr, str):    
        expresion = parse_expr(expr, transformations = standard_transformations + (implicit_multiplication_application, ))
        funtion = Poly(expresion)
        return funtion
    else:   
        if not isinstance(expr, sp.Basic):
            if not isinstance(expr, str):
                print("La expresion proporcionada es una cadena string (str), ni una de tipo sympify")
                exit()
            print("La expresion proporcionada no es de tipo sympify")

def val_cs(cifras_significativas):
    if not isinstance(cifras_significativas, int):
        print("Err(val_cs): Error en cifras significativas, el valor debe ser un numero entero")
        exit()
    if cifras_significativas < 0:
        print("Err(val_cs): El valor de cifras significativas debe ser mayor o igual a cero")
        exit()

def calc_cs(cifras_significativas):
    Err_sig = 0.5 * 10**(2 - cifras_significativas)
    return Err_sig

def get_coef(funcion):
    x = symbols("x")
    expr = funcion
        #x**4 - 7*x**3 + 13*x**2 + 23*x - 78
    coeficientes = expr.all_coeffs()
    #print("coeficientes (get_coef): ",coeficientes)
    if not coeficientes[0] == 1:
        pri_num = coeficientes[0]
        coeficientesdiv = []
        for iterador in coeficientes:
            coeficientes[iterador] = coeficientes[iterador] / pri_num

        coeficientes = coeficientesdiv
    if not len(coeficientes) == 5:
        print("Err(get_coef): La expresion ingresa es de un grado distinto de 4") 
    return coeficientes

def Metodo_Bairstow(expresion, r0, s0, cifras_significativas):
    print("-------------------- Metodo de Bairstow----------------------------")
    """Algoritmo Bairstow
    #Paso 1 : inicializar ro y so
    #Paso 2 : Calculo Es
    #Paso 3 : Determinar los valores de los coheficientes
    #Paso 4 : Determinamos los valores de C
    #Paso 5 : Determinamos D_r y D_s en las ecuaciones
    #Paso 6 : Determinar los valores actuales de r y s
    #Paso 7 : Se analiza el error
    #Paso 8 : Se pasa a determinar la raiz dependiendo la condicion
    #Paso 9 : Se encuentra el polinomio restante, con la division sintetica
    #Paso 10: Calculamos el grado del polinomio resultante"""

    Mensaje, Error = "", ""
    x = sp.symbols("x")

    func, dicc, Error = funciones_herramientas.validar_funcion(expresion)
    ro, so = r0, s0                                                                   #Paso 1 : inicializar ro y so
    verificador_error(Error)
    
    Es, Error = funciones_herramientas.calcular_Es(cifras_significativas)           #Paso 2 : Calculo Es
    #Paso 3 : Determinar los valores de los coheficientes
    coeficientes = []    
    coeficientes, Error = funciones_herramientas.obtener_coeficientes(expresion)
    verificador_error(Error)

    Mensaje = "Metodo de Bairstow\n\n"
    Mensaje = Mensaje + f"Expresion Ingresada: {expresion} ,  con ro: {r0} ,  so: {s0}\n"
    Mensaje = Mensaje + f"Cifras significativas: {cifras_significativas} y  Nivel de tolerancia: {Es}\n"
    Mensaje = Mensaje + f"Coeficientes de la expresion {expresion}: {coeficientes}\n"
    
    conteo = 1
    df = pd.DataFrame( columns = ["Iteracion","r","s","E_Dr%","E_Ds %"] )
    
    Xr, Xr1, Xr2 = 0, 0, 0

    while True:
        # continuando con el paso 3, determinamos los valores
        b4 = coeficientes[0]
        b3 = coeficientes[1] + ro*b4
        b2 = coeficientes[2] + ro*b3 + so*b4
        b1 = coeficientes[3] + ro*b2 + so*b3
        b0 = coeficientes[4] + ro*b1 + so*b2

        #Paso 4 --> Determinamos los valores de C
        c4 = b4
        c3 = b3 + ro*c4
        c2 = b2 + ro*c3 + so*c4
        c1 = b1 + ro*c2 + so*c3

        #Paso 5 --> Determinamos D_r y D_s en las ecuaciones

        #Formamos la ecuaciones
        D_r, D_s=symbols("D_r D_s") #declaro los simbolos

        #Defino las ecuaciones
        ecua1=Eq(c2*D_r + c3*D_s,-b1)
        ecua2=Eq(c1*D_r + c2*D_s,-b0)

        #Las resolvemos
        solucion=solve((ecua1,ecua2),(D_r,D_s))
        Dr,Ds=solucion.values() #utilizando desempaquetado

        #Paso 6 --> Determinar los valores actuales de r y s
        r=(ro + Dr).round(10)
        s=(so + Ds).round(10)

        #Paso 7 --> Se analiza el error
        E_Dr=(abs(Dr/r))*100
        E_Ds=(abs(Ds/s))*100

        #Tabla para mostrar datos y tener un control de las evaluaciones
        df.loc[conteo-1]=[conteo,r.round(10),s.round(10),E_Dr.round(10),E_Ds.round(10)] 

        #Paso 8 --> Se pasa a determinar la raiz dependiendo la condicion
        if (E_Dr < Es) and (E_Ds < Es): #si los dos son menores a Es, se evalua
            print(df)
            #Evaluamos Xr
            xr1 = (r + sp.sqrt(r**2 + 4*s))/2 
            xr2 = (r - sp.sqrt(r**2 + 4*s))/2
            
            #Paso 9 --> Se encuentra el polinomio restante, con la division sintetica
            # Dividimos el polinomio entre las raíces encontradas para obtener el polinomio restante
            polinomio_resto = Poly(func)  # Creamos un nuevo polinomio a partir de la expresión original
            cociente, resto = div(polinomio_resto, Poly(x - xr1)) #Dividimos el polinomio entre la primer raiz
            polinomio_resto = cociente #el polinomio ya dividido lo actualizo en la variable

            cociente, resto = div(polinomio_resto, Poly(x - xr2)) #divido el polinomio ya actualizado entre la otra raiz
            polinomio_resto = cociente #El polinomio resultante se guarda en la variable

            #Paso 10 --> Calculamos el grado del polinomio resultante
            Qx=polinomio_resto.degree()

            #Condiciones
            if Qx >= 3: #Si el grado del polinomio es mayor o igual a tres se vuelve a aplicar el metodo tomando como ro=r , so=s
                ro = r
                so = s

            elif Qx==2: #si el grado del polinomio es igual a 2 se evalua directo
                Xr1 = (r + sp.sqrt(r**2 + 4*s))/2 
                Xr2 = (r - sp.sqrt(r**2 + 4*s))/2
                Mensaje = Mensaje + f"\nEl polinomio es de grado {Qx} y sus raices son : X1 = {Xr1} y X2 = {Xr2}\n"
                #print(f"\nEl polinomio es de grado {Qx} y sus raices son : X1 = {Xr1} y X2 = {Xr2}")
            
            elif Qx == 1: #Si es de grado uno se evalua
                Xr = -(s/r)
                Mensaje = Mensaje + f"\nEl polinomio es de grado {Qx} y su raiz es: X = {Xr}\n"
                #print(f"\nEl polinomio es de grado {Qx} y su raiz es: X = {Xr}")

            break
        #regresa al paso2
        ro = r
        so = s 
        conteo += 1
    #df = funciones_herramientas.ajustar_tabla_pandas(df)
    Mensaje = Mensaje + f"{df}"#.to_string(index=False)    

    generales_Bairstow.set_transportador(expresion)
    generales_Bairstow.set_transportador(Mensaje)
    generales_Bairstow.set_transportador(Error)

    if Xr == 0:
        x_real, x_imaginaria = funciones_herramientas.validar_raices(Xr1)
        x_real, x_imaginaria, Error = funciones_herramientas.validar_CamR_I(x_real, x_imaginaria)

        x_real, x_imaginaria = funciones_herramientas.validar_raices(Xr2)
        x_real, x_imaginaria, Error = funciones_herramientas.validar_CamR_I(x_real, x_imaginaria)

        raices_reales.set_transportador(x_real)
    else:
        x_real, x_imaginaria = funciones_herramientas.validar_raices(Xr)
        x_real, x_imaginaria, Error = funciones_herramientas.validar_CamR_I(x_real, x_imaginaria)    

        raices_reales.set_transportador(x_real)

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

def Ventana_Metodo_Bairstow(frame,ventana2,ventana):

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

    #declaracion marco inferior
    marco_muestra_valores = ctk.CTkFrame(frame,width=0,height=550,corner_radius=10)
    marco_muestra_valores.pack(fill="x", expand=False, padx=10, pady=10)
    marco_muestra_valores.grid_propagate(False)


        #Label titulo
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores, text="Metodo de Bairstown", font=("Arial Black", 16))
        #posicion
    label_ingrese_funcion.place(x=50,y=20)

        #label funcion
    _func = "Ingrese una funcion"    
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = _func,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=50,y=50)

    #boton informacion funcion
    def habilitar_boton_informacion():
        if label_informacion.winfo_ismapped():
            label_informacion.place_forget()
        else:
            label_informacion.place(x=55,y=120)

    label_informacion = ctk.CTkLabel(marco_ingreso_valores, text="El método de Bairstow es una técnica\niterativa utilizada para encontrar\ntodas las raíces de un polinomio.\nSe basa en la división sintética y\nse mejora iterativamente para refinar\nlas aproximaciones de las raíces.",font=tipo_tamaño_letra_ventana2)
    label_informacion.place_forget()

    #boton_informacion = ctk.CTkButton(marco_ingreso_valores, text="i", command=habilitar_boton_informacion,height = 20,width=20)
    #boton_informacion.place(x=300, y=50)

        #entry funcion
    e_ingrese_funcion = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_funcion.place(x=50,y=80)

    #label ro
    _ro = "Ingrese ro"
    label_ingrese_ro = ctk.CTkLabel(marco_ingreso_valores,text = _ro,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_ro.place(x=500,y=50)
        #entry ro
    e_ingrese_ro = ctk.CTkEntry(marco_ingreso_valores,width=75,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_ro.place(x=500,y=80)

    #label so
    _so = "Ingrese so"
    label_ingrese_so = ctk.CTkLabel(marco_ingreso_valores,text = _so,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_so.place(x=600,y=50)
        #entry so
    e_ingrese_so = ctk.CTkEntry(marco_ingreso_valores,width=75,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_so.place(x=600,y=80)

    #label CS
    _cs = "Ingrese cantidad de cifras significativas"
    label_ingrese_funcion = ctk.CTkLabel(marco_ingreso_valores,text = _cs,font=tipo_tamaño_letra_ventana2)
        #posicion
    label_ingrese_funcion.place(x=500,y=125)
        #entry Cs
    e_ingrese_cs = ctk.CTkEntry(marco_ingreso_valores,width=200,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
        #posicion
    e_ingrese_cs.place(x=500,y=155)
    

        

    #::validaciones::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    #habilitacion de botones globales
    global boton_limpiar,boton_resolver,mostrar

    def Validacion():
        expresion = e_ingrese_funcion.get()
        so = e_ingrese_so.get()
        ro = e_ingrese_ro.get()
        cs = e_ingrese_cs.get()

        print("ro: ",ro)
        print("ro: ",type(ro),"\n")
        print("ro: ",so)
        print("ro: ",type(so))

        #Vacio
        lista_param = {_func:expresion, _ro:ro, _so:so, _cs:cs}
        if expresion == "glo?":
            mensaje = "Glogloglogloglojksdfsajfjajajajaja"
            verificador_error(mensaje)
        if validar_vacio(expresion)==False or validar_vacio(ro)==False or validar_vacio(ro)==False or validar_vacio(cs)==False:
            mens = validar_vacio_g(lista_param)
            verificador_error(mens)
        else:
            #Caracteres permitidos
            expresion, Error = funciones_herramientas.validar_caracteres(expresion)
            verificador_error(Error)
            ro, Error = funciones_herramientas.validar_numeros(ro)
            verificador_error(Error)
            so, Error = funciones_herramientas.validar_numeros(so)
            verificador_error(Error)
            cs, Error = funciones_herramientas.validar_numeros(cs, "int")
            verificador_error(Error)

            print("\n\nro: ",ro)
            print("ro: ",type(ro),"\n")
            print("ro: ",so)
            print("ro: ",type(so))

            #validar ro y so
            if ro <= 0 and so <= 0:
                Error = "ro y so no puede ser igual cero o menores"
                verificador_error(Error)
            elif ro <= 0:
                Error = "ro no puede ser igual cero o menores"    
                verificador_error(Error)
            elif so <= 0:
                Error = "ro no puede ser igual cero o menores"    
                verificador_error(Error)

            #validar cs
            if cs < 0 and not isinstance(cs, (int)):
                Error = "El valor de las cifras significativas debe ser positivo y ser un numero entero"
                verificador_error(Error)
            if cs < 0:
                Error = "El valor de las cifras significativas deben ser un numero positivo"    
                verificador_error(Error)
            if not isinstance(cs, (int)):
                Error = "El valor de las cifras significativas debe ser un numero entero"
                verificador_error(Error)

            
            #Apertura y cierre de signos de agrupacion
            expresion, Error = funciones_herramientas.validar_PCL(expresion)
            verificador_error(Error)

            """#Validar igualdad
            expresion, Error = funciones_herramientas.validar_igualdad(expresion)
            verificador_error(Error)"""

            expresion_valid, Error = funciones_herramientas.validar_multiplicacion_implicita(expresion)
            verificador_error(Error)

    
            muestra_valores = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_tabla = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            #muestra_raiz = ctk.CTkLabel(marco_muestra_valores,font=tipo_tamaño_letra_ventana2)
            muestra_grafica = ctk.CTkCanvas(marco_muestra_valores, width=100,height=100)

            #Ecuaciones_Cuadraticas(funcion, destinos) 
            Metodo_Bairstow(expresion_valid, ro, so, cs) 
        
            #impresion de datos
            muestra_valores.configure(text = generales_Bairstow.get_transportador(1), anchor='w', justify='left')

            #impresion del grafico
            fig = Grafico(generales_Bairstow.get_transportador(0), raices_reales.get_transportador())
            canvas = FigureCanvasTkAgg(fig, master = muestra_grafica)

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
            e_ingrese_funcion.delete(0, END)
            e_ingrese_ro.delete(0, END)
            e_ingrese_so.delete(0, END)
            e_ingrese_cs.delete(0, END)
        
   
    boton_resolver = ctk.CTkButton(marco_ingreso_valores,text ="Resolver",command=Validacion,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_resolver.place(x=1150,y=225)

    boton_limpiar = ctk.CTkButton(marco_ingreso_valores,text = "Limpiar",command=Limpiar,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_limpiar.place(x=200,y=225)
    boton_limpiar.configure(state=DISABLED)

    boton_salir = ctk.CTkButton(marco_ingreso_valores,text="Volver",command=lambda: Volver(ventana2, ventana),fg_color=color_fondo_boton_ventana2,text_color=color_texto_ventana2,font=tipo_tamaño_letra_ventana2,height=40,width=120,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_salir.place(x=50,y=225)

    
    
