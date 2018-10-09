"""
Mauricio Araneda H.

file: numpy_matplotlib
-------------------------
Incluye varios ejemplos sobre como utilizar numpy + matplotlib. 

Para ejecutar cada uno de los ejemplos modificar última linea en el código, 
cambiandola por "ejemploX()" segun el ejemplo que se quiera ver.
"""
import numpy as np
import matplotlib.pyplot as plt

def ejemplo1():
	#Crea vector con 100 muestras de valores entre 0 y 2pi
    x = np.linspace(0, 2 * np.pi, 100)
	#Aplica la funcion sin() a cada elemento en el vector x, devuelve un vector del mismo largo
    f = np.sin(x)
	#Funcion para graficar, necesita valores en x y su resultado en y
    plt.plot(x,f)
	#Una vez creados todos los graficos esta funcion los muestra todos juntos en pantalla
    plt.show()

def ejemplo2():
    x1 = np.linspace(0, 2 * np.pi, 100)
    x2 = x1 + 0.1
    f = np.sin(x1)
    plt.plot(x1, f, label="Linea1")
    plt.plot(x2,f, label="Linea2")
	
	#Crea cuadro con nombres de las leyendas de cada curva en el grafico
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	
	#Crea etiquetas para los ejes del grafico
    plt.xlabel("x")
    plt.ylabel("sin(x)")

    plt.show()

def ejemplo3():
	#Crea matriz con valores random entre 0 y 1
    random_matrix = np.random.random((50, 50))
	
	#Funcion para mostrar matrices, asigna color de acuerdo al valor guardado en cada posicion.
	#Notar que en el eje y el grafico es decreciente
    plt.imshow(random_matrix);
	
    plt.show()

def ejemplo4():
    zeros = np.zeros((50,50))
    plt.imshow(zeros)
	
	#Setea limites para un eje. En este caso corrige el orden decreciente en el grafico
    plt.ylim(0,50)
	
    plt.show()

def ejemplo5():
    zeros = np.zeros((50, 50))
	
	#La notacion [:] indica que se recorreran todos los elementos en esa dimension, 
	#es equivalente a [0:len(zeros)]
    zeros[:][20:30] = 100
	
    plt.imshow(zeros)
    plt.ylim(0, 50)
    plt.show()

ejemplo1()