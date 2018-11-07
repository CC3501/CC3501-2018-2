from Auxiliar.SETTINGS import *
from Figurascompuestas import *
def main():
    # Creamos una pantalla
    ancho = 800
    alto = 600
    init(ancho, alto, "titulo")
    ###

    figuras = []
    t = Triangulo(Vector(200, 200), Vector(600, 200), Vector(400, 500), (1, 0, 0))
    figuras.append(t)
    circ= Circulo(50, Vector(ancho/2, alto/2), celeste)
    figuras.append(circ)



    # Con esto mantenemos Corriendo la pantalla
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pass

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # limpiar buffers
        #figuras originales

        c = Circulo(10, Vector(10,10))
        for fig in figuras:
            fig.dibujar()
            c.dibujar()


        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()