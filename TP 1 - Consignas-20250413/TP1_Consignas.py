#!/usr/bin/env python
# coding: utf-8

# # Introducción a la Econometría para Finanzas
# ## Trabajo Práctico Nro 1 - 1º Trimestre 2025
# #### Universidad Torcuato Di Tella
# ##### Francisco Ciocchini - Bárbara Guerezta
# ## <font color='green'>CONSIGNAS</font>
# 

# ### Instrucciones
#     . El trabajo práctico es de entrega obligatoria.
#     . Se puede realizar en grupos de no más de 4 personas.
#     . Se realiza una sola entrega por grupo indicando los nombres de todos los integrantes.
#     . La fecha límite de entrega es el día miércoles 23 de abril de 2025 a las 23.59hs.
#     . Deberá subirse al campus de la facultad el html (o pdf si lo prefiere) creado con RMarkdown que contenga los códigos utilizados para la resolución del trabajo.
#     . Por cualquier consulta pueden escribir a bguerezta@gmail.com

# ## Problema 1: Estimación del $\beta$ de un activo
# ### Enunciado
# El $\beta$ de un activo es lo que comúnmente se conoce como la sensibilidad de los retornos de un activo relativo a un índice de referencia, que, en el caso de las acciones, típicamente es el índice S&P 500.\
# 
# Si lo representamos en una ecuación, ésta sería:
# 
# $$
# \begin{aligned}
# R^e_{t}=\alpha +\beta R^e_{M,t} + \mu_t
# \end{aligned}
# $$
# donde $R^e_{M,t}$ es el exceso de retorno del portafolio de mercado (S&P 500) en el período $t$ y $R^e_{t}$ es el exceso de retorno de un activo en el período $t$.\
# 
# Tomando datos de Rachev et al., Financial Econometrics, Chapter 3, replicaremos los resultados presentados en clase. 
# 
# 
# 1. El archivo "Financial_Econometrics_data.pdf" contiene un extracto del Capítulo 3 que deberemos replicar (también pueden encontrar los resultados en la clase teórica correspondiente).
# 
# 2. El archivo de excel "Financial_Econometrics_data.xlsx" contiene datos desde diciembre 2000 y noviembre 2005 con retornos mensuales anualizados de distintos activos: SandP representa al índice S&P 500, Rf corresponde a la tasa libre de riesgo de un bono del tesoro norteamericano (Treasury) a 90 días, GM hace referencia al retorno de la acción de General Motors, Oracle, al de Oracle, y Portfolio es una cartera integrada por 20 acciones (Honeywell, Alcoa, Campbell, Boeing, General Dynamics, Oracle, Sun, General Motors, Procter & Gamble, Wal-Mart, Exxon, ITT, Unilever, Hilton, Martin Marietta, Coca-Cola, Northrop Grumman, Mercury Interact, Amazon, and United Technologies). Importen ese archivo a Python, y cree un dataframe.
# 
# 3. Para cada una de los índices  que vamos a estudiar (S&P, Oracle, GM, Portfolio), computen el exceso de retorno con respecto a la tasa libre de riesgo a 90 días.
# 
# 4. Análisis Gráfico. Realicen tres gráficos de líneas que comparen, de a pares el exceso de retorno de Oracle con S&P, de GM con S&P, y del Portfolio con S&P, a lo largo del tiempo. Describan lo que ven. La librería Matplotlib puede ser útil: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
# 
# 
# 5. Análisis Gráfico II: Realicen tres gráficos de dispersión para comparar el exceso de retorno de Oracle contra S&P, de GM contra S&P, y de Portfolio contra S&P. Descríbanlos. la librería matplotlib puede ser útil.
# 
# 6. Utilizando la librería de statsmodels vista en clase, estimen 3 regresiones univariadas para computar el $beta$ de Oracle, GM y la cartera de 20 activos, replicando el modelo presentado más arriba en este problema. Presenten una tabla donde se puedan ver, al menos, los valores estimados de cada uno de esos 3 regresiones, el desvío estándar y el p-valor asociado. Pueden usar la librería stargazzer, o la función summary_col dentro del paquete de statsmodels, o alguno similar.
# 
# 7. Evalúe para cada modelo si el $\beta$ es significativamente distinto de 1 con un 95% de confianza. ¿Por qué no puede utilizar el p-value calculado por default en la estimación del modelo del punto anterior? Interprete el significado de que un activo tenga un $\beta$ igual a 1.
# 
# *Hint*: el punto 7 se puede realizar a mano copiando manualmente los resultados del punto anterior, si quisieran, pero si estiman por statmodels, cada modelo almacena los parámetros computados en la regresión bajo la forma de series, que pueden ser extraídos. Por ejemplo, si el modelo se llama "m1", pueden extraer los beta estimados utilizando m1.params; y cada elemento corresponde al beta estimado. Lo mismo ocurre con los desvíos estándares (bse) o con los p-value (pvalues). Les dejamos algunos comandos de python útiles en la sección de soluciones por si quieren explorarlo. Los que lo hagan, tendrán algún bonus en la evaluación.

# ### Solución Problema 1

# In[58]:


import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.iolib.summary2 import summary_col #Útil para presentar muchas regresiones a la vez
import matplotlib.pyplot as plt


# In[ ]:


## Comandos útiles para extraer elementos de las regresiones.
#donde model es el nombre que se le asigna al objeto "modelo de OLS" una vez que hacen la estimación de OLS
#NOTA: si corren este chunk van a tener un error porque no tienen estimado el modelo previamente.
#Manipulen este chunk, o sólo tomen lo que necesiten, pero no lo dejen suelto para que no dé error y trabe la ejecución.

model.params
model.bse
model.pvalues

model.params[0] #Obtiene el valor estimado del primer parámetro de la regresión - típicamente intercepto-
model.params['Intercept'] #Otra manera de obtener el valor estimado del intercepto.

model.bse[0] #Obtiene el valor estimado del desvío estándar correspondiente al primer parámetro de la regresión.


# In[ ]:





# In[ ]:





# ## Problema 2: Predicción de Spreads de Bonos Corporativos
# 
# ### Enunciado
# 
# Consideremos el siguiente modelo:
# 
# 
# $$
# \begin{aligned}
# S_i = \beta_0 + \beta_1 CRate_i + \beta_2 CRatio_i + \beta_3 ln(EBIT_i) + \mu_i\\
# \end{aligned}
# $$
# 
# donde:
# $S_i$ es el Spread de un bono de la empresa $i$ (en basis points)
# 
# $CRate_i$ es la tasa de cupón del bono de la empresa $i$ (en porcentaje), 
# 
# $CRatio_i$ es el coverage ratio $i$ = $\frac{EBITDA_i}{InterestExpense_i}$, 
# 
# $lnEBIT_i$ es el logaritmo natural de $EBIT$ de la empresa $i$, con $EBIT_i$ expresado en millones de dólares\
# 
# 
# 
# 1. El archivo spread_data.xlsx incluye datos extraídos del Capítulo 4 de Rachev et al. Financial Econometrics. Impórtenlo a Python.
# 
# 2. Estimen por mínimos cuadrados ordinarios la ecuación presentada previamente y muestren los resultados de la estimación, con errores robustos a la presencia de heteroscedasticidad. \
# 
# 3. Interpreten el significado de cada uno de los parámetros estimados en la regresión anterior, teniendo en cuenta las unidades de medida de las variables.
# 
# 4. Realicen una prueba de significatividad conjunta para $\beta_2$ y $\beta_3$. *Hint*: El modelo estimado en el punto 2 tiene una función asociada que se llama "f_test" que puede correr esta prueba sobre la hipótesis planteada.
# 
# 5. Evalúen el efecto sobre el spread de ser una compañía *investment grade*. Para ello computen primero una variable dicotómica que tome valor 1 cuando la variable *non_inv_grade* sea igual a 0. Luego inclúyanla como una variable explicativa dentro del modelo anterior y vuelvan a estimarlo. ¿Es relevante su efecto? Expliquen el signo, la magnitud y la lógica económica detrás del resultado de la estimación.
# 
# 

# ### Solución Problema 2

# In[ ]:





# In[ ]:





# ## Problema 5 Event Studies: Rescate de Credit Suisse
# 
# ### Enunciado
# 
# El 19 de marzo del año 2023 se firmó un acuerdo mediante el cual la compañía suiza de servicios financieros y bancarios creado en el año 1856, Credit Suisse, pasaría a formar parte de otro banco suizo, UBS. El objetivo de este problema es identificar si este anuncio tuvo algún impacto sobre el precio de la acción de UBS. 
# 
# Para responder a esta pregunta se puede estimar un modelo bajo el supuesto de que se cumple CAPM:
# 
# $$R_{UBS,t} = \alpha + \beta R_{M,t} + \gamma_{1} D1_t + \gamma_2 D2_t + \gamma_3 D3_t + \gamma_4 D4_t + \gamma_5 D5_t + \gamma_6 D6_t + \mu_t$$
# donde
# 
# $R_{UBS,t}$ es el retorno de UBS en el día $t$\
# $R_{M,t}$ es el retorno del índice SPY, que es un ETF que replica la composición del índice accionario S&P 500 -  500 grandes empresas que poseen acciones que cotizan en las bolsas NYSE o NASDAQ - (ie, "retorno del mercado") en el día $t$\
# $D1_t$ es una *dummy* que toma valor 1 en el día 16-marzo-2023 (ie, 2 días hábiles antes del anuncio)\
# $D2_t$ es una *dummy* que toma valor 1 en el día 17-marzo-2023 (ie, 1 día hábil antes del anuncio)\
# $D3_t$ es una *dummy* que toma valor 1 en el día 20-marzo-2023 (ie, 1 día hábil después del anuncio)\
# $D4_t$ es una *dummy* que toma valor 1 en el día 21-marzo-2023 (ie, 2 días hábiles después del anuncio)\
# $D5_t$ es una *dummy* que toma valor 1 en el día 22-marzo-2023 (ie, 3 días hábiles después del anuncio)\
# $D6_t$ es una *dummy* que toma valor 1 en el día 23-marzo-2023 (ie, 4 días hábiles después del anuncio)\
# 
# 
# 1. Como el banco Credit Suisse ya no existe, en el archivo de excel "Stocks.xlsx" encontrarán información de los precios diarios ajustados de UBS, de Credit Suisse, y del índice general S&P 500 entre 16-marzo-2022 y el 23-marzo-2023 inclusive (es decir, durante todo un año antes del evento hasta unos días posteriores a la noticia). *Hint: los códigos - tickers - para identificar estas acciones  son: UBS, SPY, y CS, respectivamente.*
# 
# 
# 2. Grafiquen la evolución de los precios de los 3 índices solicitados. Incluya una línea vertical en el día 20-marzo-2023 (primer día hábil luego del anuncio), y realice una *breve* descripción de lo que observa en el gráfico. Para facilitar el análisis, el dataframe con los precios provisto tiene reescalados a 100 todos los índices para el día 16-marzo-2022, y para así evitar  problemas de escala en el gráfico. 
# 
# 
# 3. Calculen los retornos diarios como la variación porcentual de cada índice.
# 
# 4. Estimen el modelo presentado previamente utilizando mínimos cuadrados ordinarios entre 17-marzo-2022 y el 23-marzo-2023, y presente los resultados.
# 
# 5. Analicen la significatividad individual de los coeficientes, e interprétenlos. ¿Qué porcentaje de variabilidad explica el modelo? ¿Hay un efecto significativo del anuncio de la compra de credit suisse en el precio de UBS en alguno de los días analizados?
# 
# 

# ### Solución Problema 3

# In[ ]:





# In[ ]:




