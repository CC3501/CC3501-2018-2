import numpy as np


def laplace(h):
    x = int(5 / h)
    y = int(5 / h)
    u = np.zeros((x, y))

    # condiciones de borde
    for i in range(0, x):
        u[0][i] = 180
    for j in range(0, y):
        u[j][0] = 80
    # calculo de w
    parte1 = np.cos(np.pi / (y - 1))
    parte2 = np.cos(np.pi / ((x) - 1))
    parte3 = (parte1 + parte2) ** 2
    parte4 = np.sqrt(4 - parte3)
    parte5 = 2 + parte4

    w = 4 / parte5

    print(u)
    iter = 0

    # Comienzo de la iteracion, usualmente se pone un error, pero se calcula con mas datos del problema(aplicaciones) asi
    # que solo pondremos iteraciones
    #IMPORTANTE: NUESTROS X E Y DEFINIERON EL TAMAÑO DE LA MATRIZ, PERO AHORA DEBEN RECORRERLA Y COMO CUENTA DESDE EL
    #CERO A X-1, DEBEMOS AJUSTARLOS PARA NO SALIRNOS DE LOS RANGOS DE LA MATRIZ
    x=x-1
    y=y-1
    r=10000000000 #valor random muy grande
    while iter < 300 or r>0.0001:
        for i in range(1, x):
            for j in range(1, y):
                # Condiciones tipo dirichlet
                r = (u[i + 1][j] + u[i - 1][j] + u[i][j + 1] + u[i][j - 1] - 4 * u[i][j]) / 4
                u[i][j] = u[i][j] + w * r
                # Condiciones tipo Neumann
                u[x][j] = u[x][j] + w * (u[x][j+1] + u[x][j-1] + (2 * u[x-1][j]) - 4 * u[x][j]) / 4
                #esquinas doble dirichlet
                u[0][0]=(u[0][1]+u[1][0])/2
                u[0][y]=(u[0][y-1]+u[2][y])/2
        iter += 1

    print(u)
    print(u[3][3])


laplace(0.5)
