"""
Mauricio Araneda H.

file: ejemplo_numpy
-------------------------
Incluye varios ejemplos sobre como utilizar numpy. 
Los resultados son mostrados por consola.
"""
import numpy as np

#De manera similiar a como se trabaja con las listas o arrays de python
#podriamos necesitar arreglos con secuencias
a = np.arange(15)
print(a)

#Una de las ventajas de numpy es su trabajo simple con arreglos multidimensionales
#podemos transformar un arreglo de dimension [1x15], en una matriz de [3x5] con un solo comando
a = a.reshape(3,5)
print(a)

#Podemos crear numpy-arrays a partir de arrays de python
b = np.array([5,7,8])
print(b)

#IMPORTANTE: Un problema común es ejecutar np.array() con varios elementos como parámetros, y no un solo array.
#Ejemplos:
#   a = np.array(1,2,3,4) No compila porque debe recibir un único parámetro
#   a = np.array([1,2,3,4]) Sí compila

#Al igual que en MATLAB podemos crear matrices vacías para rellenar luego, como una matriz llena de 0's
#o de 1's. La sintáxis es:
zeros = np.zeros((5,4))
print(zeros)

ones = np.ones((2,3,4))
print(ones)

#Los arreglos de numpy pueden ser indexados como las listas normales, además se pueden iterar y se le pueden
#extraer trocitos.

a = np.array([3,6,9,12])
print("a =", a)

#Podemos indexar
print("El valor de a[2] es:", a[2])

#Podemos sacar trocitos
print("a[1:3] =", a[1:3])

#Podemos iterar
for val in a:
    print(val)
