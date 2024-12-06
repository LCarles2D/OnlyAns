
import sympy as sp
import pandas as pd
from sympy import symbols, sympify, parse_expr
from sympy.parsing.sympy_parser import parse_expr
from sympy import Poly
from sympy.parsing.sympy_parser import transformations,_T,standard_transformations,implicit_multiplication,convert_xor,implicit_application,function_exponentiation,implicit_multiplication_application,auto_symbol,auto_number,split_symbols
from sympy import Eq, solve
import herr_polinomios 
from herr_polinomios import *

def Metodo_Muller(expresion, x0, x1, x2, cifrasSignificativas):
    
    #Paso 1 --> inicializar las variables
    X0 = validar_numero_gen(x0)
    X1 = validar_numero_gen(x1)
    X2 = validar_numero_gen(x2) 
    #x0, x1, x2, no pueden ser iguales todos
    if X0 == X1:
        if (X2 == X0 or X2 == X1):
            print("X0, X1, X2 no pueden ser las tres iguales")  
            exit()
    if X0 == X2:
        if (X1 == X0 or X1 == X2):
            print("X0, X1, X2 no pueden ser las tres iguales")  
            exit()
    if X1 == X2:
        if (X0 == X1 or X0 == X2):
            print("X0, X1, X2 no pueden ser las tres iguales")  
            exit()        
            
    print(f"Xo: {X0}\nX1: {X1}\nX2: {X2}")
    

    #Paso 2 --> Determinar Es
    cifras_significativas = validar_numero_gen(cifrasSignificativas)
    Es = 0
    if cifras_significativas == 0:
        Es = 0
        print("Nivel de tolerancia: ",Es, "%\n")
    else:     
        Es = calcular_Es(cifras_significativas)
        print("Nivel de tolerancia: ",Es, "%\n")
    

    #Paso 3 --> Calcular la funcion con los valores iniciales
    x=symbols("x") 
    funcion = validar_funcion(expresion)
    f=sp.lambdify(x,funcion)  #--> Se va a evaluar la expresion

    conteo=1
    df=pd.DataFrame(columns=["Iteracion","Xi","Ea %"])
    while True:
        #se evalua en la funcion los valores iniciales
        f0=f(X0) 
        f1=f(X1)
        f2=f(X2)

        #Paso 4 --> Calcular ho y hi
        ho=X1-X0
        hi=X2-X1

        #Paso 5 --> Calcular S0 y S1
        S0=(f1-f0)/(ho)
        S1=(f2-f1)/(hi)

        #Paso 6 --> Calcular a,b,c
        a=(S1-S0)/(hi+ho)
        b=(a*hi)+S1
        c=f2

        #Paso 7 --> calcular el discriminante
        D=sp.sqrt((b**2)-(4*a*c))

        # Paso 8 -->Condicion
        if (abs(b+D))>(abs(b-D)):
            Xr=X2+((-2*c)/(b+D))
        else:
            Xr=X2+((-2*c)/(b-D))

        #Paso 9 -->Calcular Ea
        Ea=(abs((Xr-X2)/(Xr)))*100

        #Tabla para mostrar datos y tener un control de las evaluaciones
        df.loc[conteo-1]=[conteo,Xr,Ea] 

        if Ea<Es:
            break

        X0=X1
        X1=X2
        X2=Xr
        conteo+=1

    print(df)
    print(f"\nLa raiz aproximada es {Xr} con un error de {Ea} % en la {conteo} iteracion\n")

"""
Metodo Müller
f(x)= x**3 - 13*x - 12 
X0=4.5
X1=5.5
X2=5
4 cifras significativas
"""
expresion = "x**3 - 13*x - 12"
X0 = 4.5
X1 = 5.5
X2 = 5
cifrasSignificativas = 4
Metodo_Muller(expresion, X0, X1, X2, cifrasSignificativas)

