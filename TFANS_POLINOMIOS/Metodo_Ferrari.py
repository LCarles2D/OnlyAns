"""
Metodo Ferrari
24*x**4 - 3*x**3 + 2*x**2 + x - 2 = 0
"""
from sympy import symbols, sqrt, Poly, div , root , acos
import sympy as sp
from sympy import Poly
import math as math
import cmath as cmath
import herr_polinomios
from herr_polinomios import *

def Metodo_Ferrari(expresion):
    #24*x**4 - 3*x**3 + 2*x**2 + x - 2 = 0
    expresion_ig = validar_igualdad(expresion)
    #impr("expresion_ig",expresion_ig)
    #expresion_validada = validar_expresion(expresion_ig)
    #impr("expresion_validada",expresion_validada)
    funcion = validar_funcion(expresion_ig)
    impr("funcion",funcion)
    coeficientes = obtener_coeficientes(funcion)
    impr("coeficientes",coeficientes)
    grado = obtener_grado(funcion)
    #print(grado, "type: ",type(grado))
    f, a, b, c, d = coeficientes
    #necesito

    #1. calculamos p, q, R
    p = ((8*b)-(3*a**2))/8
    q = ((8*c) - (4*a*b) + (a**3))/8
    R = ((256*d) - (64*a*c) + (16*a**2*b) - (3*a**4))/256
    #print("Datos de Ferrari:")
    #print(f"p = {p}")
    #print(f"q = {q}")
    #print(f"R = {R}")
    
    #2. Reescribimos  la expresion a una cubica

    print("::::::::::::::::::::::::::::::::::::::::::::::::")
    U = sp.symbols("U")
    expresion_v = U**3 - p/2*U**2 - R*U + ((4*p*R) - (q**2))/8
    impr("Expresion validada: ",expresion_v)
    funcion_v = sp.simplify(expresion_v)
    impr("funcion validada: ",funcion_v)
    polinomio = sp.Poly(funcion_v)
    impr("polinomio: ",polinomio)
    coeficientes_u = polinomio.all_coeffs()
    impr("coeficientes U: ,",coeficientes_u)
    #print("::::::::::::::::::::::::::::::::::::::::::::::::")
    """print(expresion_u, "type: ",type(expresion_u))
    funcion_u = validar_funcion(expresion_u)
    print(funcion_u, "type: ",type(funcion_u))
    coeficientes_u = obtener_coeficientes(funcion_u)   
    print(coeficientes_u, "type: ",type(coeficientes_u))
    grado_u = obtener_grado(funcion_u)
    print(grado_u,"type: ",type(grado))"""
    
    """REVISAR
    (U**3) - ((-11/8/2)*U**2) - (-275/256*U) + (((4*-11/8*-275/256) - (5/8**2))/8) type:  <class 'str'>
    U**3 + 11*U**2/16 + 275*U/256 + 2985/4096 type:  <class 'sympy.core.add.Add'>
    (U**3 + 11*U**2/16 + 275*U/256 + 2985/4096,) type:  <class 'tuple'>"""
    
    
    fU, aU, bU, cU = coeficientes_u

    #3. realizamos el metodo de tartaglia para encontrar U
        #calculamos la p y q
    p_t = (3*bU - aU**2)/3 
    q_t = (2*aU**3 - 9*aU*bU + 27*cU)/27

        #calculamos el discriminante
    D = (q_t/2)**2 + (p_t/3)**3
    U_=0
    
    print("")
    print("-----------------------------------------------------")
    print("Datos Tartaglia:")
    print(f"p = {p_t}")
    print(f"q = {q_t}")
    
    #metodo tartaglia
    if D == 0: #si el discriminante es igual a cero
        p_q = p_t*q_t #multiplico p * q
        if p_t == 0 and q_t == 0: #Si p y q son iguales a cero
            raiz_triple =- (aU/3) # tiene una raiz triple
            U_ = raiz_triple
            valores_x = []
            if isinstance(raiz_triple, list):
                valores_x.extend(raiz_triple)    
            else:    
                valores_x.append(raiz_triple)
            valores_validados = validar_raices(valores_x)
            impr_grafico(expresion, funcion, valores_validados)
            if isinstance(raiz_triple, int) or isinstance(raiz_triple, float):
                valores_x.append(raiz_triple)

        elif p_t*q_t != 0: #Si la multiplicacion de p * q es diferente de cero
            raiz_doble = -((3*q_t)/(2*p_t)) - (aU/3)#Se encuentra la raiz doble
            raiz = -((4*p_t**2)/(9*q_t)) - (aU/3) 
            U_ = raiz
            valores_x = []
            if isinstance(raiz_doble, list):
                valores_x.extend(raiz_doble)
            else:    
                valores_x.append(raiz_doble)
            
            if isinstance(raiz, list):
                valores_x.extend(raiz)
            else:    
                valores_x.append(raiz)

            valores_validados = valores_validados(valores_x)
            impr_grafico(expresion, funcion, valores_validados)
            #raiz triple
            print(f"Δ = {D}")
            print(f"U = {U_}")
            
    elif D > 0: #Si el discriminante es mayor a cero
        #Calculamos U y V
        U = math.cbrt((-q_t/2) + math.sqrt(D))#Con la raiz cubica a todo
        V = math.cbrt((-q_t/2) - math.sqrt(D)) #con la raiz cubica a todo
        U_ = U
        print(f"Δ = {D}")
        print(f"U = {U_}")
        #Calculamos la raiz real
        raiz_real = (U + V) - (aU/3)
        valores_x = []
        if isinstance(raiz_real, list):
            valores_x.extend(raiz_real)
        else:    
            valores_x.append(raiz_real)

        valores_validados = validar_raices(valores_x)
        impr_grafico(expresion, funcion, valores_validados)

        #Calculamos la raiz imaginaria
        raiz_imaginaria_uno =  (-((U + V ) / 2 )) - (aU/3) + complex( (((sqrt(3))/2) * (U - V)) )# i 
        raiz_imaginaria_dos =  (-((U + V ) / 2 )) - (aU/3) - complex( (((sqrt(3))/2) * (U - V)) )# i 

        
    elif D < 0: #Si el discriminante es menor a cero
        #Calculamos el angulo Cos θ
        angulo = math.acos( (-(q_t/2)) / (math.sqrt((-((p_t/3)**3)))) )
        #Utilizamos un valor de K=0,1,2
        K = 0
        if 0 < angulo < math.pi:
            raiz = 2 * math.sqrt(-(p_t/3)) * math.cos( (angulo + 2*K*math.pi) / (3) ) - (aU/3) # Se calcula la raiz
            U_ = raiz
            valores_x = []
            if isinstance(raiz, list):
                valores_x.extend(raiz)
            else:    
                valores_x.append(raiz)
            
            valores_validados = validar_raices(valores_x)
            impr_grafico(expresion, funcion, valores_validados)
            print(f"Δ = {D}")
            print(f"θ = {angulo}")
            print(f"U = {U_}")
        else:
            print("Error: M_Ferrari: D < 0: calculo raiz")
 
"""x=sp.symbols("x")
expresion=24*x**4 - 3*x**3 + 2*x**2 + x - 2 
polinomio=Poly(expresion)
coeficientes=polinomio.all_coeffs()

if coeficientes[0] != 1: # Si el primer coeficiente es diferente de 1
    expresion_obligatoria=expresion/coeficientes[0]
    nuevo_polinomio=Poly(expresion_obligatoria)
    coeficientes=nuevo_polinomio.all_coeffs()
f,a,b,c,d=coeficientes # Guardamos los coeficientes en distintas varibles

#Paso 1: Calculamos p, q, R
p=((8*b)-(3*a**2))/8
q=((8*c) - (4*a*b) + (a**3))/8
R=((256*d) - (64*a*c) + (16*a**2*b) - (3*a**4))/256
print("-----------------------------------------------------")
print("Datos de Ferrari:")
print(f"p = {p}")
print(f"q = {q}")
print(f"R = {R}")
print("-----------------------------------------------------")

#Paso 2: Reescribimos  la expresion a una cubica
U=sp.symbols("U")
expresion=(U**3) - ((p/2)*U**2) - (R*U) + (((4*p*R) - (q**2))/8)
polinomio=Poly(expresion)
coeficientes=polinomio.all_coeffs()
f_,a_,b_,c_=coeficientes

#Paso 3: Realizamos el metodo de tartaglia para encontrar U

#Calculamos la p y q
p_t=(3*b_ - a_**2)/3 
q_t=(2*a_**3 - 9*a_*b_ + 27*c_)/27

#Calculamos el discriminante
D=(q_t/2)**2 + (p_t/3)**3
U_=0
print("")
print("-----------------------------------------------------")
print("Datos Tartaglia:")
print(f"p = {p_t}")
print(f"q = {q_t}")
#Condiciones
if D==0: #Si el discriminante es igual a cero
    p_q=p_t*q_t #multiplico p * q
    if p_t==0 and q_t==0: #Si p y q son iguales a cero
        raiz_triple=-(a_/3) # tiene una raiz triple
        U_=raiz_triple
    elif p_t*q_t != 0: #Si la multiplicacion de p * q es diferente de cero
        raiz_doble=-((3*q_t)/(2*p_t)) - (a_/3)#Se encuentra la raiz doble
        raiz=-((4*p_t**2)/(9*q_t)) - (a_/3) 
        U_=raiz
        print(f"Δ = {D}")
        print(f"U = {U_}")
        
elif D>0: #Si el discriminante es mayor a cero
    #Calculamos U y V
    U = math.cbrt((-q_t/2) + math.sqrt(D))#Con la raiz cubica a todo
    V = math.cbrt((-q_t/2) - math.sqrt(D)) #con la raiz cubica a todo
    U_=U
    print(f"Δ = {D}")
    print(f"U = {U_}")
    #Calculamos la raiz real
    raiz_real = (U + V) - (a_/3)

    #Calculamos la raiz imaginaria
    raiz_imaginaria_uno =  (-((U + V ) / 2 )) - (a_/3) + complex( (((sqrt(3))/2) * (U - V)) )# i 
    raiz_imaginaria_dos =  (-((U + V ) / 2 )) - (a_/3) - complex( (((sqrt(3))/2) * (U - V)) )# i 

    
elif D<0: #Si el discriminante es menor a cero
    #Calculamos el angulo Cos θ
    angulo = math.acos( (-(q_t/2)) / (math.sqrt((-((p_t/3)**3)))) )
    #Utilizamos un valor de K=0,1,2
    K=0
    if 0<angulo< math.pi:
        raiz = 2 * math.sqrt(-(p_t/3)) * math.cos( (angulo + 2*K*math.pi) / (3) ) - (a_/3) # Se calcula la raiz
        U_=raiz
        print(f"Δ = {D}")
        print(f"θ = {angulo}")
        print(f"U = {U_}")
    else:
        print("")
        

print("-----------------------------------------------------\n")
#Paso 4: Calculamos V y W ya con el metodo de ferrari
V=math.sqrt((2*U_) - p)
W=-(q/(2*V))
print("-----------------------------------------------------")
print("Datos de Ferrari:")
print(f"V = {V}")
print(f"W = {W}")
print("-----------------------------------------------------")
#Paso 5: Calculamos las raices

raiz_uno = (( (V) + (sp.sqrt((V**2) - (4*(U_ - W)))) ) / 2) - (a/4) #cmath calcula el numero negativo de una raiz cuadrada
raiz_dos = (( (V) - (sp.sqrt((V**2) - (4*(U_ - W)))) ) / 2) - (a/4) 
raiz_tres = (( (-V) + (sp.sqrt((V**2) - (4*(U_ + W)))) ) / 2) - (a/4)
raiz_cuatro = (( (-V) - (sp.sqrt((V**2) - (4*(U_ + W)))) ) / 2) - (a/4)

print("Raices :")
print(f"x = {raiz_uno}")
print(f"x = {raiz_dos}")
print(f"x = {raiz_tres}")
print(f"x = {raiz_cuatro}\n")"""

expresion = "24*x**4 - 3*x**3 + 2*x**2 + x - 2 = 0"
#otro ejemplo: "24*x**4 - 7*x**3 + 2*x**2 - 4 = 0"
Metodo_Ferrari(expresion)

