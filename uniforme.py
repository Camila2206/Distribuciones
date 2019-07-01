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


a = (float)(eg.enterbox(msg='Valor para a donde (0<=a<=b',
                                title='Ingreso de datos',
                                default='1', strip=True)
)

b = (float)(eg.enterbox(msg='Valor para a donde (a<=b<=1',
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



# Graficando Uniforme
uniforme = stats.uniform()
x = np.linspace(uniforme.ppf(a),
                uniforme.ppf(b), n)
fp = uniforme.pdf(x) # Función de Probabilidad
fig, ax = plt.subplots()
ax.plot(x, fp, '--')
ax.vlines(x, 0, fp, colors='b', lw=5, alpha=0.5)
ax.set_yticks([0., 0.2, 0.4, 0.6, 0.8, 1., 1.2])
plt.title('Distribución Uniforme')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()

eg.msgbox(x,
          title='Presentar: aleatorios generados del histograma', 
          ok_button='Continuar')

presentar1=("La media es: ",np.mean(x), "La mediana es: ", np.median(x)
    , "La varianza es: ", np.var(x), "La desv. estandar es: ", np.std(x), "La moda es: ", stats.mode(x))

eg.msgbox(presentar1,
          title='Control: msgbox', 
          ok_button='Continuar')


# Grafica del histograma
aleatorios = uniforme.rvs(n) # genera aleatorios
cuenta, cajas, ignorar = plt.hist(aleatorios, intervalos)
plt.ylabel('frequencia')
plt.xlabel('valores')
plt.title('Histograma Uniforme')
plt.show()

eg.msgbox(aleatorios,
          title='Presentar: aleatorios generados del histograma', 
          ok_button='Continuar')

presentar2=("La media es: ",np.mean(aleatorios), "La mediana es: ", np.median(aleatorios)
    , "La varianza es: ", np.var(aleatorios), "La desv. estandar es: ", np.std(aleatorios), "La moda es: ", stats.mode(aleatorios))

eg.msgbox(presentar2,
          title='Control: msgbox', 
          ok_button='Continuar')
