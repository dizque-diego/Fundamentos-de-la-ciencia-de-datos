#1. Considere las siguientes médidas para describir conjuntos de datos:
#- Media
#- Mediana
#- Moda
#- Varianza
#- Desviación Estandar
#- Coeficiente de variación
#- Normalización Z
#2. Describa formalmente cada medida y presente cómo se construyen.
#3. Cree las funciones en python. Presente el código y expliquelo.
#4. Referencias

#Media
# La media es una herramienta estadistica basica, en la cual se tiene una agrupación de numeros
# se suman todos los valores dentro de la agrupacion de numeros
# este valor se divide por el numero de elementos que componen dicha agrupación


def promedio(x):            #se define la funcion con nombre promedio
    n = len(x)              #se establece la variable n que es igual al numero de elementos que conformen una lista
    suma = sum(x)           #se establece que la variable suma sea igual a la suma de los elementos que conformn la lista
    return 1/n * suma       #se establece que el valor de retorno sea la division de ''suma'' entre n
lista = [1 , 5 , 6 , 3]
print (promedio(lista))



# Mediana
# La mediana el el valor que se encuentra en la mitad del conjunto
# Es decir, que al ordenar los numeros, és se encuentra justamente en el medio

def mediana(y):
    s = sorted(y)                           #se utiliza el metodo de sort para ordenar los elementos de la lista en orden
    t = len(y)                              # se utiliza el metodo len para medir el numero de elementos que la componen
    if len(y) % 2 != 0 :                    # si el numero de elementos no es numero pan
        return  len(y) // 2                     #retorna el numero de elementos dividido entre dos
    elif len(y) % 2 == 0:                   # si el numero de elementos es par  
        return (len(y) - 1 // 2)                #el numero de elementos es restado con -1 y posteriormente dividido entre dos
numeros = [2 , 3 , 4 , 75 , 7 , 6]
print (mediana(numeros))

# Moda
# La moda es el valor mas frecuente o repetido dentro de un conjunto de datos

def moda(z):
    max_cuenta = 0                  # se establece una variable para mantener la cuenta maxima de un registro
    modae = []                      # se crea la lista ''modae'' para al macenar el numero de elementos que se puede repetir
    for i in range(len(z)):         # para un indice en el rango de una lista
        cuenta = 0                  # su cuenta comenzaria en 0
    for j in range(len(z)):         # para otro indice en el rango de una lista
        if z[i] == z[j]:            # si los dos indices anteriormente mencionados son los mismos
                cuenta += 1             # la cuenta de este indice aumentaria en +1
        if cuenta > max_cuenta:     # si la variable cuenta es mayor que la variable cuenta maxima
                max_cuenta = cuenta # la variable cuenta se vuelve la variable cuenta maxima
                modae = z[i]       # variable ''modae'' es igual a un indice en una lista
    print (modae)                   # Imprimir moda
aglomeracion = [ 15 , 35 , 20 , 15 , 32 , 15 , 15 ]
print (moda(aglomeracion))
# DISCLAIMER la sintaxis del codigo aparentemente esta bien, en este caso da que la moda es ''none'' cuando se usó en Visual studio code
#  se probó con paiza.io el codigo y si funcionó

# Varianza
# La varianza es una medida que busca indicar cuán dispersos estan los valores de un conjunto numerico respecto al promedio.

def calcular_varianza (w):                              
    promedio(w)                                 # Se utiliza la funcion previamente creada de promedio
    suma_dif_cua = 0                            # se crea la variable ''suma_dif_cua'' con valor 0
    for p in w:                                 # para un indice dentro de una lista
        suma_dif_cua += (p - promedio(w)) ** 2  # se realiza la resta entre el indice y el promedio, luego se eleva al cuadrado. este valor ocupara la variable ''suma_dif_cua''
        variance = suma_dif_cua / (len(w) - 1)  # la variable ''suma_dif_cua'' es dividida por el numero elementos que conforman la lista - 1, este valor tomara la variable ''variance''
        return variance                         # retorne el valor de la variable ''variance''

grupo = [2 , 4 , 5 , 6 , 7 , 9]
calcular_varianza(grupo)
print (calcular_varianza(grupo))

# Desviación estandar
# La desviacion estandar es una medida de variacion estadistica, 
# se utiliza para calcular la dispersion en que los datos difieren de la media
# una baja desviacion indica que los datos estan mas cerca de la media, mientras que mayor desviación indica que los valores estan dispersos en un rango mayor
# es la raiz cuadrada de la varianza
# la manera mas sencilla de realizarlo teniendo en cuenta las funciones previamente mencionadas sería:
def no_nonsense_deviation (q):              
    calcular_varianza(q)                            #se llama la funcion previamente creada para la varianza
    desviacion = calcular_varianza(q) ** 0.5        # al valor que resulta de la funcion previamente mencionada se eleva por 0.5, este valor tomará la variable ''desviacion''
                                                    # teniendo en cuenta las propiedades de la potenciacion, una raiz cuadrada es igual a un numero elevado por un fraccionario
                                                    # una raiz cuadrada = a^1/2 y 1/2 = 0.5 
    return desviacion                               # retorne la variable ''desviacion''
no_nonsense_deviation(grupo)                        
print(no_nonsense_deviation(grupo))


# Coeficiente de variación
# Es una medida estadistica que ofrece informacion sobre la dispercion de un conjunto de datos
# Esta permite el analisis de las desviaciones de los datos con respecto a la media y con los datos dispersos entre sí
# se puede presentar de forma relativa o porcentual, para esta ultima solo es necesario multiplicar por 100 su forma relativa
# Esta es la Desvicación estandar Dividido entre la Media

def cv (v):                                         #en este caso se utilizarán dos funciones previamente definidas, las de desviacion estandar y promedio
    coef = no_nonsense_deviation(v) / promedio (v)  #se operan las funciones previamente mencionadas, desviacion estandar / promedio, este valor tomará la variable ''coef''
    perc = coef * 100                               #el valor de la variable ''coef'' se multiplica por 100. este valor tomará la variable de ''perc''
    return perc                                     #retorne el valor de la variable ''perc''
cv(grupo)
print (cv(grupo))

# Normalización Z 
# La normalizacion es una tecnica que sirve para pre- procesar los datos que se utilizan para ajustar caracteristicas de los datos dentro de un rango especifico
# en el caso puntual de la normalizacion z, es util porque permite comparar caracteristicas con diferentes unidades y rangos de valores
# Consiste en transformar los valores de una caracteristica en un conjunto de datos que tengan una media de 0 y una desviacion estandar de 1
# se logra restando la media de los datos y dividiendo el resultado por la desviacion estandar.

def norma_z (h):
    media = promedio(h)                 #se llama una funcion previamente utilizada, tomara el nombre de ''media''
    sd = no_nonsense_deviation(h)       #se llama una funcion previamente utilizada, tomara el nombre de ''sd''
    for f in h:                         #para un indice ''f'' dentro de una lista
        norma = [( f - media) / sd]     # se resta el indice ''f'' con la variable ''media'' y se divide entre ''sd'' este valor tomará la variable ''norma''
        return(norma)                   #retorne el valor de norma.

norma_z(grupo)
print (norma_z(grupo))




