#!/usr/bin/env python
# coding: utf-8

# ## GUÍA EJERCICIOS NRO 1
# 
# ### ECONOMETRÍA PARA FINANZAS
# #### UNIVERSIDAD TORCUATO DI TELLA - 1° TRIMESTRE 2025
# ##### Francisco Ciocchini - Bárbara Guerezta

# In[1]:


import nbconvert
import pandas as pd


# ### OBJETIVO

# El objetivo de este trabajo práctico es familiarizarse con el uso de Python, conocer algunas herramientas que serán útiles durante la materia.\
# Mucho del material que utilizamos en este trabajo proviene del libro "Automate the Boring Stuff with Python"\
# Para resolver este trabajo puede ser útil consultar el material de consulta.

# ### PROBLEMA 1 - DEBUGGING DE UN CÓDIGO

# Hemos armado la siguiente rutina de operaciones:\
# Un programa pide que el usuario piense un número, y luego de un conjunto de operaciones matemáticas, el programa adivina el número que el usuario estaba pensando! Es una simple operación de despeje.\
# Pero lamentablemente el programa está roto! Hay dos errores que nos impiden llegar al final del programa, que debemos resolver

# In[1]:


print("Hola! Vamos a divertinos un rato. Te pido que pienses un número del 0 al 9 y le sumes 10")
print("A ese número luego te pido que lo multipliques por 2")
print("Al resultado, restále 5")
print("¿Terminaste? ¿Escribí el resultado en el box")


# In[2]:


rdo = input()


# El truco para encontrar el número que pensó el usuario es desandar todas las operaciones: sumar 5, /2 -10.

# In[5]:


a = rdo + 5
b = a / 2
c = b - 10


# La variable "c" almacena el resultado de toda la operación. Noten que creamos tres variables, podríamos haber encadenado las funciones, pero esto puede resultar más fácil de comprender

# **¿Por qué da error la sintaxis a = rdo + 5?**\
# Arreglá la sintaxis y explicá brevemente qué hiciste para resolverlo

# **RTA:** 

# Ahora que ya está resuelto y que sabemos que la variable "c" contiene el número que la persona pensó, vamos a sorprenderla con la respuesta:

# In[10]:


print("Acaso pensaste en ... " + c)


# **¿Por qué da error el print?** Arreglá la sintaxis y explicá brevemente qué hiciste para resolverlo

# **RTA:**

# <h6><center>FIN PROBLEMA 1</center></h6>
# <p style="page-break-after:always;"></p>

# ### PROBLEMA 2 - PANDAS DATAFRAMES

# Cierto inversor tiene contabilizados todos los activos que posee en su cartera de inversión en un papel. Allí tiene: nombre del activo, cantidad de unidades adquiridas, precio de compra y precio actual. Supongamos que compró todos los activos el mismo día, y que nunca más movió su cartera. En la lista "port" almacenamos esa información:

# In[20]:


import pandas as pd


# In[17]:


port = [['SPY', 20, 476.16, 417],
        ['TSLA', 10, 1056.78, 766.17],
        ['NFLX', 20, 602.44, 331.01],
        ['GLD', 100, 170.96, 182.30]
]


# **Pregunta 1** Almacenar todas las tenencias en un dataframe cuyas columnas sean:\
# "Ticker, Q, Pc, Pa" donde Q= cantidad, Pc= Precio de compra y Pa =Precio actual

# In[ ]:





# **Pregunta 2** ¿Cuánta plata invirtió inicialmente y cuál es el valor actual del portafolio?

# In[ ]:





# In[ ]:





# **Pregunta 3** Calcular la rentabilidad obtenida (ie, variación %) de cada una de las inversiones, y calcular luego la rentabilidad de toda la cartera

# In[ ]:





# <h6><center>FIN PROBLEMA 2</center></h6>
# <p style="page-break-after:always;"></p>

# ### PROBLEMA 3 - ARCHIVOS DE EXCEL

# Nos contactó una heladería que quiere analizar sus ingresos por la venta de helados.\
# Nos entregó un excel que contiene las ventas de helado desde el año 2002 hasta el año 2021 inclusive.\
# Las ventas fueron todas expresadas en términos de kilos de helado; y fueron agrupadas de acuerdo a la estación del año ('verano', 'otoño', 'invierno', 'primavera').

# **Pregunta 1** Importar el archivo de excel, guardarlo en un dataframe "helados". Imprimir las primeras y las últimas filas del dataframe en pantalla \
# El dataframe está estructurado de esta manera: columna 'year' contiene el año que se tabula. Cada año está separado en trimestres de acuerdo a la estación del año: 'verano', 'otoño', 'invierno', 'primavera' (¿Se les ocurre por qué?). La variable 'Ventas_mes' contiene las ventas promedio en cada mes de esa estación de ese año, escaladas en términos de kilos de helado. 'Precio_kg' es el precio promedio del kilo de helado de esa temporada. 'IPC' es el índice de precios al consumidor de Buenos Aires para esa estación del año

# In[ ]:





# **Pregunta 2** Análisis exploratorio:\
# Calcular los ingresos promedio *mensuales* y los ingresos acumulados en cada temporada (ie. *trimestrales*) de la heladería (Kg * precio)

# In[ ]:





# **Pregunta 3** ¿Cuántos kilos de helado vendió la heladería y a cuánto ascendieron sus ingresos en el año 2021? ¿Cuál fue el precio promedio de venta del kilo de helado en el año 2021?

# In[ ]:





# **Pregunta 4** Calcular las variaciones porcentuales interanuales de las ventas de kilos de helado, del precio del helado y de la inflación en Buenos Aires

# In[ ]:





# **Pregunta 5** Graficar la evolución de la variación del precio del helado y la variación de la inflación observada en Buenos Aires a lo largo del tiempo

# In[ ]:





# **Pregunta 6** Estimar una regresión univariada para explicar la variación en el precio del helado con respecto a la variación de la inflación observada en Buenos Aires

# In[ ]:





# <h6><center>FIN PROBLEMA 3</center></h6>
# <p style="page-break-after:always;"></p>
