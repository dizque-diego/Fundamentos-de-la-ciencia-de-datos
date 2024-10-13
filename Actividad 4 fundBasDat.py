#Actividad 4
#Ejercicio 1
# Escribir un programa en Python que declare una lista y la vaya llenando de números hasta
# que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los
# valores introducidos).


import random
lista_actividad1 = []
for _ in range(10):
    aleatorio = random.randint(-10,10)
    if aleatorio >= 0 :
        lista_actividad1.append(aleatorio) 
    else: break 
print(lista_actividad1)


#Ejercicio 2
# Escribir un programa en Python que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco
# enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.


import random
lista1_a2 = []
lista2_a2 = []
lista3_a2 = []
for i in range(5):
    print(f'ingrese 5 numeros para la lista 1')
    numlist1 = int(input(f'el numero {i+1} es '))
    lista1_a2.append(numlist1)
for i in range(5):
    print(f'ingrese 5 numeros para la lista 2')
    numlist2 = int(input(f'el numero {i+1} es ')) 
    lista2_a2.append(numlist2)

lista3_a2.extend(lista1_a2)
lista3_a2.extend(lista2_a2)
print(f'la lista 1 es {lista1_a2}')
print(f'la lista 2 es {lista2_a2} ')
print(f'la ultima lista es {lista3_a2}')


# Ejercicio 3
# Escribir un programa en Python que guarde la temperatura mínima y máxima de los
# últimos 5 días. El programa debe recibir la información, almacenarla y mostrar:
# -La temperatura media de cada día
# -Los días con menor temperatura
# -Después de almacenar la información de los 5 días, el programa debe reconocer una
# temperatura más por teclado y mostrar los días cuya temperatura máxima coincide
# con ella. si no existe ningún día se muestra un mensaje de información.


def promedio(x):
    n = len(x)
    suma = sum(x)
    return suma / n

dia_1 = []
dia_2 = []
dia_3 = []
dia_4 = []
dia_5 = []
temperaturas = []

min1 = float(input(f'ingrese por favor la temperatura minima del dia 1 '))
dia_1.append(min1)
max1 = float(input(f'ingrese por favor la temperatura maxima del dia 1 '))
dia_1.append(max1)
min2 = float(input(f'ingrese por favor la temperatura minima del dia 2 '))
dia_2.append(min2)
max2 = float(input(f'ingrese por favor la temperatura maxima del dia 2 '))
dia_2.append(max2)
min3 = float(input(f'ingrese por favor la temperatura minima del dia 3 '))
dia_3.append(min3)
max3 = float(input(f'ingrese por favor la temperatura maxima del dia 3 '))
dia_3.append(max3)
min4 = float(input(f'ingrese por favor la temperatura minima del dia 4 '))
dia_4.append(min4)
max4 = float(input(f'ingrese por favor la temperatura maxima del dia 4 '))
dia_4.append(max4)
min5 = float(input(f'ingrese por favor la temperatura minima del dia 5 '))
dia_5.append(min5)
max5 = float(input(f'ingrese por favor la temperatura maxima del dia 5 '))
dia_5.append(max5)

temperaturas.append(dia_1)
temperaturas.append(dia_2)
temperaturas.append(dia_3)
temperaturas.append(dia_4)
temperaturas.append(dia_5)

print(f'la temperatura del dia 1 estuvieron entre {dia_1}')
print(f'la temperatura del dia 1 estuvieron entre {dia_2}')
print(f'la temperatura del dia 1 estuvieron entre {dia_3}')
print(f'la temperatura del dia 1 estuvieron entre {dia_4}')
print(f'la temperatura del dia 1 estuvieron entre {dia_5}')

print(f'la Temperatura promedio del dia 1 fue de {promedio(dia_1)} grados')
print(f'la Temperatura promedio del dia 2 fue de {promedio(dia_2)} grados')
print(f'la Temperatura promedio del dia 3 fue de {promedio(dia_3)} grados')
print(f'la Temperatura promedio del dia 4 fue de {promedio(dia_4)} grados')
print(f'la Temperatura promedio del dia 5 fue de {promedio(dia_5)} grados')

Temperatura_buscar = float(input(f'ingrese la temperatura máxima a buscar: '))
días_con_temp_max = [i + 1 for i, (_, max_temp) in enumerate(temperaturas) if max_temp == Temperatura_buscar]

if días_con_temp_max:
    días_str = ''
    for dia in días_con_temp_max:
        días_str += f"{dia}, "  
    días_str = días_str.rstrip(', ') 
    print(f"Día(s) cuya temperatura máxima coincide con {Temperatura_buscar} grados: {días_str}")
else:
    print(f"No hay días con una temperatura máxima de {Temperatura_buscar} grados.")


# Ejercicio 4
# Crea un programa en Python que permita adivinar un número. La aplicación genera un
# número aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si
# el número a adivinar es mayor o menor que el introducido, así como el número de intentos
# que quedan, se contarán con 10 intentos para adivinar el número). El programa termina
# cuando se acierta el número y debe indicar en que intento fue acertado, si se llega al límite
# de intentos, el programa debe mostrar que se había generado.


import random
Numero_adivinar = random.randint(1,100)
intentos = 10
intento_act = 0
for intact in range(1, intentos +1):
    numero_elegido = int(input(f'Elija un numero entre el 1 al 100, tiene {intentos} intentos para adivinar '))
    intento_act += 1 
    intentos -=1
    if numero_elegido == Numero_adivinar:
        print(f'¡Felicidades! has adivinado el numero, el numero es {Numero_adivinar}, lo lograste en {intento_act} intentos. te quedaban {intentos} intentos')
        break
    elif numero_elegido > Numero_adivinar:
        print(f'incorrecto, elegiste el numero {numero_elegido}, el numero a adivinar es menor. Llevas {intento_act} intentos')
    elif numero_elegido < Numero_adivinar:
        print(f'Incorrecto, usted ha elegido el numero {numero_elegido}, el numero a adivinar es mayor. Llevas {intento_act} intentos')
if intentos == intento_act:
        print(f'¡Caramba! elegiste {numero_elegido} ¡Perdiste! ¡Te quedaste sin intentos! El numero a adivinar era {Numero_adivinar}')



