
from sympy import symbols, sqrt, Poly, div , root , acos
import sympy as sp
from sympy import Poly
import herr_polinomios
from herr_polinomios import *
import math as math

def Metodo_Tartaglia(expresion):
    x=sp.symbols("x")
    #expresion_valida = validar_expresion(expresion)
    funcion = validar_funcion(expresion)
    impr("funcion",funcion)
    polinomio = sp.Poly(funcion)
    coeficientes = polinomio.all_coeffs()
    impr("coeficientes",coeficientes)
    grado = polinomio.degree()
    #impr("grado",grado)

    if grado != 3:
        print("Error: grado invalido: el grado de la funcion es distinta de ^2")
        exit()
        
    if coeficientes[0] != 1:# Si el primer coeficiente es diferente de 1
        primer_coeficiente = coeficientes[0]
        #impr("primer coeficiente",coeficientes[0])
        nuevo_coeficientes = [coef / primer_coeficiente for coef in coeficientes]
        #impr("nuevo_coeficientes", nuevo_coeficientes)
        coeficientes = nuevo_coeficientes
        #impr("nuevos coeficientes",coeficientes)
        
    f, a, b, c = coeficientes # Guardamos los coeficientes en distintas varibles
    print(f"f: {f}, a: {a}, b: {b}, c: {c}")

    #1. calcular p y q
    p = (3*b - a**2)/3 
    q = (2*a**3 - 9*a*b + 27*c)/27

    #2. calculamos el discriminante
    D = (q/2)**2 + (p/3)**3

    #Condiciones
    if D == 0: #Si el discriminante es igual a cero
        p_q = p*q #multiplico p * q
        if p == 0 and q == 0: #Si p y q son iguales a cero
            raiz_triple = -(a/3) # tiene una raiz triple
            valores_x = validar_raices(raiz_triple)
            raices_validadas = validar_raices(valores_x)
            impr_grafico(expresion, funcion, raices_validadas)
            print(f"Se encontro que el discriminante es :{D}\np = {p} y q = {q}")
            print("Tiene una raiz triple :\nx = {raiz_triple}")

        elif p_q != 0: #Si la multiplicacion de p * q es diferente de cero
            valores_x = []
            raiz_doble = -((3*q)/(2*p)) - (a/3)#Se encuentra la raiz doble
            raiz = -((4*p**2)/(9*q)) - (a/3) 
            print(f"Se encontro que el discriminante es :{D}\np = {p} y q = {q}\np * q = {p_q}\n\nSe tienen las raices:\nx = {raiz_doble} -->Raiz doble\nx = {raiz}\n")
            valores_x.extend(validar_raices(raiz_doble))
            valores_x.extend(validar_raices(raiz))
            raices_validadas = validar_raices(valores_x)
            impr_grafico(expresion, funcion, raices_validadas)

    elif D>0: #Si el discriminante es mayor a cero
        #Calculamos U y V
        U = math.cbrt((-q/2) + sp.sqrt(D))#Con la raiz cubica a todo
        V = math.cbrt((-q/2) - sp.sqrt(D)) #con la raiz cubica a todo

        #Calculamos la raiz real
        #raiz_real = (( sp.root((-(q/2)) + sqrt(D),3) ) + (sp.root( (-(q/2)) - sp.sqrt(D),3) ) )- (a/3) 
        raiz_real = (U + V) - (a/3)
        valores_x = []
        valores_x = validar_raices(raiz_real)
        raices_validadas = validar_raices(valores_x)
        impr_grafico(expresion, funcion, raices_validadas)

        #Calculamos la raiz imaginaria
        raiz_imaginaria_uno =  (-((U + V ) / 2 )) - (a/3) + complex( (((sqrt(3))/2) * (U - V)) )# i 
        raiz_imaginaria_dos =  (-((U + V ) / 2 )) - (a/3) - complex( (((sqrt(3))/2) * (U - V)) )# i 

        print(f"Se encontro que el discriminante es :{D}\np = {p}\nq = {q}\nU = {U}\nV = {V}\nSe tiene las raices :\nRaiz real\n x = {raiz_real}\n\nRaices imaginarias\nx = {raiz_imaginaria_uno}\nx = {raiz_imaginaria_dos}")

    elif D<0: #Si el discriminante es menor a cero
        #Calculamos el angulo Cos θ
        angulo = sp.acos( (-(q/2)) / (sp.sqrt((-((p/3)**3)))) )
        #Utilizamos un valor de K=0,1,2
        
        if 0 < angulo < sp.pi:
            K = 0
            raiz1 = 2 * (sp.sqrt(-(p/3))) * sp.cos( (angulo + 2*K*sp.pi) / (3) ) - (a/3) # Se calcula la raiz
            K = 1
            raiz2 = 2 * (sp.sqrt(-(p/3))) * sp.cos( (angulo + 2*K*sp.pi) / (3) ) - (a/3) # Se calcula la raiz
            K = 2
            raiz3 = 2 * (sp.sqrt(-(p/3))) * sp.cos( (angulo + 2*K*sp.pi) / (3) ) - (a/3) # Se calcula la raiz
            valores_x = []       
            valores_x.extend(validar_raices(raiz1))
            valores_x.extend(validar_raices(raiz2))
            valores_x.extend(validar_raices(raiz3))
            raices_validadas = validar_raices(valores_x)
            impr_grafico(expresion, funcion, raices_validadas)
            print(f"Con un discriminante: {D}, p = {p} y q = {q}")
            print(f"Con K = {0}, primera raiz: {raiz1}")
            print(f"Con K = {1}, primera raiz: {raiz2}")
            print(f"Con K = {2}, primera raiz: {raiz3}")     
            
        else:
            print(f"Error: Se encontro que el discriminante es :{D}\np = {p} y q = {q}\nEl angulo es :{angulo} este no se encuentra entre 0 y pi")    

expresion = "25*x**3 + 15*x**2 - 9*x + 1"
Metodo_Tartaglia(expresion)


"""x=sp.symbols("x")
expresion=25*x**3 + 15*x**2 - 9*x + 1     
polinomio=Poly(expresion)
coeficientes=polinomio.all_coeffs()

if coeficientes[0] != 1: # Si el primer coeficiente es diferente de 1
    expresion_obligatoria=expresion/coeficientes[0]
    nuevo_polinomio=Poly(expresion_obligatoria)
    coeficientes=nuevo_polinomio.all_coeffs()
f,a,b,c=coeficientes # Guardamos los coeficientes en distintas varibles

# PASO 1: Calcular p y q
p=(3*b - a**2)/3 
q=(2*a**3 - 9*a*b + 27*c)/27


# PASO 2: Calculamos el discriminante
D=(q/2)**2 + (p/3)**3

#Condiciones
if D==0: #Si el discriminante es igual a cero
    p_q=p*q #multiplico p * q
    if p==0 and q==0: #Si p y q son iguales a cero
        raiz_triple=-(a/3) # tiene una raiz triple
        print(f"Se encontro que el discriminante es :{D}\np = {p} y q = {q}\nTiene una raiz triple :\nx = {raiz_triple}")

    elif p_q != 0: #Si la multiplicacion de p * q es diferente de cero
        raiz_doble=-((3*q)/(2*p)) - (a/3)#Se encuentra la raiz doble
        raiz=-((4*p**2)/(9*q)) - (a/3) 
        print(f"Se encontro que el discriminante es :{D}\np = {p} y q = {q}\np * q = {p_q}\n\nSe tienen las raices:\nx = {raiz_doble} -->Raiz doble\nx = {raiz}\n")

elif D>0: #Si el discriminante es mayor a cero
    #Calculamos U y V
    U = math.cbrt((-q/2) + sp.sqrt(D))#Con la raiz cubica a todo
    V = math.cbrt((-q/2) - sp.sqrt(D)) #con la raiz cubica a todo

    #Calculamos la raiz real
    #raiz_real = (( sp.root((-(q/2)) + sqrt(D),3) ) + (sp.root( (-(q/2)) - sp.sqrt(D),3) ) )- (a/3) 
    raiz_real = (U + V) - (a/3)

    #Calculamos la raiz imaginaria
    raiz_imaginaria_uno =  (-((U + V ) / 2 )) - (a/3) + complex( (((sqrt(3))/2) * (U - V)) )# i 
    raiz_imaginaria_dos =  (-((U + V ) / 2 )) - (a/3) - complex( (((sqrt(3))/2) * (U - V)) )# i 

    print(f"Se encontro que el discriminante es :{D}\np = {p}\nq = {q}\nU = {U}\nV = {V}\nSe tiene las raices :\nRaiz real\n x = {raiz_real}\n\nRaices imaginarias\nx = {raiz_imaginaria_uno}\nx = {raiz_imaginaria_dos}")

elif D<0: #Si el discriminante es menor a cero
    #Calculamos el angulo Cos θ
    angulo = sp.acos( (-(q/2)) / (sp.sqrt((-((p/3)**3)))) )
    #Utilizamos un valor de K=0,1,2
    K=0
    if 0<angulo< sp.pi:
        raiz = 2 * (sp.sqrt(-(p/3))) * sp.cos( (angulo + 2*K*sp.pi) / (3) ) - (a/3) # Se calcula la raiz
        print(f"Se encontro que el discriminante es {D}\np = {p} y q = {q}\nEl angulo es :{angulo} este se encuentra entre 0 y pi\nLa raiz es :\nx = {raiz}")

    else:
        print(f"Se encontro que el discriminante es :{D}\np = {p} y q = {q}\nEl angulo es :{angulo} este no se encuentra entre 0 y pi")

Metodo Tartaglia
25*x**3 + 15*x**2 - 9*x + 1 = 0
"""