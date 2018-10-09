import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


#Condiciones Dircihlet
c0 = 40
c1 = 0
c2 = 25

#puntos
h = 0.1
puntos = int(5/h)

#Matriz indices
indices = np.zeros((puntos, puntos), dtype = int)
for i in range(puntos):
    for j in range(puntos):
        indices[i][j] = i + j * puntos

#Matriz ecuaciones
ecuaciones = np.zeros((puntos ** 2, puntos ** 2))

# Matriz resultados
resultados = np.zeros(puntos ** 2)

#Condiciones Dirichlet
for i in range(puntos):
    #eje i
    resultados[indices[i][0]] = c0
    ecuaciones[indices[i][0]][indices[i][0]] = 1

    resultados[indices[i][puntos - 1]] = c1
    ecuaciones[indices[i][puntos - 1]][indices[i][puntos - 1]] = 1

    #eje j
    resultados[indices[0][i]] = c2
    ecuaciones[indices[0][i]][indices[0][i]] = 1

##Asignamos el resto de las ecuaciones
# -4 * u_ij + u_i+1j + u_ij-1 + u_ij+1 + u_ij-1 = 0
#  -4 * u_ij + 2 * u_i-1j + u_ij+1 + u_ij-1 = 0 Para el borde derecho con u' = 0
#cuidado con los puntos vecinos a los bordes de cond Dirichlet

for i in range(1, puntos):
    for j in range(1, puntos -1):
        indice = indices[i][j]
        ecuaciones[indice][indice] = -4

        #eje j
        if( j -1 == 0):
            resultados[indice] -= c0
            ecuaciones[indice][indices[i][j + 1]] = 1
        elif( j + 1 == puntos - 1):
            resultados[indice] -= c1
            ecuaciones[indice][indices[i][j - 1]] = 1
        else:
            ecuaciones[indice][indices[i][j + 1]] = 1
            ecuaciones[indice][indices[i][j - 1]] = 1

        #eje i

        if( i - 1 == 0):
            resultados[indice] -= c2
            ecuaciones[indice][indices[i + 1][j]] = 1
        elif( i == puntos - 1):
            ecuaciones[indice][indices[i - 1][j]] = 2
        else:
            ecuaciones[indice][indices[i + 1][j]] = 1
            ecuaciones[indice][indices[i - 1][j]] = 1

# ecuaciones * soluciones = resultados
# soluiones = resultados * ecuaciones ^ -1
ecuacionesInv = np.linalg.inv(ecuaciones)
soluciones = np.dot(resultados, ecuacionesInv)

#Graficamos

#Matriz solucion A
A = np.zeros((puntos, puntos))
for i in range(puntos):
    for j in range(puntos):
        A[i][j] = soluciones[indices[i][j]]

plt.imshow(A)
plt.colorbar()

#Ploteo 3d

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = []
Y = []
for i in range(puntos):
    X.append(i*h + h)
    Y.append(i*h + h)
X, Y = np.meshgrid(X, Y)
Z = A


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm ,linewidth=0 , antialiased=False)
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
print(X)
plt.show()