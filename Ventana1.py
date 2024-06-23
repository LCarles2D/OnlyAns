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
from PIL import Image, ImageTk  # Importar Image y ImageTk
import os

from Metodo_Biseccion import Volver,Ventana_Biseccion
from Falsa_Posicion import Volver,Ventana_Falsa_Posicion
from Punto_Fijo import Volver,Ventana_Punto_Fijo
from Metodo_Secante import Volver,Ventana_Secante
from Newton_Rapson import Volver,Ventana_Newton_Rapson
from Newton_Rapson_Modificado import Volver,Ventana_Newton_Rapson_Modificado
from Diferencias_Finitas import Volver,Ventana_Diferencias_Finitas
from Interpolacion_Lineal import Volver,Ventana_Interpolacion_Lineal
from InterpolacionLagrange import Volver,Ventana_Interpolacion_Lagrange
from Newton_recursivo import Volver, Ventana_Newton_Recursivo
from Newton_diferencias_dividas import Volver, Ventana_Newton_diferencias
from hermite import Volver, Ventana_Hermite
from Trazadores_cubicos import Volver, Ventana_Trazadores_Cubicos
from Simpson_adaptativo import Volver, Ventana_Simpson_Adaptativo
from Rungen_Kutta import Volver, Ventana_Rungen_Kutta
from Metodo_Integracion_Numerica import Volver, Ventana_Metodo_Integracion
from Metodo_multipasos import Volver, Ventana_Multipasos

#Creo una segunda ventana-------------------------------------------------------------------------------


ventana2 = None
ventana = None

color_fondo_boton_ventana2 = "#2c2b4b"
color_texto_ventana2 = "white"
tipo_tamaño_letra_ventana2 = ("Currier",12,"bold")

color_boton_pasar_mouse_ventana2 = "#5603b6"
color_borde_ventana2  = "white"
ancho_borde_ventana2 = 2

frame = None



#-------------------Creo funciones para activar cada metodo dependiendo cual se seleccione------------------------------------------

def Activar_Metodo_Biseccion():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    #ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.attributes("-fullscreen", "True")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")
    ventana2.columnconfigure(0, weight=1)
    ventana2.rowconfigure(0, weight=1)# desactivar el boton de cerrar
    ventana2.title("Metodo Biseccion") 

    
 # Deshabilitar los botones de minimizar y maximizar usando wmctrl
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert')

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    Ventana_Biseccion(frame,ventana2,ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()



    
    

    
    
    
def Activar_Falsa_Posicion():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Falsa Posicion") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    Ventana_Falsa_Posicion(frame,ventana2,ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Punto_Fijo():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Punto Fijo") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    Ventana_Punto_Fijo(frame,ventana2,ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodo_Secante():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Secante") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    Ventana_Secante(frame,ventana2,ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Newton_Raphson():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Newton Raphson") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    Ventana_Newton_Rapson(frame,ventana2,ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Newton_Raphson_Modificado():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Newton Raphson Modificado") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    Ventana_Newton_Rapson_Modificado(frame,ventana2,ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Ecuaciones_Cuadraticas():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Ecuaciones Cuadraticas") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #Ventana_Biseccion(frame,ventana2,ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodo_Tartaglia():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Tartaglia") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodo_Ferrari():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Ferrari") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodo_Horner():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Horner") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodo_Bairstown():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Bairstown") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodo_Muller():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Muller") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    



def Activar_Interpolacion_Lineal():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    #ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    #ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Interpolacion Lineal") 

    
    # Deshabilitar el botón de minimiza    #Creo un frame
       # Deshabilitar los botones de minimizar y maximizar usando wmctrl
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 

    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funciones
    Ventana_Interpolacion_Lineal(frame, ventana2, ventana)
    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Polinomio_Interpolacion_LaGrange():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.geometry("1500x800")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Interpolacion de LaGrange") 

    
    # Deshabilitar el botón de minimizar
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 

   #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funciones
    Ventana_Interpolacion_Lagrange(frame, ventana2, ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Polinomio_Interpolacion_Newton():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    #ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    #ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Polinomio de Interpolacion de Newton") 

    
    # Deshabilitar el botón de minimiz # Deshabilitar el botón de minimizar
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 

       #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion
    Ventana_Newton_Recursivo(frame, ventana2, ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Diferencias_Divididas():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.geometry("1500x800")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Diferencias Divididas") 

    
    # Deshabilitar el botón de minimizar
       #Creo un frame
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 



    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion
    Ventana_Newton_diferencias(frame, ventana2, ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Interpolacion_Hermite():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.geometry("1500x800")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Interpolacion Hermite") 

    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 


    # Deshabilitar el botón de minimizar
       #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion   
    Ventana_Hermite(frame, ventana2, ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Trazadores_Cubicos():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.geometry("1500x800")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Trazadores Cubicos") 


    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 


       #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion
    Ventana_Trazadores_Cubicos(frame, ventana2, ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    


def Activar_Diferenciacion_Numerica():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Diferenciacion Numerica") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    Ventana_Diferencias_Finitas(frame,ventana2,ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    
    

def Activar_Extrapolacion_Richardson():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Extrapolacion de Richardson") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Integracion_Numerica():
    global ventana,ventana2
    ventana2 =ctk.CTk()
    ventana2.geometry("1500x800")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Interpolacion Numerica") 

    
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion
    Ventana_Metodo_Integracion(frame,ventana2,ventana)
    
    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodos_Adaptativos():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.geometry("1500x800")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodos Adaptativos") 

    
    # Deshabilitar el botón de minimizar
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 

       #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion
    Ventana_Simpson_Adaptativo(frame, ventana2, ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Cuadratura_Gaussiana():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Cuadratura Gaussiana") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    


def Activar_Metodo_Euler():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Euler") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodo_Taylor():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.iconbitmap("Imagenes/icono.ico")
    ventana2.geometry("1500x800")
    ventana2.state("zoomed")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Taylor") 

    
    # Deshabilitar el botón de minimizar
    hwnd = ctypes.windll.user32.GetParent(ventana2.winfo_id())
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    new_style = current_style & ~0x00020000 & ~0x00010000
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

def Activar_Metodo_Runge_Kutta():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.geometry("1500x800")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Runge Kutta") 

    
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 

    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion
    Ventana_Rungen_Kutta(frame, ventana2, ventana)
    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    
    
def Activar_Metodo_Multipasos():
    global ventana,ventana2

    ventana2 =ctk.CTk()
    ventana2.geometry("1500x800")
    ventana2.resizable(False,False)
    ventana2.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    ventana2.title("Metodo Multipasos") 

    
    # Deshabilitar el botón de minimizar
    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert') 


    #Creo un frame
    frame = ctk.CTkFrame(master=ventana2)
    frame.pack(expand=True, fill='both')


    #se manda a llamar la funcion
    Ventana_Multipasos(frame, ventana2, ventana)

    ventana.withdraw()
    ventana2.protocol("WM_DELETE_WINDOW", lambda: Volver(ventana2, ventana))
    ventana2.mainloop()
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------PROGRAMACION DE LOS BOTONES DE LA INTERFAZ GRAFICA--------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


#-------------------------Cuando se activa el boton de cualquier unidad---------------------------
boton_Unidad_2 = None
boton_Unidad_3 = None
boton_Unidad_4 = None
boton_Unidad_5 = None
#---------------------------------------------------------------------------------------------------

#----------------------------- Declaro todos los botones ------------------------------------------------

botones_activados = False
botones_dentro_activados_metodos_cerrados = False
botones_dentro_activados_metodos_abiertos = False
botones_dentro_activados_polinomios = False

#Botones unidad 2
boton_Metodos_cerrados = None
boton_Metodos_abiertos = None
boton_polinomios = None
#Botones dentro de la unidad 2
boton_metodo_biseccion = None
boton_falsa_posicion = None
boton_punto_fijo = None

boton_metodo_secante = None
boton_newton_raphson = None
boton_newton_raphson_modificado = None

boton_ecuaciones_cuadraticas = None
boton_metodo_tartaglia = None
boton_metodo_ferrari = None
boton_metodo_horner = None
boton_metodo_bairstown = None
boton_metodo_muller = None


#Botones de la unidad 3
boton_interpolacion_lineal = None
boton_Polinomio_interpolacion_laGrange = None
boton_Polinomio_interpolacion_newton = None
boton_diferencias_divididas = None
boton_interpolacion_hermite = None
boton_trazadores_cubicos = None

#Botones de la unidad 4
boton_diferenciacion_numerica = None
boton_extrapolacion_richardson = None
boton_integracion_numerica = None
boton_metodos_adaptativos = None
boton_cuadratura_gaussiana = None

#Botones de la unidad 5
boton_metodo_euler = None
boton_metodo_taylor = None
boton_metodo_runge_kutta = None
boton_metodo_multipasos = None
#---------------------------------------------------------------------------------------

#----------Darle colores o demas a los botones------------------------------------------

color_fondo_boton = "#2c2b4b"
color_texto = "white"
tipo_tamaño_letra = ("Roboto",14,"bold")
color_boton_pasar_mouse = "#5603b6"
color_borde  = "white"
ancho_borde = 2


#-----------------------------------------------------------------------------------------

 #-------------Boton Abandonar--------------------------------------------------------------------------------------------
def Abandonar():
    global ventana
    ventana.destroy()
#------------------------------------------------------------------------------------------------------------------------
        

def Ventana_Principal():
    global ventana,boton_Unidad_2,boton_Unidad_3,boton_Unidad_4,boton_Unidad_5

    #-------------------------Ventana principal--------------------------------------------
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    ventana = ctk.CTk()
    ventana.geometry("1500x800")
    ventana.title("ANALISIS NUMERICOS") 

    fondo = PhotoImage(file="Imagenes/3.png")
    label_fondo = Label(ventana, image=fondo)
    label_fondo.image = fondo 
    label_fondo.place(x=0, y=0)

    #ventana.iconbitmap("Imagenes/icono.ico")
    ventana.protocol("WM_DELETE_WINDOW", "onexit")  # desactivar el boton de cerrar
    #ventana.state("zoomed")
    ventana.resizable(False,False)

    # Deshabilitar el botón de minimizar
    #hwnd = ctypes.windll.user32.GetParent(ventana.winfo_id())
    #current_style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    #new_style = current_style & ~0x00020000 & ~0x00010000
    #ctypes.windll.user32.SetWindowLongW(hwnd, -16, new_style)

    ventana.update_idletasks()  # Asegúrate de que la ventana está completamente creada
    window_id = ventana.winfo_id()
    os.system(f'wmctrl -ir {window_id} -b add,maximized_horz,maximized_vert')

    #---------------------------------------------------------------------------------------


    #---- Botones de la unidad 5 -------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def Botones_Unidad_5():
        global botones_activados
        global boton_metodo_euler 
        global boton_metodo_taylor
        global boton_metodo_runge_kutta
        global boton_metodo_multipasos

        global color_fondo_boton 
        global color_texto
        global tipo_tamaño_letra
        global color_boton_pasar_mouse
        global color_borde
        global ancho_borde

        if not botones_activados:

            boton_metodo_euler = ctk.CTkButton(ventana,text="Metodo de Euler",command=Activar_Metodo_Euler,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_euler.place(x=1000,y=250)

            boton_metodo_taylor = ctk.CTkButton(ventana,text ="Metodo de Taylor",command=Activar_Metodo_Taylor,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_taylor.place(x=1000,y=350)

            boton_metodo_runge_kutta = ctk.CTkButton(ventana,text ="Metodo de Runge Kutta",command=Activar_Metodo_Runge_Kutta,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_runge_kutta.place(x=1000,y=450)

            boton_metodo_multipasos = ctk.CTkButton(ventana,text ="Metodos Multipasos",command=Activar_Metodo_Multipasos,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_multipasos.place(x=1000,y=550)

            botones_activados=True

            boton_Unidad_2.configure(state=DISABLED)
            boton_Unidad_3.configure(state=DISABLED)
            boton_Unidad_4.configure(state=DISABLED)

        else:
            boton_metodo_euler.destroy()
            boton_metodo_taylor.destroy()
            boton_metodo_runge_kutta.destroy()
            boton_metodo_multipasos.destroy()
            botones_activados=False

            boton_Unidad_2.configure(state=NORMAL)
            boton_Unidad_3.configure(state=NORMAL)
            boton_Unidad_4.configure(state=NORMAL)




    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




    #---- Botones de la unidad 4 -------------------------------------------------------------------------------------------------------------------------------------------------------------


    def Botones_Unidad_4():
        global botones_activados
        global boton_diferenciacion_numerica
        global boton_extrapolacion_richardson
        global boton_integracion_numerica 
        global boton_metodos_adaptativos
        global boton_cuadratura_gaussiana

        global color_fondo_boton 
        global color_texto
        global tipo_tamaño_letra
        global color_boton_pasar_mouse
        global color_borde
        global ancho_borde

        if not botones_activados:
            boton_diferenciacion_numerica = ctk.CTkButton(ventana,text ="Diferenciacion Numerica",command=Activar_Diferenciacion_Numerica,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_diferenciacion_numerica.place(x=700,y=250)

            boton_extrapolacion_richardson = ctk.CTkButton(ventana,text = "Extrapolacion de Richardson",command=Activar_Extrapolacion_Richardson,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_extrapolacion_richardson.place(x=700,y=350)

            boton_integracion_numerica = ctk.CTkButton(ventana,text ="Integracion Numerica",command=Activar_Integracion_Numerica,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_integracion_numerica.place(x=700,y=450)

            boton_metodos_adaptativos = ctk.CTkButton(ventana,text = "Metodos Adaptativos",command=Activar_Metodos_Adaptativos,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodos_adaptativos.place(x=1000,y=300)

            boton_cuadratura_gaussiana = ctk.CTkButton(ventana,text = "Cuadratura Gaussiana",command=Activar_Cuadratura_Gaussiana,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_cuadratura_gaussiana.place(x=1000,y=400)

            botones_activados=True

            boton_Unidad_2.configure(state=DISABLED)
            boton_Unidad_3.configure(state=DISABLED)
            boton_Unidad_5.configure(state=DISABLED)


        else:
            boton_diferenciacion_numerica.destroy()
            boton_extrapolacion_richardson.destroy()
            boton_integracion_numerica.destroy() 
            boton_metodos_adaptativos.destroy()
            boton_cuadratura_gaussiana.destroy()

            botones_activados=False

            boton_Unidad_2.configure(state=NORMAL)
            boton_Unidad_3.configure(state=NORMAL)
            boton_Unidad_5.configure(state=NORMAL)



    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    #---- Botones de la unidad 3 -------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Botones_Unidad_3():
        global botones_activados
        global boton_interpolacion_lineal 
        global boton_Polinomio_interpolacion_laGrange 
        global boton_Polinomio_interpolacion_newton 
        global boton_diferencias_divididas 
        global boton_interpolacion_hermite 
        global boton_trazadores_cubicos 

        global color_fondo_boton 
        global color_texto
        global tipo_tamaño_letra
        global color_boton_pasar_mouse
        global color_borde
        global ancho_borde

        if not botones_activados:

            boton_interpolacion_lineal = ctk.CTkButton(ventana,text = "Interpolacion Lineal",command=Activar_Interpolacion_Lineal,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_interpolacion_lineal.place(x=400,y=250)

            boton_Polinomio_interpolacion_laGrange = ctk.CTkButton(ventana,text="Interpolacion de LaGrange",command=Activar_Polinomio_Interpolacion_LaGrange,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_Polinomio_interpolacion_laGrange.place(x=400,y=350)

            boton_Polinomio_interpolacion_newton = ctk.CTkButton(ventana,text = "Interpolacion de Newton",command=Activar_Polinomio_Interpolacion_Newton,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_Polinomio_interpolacion_newton.place(x=400,y=450)

            boton_diferencias_divididas = ctk.CTkButton(ventana,text="Diferencias Divididas",command=Activar_Diferencias_Divididas,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_diferencias_divididas.place(x=700,y=250)

            boton_interpolacion_hermite = ctk.CTkButton(ventana,text ="Interpolacion de Hermite",command=Activar_Interpolacion_Hermite,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_interpolacion_hermite.place(x=700,y=350)

            boton_trazadores_cubicos = ctk.CTkButton(ventana,text = "Trazadores Cubicos",command=Activar_Trazadores_Cubicos,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_trazadores_cubicos.place(x=700,y=450)

            botones_activados=True
            boton_Unidad_2.configure(state=DISABLED)
            boton_Unidad_4.configure(state=DISABLED)
            boton_Unidad_5.configure(state=DISABLED)

        else : 
            boton_interpolacion_lineal.destroy()
            boton_Polinomio_interpolacion_laGrange.destroy()
            boton_Polinomio_interpolacion_newton.destroy()
            boton_diferencias_divididas.destroy()
            boton_interpolacion_hermite.destroy()
            boton_trazadores_cubicos.destroy()

            botones_activados=False

            boton_Unidad_2.configure(state=NORMAL)
            boton_Unidad_4.configure(state=NORMAL)
            boton_Unidad_5.configure(state=NORMAL)
                
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                        #FUNCIONALIDAD DEL BOTON DE LA UNIDAD 2

    #--- Botones dentro de cada metodo de la unidad 2 ---------------------------------------------------------------------------------------------------------------------------
    def Botones_Metodos_Cerrados():
        global botones_activados
        global botones_dentro_activados_polinomios
        global botones_dentro_activados_metodos_abiertos
        global botones_dentro_activados_metodos_cerrados

        global boton_metodo_biseccion 
        global boton_falsa_posicion 
        global boton_punto_fijo 

        global color_fondo_boton 
        global color_texto
        global tipo_tamaño_letra
        global color_boton_pasar_mouse
        global color_borde
        global ancho_borde


        if not botones_dentro_activados_metodos_cerrados:

            boton_metodo_biseccion = ctk.CTkButton(ventana,text = "Metodo Biseccion",command=Activar_Metodo_Biseccion,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_biseccion.place(x=400,y=250)

            boton_falsa_posicion = ctk.CTkButton(ventana,text = "Reglas de Falsa Posicion",command=Activar_Falsa_Posicion,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_falsa_posicion.place(x=675,y=250)

            boton_punto_fijo = ctk.CTkButton(ventana,text = "Punto Fijo",command=Activar_Punto_Fijo,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_punto_fijo.place(x=950,y=250)

            botones_dentro_activados_metodos_cerrados=True

        else:
            boton_metodo_biseccion.destroy()
            boton_falsa_posicion.destroy() 
            boton_punto_fijo.destroy()

            botones_dentro_activados_metodos_cerrados=False 



    def Botones_Metodos_Abiertos():
        global botones_activados
        global botones_dentro_activados_polinomios
        global botones_dentro_activados_metodos_abiertos
        global botones_dentro_activados_metodos_cerrados

        global boton_metodo_secante 
        global boton_newton_raphson 
        global boton_newton_raphson_modificado

        global color_fondo_boton 
        global color_texto
        global tipo_tamaño_letra
        global color_boton_pasar_mouse
        global color_borde
        global ancho_borde

        if not botones_dentro_activados_metodos_abiertos:

            boton_metodo_secante = ctk.CTkButton(ventana,text = "Metodo Secante",command=Activar_Metodo_Secante,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_secante.place(x=400,y=350)

            boton_newton_raphson  = ctk.CTkButton(ventana,text = "Newton Raphson",command=Activar_Newton_Raphson,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_newton_raphson.place(x=675,y=350)

            boton_newton_raphson_modificado = ctk.CTkButton(ventana,text  = "Newton Raphson Modificado",command=Activar_Newton_Raphson_Modificado,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_newton_raphson_modificado.place(x=950,y=350)

            botones_dentro_activados_metodos_abiertos=True
        else:
            boton_metodo_secante.destroy()
            boton_newton_raphson.destroy()
            boton_newton_raphson_modificado.destroy()

            botones_dentro_activados_metodos_abiertos=False



    def Botones_Polinomios():
        global botones_activados
        global botones_dentro_activados_polinomios
        global botones_dentro_activados_metodos_abiertos
        global botones_dentro_activados_metodos_cerrados

        global boton_ecuaciones_cuadraticas 
        global boton_metodo_tartaglia 
        global boton_metodo_ferrari 
        global boton_metodo_horner 
        global boton_metodo_bairstown 
        global boton_metodo_muller 

        global color_fondo_boton 
        global color_texto
        global tipo_tamaño_letra
        global color_boton_pasar_mouse
        global color_borde
        global ancho_borde

        if not botones_dentro_activados_polinomios:

            boton_ecuaciones_cuadraticas = ctk.CTkButton(ventana,text="Ecuaciones Cuadraticas",command=Activar_Ecuaciones_Cuadraticas,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_ecuaciones_cuadraticas.place(x=400,y=450)

            boton_metodo_tartaglia = ctk.CTkButton(ventana,text ="Metodo Tartaglia-gardano",command=Activar_Metodo_Tartaglia,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_tartaglia.place(x=675,y=450)

            boton_metodo_ferrari = ctk.CTkButton(ventana,text = "Metodo Ferrari",command=Activar_Metodo_Ferrari,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_ferrari.place(x=950,y=450)

            boton_metodo_horner = ctk.CTkButton(ventana,text = "Metodo Horner",command=Activar_Metodo_Horner,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_horner.place(x=400,y=550)

            boton_metodo_bairstown = ctk.CTkButton(ventana,text="Metodo Bairstown",command=Activar_Metodo_Bairstown,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_bairstown.place(x=675,y=550)

            boton_metodo_muller = ctk.CTkButton(ventana,text  ="Metodo Müller",command=Activar_Metodo_Muller,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_metodo_muller.place(x=950,y=550)

            botones_dentro_activados_polinomios=True
        
        else:
            boton_ecuaciones_cuadraticas.destroy() 
            boton_metodo_tartaglia.destroy()
            boton_metodo_ferrari.destroy() 
            boton_metodo_horner.destroy() 
            boton_metodo_bairstown.destroy() 
            boton_metodo_muller.destroy() 
            
            botones_dentro_activados_polinomios=False


    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        

    # Botones dentro de la Unidad 2 --------------------------------------------------------------------------------------------- 

    def Botones_Unidad_2():
        global botones_activados
        global botones_dentro_activados_polinomios
        global botones_dentro_activados_metodos_abiertos
        global botones_dentro_activados_metodos_cerrados

        global boton_Metodos_abiertos
        global boton_Metodos_cerrados
        global boton_polinomios

        global boton_metodo_biseccion 
        global boton_falsa_posicion 
        global boton_punto_fijo 

        global boton_metodo_secante 
        global boton_newton_raphson 
        global boton_newton_raphson_modificado 

        global boton_ecuaciones_cuadraticas 
        global boton_metodo_tartaglia 
        global boton_metodo_ferrari 
        global boton_metodo_horner 
        global boton_metodo_bairstown 
        global boton_metodo_muller 

        global color_fondo_boton 
        global color_texto
        global tipo_tamaño_letra
        global color_boton_pasar_mouse
        global color_borde
        global ancho_borde



        #si no se han activado los botones
        if not botones_activados and not botones_dentro_activados_metodos_cerrados and not botones_dentro_activados_metodos_abiertos and not botones_dentro_activados_polinomios:
            boton_Metodos_cerrados = ctk.CTkButton(ventana,text="Metodos Cerrados",command=Botones_Metodos_Cerrados,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_Metodos_cerrados.place(x=100,y=250)

            boton_Metodos_abiertos = ctk.CTkButton(ventana,text="Metodos Abiertos",command=Botones_Metodos_Abiertos,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_Metodos_abiertos.place(x=100,y=350)

            boton_polinomios = ctk.CTkButton(ventana,text="Polinomios",command=Botones_Polinomios,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
            boton_polinomios.place(x=100,y=450)

            botones_activados=True
            boton_Unidad_3.configure(state=DISABLED)
            boton_Unidad_4.configure(state=DISABLED)
            boton_Unidad_5.configure(state=DISABLED)

        else:
            #Cuado los botones ya estan activados


            #Si ningun boton interno esta activado
            if botones_dentro_activados_metodos_cerrados==False and botones_dentro_activados_metodos_abiertos==False and botones_dentro_activados_polinomios==False:
                boton_Metodos_abiertos.destroy()
                boton_Metodos_cerrados.destroy()
                boton_polinomios.destroy()

                botones_activados=False

                boton_Unidad_3.configure(state=NORMAL)
                boton_Unidad_4.configure(state=NORMAL)
                boton_Unidad_5.configure(state=NORMAL)

            #Si todos los botones internos estan abiertos
            elif botones_dentro_activados_metodos_cerrados==True and botones_dentro_activados_metodos_abiertos==True and botones_dentro_activados_polinomios==True:
                boton_metodo_biseccion.destroy() 
                boton_falsa_posicion.destroy() 
                boton_punto_fijo.destroy() 

                boton_metodo_secante.destroy() 
                boton_newton_raphson.destroy() 
                boton_newton_raphson_modificado.destroy() 

                boton_ecuaciones_cuadraticas.destroy() 
                boton_metodo_tartaglia.destroy() 
                boton_metodo_ferrari.destroy() 
                boton_metodo_horner.destroy() 
                boton_metodo_bairstown.destroy() 
                boton_metodo_muller.destroy()

                boton_Metodos_abiertos.destroy()
                boton_Metodos_cerrados.destroy()
                boton_polinomios.destroy()

                botones_dentro_activados_metodos_cerrados = False
                botones_dentro_activados_metodos_abiertos  = False
                botones_dentro_activados_polinomios = False
                botones_activados=False

                boton_Unidad_3.configure(state=NORMAL)
                boton_Unidad_4.configure(state=NORMAL)
                boton_Unidad_5.configure(state=NORMAL)

            # Si algun boton se encuentra activado
            elif  botones_dentro_activados_metodos_cerrados==True or botones_dentro_activados_metodos_abiertos==True or botones_dentro_activados_polinomios==True: 

                #Si solo esta activado el de los metodos abiertos
                if botones_dentro_activados_metodos_abiertos==True and botones_dentro_activados_metodos_cerrados==False and botones_dentro_activados_polinomios==False:
                    boton_metodo_secante.destroy() 
                    boton_newton_raphson.destroy() 
                    boton_newton_raphson_modificado.destroy() 

                    boton_Metodos_abiertos.destroy()
                    boton_Metodos_cerrados.destroy()
                    boton_polinomios.destroy()

                    botones_activados=False
                    botones_dentro_activados_metodos_abiertos=False

                    boton_Unidad_3.configure(state=NORMAL)
                    boton_Unidad_4.configure(state=NORMAL)
                    boton_Unidad_5.configure(state=NORMAL)



                #Si solo esta activado el de los metodos cerrados
                elif botones_dentro_activados_metodos_cerrados==True and botones_dentro_activados_metodos_abiertos==False and botones_dentro_activados_polinomios==False:
                    boton_metodo_biseccion.destroy()
                    boton_falsa_posicion.destroy() 
                    boton_punto_fijo.destroy()

                    boton_Metodos_abiertos.destroy()
                    boton_Metodos_cerrados.destroy()
                    boton_polinomios.destroy()

                    botones_activados=False
                    botones_dentro_activados_metodos_cerrados=False 
                    
                    boton_Unidad_3.configure(state=NORMAL)
                    boton_Unidad_4.configure(state=NORMAL)
                    boton_Unidad_5.configure(state=NORMAL)

                #Si solo esta activado el de los polinomios
                elif botones_dentro_activados_polinomios==True and botones_dentro_activados_metodos_cerrados==False and botones_dentro_activados_metodos_abiertos==False:
                    boton_ecuaciones_cuadraticas.destroy() 
                    boton_metodo_tartaglia.destroy()
                    boton_metodo_ferrari.destroy() 
                    boton_metodo_horner.destroy() 
                    boton_metodo_bairstown.destroy() 
                    boton_metodo_muller.destroy() 

                    boton_Metodos_abiertos.destroy()
                    boton_Metodos_cerrados.destroy()
                    boton_polinomios.destroy()

                    botones_activados=False
                    botones_dentro_activados_polinomios=False
                    
                    boton_Unidad_3.configure(state=NORMAL)
                    boton_Unidad_4.configure(state=NORMAL)
                    boton_Unidad_5.configure(state=NORMAL)


                #Si esta activado el metodo abierto y el cerrado
                elif botones_dentro_activados_metodos_abiertos==True and botones_dentro_activados_metodos_cerrados==True and botones_dentro_activados_polinomios==False:
                    boton_metodo_secante.destroy() 
                    boton_newton_raphson.destroy() 
                    boton_newton_raphson_modificado.destroy() 

                    boton_metodo_biseccion.destroy()
                    boton_falsa_posicion.destroy() 
                    boton_punto_fijo.destroy()

                    boton_Metodos_abiertos.destroy()
                    boton_Metodos_cerrados.destroy()
                    boton_polinomios.destroy()

                    botones_activados=False
                    botones_dentro_activados_metodos_cerrados=False 
                    botones_dentro_activados_metodos_abiertos=False

                    boton_Unidad_3.configure(state=NORMAL)
                    boton_Unidad_4.configure(state=NORMAL)
                    boton_Unidad_5.configure(state=NORMAL)

                #Si esta activado el metodo abierto y polinomio
                elif botones_dentro_activados_metodos_abiertos==True and botones_dentro_activados_polinomios==True and botones_dentro_activados_metodos_cerrados==False:
                    boton_metodo_secante.destroy() 
                    boton_newton_raphson.destroy() 
                    boton_newton_raphson_modificado.destroy()

                    boton_ecuaciones_cuadraticas.destroy() 
                    boton_metodo_tartaglia.destroy()
                    boton_metodo_ferrari.destroy() 
                    boton_metodo_horner.destroy() 
                    boton_metodo_bairstown.destroy() 
                    boton_metodo_muller.destroy() 

                    boton_Metodos_abiertos.destroy()
                    boton_Metodos_cerrados.destroy()
                    boton_polinomios.destroy()

                    botones_activados=False
                    botones_dentro_activados_polinomios=False
                    botones_dentro_activados_metodos_abiertos=False

                    boton_Unidad_3.configure(state=NORMAL)
                    boton_Unidad_4.configure(state=NORMAL)
                    boton_Unidad_5.configure(state=NORMAL)


                #Si esta abierto el metodo cerrado y el polinomio
                elif botones_dentro_activados_metodos_cerrados==True and botones_dentro_activados_polinomios==True and botones_dentro_activados_metodos_abiertos==False:
                    boton_metodo_biseccion.destroy()
                    boton_falsa_posicion.destroy() 
                    boton_punto_fijo.destroy()

                    boton_ecuaciones_cuadraticas.destroy() 
                    boton_metodo_tartaglia.destroy()
                    boton_metodo_ferrari.destroy() 
                    boton_metodo_horner.destroy() 
                    boton_metodo_bairstown.destroy() 
                    boton_metodo_muller.destroy() 

                    boton_Metodos_abiertos.destroy()
                    boton_Metodos_cerrados.destroy()
                    boton_polinomios.destroy()

                    botones_activados=False
                    botones_dentro_activados_polinomios=False
                    botones_dentro_activados_metodos_cerrados=False

                    boton_Unidad_3.configure(state=NORMAL)
                    boton_Unidad_4.configure(state=NORMAL)
                    boton_Unidad_5.configure(state=NORMAL)
        

    #----- BOTONES DONDE SE MUESTRAN LAS UNIDADES --------------------------------------------------------------------------------------
    boton_Unidad_2 = ctk.CTkButton(ventana,text = "Unidad 2",command=Botones_Unidad_2,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
    boton_Unidad_2.place(x=100,y=100)

    boton_Unidad_3 = ctk.CTkButton(ventana,text = "Unidad 3",command=Botones_Unidad_3,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
    boton_Unidad_3.place(x=400,y=100)

    boton_Unidad_4 = ctk.CTkButton(ventana,text = "Unidad 4",command=Botones_Unidad_4,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
    boton_Unidad_4.place(x=700,y=100)

    boton_Unidad_5 = ctk.CTkButton(ventana,text = "Unidad 5",command=Botones_Unidad_5,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 80,width=250,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
    boton_Unidad_5.place(x=1000,y=100)

    boton_abandonar = ctk.CTkButton(ventana,text = "Salir",command=Abandonar,fg_color = color_fondo_boton,text_color = color_texto,font = tipo_tamaño_letra,height = 40,width=120,hover_color=color_boton_pasar_mouse,border_color=color_borde,border_width=ancho_borde)
    boton_abandonar.pack(side="bottom", anchor="sw", padx=10, pady=10)

    #----------------------------------------------------------------------------------------------------------------------------

    ventana.mainloop() #Se muestra en pantalla

    return ventana

