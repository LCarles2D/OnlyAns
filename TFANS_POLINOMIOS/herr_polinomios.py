#metodos de uso comun entre metodos
import re
import sympy as sp
from sympy import degree
import numpy as np
import matplotlib.pyplot as plt

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
	-Ecuaciones cuadráticas                     (hh)    ✅
	-Ecuaciones cubicas (tartaglia-gardano)     (hh)    ✅
	-Ecuaciones cuarticas (Ferrari)             (hh)    ✅
	-Horner (de grado mayor a cuatro)           (hh)    ✅
	-Bairstown                                  (hh)    👀
	-Müller                                     (hh)    ✅ 

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


def validar_expresion(expresion):
    
    patron = r'^(\s*\d+|\+|\-|\{1,2}|/|\(|\)|x|e|sin\(x\)|cos\(x\)|tan\(x\)|asin\(x\)|acos\(x\)|atan\(x\)|log\(x\)|ln\(x\)|sqrt\(x\)|sqrt\d\(x\))\s$'
    if re.match(patron,  expresion):
        #print(type(expresion))
        return True
    else:
        print("Error: validar_expresion: La epresion posee caracteres no validos")
        return False
    
def validar_funcion(funcion):
    x = sp.symbols("x")
    U = sp.symbols("U")
    if funcion == None:
        #"Error: validar_funcion: la funcion recibida esta vacia"
        return None
    if isinstance(funcion, str):
        try:
            funcion_valida = sp.simplify(funcion)
            return funcion_valida
        except (sp.SympifyError, sp.SimplifyError) as e:
            print(f"Error: validar_funcion: al simplificar la función: {e}")
            return None
    if isinstance(funcion, sp.Basic):
        return funcion    

def validar_igualdad(expresion):
    igualdad = False
    for caracter in expresion:
        if caracter == '=':
            igualdad = True
    if igualdad == True:
        #separar la ecuación en el lado izquierdo y derecho del signo igual
        lado_izquierdo, lado_derecho = expresion.split('=')
        
        #parsear las expresiones usando sympy
        lado_izquierdo = sp.sympify(lado_izquierdo.strip())
        lado_derecho = sp.sympify(lado_derecho.strip())
        
        #mover todos los términos al lado izquierdo restando el lado derecho
        nueva_ecuacion = lado_izquierdo - lado_derecho
        
        #simplificar la ecuación resultante
        nueva_ecuacion = sp.simplify(nueva_ecuacion)
        
        #crear la ecuación igualada a 0
        nueva_ecuacion_str = f"{nueva_ecuacion}"
        
        return nueva_ecuacion_str    
    else: 
        return expresion
    

    if isinstance(numero, tipo):
        return numero
    else:
        try:
            valor = tipo(numero)
            return valor
        except ValueError as e:
            print("Error: validar_numero: ",e)
            return None

def convert_numeros(numero):
    return

def validar_limites(lim_a, lim_b):
    # Intentar convertir los límites a tipo float
    limite_inferior = lim_a
    limite_superior = lim_b
    if not isinstance(lim_a, int):
        try:
            limite_inferior = int(lim_a)
        except ValueError as e:
            try:
                limite_inferior = float(lim_a)
            except ValueError as e:
                limite_inferior = None
                impr("Error: validar_limite: El límite inferior debe ser un numero entero o decimal")
    if not isinstance(lim_b, int):
        try:
            limite_superior = int(lim_b)
        except ValueError as e:
            try:
                limite_superior = float(lim_b)
            except ValueError as e:
                limite_superior = None
                impr("Error: validar_superior: El límite inferior debe ser un numero entero o decimal")

    if not limite_inferior == None and not limite_superior == None:
        # Validar que el límite inferior sea menor que el límite superior
        if limite_inferior >= limite_superior:
            impr("lima: ",limite_inferior)
            impr("limb: ",limite_superior)
            impr("Error: validar_limites: El límite inferior debe ser menor que el límite superior")
            return None, None, 

        # Retornar los valores validados
        return limite_inferior, limite_superior

def validar_numero_int(numero, mensaje_err = None):
    if isinstance(numero, int):
        return numero
    if mensaje_err == None:
        mensaje_err = ""
    try:
        valor = int(numero)
        return valor
    except ValueError as e:    
        print(f"Error: validar_numero_int {mensaje_err}")
        return None

def validar_numero_float(numero, mensaje_err = None):
    if isinstance(numero, float):
        return numero
    if mensaje_err == None:
        mensaje_err = ""
    try:
        valor = float(numero)
        return valor
    except ValueError as e:    
        print(f"Error: validar_numero_float {mensaje_err}")
        return None

def validar_numero_gen(numero):
    err = ""
    if isinstance(numero, int):
        return numero
    elif isinstance(numero, float):        
        return numero
    else: 
        try:
            valor = int(numero)
            #retorna un numero entero (int)
            return valor
        except ValueError as e:
            err = err + e
            try:
                valor = float(numero)
                #retorna un numero entero (int)
                return valor
            except ValueError as e:
                err = err + e
                print("Error: validar_numero_gen: el numero no es de tipo (int) o (float) y no se puede convertir")
    
def calcular_Es(cifrasSignificativas):
    Es = (0.5*10**(2 - cifrasSignificativas))
    return Es

def obtener_coeficientes(funcion):
    #necesita (funcion)
    x = sp.symbols('x')
    #convertir la expresión a un polinomio
    polinomio = sp.Poly(funcion, x)
    #obtener los coeficientes
    coeficientes = polinomio.all_coeffs()
    tupla_coeficientes = tuple(coeficientes)
    #print("coeficientes: ",coeficientes)
    return tupla_coeficientes

def obtener_Es(cs):
    # Verificar si CS se puede convertir a un entero
    try:
        cs_int = int(cs)
    except ValueError:
        return "Error: CS debe ser convertible a un número entero."

    # Validar que CS sea mayor o igual a cero
    if cs_int < 0:
        return "Error: CS debe ser mayor o igual a cero."

    # Calcular Es
    es = 0.5 * 10 ** (2 - cs_int)
    return es

def obtener_grado(funcion):
    #necesita (funcion)
    #print("coeficientes: ",type(funcion))
    if funcion == None:
        return "Error: obtener_grado: lista de coeficientes vacia"
    try:
        polinomio = sp.Poly(funcion)
        grado = polinomio.degree()
        #print("grado: ",grado)
        return grado
    except sp.SympifyError:
        return "Error: La expresión no se pudo simplificar."    

def impr(text, elemento = None):
    if elemento == None:
        print(f"{text}")
    else:
        print(f"{text}: {elemento}")

def imprT(text, elemento = None):
    print(f"{text}: {elemento}, type: ,{type(elemento)}")

def validar_raices(soluciones_x):
    # Asegurarse de que soluciones_x sea una lista
    if not isinstance(soluciones_x, list):
        soluciones_x = [soluciones_x]

    # Filtrar y evaluar los valores reales
    valores_x = [sol.evalf() for sol in soluciones_x if sol.is_real]
    return valores_x

def impr_grafico(expresion, funcion, valores_x):
    x = sp.symbols('x')
    funcion_gf = sp.lambdify(x, funcion, 'numpy')
    valores_x_np = np.array(valores_x, dtype=float)

    x_vals = np.linspace(-10, 10, 400)
    y_vals = funcion_gf(x_vals)

    # Graficar la función
    plt.plot(x_vals, y_vals, color='blue', linestyle='--', linewidth=2, label=expresion)

    # Agregar puntos específicos
    if len(valores_x_np) > 0:
        puntos_y = funcion_gf(valores_x_np)
        plt.scatter(valores_x_np, puntos_y, color='red', marker='o', label='Puntos')

    # Agregar títulos y etiquetas
    plt.title('Gráfico de ' + expresion)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    # Mostrar la leyenda
    plt.legend()
    # Mostrar el gráfico
    plt.show()

def division_sintetica(coeficientes, divisor):
    #necesita (coeficientes) y (divisor)
    if len(coeficientes) == 0 or coeficientes == None:
        return "Error: division_sintetica: lista de coeficientes vacia"
    if divisor == 0 or divisor == None:
        return "Error: division_sintetica: divisor esta vacia"

    resultado = [coeficientes[0]]
    
    #división sintética
    for i in range(1, len(coeficientes)):
        resultado.append(coeficientes[i] + divisor * resultado[-1])
    
    residuo = resultado.pop()
    residuo = sp.simplify(residuo)
    nresiduo = sp.N(residuo, 5)
    
    return resultado, residuo ,nresiduo





"""# validar funcion
expresion = "sin(x)"
resultado = validar_funcion(expresion)
print(resultado)"""

"""# grado
expresion = "2*x**4 + 3*x**2 + 2*x + 1"
coeficientes, grado = obtener_grado(expresion)
print(f"Coeficientes: {coeficientes}")
print(f"Grado: {grado}")"""

"""# division sintetica
# Representa el polinomio 3x^3 - 6x^2 + 2x - 1
coeficientes = (6, 5, 3, 1)
divisor = -0.45  # Representa el divisor (x - 2)
cociente, residuo, nresiduo = division_sintetica(coeficientes, divisor)
print(f"coeficientes: {coeficientes}, divisor: {divisor}")
print(f"Cociente: {cociente}")
print(f"Residuo: {residuo}")
print(f"Residuo simplificado: {nresiduo}")
print("---------------------------------------------------------------")
cociente, residuo, nresiduo = division_sintetica(cociente, divisor)
print(f"coeficientes: {cociente}, divisor: {divisor}")
print(f"Cociente: {cociente}")
print(f"Residuo: {residuo}")
print(f"Residuo simplificado: {nresiduo}")"""



