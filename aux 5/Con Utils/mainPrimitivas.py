
from Auxiliar.SETTINGS import *
from Primitivas import *


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

        glBegin(GL_LINES)
        glColor(0.8, 0.1, 0.4)  # MORADO
        glVertex2f(400, 500)
        glVertex2f(800, 500)
        glEnd()
        # ES SUPER IMPORTANTE QUE PONGAN EL GLEND O LA FUNCION NO SABRA CUANDO DEJARON DE DIBUJAR
        glBegin(GL_TRIANGLES)
        glColor(1, 0, 0)  # ROJO, se pone en decimal
        glVertex2f(30, 30)
        glVertex2f(90, 30)
        glVertex2f(60, 60)
        glEnd()

        glBegin(GL_POLYGON)
        glColor(0.7, 1, 1)  # ROJO, se pone en decimal
        glVertex2f(200, 30)
        glVertex2f(300, 30)
        glVertex2f(350, 60)
        glVertex2f(300, 90)
        glVertex2f(200, 90)
        glVertex2f(150, 60)
        glVertex2f(200, 30)

        glEnd()
        #CIRCULO, SE HACE COMO UN VENTILADOR DE TRIANGULOS
        glBegin(GL_TRIANGLE_FAN)
        glColor(1, 0.08, 0.58)  # blanco
        glVertex2f(400, 300)
        ang = 2 * pi / 20
        radio=70
        for i in range(20):
            ang_i = ang * i
            glVertex2f(400 + cos(ang_i) * radio, 300 + sin(ang_i) * radio)
        glVertex2f(400 + radio, 300)
        glEnd()

        for fig in figuras:
           fig.dibujar()
        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()


main()
