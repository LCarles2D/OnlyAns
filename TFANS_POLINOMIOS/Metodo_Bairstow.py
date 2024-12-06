"""
CA20076
Metodo de Bairstow
x**4 - 7*x**3 + 13*x**2 +23*x = 78   --> x**4 - 7*x**3 + 13*x**2 +23*x - 78
ro=1
so=1
4 cifras significativas

"""

from sympy import symbols, sqrt, Poly, div
import sympy as sp
import pandas as pd
from sympy import symbols, sympify, parse_expr
from sympy.parsing.sympy_parser import parse_expr
from sympy import Poly
from sympy.parsing.sympy_parser import transformations,_T,standard_transformations,implicit_multiplication,convert_xor,implicit_application,function_exponentiation,implicit_multiplication_application,auto_symbol,auto_number,split_symbols
from sympy import Eq, solve
import herr_polinomios 
from herr_polinomios import *

def Metodo_Bairstow(expresion, r0, s0, cifrasSignificativas):
    print("-------------------- Metodo de Bairstow----------------------------")
    x = symbols("x")
    ro = validar_numero_gen(r0)
    so = validar_numero_gen(s0)
    print(f"ro: {ro}\nso: {so}")
    cifras_significativas = validar_numero_gen(cifrasSignificativas)
    expresion_ig = validar_igualdad(expresion)
    #expresion_val = validar_expresion(expresion_ig)
    funcion = validar_funcion(expresion_ig)
    coeficientes = obtener_coeficientes(funcion)
    #   impr("coeficientes",coeficientes)
    Es = obtener_Es(cifras_significativas)
    print(f"Cifras significativas: {cifras_significativas}\nNivel de tolerancia: {Es} %\n")

    a4, a3, a2, a1, a0=coeficientes #--> utilizando desepaquetamiento
    conteo=1
    df=pd.DataFrame(columns=["Iteracion","r","s","E_Dr %","E_Ds %"])
    while True:
        # continuando con el paso 3, determinamos los valores
        b4=a4
        b3=a3 + ro*b4
        b2=a2 + ro*b3 + so*b4
        b1=a1 + ro*b2 + so*b3
        b0=a0 + ro*b1 + so*b2

        #Paso 4 --> Determinamos los valores de C
        c4=b4
        c3=b3 + ro*c4
        c2=b2 + ro*c3 + so*c4
        c1=b1 + ro*c2 + so*c3

        #Paso 5 --> Determinamos D_r y D_s en las ecuaciones

        #Formamos la ecuaciones
        D_r,D_s=symbols("D_r D_s") #declaro los simbolos

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
            xr1= (r + sp.sqrt(r**2 + 4*s))/2 
            xr2= (r - sp.sqrt(r**2 + 4*s))/2
            
            #Paso 9 --> Se encuentra el polinomio restante, con la division sintetica
            # Dividimos el polinomio entre las raíces encontradas para obtener el polinomio restante
            polinomio_resto = Poly(expresion)  # Creamos un nuevo polinomio a partir de la expresión original
            cociente, resto = div(polinomio_resto, Poly(x - xr1)) #Dividimos el polinomio entre la primer raiz
            polinomio_resto = cociente #el polinomio ya dividido lo actualizo en la variable

            cociente, resto = div(polinomio_resto, Poly(x - xr2)) #divido el polinomio ya actualizado entre la otra raiz
            polinomio_resto = cociente #El polinomio resultante se guarda en la variable

            #Paso 10 --> Calculamos el grado del polinomio resultante
            Qx=polinomio_resto.degree()

            #Condiciones
            if Qx >= 3: #Si el grado del polinomio es mayor o igual a tres se vuelve a aplicar el metodo tomando como ro=r , so=s
                ro=r
                so=s

            elif Qx==2: #si el grado del polinomio es igual a 2 se evalua directo
                Xr1= (r + sp.sqrt(r**2 + 4*s))/2 
                Xr2= (r - sp.sqrt(r**2 + 4*s))/2
                print(f"\nEl polinomio es de grado {Qx} y sus raices son : X1 = {Xr1} y X2 = {Xr2}")
            
            elif Qx==1: #Si es de grado uno se evalua
                Xr=-(s/r)
                print(f"\nEl polinomio es de grado {Qx} y su raiz es: X = {Xr}")



            break
        #regresa al paso2
        ro=r
        so=s
        conteo+=1

"""#Paso 1 --> inicializar ro y so
    ro=1
    so=1
    print(f"ro: {ro}\nso: {so}")

    #Paso 2 --> Calculo Es
    cifras_significativas=4
    Es=0.5*10**(2-cifras_significativas)
    print(f"Cifras significativas: {cifras_significativas}\nNivel de tolerancia: {Es} %\n")

    #Paso 3--> Determinar los valores de los coheficientes
    x=symbols("x") #--> declaro el simbolo
    expresion=x**4-7*x**3+13*x**2+23*x-78 #Creo la expresion matematica
    polinomio=Poly(expresion) #la expresamos como polinomio
    coeficientes=polinomio.all_coeffs() #obtenemos los coheficientes

    #Ahora guardamos cada coeficiente en diferentes variables
    a4,a3,a2,a1,a0=coeficientes #--> utilizando desepaquetamiento"""

Metodo_Bairstow("x**4-7*x**3+13*x**2+23*x-78", 1.5, 1.5, 4)
