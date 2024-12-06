"""
Metodo de Horner
4 cifras significativas
P(x) = 1 + 3*x + 5*x**2 + 6*x**3
Xo=-0.45
"""
import sympy as sp
import pandas as pd
from sympy import symbols, sympify, parse_expr
from sympy.parsing.sympy_parser import parse_expr
from sympy import Poly
from sympy.parsing.sympy_parser import transformations,_T,standard_transformations,implicit_multiplication,convert_xor,implicit_application,function_exponentiation,implicit_multiplication_application,auto_symbol,auto_number,split_symbols
from sympy import Eq, solve
import herr_polinomios
from herr_polinomios import *

def Metodo_Horner(expresion, cifrasSignificativas, X0):
    print("----------------------Metodo de Horner----------------------")
    #Paso 1 -->Inicializar Xo
    Xo = validar_numero_gen(X0)
    print("Xo: ",Xo)

    #Paso 2 --> Calcular Es
    cifras_significativas = validar_numero_gen(cifrasSignificativas)
    print("Cifras significaticas: ",cifras_significativas)
    Es = 0
    if cifras_significativas == 0:
        Es = 0
        print("Nivel de tolerancia: ",Es, "%\n")
    else:     
        Es = calcular_Es(cifras_significativas)
        print("Nivel de tolerancia: ",Es, "%\n")

    #Paso 3 -->Realizar division sintetica dos veces
    x=symbols("x") # --> Definimos el simbolo
    #expresionm = 1 + 3*x + 5*x**2 + 6*x**3 # --> Creamos la expresion matematica
    #polinomio = Poly(expresionm) # --> La expresamos como polinomio
    #coeficientes=polinomio.all_coeffs() #-->Obtenemos los coheficientes
    #print(coeficientes)
    funcion = validar_funcion(expresion)
    coeficientes = obtener_coeficientes(funcion)
    print(f"funcion: {funcion} /:/ coeficientes: {coeficientes}")

    conteo=1
    df=pd.DataFrame(columns=["Iteracion","Xi","Ea %"])
    while True:
        #Ahora realizamos la division sintetica
        #Primera division sintetica
        n=len(coeficientes) #-->Tomamos la longitud de los coheficientes
        evaluacion= coeficientes[0] #--> evaluamos con el termino inicial
        D_sintetica_uno=[] 
        D_sintetica_uno.append(evaluacion)
        #Ahora iteramos desde el segundo termino
        for i in range(1,n):
            evaluacion=evaluacion*Xo + coeficientes[i]
            D_sintetica_uno.append(evaluacion)

        R=D_sintetica_uno[-1] #--> guardamos el ultimo elemento
    
        #Segunda division sintetica
        n=len(D_sintetica_uno) - 1#-->Tomamos la longitud de la primera division sintetica
        evaluacion=D_sintetica_uno[0] #-->evaluamos con el termino inicial
        D_sintetica_dos=[]
        D_sintetica_dos.append(evaluacion)
        #Ahora iteramos desde el segundo termino
        for i in range(1,n):
            evaluacion=evaluacion*Xo + D_sintetica_uno[i]
            D_sintetica_dos.append(evaluacion)

        S=D_sintetica_dos[-1] #--> guardamos el ultimo elemento

        #Paso 4 --> Utilizamos la formula de Xi=Xo-(R/S)
        Xi=Xo-(R/S)

        #Paso 5 --> Calculamos Ea
        Ea=abs((Xi-Xo)/(Xi))*100
        
        #Tabla para mostrar datos y tener un control de las evaluaciones
        df.loc[conteo-1]=[conteo,Xi,Ea] 
                
        #Si cumple la condicion se termina de iterar
        if Ea<Es:
            break
        conteo+=1
        Xo=Xi
    print(df)
    print(f"\nLa raiz aproximada es {Xi} con un error de {Ea} % en la {conteo} iteracion\n")

Metodo_Horner("1 + 3*x + 5*x**2 + 6*x**3", 4, -0.45)