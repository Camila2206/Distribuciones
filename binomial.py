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
N = (int)(eg.enterbox(msg='Valor para N',
                                title='Ingreso de datos',
                                default='1', strip=True)
)

p = (float)(eg.enterbox(msg='Valor para p',
                                title='Ingreso de datos',
                                default='1', strip=True)
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
##-------Creo los aleatorios
binomial = stats.binom(N, p) # Distribución
x = np.arange(binomial.ppf(0.01),
              binomial.ppf(0.99))


# histograma
##---Imprimo los datos
eg.msgbox(x,
          title='Presentar: aleatorios generados', 
          ok_button='Continuar')

presentar=("La media es: ",np.mean(x), "\n La mediana es: ", np.median(x)
    , "\n La varianza es: ", np.var(x), "\n La desv. estandar es: ", np.std(x))

eg.msgbox(presentar,
          title='Control: msgbox', 
          ok_button='Continuar')

# Graficando Binomial
fmp = binomial.pmf(x) # Función de Masa de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()


#### Graficando Histograma
aleatorios = binomial.rvs(n)  # genera aleatorios
cuenta, cajas, ignorar = plt.hist(aleatorios, intervalos)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Binomial')
plt.show()

eg.msgbox(aleatorios,
          title='Presentar: aleatorios generados del histograma', 
          ok_button='Continuar')

presentar2=("La media es: ",np.mean(aleatorios), "La mediana es: ", np.median(aleatorios)
    , "La varianza es: ", np.var(aleatorios), "La desv. estandar es: ", np.std(aleatorios), "La moda es: ", stats.mode(aleatorios))

eg.msgbox(presentar2,
          title='Control: msgbox', 
          ok_button='Continuar')
