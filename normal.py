# importando modulos necesarios 
from random import randint, uniform,random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import statistics as stats
import seaborn as sns 
import random
import math
from easygui import *
import easygui as eg
from scipy import stats 

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})

##Inicio y fin de los aleatorios
# rangoInicial=(int)(input("Ingrese un margen I: "))
# rangoFinal=(int)(input("Ingrese un margen F: "))

# #lleno el arreglo con los aleatorios
# def listaAleatorios(n):
#       lista = [0]  * n
#       for i in range(n):
#           lista[i] = random.randint(rangoInicial, rangoFinal)
#       return lista

# print("Ingrese cuantos numeros aleatorios desea obtener") #Cuantos aleatorios quiero generar
# n=int(input())

# aleatorios=listaAleatorios(n) # asignos a aleatorios los elementos de lista

#######--------------MODA---------
# def modaLista(lista):
#     moda=[]
#     valorInicial=aleatorios.count(aleatorios[0])
#     for i in range(n):
#             var =aleatorios[i]
#             repetido=aleatorios.count(var)
#             if(repetido > valorInicial):
#                 valorInicial=repetido
#                 moda=[]
#                 moda.insert(0, var)
#             elif(repetido==valorInicial and var not in moda):
#                 valorInicial=repetido
#                 moda.insert(i,var)
#     return moda        

# m=(int)(n/2)
# def haymoda(lista):
#     aleatorios.sort #oredeno la lista
#     aux1, aux2, aux3, aux4=0,0,0,0
#     posCero=aleatorios.count(aleatorios[0])
#     posCinco=aleatorios.count(aleatorios[m])
#     for i in range(n):
#         apoyo=aleatorios.count(aleatorios[i])
#         if apoyo ==2:
#             aux1=aux1+1
#         elif apoyo ==n:
#             aux2=aux2+1
#         elif apoyo ==1:
#             aux3=aux3+1
#         else:
#             aux4=aux4+1
#     if aux1==n or aux2==n or aux3==n or (posCero==m and posCinco==m):
#         print("No hay moda")
#     else:
#         print("La moda es:", moda)

##---Imprimo los datos
# print("Los aleatorios son: ")
# print(aleatorios)

# print("La media es: ")
# print(stats.mean(aleatorios)) #media de los aleatorios
# print("La mediana es: ")
# print(stats.median(aleatorios)) #mediana de los aleatorios 

# print("La varianza es: ")
# print(stats.variance(aleatorios)) # varianza de los aleatorios
# print("La desviacion estandar es: ")
# print(stats.pstdev(aleatorios)) #desviacion estandar

# moda=modaLista(aleatorios)
# haymoda(moda) #moda
#print("La moda es : ")
#print(stats.mode(aleatorios))

media = (float)(eg.enterbox(msg='Media',
                                title='Ingresode datos',
                                default='1', strip=True,
                                image=None)
)

desviacion = (float)(eg.enterbox(msg='Desviacion estandar',
                                title='Ingreso de datos',
                                default='1', strip=True,
                                image=None)
)

n = (int)(eg.enterbox(msg='Numero de aleatorios a crear',
                    title='Ingreso de datos',
                    default='100',
                    image=None)
                    )

intervalos = (int)(eg.enterbox(msg='Intervalos a crear',
                    title='Ingreso: de datos',
                    default='',
                    image=None)
)


#### histograma de distribución normal.
s = np.random.normal(media, desviacion, n) # creando muestra de datos
eg.msgbox(s,
          title='Presentar: aleatorios generados', 
          ok_button='Continuar')

presentar=("La media es: ",np.mean(s), "\n La mediana es: ", np.median(s)
    , "\n La varianza es: ", np.var(s), "\n La desv. estandar es: ", np.std(s))

eg.msgbox(presentar,
          title='Control: msgbox', 
          ok_button='Continuar')

x_1 = np.linspace(stats.norm(media, desviacion).ppf(0.01),
                  stats.norm(media, desviacion).ppf(0.99), n)


# Graficando Función de Densidad de Probibilidad con Python
FDP_normal = stats.norm(media, desviacion).pdf(x_1) # FDP
plt.plot(x_1, FDP_normal, label='FDP nomal')
plt.title('Función de Densidad de Probabilidad')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()


cuenta, cajas, ignorar = plt.hist(s, intervalos, normed=True)
normal = plt.plot(cajas, 1/(desviacion * np.sqrt(2 * np.pi)) *
         np.exp( - (cajas - media)**2 / (2 * desviacion**2) ),
         linewidth=2, color='r')
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma')
plt.show()

