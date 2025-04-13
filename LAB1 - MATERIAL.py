#!/usr/bin/env python
# coding: utf-8

# ## GUÍA EJERCICIOS NRO 1 - MATERIAL DE CONSULTA
# 
# ### ECONOMETRÍA PARA FINANZAS
# #### UNIVERSIDAD TORCUATO DI TELLA - 1° TRIMESTRE 2025
# ##### Francisco Ciocchini - Bárbara Guerezta

# ### Objetivo

# El objetivo de este trabajo práctico es familiarizarse con el uso de Python, conocer algunas herramientas que serán útiles durante la materia.\
# Mucho del material que utilizamos en este trabajo proviene del libro "Automate the Boring Stuff with Python"

# ### Operaciones básicas en Python

# Podemos utilizar Python como una calculadora recurriendo a operadores:\
# 1. ** Exponente
# 2. % Módulo o resto en una división
# 3. // El entero en una división
# 4. / División
# 5. '* Multiplicación
# 6. '- Resta
# 7. '+ Suma

# *Ejemplos*

# In[1]:


2 + 3 * 6 # Noten que separa en términos!


# In[2]:


(2 + 3) *6


# In[3]:


2**3


# In[4]:


3*5


# In[5]:


28//8


# In[6]:


28/8


# In[7]:


28%8


# ### Tipos de Datos: integer, floating and string

# Un tipo de dato es una categoría para un valor; todos los valores pertenecen a un tipo de dato. Los más comunes son los integers (whole numbers), floating (decimals), strings (text).

# In[8]:


type(-2)


# In[9]:


type(5)


# In[10]:


type(0.5)


# In[11]:


type(a)


# In[12]:


type("a")


# Noten que "a" es reconocida como string cuando está entre comillas. Si me olvido las comillas Python asume que se trata de un objeto, y como no lo hemos definido, no lo encuentra.

# ### Concatenar

# Un operador puede tener diferente significado en función del tipo del dato, por eso es muy importante tener bien delimitados los valores en Python. Veamos cómo funciona el operador "+" para dos tipos de datos: strings y numerics.

# In[13]:


2 + 5


# In[14]:


"2" + "5"


# ¿qué ocurrió? '2' y '5' están entre comillas. Eso significa que para python, el 2 y el 5 son textos. El "+" allí no funciona como un operador de suma, sino que concatena los valores. Veamos con otros ejemplos:

# In[15]:


"Hello" + "world"


# In[16]:


"Hello " + "world"


# In[17]:


"Alice" + 42


# El error anterior radica en que Python no puede concatenar strings con integers. ¿Cómo lo podemos salvar?

# In[ ]:


"Alice tiene " + "42" + " años"


# Ahora sí.

# ¿Qué ocurre con el operador '*'?

# In[18]:


2*4


# In[19]:


'Alice' * 2


# Nota: ES FUNDAMENTAL TENER BIEN IDENTIFICADOS LOS TIPOS DE VALORES PARA QUE LOS OPERADORES REALICEN LA TAREA QUE QUEREMOS.

# ### Funciones básicas

# Cuando instalamos Python incorporamos algunas operaciones primitivas: como los operadores que vimos antes, pero también algunas otra funcionalidades. Estas funciones tienen una sintaxis similar a lo que conocemos como funciones en matemática: f(x). Sobre el argumento "x" aplicamos una operación que se llama "f". Veamos algunas:

# In[20]:


len(edad) #La función len cuenta la cantidad de caracteres de un argumento. Este argumento puede ser numérico, o string


# In[21]:


len("Marcelo")


# In[22]:


str(42) #La función "str" convierte en string un valor que puede no serlo originalmente. Aquí convertimos en string el número


# In[23]:


int("42") #Equivalentemente int puede convertir un string en integer


# In[24]:


float(42) #La función float convierte en un número decimal un integer o un string


# In[25]:


float("42")


# In[26]:


print("Hola") #La función print permite imprimir en pantalla (ahora puede parecer "innecesaria", pero no lo es)


# Hay más funciones nativas, y las iremos viendo a lo largo del curso (con ayuda de Google incluso!)

# ### Guardar valores en variables

# Hasta ahora no hemos guardado nada en el disco ni en la memoria de la computadora. Simplemente estamos "viendo" elementos.\
# Nosotros vamos a necesitar guardar cierta información o valores al menos transitoriamente a lo largo del curso.\
# Es decir, vamos a crear *variables* para guardar *valores*

# In[ ]:





# In[29]:


edad = 33 #Creamos un objeto, llamado 'edad' que toma valor 33


# Noten que la variable *edad* está asociada a un valor, 33. Ahora podemos hacer uso del número 33 a través de su "nombre", que es "edad".

# In[30]:


edad


# In[31]:


print(edad) #print es una función primitiva de python que permite imprimir en pantalla cierta información.


# Supongamos que Ana tiene 33 años, y queremos saber cuántos años tendrá dentro de 5 años

# In[32]:


edad + 5


# In[33]:


type(edad)


# In[15]:


"Tengo " + edad + " años"


# ¿Por qué da error? Exacto! Porque edad es una variable integer, y no puede ser concatenada con texto, ¿cómo lo corregimos?

# In[17]:


"Tengo " + str(edad) + " años"


# Noten que podemos encadenar funciones también!

# In[34]:


len(str(edad + 5))


# ¿Qué hicimos? A la variable edad le sumamos 5; luego lo convertimos en un string; y finalmente contamos la cantidad de caracteres que tiene ese string.

# ### Nuestro primer programa

# Intentaremos crear una rutina muy simple de preguntas y respuestas con el usuario que está frente a la computadora, es decir: Uds!

# In[35]:


print("Hola!")
print("Me dirías tu nombre?") 
nombre = input()
print("Qué gusto conocerte " + nombre)
print("Tu nombre tiene " + str(len(nombre)) + " letras")
print("¿Cuántos años tienes?")
edad = input()
print("Tendrás "+ str(int(edad) + 5) + " dentro de 5 años.")
input()


# ¿qué hizo este programa? Interatuó con el usuario, preguntándole su nombre y asombrándolo con una operación matemática.\
# Noten que cuando devolvió la edad que el usuario tendrá dentro de 5 años, debió convertir la variable "edad" a integer, para luego sumarle 5 años y finalmente volverlo a clasificar como "string" y poder así concatenerlo con otro texto, ¿se dan cuenta por qué?

# ### Más tipos de datos

# En Python existen otros tipos de datos que permiten almacenar valores; y de hecho, algunos de ellos permiten almacenar múltiples datos a la vez.

# **Listas**
# Las listas, como el nombre indica permite almacenar valores (que pueden ser string, floats, integers, boolean).\
# Se identifican porque están escritas entre corchetes, '[]'\
# Los elementos que se almacenan en una lista se llaman "items", y se separan por comas.\
# Cada item tiene una posición, "índice". Y esa posición se numera de izquierda a derecha arrancando por 0 (y sumando de a 1). O de derecha a izquierda, empezando por -1 (y restando de a 1).
# 

# In[36]:


[4, 5, 6, 7]


# Las listas pueden almacenarse con un nombre:

# In[37]:


lista1 = [10, 15, "Brenda", "Marcos"] ; print(lista1)


# Podemos acceder a los elementos de la lista (items):la sintaxis es lista[idx] donde idx es el número de índice

# In[38]:


lista1[0]


# In[39]:


lista1[-1]


# In[40]:


lista1[3]


# In[42]:


lista1[0:2]


# In[45]:


lista1[2:]


# In[47]:


lista1[0:2]


# In[48]:


lista1[-2:]


# Noten que cada item tiene 2 índices posibles. Por ejemplo, el elemento "Marcos" tiene índice 3 y también índice -1.

# **Operaciones con listas**

# In[49]:


len(lista1) #Cuenta la cantidad de elementos que hay en la lista


# In[50]:


lista0 = [1, 2, 3, 4]


# In[51]:


sum(lista0) #Cuando la lista contiene sólo números puede hacer operaciones matemáticas simples


# In[52]:


max(lista0)


# In[53]:


min(lista0)


# In[54]:


lista0 *2 #Duplica la lista


# Podemos cambiar los elementos de una lista

# In[55]:


lista0


# In[31]:


lista0[2] = 50 ; lista0 #Noten que cambiamos el item cuyo índice es 2, por un 50


# Podemos encontrar el índice de un elemento presente en una lista. Supongamos que queremos saber en qué posición está el nro 1:

# In[56]:


lista0.index(1)


# In[57]:


lista1.index("Brenda")


# In[58]:


lista0.sort() ; lista0


# **DataFrames**
# Los dataframe son un objeto de Pandas. Pandas es una librería muy conocida de Python (para usarla primero hay que instalarla) que permite manipular datos tabulados.\
# Un dataframe es una estructura de datos de dos dimensiones que permite almacenar datos de distinto tipo (string, integer, float, etc) en columnas. Es similar a una hoja de cálculo de Excel, o un data.frame de R. Cada elemento tiene un índice bidimensional, como en las matrices. Y al igual que con las listas, los índices comienzan a contar desde el 0.

# Para poder utilizar los dataframes primero debemos instalar la librería de pandas.\
# El que no lo haya hecho nunca, debe ir al "cmd" y escribir: "pip3 install pandas"
# 

# In[59]:


import pandas as pd


# In[73]:


lista1 = [['ARG', "CABA"],
         ['BRA', "Brasilia"],
         ['COL', "Bogotá"],
         ['PER', "Lima"]]


# In[74]:


lista1


# In[75]:


df1 = pd.DataFrame(lista1, columns = ['Pais', 'Ciudad'])


# In[76]:


df1


# El objeto lista1 es una lista de listas: cada elemento de la lista es a su vez una lista de 2 elementos.\
# El objeto "df1" es un DataFrame que creamos gracias a la librería pandas ("pd"). Convertimos la lista1 en un dataframe. Cada elemento de esa lista se convirtió en una fila con dos columnas: País, y Ciudad.

# **Operaciones con DataFrames** 

# Existen diversas operaciones que se pueden hacer en un dataframe.

# *Agregar una columna*

# In[77]:


df1['Hab'] = [45.1, 212.6, 50.9, 33.1] ; df1


# *Ordenar los elementos del DataFrame de mayor a menor*

# In[78]:


df1


# In[79]:


df1.sort_values(by = "Hab", ascending = False)


# In[81]:


df1 = df1.sort_values(by = "Hab", ascending = False) ; df1


# *Sumar, Restar, máximo, mínimo*

# In[82]:


sum(df1['Hab'])


# In[83]:


min(df1['Hab'])


# In[84]:


max(df1['Hab'])


# In[86]:


df1['Hab'].mean()


# In[87]:


df1['Hab'].max()


# In[91]:


df1.iloc[0, 2]


# In[100]:


mean_hab = df1['Hab'].mean()


# In[102]:


df1.loc[df1['Hab'] < mean_hab]


# *Agregar otra columna*

# In[47]:


df1


# In[103]:


df1['Sup'] = [8.515, 1.142, 2.792, 1.285]


# In[119]:


df1


# *Crear una columna a partir de otras dos*

# In[105]:


df1['Hab_km2'] = df1['Hab'] / df1['Sup'] ; df1


# Así como podemos identificar índices en una lista a partir de los valores de los items, de manera equivalente podemos seleccionar elementos en un dataframe. Supongamos que queremos encontrar al país de nuestro dataframe que posee la mayor cantidad de habitantes

# In[106]:


df1.loc[df1['Hab'] == df1['Hab'].max()]


# La sintaxis es simple: df1.loc["condición"].\
# Noten que el símbolo "==" se utiliza para evaluar si cierta condición es cierta o falsa.

# Equivalentemente podríamos identificar los países que superan cierto umbral de densidad demográfica

# In[107]:


df1.loc[df1['Hab_km2'] > 20]


# ### Interacción con Microsoft Excel

# **Leer archivos de excel**

# Existen muchos caminos para poder procesar archivos de Microsoft Excel en Python. Pandas tiene algunas funciones, pero no es la única. E incluso en Pandas hay, por lo menos, dos caminos alternativos:

# Supongamos que contamos con información (falsa) de las ventas de una heladería desde el año 2002 hasta el año 2021 inclusive. Esas ventas están almacenadas en un archivo de excel que debemos importar

# In[108]:


import pandas as pd # No es necesario importar la librería cada vez que se la usa, se puede importar todo una vez al comienzo del código


# In[ ]:


#pip3 install openpyxl


# In[110]:


helados = pd.read_excel("Problema3_Ventas.xlsx")


# In[111]:


type(helados)


# In[112]:


helados.head()


# El dataframe está estructurado de esta manera: columna 'year' contiene el año que se tabula. Cada año está separado en trimestres de acuerdo a la estación del año: 'verano', 'otoño', 'invierno', 'primavera' (¿Se les ocurre por qué?). La variable 'Ventas_mes' contiene las ventas promedio en cada mes de esa estación de ese año, escaladas en términos de kilos de helado. 'Precio_kg' es el precio promedio del kilo de helado de esa temporada. 'IPC' es el índice de precios al consumidor de Buenos Aires para esa estación del año

# **Variación de ventas**
# Para calcular el aumento de las ventas de helado a lo largo del tiempo podemos hacerlo de dos maneras:\
# 1. La variación de cada temporada contra la temporada anterior (variación trimestral)
# 2. La variación de cada temporada contra la misma temporada del año anterior (variación interanual)

# In[113]:


#Creamos una columna nueva donde se almacenará la variación trimestral
helados['Kg_trim'] = helados['Ventas_mes'].pct_change()


# In[114]:


#Creamos una columna nueva donde se almacenará la variación interanual
helados['Kg_yoy'] = helados['Ventas_mes'].pct_change(4)


# In[115]:


helados.head()


# In[116]:


#Validaciones:
print("Var trimestral: " + str(301/200-1))
print("Var yoy: " + str(301/280-1))


# In[117]:


#Validaciones (Camino 2):
trim = helados.iloc[4,2]/helados.iloc[3,2]-1
yoy = helados.iloc[4,2]/helados.iloc[0,2]-1


# In[118]:


print("Validaciones: \n Var trimestral: " + str(trim) + "\n Var yoy: " + str(yoy))

