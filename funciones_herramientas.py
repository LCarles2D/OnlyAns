#AL FINAL ESTAN LAS NUEVAS FUNCIONES
import math
import re
from tkinter import messagebox
from typing import List, Optional
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import sympy as sp
from sympy import Poly, parse_expr
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import pandas as pd
from IPython.display import display


"""CREAR UN PROGRAMA PARA LAS UNIDADES;
A) SOLUCION DE ECUACION DE UNA SOLA VARIABLE
-Métodos cerrados
	--Bisección
	--Regla de falsa posición
	--Punto fijo
-Métodos abiertos
	--Secante
	--Newton Raphson
	--Newton Raphson Modificado
Polinomios
	-Ecuaciones cuadráticas                     (hh)    ✅✅
	-Ecuaciones cubicas (tartaglia-gardano)     (hh)    ✅✅
	-Ecuaciones cuarticas (Ferrari)             (hh)    ✅✅
	-Horner (de grado mayor a cuatro)           (hh)    ✅✅
	-Bairstown                                  (hh)    ✅✅
	-Müller                                     (hh)    ✅✅ 

B) INTERPOLACION Y APROXIMACION LINEAL
-Interpolación lineal
-Polinomio de interpolación de LaGrange
-Polinomio de interpolación de Newton
-Diferencias divididas
-Interpolación de Hermite
-Trazadores cúbicos

C) DIFERENCIACION E INTEGRACION
-Diferenciación numérica
-Extrapolación de Richardson
-Integración numérica                           (hh)    👨🏽‍💻
    -Trapecio Simple                                    👨🏽‍💻
    -Trapecio Compuesto                                 👨🏽‍💻
    -Simpson 1/3                                        👨🏽‍💻
    -Simpson 3/8                                        👨🏽‍💻
-Métodos adaptativos
-Cuadratura Gaussiana

D) PROBLEMAS DE VALOR INICIAL
-Teoría elemental de los problemas de valor inicial para EDO
-Método de Euler
-Método de Taylor                               (hh)    👨🏽‍💻
-Método Runge Kutta
-Métodos multipasos                             (hh)    👨🏽‍💻
"""

"""::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
#::Herramientas de validacion::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::validar si esta vacio
def validar_vacio(expresion):
    if expresion == "" or expresion == None:
        return False

    return True

def validar_vacio_g(elementos: dict):
    Mensaje = ""

    for key, value in elementos.items():
        if not value.strip():  # Verificar si el valor está vacío o solo contiene espacios
            Mensaje += f"Parámetro '{key}' está vacío.\n"

    return Mensaje

#::validar si posee caracteres permitidos
def validar_caracteres(expresion):
    Error = ""

    caracteres_no_permitidos = r'|!"#$&\'?¿¡´:_@<>~`°\¬,\\'

    caracteres_encontrados = [char for char in expresion if char in caracteres_no_permitidos]
    
    if caracteres_encontrados:
        if len(caracteres_encontrados) == 1:
            Error = f"La expresion posee este valor no permitido: {caracteres_encontrados[0]}"
        else:
            Error = f"La expresion posee estos valores no permitidos: {caracteres_encontrados}"

    return expresion, Error

#::validar signos de agrupacion
def validar_PCL(expresion):                                                       
    char1, char2, char3, char4, char5, char6 = '(', ')','{','}','[',']'
    Error = ""
    contador = 0
    #parentesis
    for char in expresion:
        if char == char1:
            contador += 1
        elif char == char2:
            contador -= 1
    if contador > 0:
        er1 = f"Hay {contador} {char1} que no ha sido cerrado\n"
        Error = Error + er1       

    if contador < 0:
        er1 = f"Hay {abs(contador)} {char2} que no ha sido iniciado\n" 
        Error = Error + er1

    contador2 = 0       
    #corchetes     
    for char in expresion:
        if char == char3:
            contador2 += 1
        elif char == char4:
            contador2 -= 1
    if contador2 > 0:
        er2 = f"Hay {contador2} {char3} que no ha sido cerrado\n"    
        Error = Error + er2

    if contador2 < 0:
        er2 = f"Hay {abs(contador2)} {char4} que no ha sido iniciado\n"     
        Error = Error + er2

    contador3 = 0
    #llaves
    for char in expresion:
        if char == char5:
            contador3 += 1
        elif char == char6:
            contador3 -= 1                
    if contador3 > 0:
        er3 = f"Hay {contador3} {char5} que no ha sido cerrado\n"      
        Error = Error + er3 
    if contador3 < 0:
        er3 = f"Hay {abs(contador3)} {char6} que no ha sido iniciado\n"   
        Error = Error + er3
        
    return expresion, Error

#::validar numeros
def validar_numeros(numero, tipo:str = None):
    Error = ""
    if tipo == None:
        if isinstance(numero, (int, float)):
            return numero, Error
        elif isinstance(numero, str):
            try:
                num = float(numero)
                return num, Error
            except ValueError as err:
                Error = f"Error {numero} no es un numero (int o float)"
                return numero, Error
    elif tipo == "int":        
        try:
            num = int(numero)
            return num, Error
        except ValueError as err:
            Error = f"Error {numero} no es un numero (int o float)"
            return numero, Error
        

#::validar si es una igualdad y normalizarla
def validar_igualdad(expresion):
    error = ""
    funcion = None  # Inicializamos la variable función
    
    try:
        if isinstance(expresion, str):
            # Contar el número de signos '='
            contador = expresion.count('=')
            
            if contador == 1:
                # Separar la ecuación en el lado izquierdo y derecho del signo igual
                lado_izquierdo, lado_derecho = expresion.split('=')
                
                # Parsear las expresiones usando Sympy con transformaciones para la multiplicación implícita
                lado_izquierdo = parse_expr(lado_izquierdo.strip(), transformations=standard_transformations + (implicit_multiplication_application,))
                lado_derecho = parse_expr(lado_derecho.strip(), transformations=standard_transformations + (implicit_multiplication_application,))
                
                # Mover todos los términos al lado izquierdo restando el lado derecho
                nueva_ecuacion = lado_izquierdo - lado_derecho
                
                # Simplificar la ecuación resultante
                nueva_ecuacion = sp.simplify(nueva_ecuacion)
                
                # Crear la ecuación igualada a 0
                funcion = sp.Eq(nueva_ecuacion, 0)
                
            elif contador > 1:
                error = "La expresión no puede poseer más de un '='"
            else:
                # Si no hay '=', asumimos que es una expresión igualada a 0
                funcion = parse_expr(expresion, transformations=standard_transformations + (implicit_multiplication_application,))
                funcion = sp.Eq(funcion, 0)
        
        elif isinstance(expresion, sp.Basic):
            # Si la entrada es una expresión de SymPy, convertirla en una igualdad igualándola a 0
            funcion = sp.Eq(expresion, 0)
        
        else:
            error = "La expresión proporcionada debe ser una cadena (str) o un objeto de SymPy"

    except Exception as e:
        error = f"Ha ocurrido un error: {e}"
    
    return funcion, error

def validar_funcion_x(expresion):
    Error = ""
    while True:
        try:
            funcion = sp.sympify(expresion)
            
            # Verificar que todas las variables en la expresión sean simbólicas
            if not all(isinstance(sym, sp.Symbol) for sym in funcion.free_symbols):
                Error = "La función debe contener solo variables simbólicas."
                return funcion, Error
            # Si no hay errores, retornamos la función y un error vacío
            return funcion, Error
        except (sp.SympifyError, TypeError, ValueError):
            Error = "Entrada inválida. Por favor, ingrese una función válida en términos de variables simbólicas."
            return expresion, Error   
        
def validar_funcion_xyz(expresion: str):
    # Definir las variables simbólicas posibles
    x, y, z = sp.symbols('x y z')
    variables_validas = {x, y, z}
    Error = ""

    try:
        # Convertir la expresión a una función simbólica
        funcion = sp.sympify(expresion)
        
        # Verificar que todas las variables en la expresión sean simbólicas y sean x, y o z
        if not funcion.free_symbols.issubset(variables_validas):
            Error = ("La función debe contener solo las variables x, y o z.")
            return None, [], Error
        
        # Obtener las variables válidas encontradas en la expresión
        lista_variables = list(funcion.free_symbols)
        
        return funcion, lista_variables, Error
    
    except (sp.SympifyError, TypeError, ValueError) as e:
        Error = f"Error: validar_funcion_xyz: {e}"
        return None, [], Error

def evaluar_funcion(funcion: sp.Expr, valores: dict) -> sp.Expr:
    # Evaluar la función en los valores dados
    resultado = funcion.subs(valores)
    return resultado        

"""
expresion_y = "y**2 + 3*y + 2"
funcion_y, mensaje_y = validar_y_convertir_funcion(expresion_y)
print(mensaje_y)

if funcion_y:
    puntos_y = [1.0, 2.0, 3.0]
    for punto in puntos_y:
        try:
            valor_evaluado_y = evaluar_funcion(funcion_y, {sp.Symbol('y'): punto})
            print(f"y = {punto}, f(y) = {valor_evaluado_y.evalf()}")
        except Exception as e:
            print(f"Error al evaluar en y = {punto}: {e}")
"""

def convert_funcion_x(expresion):
    x = sp.symbols('x')
    funcion = sp.lambdify(expresion)
    return funcion

def validar_funcion(expresion):
    Error = ""
    try:
        # Asegurarse de que la expresión sea una cadena de texto
        if not isinstance(expresion, str):
            expresion_str = str(expresion)
        else:
            expresion_str = expresion
        
        # Detectar todas las letras en la cadena de texto (excepto letras reservadas por SymPy como 'I' para la unidad imaginaria)
        letras = re.findall(r'[a-zA-Z]', expresion_str)
        
        # Crear un conjunto de letras únicas para evitar duplicados
        letras_unicas = list(set(letras))
        
        # Declarar variables simbólicas para cada letra
        variables = sp.symbols(' '.join(letras_unicas))
        
        # Asegurarse de que variables sea siempre una lista, incluso si solo hay un elemento
        if isinstance(variables, sp.Symbol):
            variables = [variables]
        
        # Crear un diccionario de mapeo de nombres a símbolos
        diccionario_variables = dict(zip(letras_unicas, variables))
        
        # Convertir la cadena de texto en una expresión simbólica utilizando el diccionario de variables
        expresion_simb = sp.sympify(expresion_str, locals=diccionario_variables)
        
        # Devolver la expresión simbólica y el diccionario de variables
        return expresion_simb, diccionario_variables, Error
    
    except (sp.SympifyError, TypeError, ValueError) as e:
        # Capturar cualquier error que ocurra durante el proceso de conversión
        Error = f"Error en la conversión de la expresión: {str(e)}"
        return None, None, Error
    
    #REVISAR
def validar_multiplicacion_implicita(expr):
    Error = ""
    try:
        if isinstance(expr, str):
            expr = parse_expr(expr, transformations=standard_transformations + (implicit_multiplication_application,))

        elif not isinstance(expr, sp.Basic):
            Error = "La expresión proporcionada debe ser una cadena (str) o un objeto de SymPy"
            
            return None, Error
        return expr, Error
    except Exception as e:
        
        Error = "Ha ocurrido un Error en validar_multiplicacion_implicita()\nposible problema en la entrada de datos."
        return None, Error

def validar_div_cero(expresion):
    try:
        # Convertir la expresión en una expresión simbólica de SymPy
        expr = sp.sympify(expresion)
        
        # Verificar si hay divisiones por cero en la expresión
        if any(sp.simplify(denom).is_zero for denom in expr.as_numer_denom()[1].atoms(sp.Pow)):
            return expresion, "Division entre cero"
        if any(denom.is_zero for denom in expr.as_numer_denom()[1].atoms(sp.Symbol)):
            return expresion, "Division entre cero"

        return expresion, ""
    except Exception as e:
        return expresion, f"Error al analizar la expresión: {e}"
    
"""::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
#::Herramientas de metodos:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#::ajuste de tablas pd
def ajustar_tabla_pandas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajusta el ancho de las columnas de un DataFrame de pandas según el ancho máximo de sus datos.

    :param df: DataFrame a ajustar.
    :return: DataFrame con los anchos de columna ajustados.
    """
    # Configurar los anchos máximos de cada columna
    max_ancho_columna = []
    for col in df.columns:
        max_ancho = max(df[col].astype(str).map(len).max(), len(col))
        max_ancho_columna.append(max_ancho)

    # Ajustar los anchos de las columnas
    for i, col in enumerate(df.columns):
        display(df.style.set_properties(subset=[col], **{'width': f'{max_ancho_columna[i]}ch'}))
    
    return df

#::calcular raiz cuadrada
def calcular_raiz_cuadrada(numero):
    Error = ""
    if numero < 0:
        Error = f'No se puede calcular la raíz cuadrada de un número negativo: {numero}'
        return numero, Error
    else:
        return math.sqrt(numero), Error

#::Division sintetica
def division_sintetica(coeficientes, divisor):
    Error = ""
    resultado = []
    
    # Verificar si coeficientes es una lista válida y tiene elementos
    if not isinstance(coeficientes, list) or len(coeficientes) == 0:
        Error = "La lista de coeficientes está vacía o no es válida"
        return resultado, Error
    
    try:
        # El primer coeficiente se mantiene
        resultado.append(float(coeficientes[0]))

        # Realizamos la división sintética
        for i in range(1, len(coeficientes)):
            # El nuevo coeficiente es el anterior más el producto del divisor y el resultado previo
            nuevo_coeficiente = float(coeficientes[i]) + float(divisor) * resultado[-1]
            resultado.append(nuevo_coeficiente)

        return resultado, Error
    except (ValueError, TypeError) as err:
        Error = f"Ha ocurrido un error en la división sintética: {err}"
        return [], Error

#::convertir cifras significativas
def calcular_Es(cifras_sigficativas):
    Error = ""
    try:
        Es = 0.5 * (10 ** (2 - cifras_sigficativas))
        return Es, Error 
    except ValueError as err:     
        Error = "Error al calcular Es"
        return cifras_sigficativas, Error
    
    #::convertir Error de Aproximacion
def calcular_Ea(aprx, vr):
    Error = ""
    try:
        Ea = abs((aprx - vr)/aprx)*100
        return Ea, Error
    except ValueError as err:
        Error = f"Error en calcular Ea: {err}"
        return None, Error    



#::guardado de coeficientes
def guardar_coeficientes(coeficientes, lista_variables):
    Error = ""
    if not isinstance(coeficientes, list):
        Error = "No se a pasado una lista con coeficientes"
        return None, Error
    
    if not isinstance(lista_variables, list):
        Error = "No se a pasado una lista con las variables"
        return None, Error
    
    if len(coeficientes) != len(lista_variables):
        Error = "La cantidad de coeficientes de la lista 1, y la cantidad de elementos de la lista 2 son diferentes"
        return None, Error
    else:
        for elemento in coeficientes:
            try:
                lista_variables[elemento] = coeficientes[elemento]
            except ValueError as err:    
                Error = "Error en la asignacion de coeficientes con las variables"
                return None, Error

#::Herramienta transportador
class Transportador:
    def __init__(self):
        self.contenedor = [] 

    def set_transportador(self, bloque):
        if isinstance(bloque, list):
            self.contenedor.extend(bloque)  
        else:
            self.contenedor.append(bloque) 
            
    def get_transportador(self, indice=None):
        if len(self.contenedor) == 0:
            return 0
        else:
            if indice is None or indice == "":
                return self.contenedor  
            else:
                if 0 <= indice < len(self.contenedor):
                    return self.contenedor[indice]  
                else:
                    return 0
                
    def obtener_todos(self):
        return self.contenedor 

#::obtener coeficientes
def obtener_coeficientes(expresion):
    Error = ""
    try:
        polinomio = sp.Poly(expresion)
        coeficientes = polinomio.all_coeffs()
        return coeficientes, Error
    except ValueError as err:
        Error = "Ha ocurrido un error a la hora de optener los coeficientes"
        return expresion, Error

#::obtener grado de la funcion
def obtener_grado(funcion, grado_esperado:int):
    Error = ""
    polinomio = sp.Poly(funcion)
    grado = polinomio.degree()
    if grado != grado_esperado:
        return grado, Error
    else:
        return grado, Error

#::obtener raices reales y raices imaginarias
def validar_raices(soluciones_x):
    reales = []
    imaginarias = []

    if isinstance(soluciones_x, list):
        for sol in soluciones_x:
            if isinstance(sol, (int, float)):
                reales.append(sol)
            elif isinstance(sol, complex):
                if sol.imag == 0:
                    reales.append(sol.real)
                else:
                    imaginarias.append(sol)
            else:
                imaginarias.append(sol)
    else:
        if isinstance(soluciones_x, (int, float)):
            reales.append(soluciones_x)
        elif isinstance(soluciones_x, complex):
            if soluciones_x.imag == 0:
                reales.append(soluciones_x.real)
            else:
                imaginarias.append(soluciones_x)
        else:
            imaginarias.append(soluciones_x)

    return reales, imaginarias

def validar_CamR_I(reales: list, imaginarios: list):
    Error = ""
    if isinstance(reales, list) and isinstance(imaginarios, list):
        num_ = f"{imaginarios[0]}"
        cont = 0
        for carac in num_:
            if carac == 'I':
                cont += 1
        if cont == 0:
            reales.append(imaginarios[0])
            imaginarios.clear()  
            return reales, imaginarios, Error

#::convertir numero a numeros con decimales
def convertir_float(valor):
    Error = ""
    try:
        val = float(valor)
        return val, Error
    except ValueError as e:
        Error = "Error al intentar convertir a float: ",valor
        return valor, Error
    
#::graficador    
    #1706
"""def Grafico(funcion, xvals):
    x = sp.symbols("x")
    funcion_numerica = sp.lambdify(x, funcion)
    
    if isinstance(xvals, list):
        # Crear figura y ejes
        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
        
        for X_r in xvals:
            # Verificar que X_r sea un número y no una lista
            if isinstance(X_r, (int, float)):
                # Definir el rango de valores de x para graficar alrededor de cada raíz
                valores_x = np.linspace(X_r - 5, X_r + 5, 1000)
                # Calcular los valores de y correspondientes
                valores_y = funcion_numerica(valores_x)
                
                # Graficar la función y la raíz encontrada por el método de la secante
                ax.plot(valores_x, valores_y, label=f"f(x) cerca de {X_r}", color="blue")
                ax.scatter(X_r, funcion_numerica(X_r), color="red", label=f"Raíz: {X_r}")
        
        # Agregar líneas de referencia y etiquetas
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Gráfico')
        ax.grid(True)

        # Evitar duplicación de etiquetas en la leyenda
        handles, labels = ax.get_legend_handles_labels()
        unique_labels = dict(zip(labels, handles))
        ax.legend(unique_labels.values(), unique_labels.keys())

        return fig"""

def Grafico(funcion, xvals):
    x = sp.symbols("x")
    funcion_numerica = sp.lambdify(x, funcion)
    list1 = []

    if isinstance(xvals, list):
        # Caso: xvals es una lista de valores
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        
        #1706
        list1.extend([float(posi) for posi in xvals])

    for X_r in list1:
        # Definir el rango de valores de x para graficar alrededor de cada raíz
        valores_x = np.linspace(X_r - 5, X_r + 5, 1000)
        # Calcular los valores de y correspondientes
        valores_y = funcion_numerica(valores_x)
        
        # Graficar la función y la raíz encontrada por el método de la secante
        ax.plot(valores_x, valores_y, label=str(funcion), color="blue")
        ax.scatter(X_r, funcion_numerica(X_r), color="red", label=f"Raíz: {X_r}")
        
        # Agregar líneas de referencia y etiquetas
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Gráfico')
        ax.grid(True)

        return fig

"""::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
#::Herramientas personales:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

