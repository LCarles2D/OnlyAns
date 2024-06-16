
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

class herramientas:
     
    def IngresarEnCadena(marco, fuente, color, x, y, cantidad):
        ingresos = []
        for i in range(0, cantidad):
            ingresos.append(ctk.CTkEntry(marco,width=100,height=30,corner_radius=10,font = fuente,text_color=color))
            ingresos[i].place(x=x,y=(y + 30*i + 10*i))
        return ingresos
    def has_unique_values(arr):
        seen = set()
        for value in arr:
            if value in seen:
                return False
            seen.add(value)
        return True
#   


