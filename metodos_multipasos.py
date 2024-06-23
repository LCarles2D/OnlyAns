#!/usr/bin/env python3
import sympy as sp
from sympy import *
import pandas as pd
from sympy.core.numbers import *

x,y=sp.symbols("x y")

#ingresara el Xi
xi=0
#ingresa Yi
yi=1
#ingresa x final
xf=0.75
#ingresar el paso que se calculara 2,4
paso=4
#ingresar salto
h=0.25
#ecuacion diferencial EDO
iteracion=0
edo=x-y+1


if paso!=2 and paso!=4:
    print(f"Error no se puede calcular el paso seleccionado")

if xi>=xf:
    print(f"Error el X inicial debe de ser menor al X final")

if h<=0:
    print(f"Error el salto(h) debe de ser mayor a 0")

if paso==2 and (xi+2*h)>xf:
    print(f"Error el salto(h) no permite generar los valores (x) y (y) necesarios para el paso 2")

if paso==4 and (xi+4*h)>xf:
    print(f"Error el salto(h) no permite generar los valores (x) y (y) necesarios para el paso 4")

if   paso==2:
    print(f"Error el X inicial debe de ser menor al X iinal")
    tabla=[[],[],[],[],[],[]]
    columnas=["iteracion","xi","yi","k1","k2","yi+1"]

    while xi+h<xf:
      tabla[0].append(iteracion)
      tabla[1].append(xi)
      tabla[2].append(yi)
      print(iteracion)
      k_1=N(edo,8,subs={x:xi}).evalf(n=8)
      k1=N(k_1,8,subs={y:yi}).evalf(n=8)
      k_2=N(edo,8,subs={x:xi+h}).evalf(n=8)
      k2=N(k_2,8,subs={y:yi+k1*h}).evalf(n=8)
      if k1.is_real==False:
          print("En el valor k1 se generaron numeros no reales")
          break
      elif k2.is_real==False:
           print("En el valor k2 se generaron numeros no reales")
           break
      else:
            yi_sig=N(yi+(1/2)*h*(k1+k2),8)
            tabla[3].append(k1)
            tabla[4].append(k2)
            tabla[5].append(yi_sig)
            iteracion=iteracion+1
            xi=(xi+h)
            yi=yi_sig
      
    df=pd.DataFrame(tabla,columnas).T
    print(df)
    y_predictor=tabla[5][len(tabla[5])-1]+(h/2)*(3*edo.subs({x:tabla[1][len(tabla[0])-1]+h,y:tabla[5][len(tabla[2])-1]})-edo.subs({x:tabla[1][len(tabla[0])-1],y:tabla[2][len(tabla[0])-1]}))
    print(y_predictor)
    y_corrector=tabla[5][len(tabla[5])-1]+(h/2)*(edo.subs({x:tabla[1][len(tabla[0])-1]+2*h,y:y_predictor})+edo.subs({x:tabla[1][len(tabla[0])-1]+h,y:tabla[1][len(tabla[0])-1]}))





elif paso ==4:
    tabla=[[],[],[],[],[],[],[],[]]
    columnas=["iteracion","xi","yi","k1","k2","k3","k4","yi+1"]

    while xi+h<xf:
      tabla[0].append(iteracion)
      tabla[1].append(xi)
      tabla[2].append(yi)
      print(iteracion)
      k_1=N(edo,8,subs={x:xi}).evalf(n=8)
      k1=N(k_1,8,subs={y:yi}).evalf(n=6)
      k_2=N(edo,8,subs={x:xi+(h/2)}).evalf(n=6)
      k2=N(k_2,8,subs={y:yi+(h/2)*k1}).evalf(n=6)
      k_3=N(edo,8,subs={x:xi+(h/2)}).evalf(n=6)
      k3=N(k_3,8,subs={y:yi+k2*(h/2)}).evalf(n=6)
      k_4=N(edo,8,subs={x:xi+(h)}).evalf(n=6)
      k4=N(k_4,8,subs={y:yi+k3*h}).evalf(n=6)
      if k1.is_real==False:
          print("En el valor k1 se generaron numeros no reales")
          break
      elif k2.is_real==False:
           print("En el valor k2 se generaron numeros no reales")
           break
      elif k3.is_real==False:
          print("En el valor k2 se generaron numeros no reales")
          break
      elif k4.is_real==False:
           print("En el valor k2 se generaron numeros no reales")
           break
      else:
            yi_sig=N(yi+(1/6)*h*(k1+2*k2+2*k3+k4),8)
            tabla[3].append(k1)
            tabla[4].append(k2)
            tabla[5].append(k3)
            tabla[6].append(k4)
            tabla[7].append(yi_sig)
            iteracion=iteracion+1
            xi=xi+h
            yi=yi_sig
    df=pd.DataFrame(tabla,columnas).T
    print(df)
    print(f"Respuesta {tabla[7][len(tabla[7])-1]}")
    eva1=edo.subs({x:tabla[1][len(tabla[0])-1]+h,y:tabla[7][len(tabla[7])-1]})
    print(eva1)
    eva2=edo.subs({x:tabla[1][len(tabla[0])-1],y:tabla[2][len(tabla[7])-1]})
    print(eva2)
    eva3=edo.subs({x:tabla[1][len(tabla[0])-2],y:tabla[2][len(tabla[7])-2]})
    print(eva3)
    eva4=edo.subs({x:tabla[1][len(tabla[0])-3],y:tabla[2][len(tabla[7])-3]})
    print(eva4)
    #predictor 
    y_predictor=tabla[7][len(tabla[7])-1]+(h/24)*(55*eva1-59*eva2+37*eva3-9*eva4)
    #(55*edo.subs({x:xi+h,y:tabla[7][len(tabla[7])-1]})-59*edo.subs({x:tabla[1][len(tabla[0])-1],y:tabla[2][len(tabla[7])-1]})+37*edo.subs({x:tabla[1][len(tabla[0])-2],y:tabla[2][len(tabla[7])-2]})-9*edo.subs({x:tabla[1][len(tabla[0])-3],y:tabla[2][len(tabla[7])-3]})).evalf()
    print(y_predictor)
    #corrector
    eva5=edo.subs({x:tabla[1][len(tabla[0])-1]+2*h,y:y_predictor})
    print(eva5)
    eva6=edo.subs({x:tabla[1][len(tabla[0])-1]+h,y:tabla[7][len(tabla[7])-1]})
    print(eva6)
    eva7=edo.subs({x:tabla[1][len(tabla[0])-1],y:tabla[2][len(tabla[7])-1]})
    print(eva7)
    eva8=edo.subs({x:tabla[1][len(tabla[0])-2],y:tabla[2][len(tabla[7])-2]})
    print(eva8)
    y_corrector=tabla[7][len(tabla[7])-1]+(h/24)*(9*eva5+19*eva6-5*eva7+eva8)
    print(y_corrector)
    #abc