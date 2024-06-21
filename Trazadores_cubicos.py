#!/usr/bin/env python3
import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import re
import ctypes
from functools import partial

mostrar= False

def Trazadores_Cubicos(valores_x,valores_y, punto_evaluar,grado):
    global mostrar
    output_text = ""
    output_text += "---------------------------Trazadores Cubicos---------------------------------------------------\n"
    output_text += f"x : {valores_x}\n"
    output_text += f"y : {valores_y}\n"
    output_text += "---------------------------------------------------------------------------\n"
    
    #Paso 1  : Identifico los intervalos
    intervalos = [(valores_x[i], valores_x[i + 1]) for i in range(len(valores_x) - 1)]
    output_text += f"Intervalos : {intervalos}\n"


    if grado == 0:
       output_text += "\n---------Grado Cero -----------\n"

       n = len(valores_x)

       # Evaluar un punto
       evaluado = False
       for j in range(n-1):
           if valores_x[j] <= punto_evaluar <= valores_x[j+1]:
               punto_evaluado = valores_y[j]
               evaluado = True
               break

       if evaluado:
           output_text += f"El punto {punto_evaluar} se encuentra en el intervalo [{valores_x[j]}, {valores_x[j+1]}] y su valor evaluado es {punto_evaluado}.\n"
       else:
           output_text += f"El punto {punto_evaluar} no se encuentra en ningún rango.\n"

       # GRAFICA
       # Para spline de grado 0, simplemente dibujamos líneas horizontales entre los puntos


    elif grado == 1:
        output_text += "\n---------Grado Uno -----------\n"

        n = len(valores_x)

        # Valores h
        h = np.zeros(n-1, dtype=float)
        for j in range(0, n-1):
            h[j] = valores_x[j+1] - valores_x[j]

        # Coeficientes del polinomio lineal
        a = np.zeros(n-1, dtype=float)
        b = np.zeros(n-1, dtype=float)
        for j in range(0, n-1):
            a[j] = (valores_y[j+1] - valores_y[j]) / h[j]
            b[j] = valores_y[j] - a[j] * valores_x[j]

        # Polinomio trazador
        x = sp.Symbol('x')
        px_tabla = []
        for j in range(0, n-1):
            pxtramo = a[j] * x + b[j]
            pxtramo = pxtramo.expand()
            px_tabla.append(pxtramo)

        # SALIDA
        output_text += 'Funciones: \n'
        for tramo in range(1, n):
            output_text += f'{px_tabla[tramo-1]} \t, [{valores_x[tramo-1]}, {valores_x[tramo]}]\n'

        # Evaluar un punto
        evaluado = False
        for j in range(n-1):
            if valores_x[j] <= punto_evaluar <= valores_x[j+1]:
                pxtramo = px_tabla[j]
                pxt = sp.lambdify('x', pxtramo)
                punto_evaluado = pxt(punto_evaluar)
                evaluado = True
                break

        if evaluado:
            output_text += f"\nEl punto {punto_evaluar} se encuentra en el intervalo [{valores_x[j]}, {valores_x[j+1]}] y en la función {pxtramo}.\n"
            output_text += f"f({punto_evaluar}) : {punto_evaluado}\n"
        else:
            output_text += f"El punto {punto_evaluar} no se encuentra en ningún rango.\n"

        # GRAFICA
        # Puntos para graficar cada tramo
        xtraza = np.array([])
        ytraza = np.array([])
        tramo = 1
        while tramo < n:
            a = valores_x[tramo-1]
            b = valores_x[tramo]
            xtramo = np.linspace(a, b, 100)
            
            # Evalua polinomio del tramo
            pxtramo = px_tabla[tramo-1]
            pxt = sp.lambdify('x', pxtramo)
            ytramo = pxt(xtramo)

            # Vectores de trazador en x, y
            xtraza = np.concatenate((xtraza, xtramo))
            ytraza = np.concatenate((ytraza, ytramo))
            tramo += 1


    elif grado == 2:
        output_text += "\n---------Grado Dos -----------\n"
        n = len(valores_x)
        a = np.zeros(n-1, dtype=float)
        b = np.zeros(n-1, dtype=float)
        c = np.zeros(n-1, dtype=float)

        for j in range(n-1):
            h = valores_x[j+1] - valores_x[j]
            a[j] = (valores_y[j+1] - valores_y[j]) / (2 * h)
            b[j] = (valores_y[j+1] - valores_y[j]) / h - h * a[j]
            c[j] = valores_y[j]

        # Polinomio trazador
        x = sp.Symbol('x')
        px_tabla = []

        for j in range(n-1):
            pxtramo = a[j] * (x - valores_x[j])**2 + b[j] * (x - valores_x[j]) + c[j]
            pxtramo = pxtramo.expand()
            px_tabla.append(pxtramo)

        # PROCEDIMIENTO
        # Tabla de polinomios por tramos
        muestras = 10  # Para la grafica

        # SALIDA
        output_text += 'Funciones: \n'
        for tramo in range(1, n, 1):
            output_text += str(px_tabla[tramo-1]) + ' \t, [' + str(valores_x[tramo-1]) + ',' + str(valores_x[tramo]) + ']\n'

        # Evaluar un punto
        evaluado = False
        for j in range(n-1):
            if valores_x[j] <= punto_evaluar <= valores_x[j+1]:
                pxtramo = px_tabla[j]
                pxt = sp.lambdify('x', pxtramo)
                punto_evaluado = pxt(punto_evaluar)
                evaluado = True
                break
            else:
                evaluado = False

        if evaluado:
            output_text += f"\nEl punto {punto_evaluar} se encuentra en el intervalo [{valores_x[j]}, {valores_x[j+1]}] y en la función {pxtramo}.\n"
            output_text += f"f({punto_evaluar}) : {punto_evaluado}\n"
        else:
            output_text += f"El punto {punto_evaluar} no se encuentra en ningún rango.\n"

        # GRAFICA
        # Puntos para graficar cada tramo
        xtraza = np.array([])
        ytraza = np.array([])
        tramo = 1

        while tramo < n:
            a_tramo = valores_x[tramo-1]
            b_tramo = valores_x[tramo]
            xtramo = np.linspace(a_tramo, b_tramo, muestras)

            # evaluar polinomio del tramo
            pxtramo = px_tabla[tramo-1]
            pxt = sp.lambdify('x', pxtramo)
            ytramo = pxt(xtramo)

            # vectores de trazador en x, y
            xtraza = np.concatenate((xtraza, xtramo))
            ytraza = np.concatenate((ytraza, ytramo))
            tramo += 1

        # Gráfica
                

                


    elif grado == 3:
        output_text += "\n---------Grado Tres -----------\n"
        
        # Trazador cúbico natural
        # Condición: S''(x_0) = S''(x_n) = 0

        n = len(valores_x)
        
        # Valores h
        h = np.zeros(n-1, dtype = float)
        for j in range(0,n-1,1):
            h[j] = valores_x[j+1] - valores_x[j]
        
        # Sistema de ecuaciones
        A = np.zeros(shape=(n-2,n-2), dtype = float)
        B = np.zeros(n-2, dtype = float)
        S = np.zeros(n, dtype = float)

        A[0,0] = 2*(h[0]+h[1])
        A[0,1] = h[1]
        B[0] = 6*((valores_y[2]-valores_y[1])/h[1] - (valores_y[1]-valores_y[0])/h[0])

        for i in range(1,n-3,1):
            A[i,i-1] = h[i]
            A[i,i] = 2*(h[i]+h[i+1])
            A[i,i+1] = h[i+1]
            factor21 = (valores_y[i+2]-valores_y[i+1])/h[i+1]
            factor10 = (valores_y[i+1]-valores_y[i])/h[i]
            B[i] = 6*(factor21 - factor10)
            
        A[n-3,n-4] = h[n-3]
        A[n-3,n-3] = 2*(h[n-3]+h[n-2])
        factor12 = (valores_y[n-1]-valores_y[n-2])/h[n-2]
        factor23 = (valores_y[n-2]-valores_y[n-3])/h[n-3]
        B[n-3] = 6*(factor12 - factor23)
        
        # Resolver sistema de ecuaciones S
        r = np.linalg.solve(A,B)
        for j in range(1,n-1,1):
            S[j] = r[j-1]
        S[0] = 0
        S[n-1] = 0
        
        # Coeficientes
        a = np.zeros(n-1, dtype = float)
        b = np.zeros(n-1, dtype = float)
        c = np.zeros(n-1, dtype = float)
        d = np.zeros(n-1, dtype = float)
        for j in range(0,n-1,1):
            a[j] = (S[j+1]-S[j])/(6*h[j])
            b[j] = S[j]/2
            factor10 = (valores_y[j+1]-valores_y[j])/h[j]
            c[j] = factor10 - (2*h[j]*S[j]+h[j]*S[j+1])/6
            d[j] = valores_y[j]
        
        # Polinomio trazador
        x = sp.Symbol('x')
        px_tabla = []
        for j in range(0,n-1,1):

            pxtramo = a[j]*(x-valores_x[j])**3 + b[j]*(x-valores_x[j])**2
            pxtramo = pxtramo + c[j]*(x-valores_x[j])+ d[j]
            
            pxtramo = pxtramo.expand()
            px_tabla.append(pxtramo)
        


        # PROCEDIMIENTO
        # Tabla de polinomios por tramos
        n = len(valores_x)
        muestras = 10 # Para la grafica

        # SALIDA
        output_text += 'Funciones: \n'
        for tramo in range(1,n,1):
            output_text += str(px_tabla[tramo-1]) + ' \t, ['+str(valores_x[tramo-1]) +','+str(valores_x[tramo])+']\n'
            
        #Evaluar un punto
        evaluado = False
        for j in range(n-1):
            if valores_x[j] <= punto_evaluar <= valores_x[j+1]:
                pxtramo = px_tabla[j]
                pxt = sp.lambdify('x', pxtramo)
                punto_evaluado = pxt(punto_evaluar)
                evaluado = True
                break
            else:
                evaluado = False

        if  evaluado == True:
            output_text += f"\nEl punto {punto_evaluar} se encuentra en el intervalo [{valores_x[j]}, {valores_x[j+1]}] y en la funcion {pxtramo}.\n"
            output_text += f"f({punto_evaluar}) : {punto_evaluado}\n"
        else:
            output_text += f"El punto {punto_evaluar} no se encuentra en ningún rango.\n"

        # GRAFICA
        # Puntos para graficar cada tramo
        xtraza = np.array([])
        ytraza = np.array([])
        tramo = 1
        while not(tramo>=n):
            a = valores_x[tramo-1]
            b = valores_x[tramo]
            xtramo = np.linspace(a,b,muestras)
            
            # evalua polinomio del tramo
            pxtramo = px_tabla[tramo-1]
            pxt = sp.lambdify('x',pxtramo)
            ytramo = pxt(xtramo)

            # vectores de trazador en x,y
            xtraza = np.concatenate((xtraza,xtramo))
            ytraza = np.concatenate((ytraza,ytramo))
            tramo = tramo + 1
    mostrar = True
    print(output_text)
    return output_text


 
color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2
toggle = False
mostrar_y = True
grados = 0


def Ventana_Trazadores_Cubicos(frame, ventana2, ventana):
    global toggle
    global marco_muestra_valores
    global canvas
    global grados

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

    etiqueta_grados_text = ctk.CTkLabel(marco_ingreso_valores, text = "Grados:", font=tipo_tamaño_letra_ventana2)
    etiqueta_grados_text.place(x= 875, y= 105)

    etiqueta_grados = ctk.CTkLabel(marco_ingreso_valores, text = grados, font = tipo_tamaño_letra_ventana2)
    etiqueta_grados.place(x= 900, y= 125)

    necesarios = [marco_ingreso_valores, tipo_tamaño_letra_ventana2, color_texto_ventana2]
    
    ############# ingresos_y de valores
    ingresos_x0 =IngresarEnCadena(*necesarios, 100, 60, 2)
    ingresos_y = IngresarEnCadena(*necesarios, 325, 60, 2)

    ingreso_interpolacion = ctk.CTkEntry(marco_ingreso_valores,width=100,height=30,corner_radius=10,font = tipo_tamaño_letra_ventana2,text_color=color_texto_ventana2)
    ingreso_interpolacion.place(x=600,y=60)

    def agregar_grados():
        global grados
        if grados < 3:
            grados += 1
            etiqueta_grados.configure(text=grados)

    def eliminar_grados():
        global grados
        if grados > 0:
            grados -= 1 
            etiqueta_grados.configure(text=grados)
    
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
    
    boton_agregar_grados = ctk.CTkButton(marco_ingreso_valores,text ="-",command=eliminar_grados,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_agregar_grados.place(x=850,y=60)
    boton_eliminar_grados = ctk.CTkButton(marco_ingreso_valores,text ="+",command=agregar_grados,fg_color = color_fondo_boton_ventana2,text_color = color_texto_ventana2,font = tipo_tamaño_letra_ventana2,height = 40,width=50,hover_color=color_boton_pasar_mouse_ventana2,border_color=color_borde_ventana2,border_width=ancho_borde_ventana2)
    boton_eliminar_grados.place(x=905,y=60)


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
        #Si estan vacios todos
        if (x_llenados == True or interpolacion == '') or (y_llenados == True and funcion == '') :
            messagebox.showerror("¡ ERROR CRITICO !",message="Debe llenar todos los campos de forma correcta")
        else:
            
            if numero_valido(valores_x[0]) and numero_valido(valores_x[1]) and numero_valido(interpolacion):
                x= sp.symbols('x')
                valores_x = [float(valor) for valor in valores_x]
                if funcion == '':    
                    valores_y = [float(valores) for valores in valores_y]
                    funcion = None
                else:
                    booleano, funcion = Validar_y_Reemplazar_funcion(funcion)
                    
                    if booleano == False:
                        messagebox.showerror('ERROR', message='Ingrese una funcion valida')
                        return
                    valores_y = [funcion.subs(x, xi) for xi in valores_x]


                interpolacion = float(interpolacion)

                muestra_valores = ctk.CTkLabel(marco_muestra_valores,font= ("Currier",15,"bold"), justify= 'left', anchor='w', wraplength=1000)
                
                string = Trazadores_Cubicos(valores_x, valores_y, interpolacion, grados)
 #def Newton_recursivo(x_array, y_array=None, ecuacion = None, x_inter=Non:

                muestra_valores.configure(text=string)

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


