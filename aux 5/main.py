import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from math import *

from Auxiliar.SETTINGS import *
def init():
    pygame.init()
    pygame.display.set_mode((ancho, alto), OPENGL| DOUBLEBUF)
    pygame.display.set_caption("Auxiliar 5")
    # inicializar opengl
    glViewport(0, 0, ancho, alto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, ancho, 0.0, alto)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # definir variables de opengl
    glClearColor(0.0, 0.0, 0.0, 0.0)  # color del fondo
    glShadeModel(GL_SMOOTH)
    glClearDepth(1.0)
    # glDisable(GL_DEPTH_TEST)
    return

def main():
    init()
    run=True
    fig= []
    from Auxiliar.Persona import Persona
    fig1= Persona((ancho/2,alto/2))
    fig.append(fig1)
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glPushMatrix()
            glRotate(30, 0, 0, 1)
            glTranslate(300, 0, 1)
            glScale(0.5,0.5,1)



            glBegin(GL_QUADS)
            glColor(0,0.5,0.5)
            glVertex2f(200,150)
            glVertex2f(800, 150)
            glVertex2f(800, 300)
            glVertex2f(200, 300)
            glEnd()

            #Techo
            glBegin(GL_POLYGON)
            glColor(1, 0.5, 0)
            glVertex2f(300, 300)
            glVertex2f(800, 300)
            glVertex2f(700, 500)
            glVertex2f(300, 500)
            glEnd()
            glBegin(GL_TRIANGLES)
            glColor(1, 0, 0)
            glVertex2f(200, 300)
            glVertex2f(300, 500)
            glVertex2f(400, 300)

            glEnd()

            # Linea
            glBegin(GL_LINES)
            glColor(0, 0, 1)  # azul
            glVertex2f(400, 300)
            glVertex2f(400, 150)
            glEnd()

            # Puerta
            glBegin(GL_QUADS)
            glColor(0.5, 0.5, 0)  # cafe
            glVertex2f(250, 150)
            glVertex2f(350, 150)
            glVertex2f(350, 250)
            glVertex2f(250, 250)
            glEnd()

            # Manilla
            glBegin(GL_TRIANGLE_FAN)
            glColor(0, 0.0, 0.58)
            glVertex2f(340, 200) #CENTRO
            ang = 2 * pi / 20
            radio = 10
            for i in range(20):
                ang_i = ang * i
                glVertex2f(340 + cos(ang_i) * radio, 200 + sin(ang_i) * radio)
            glVertex2f(340 + radio, 200)
            glEnd()

            # VENTANA
            glBegin(GL_QUADS)
            glColor(1, 1, 1)
            glVertex2f(550, 180)
            glVertex2f(700, 180)
            glVertex2f(700, 280)
            glVertex2f(550, 280)

            glColor(0, 0, 0)
            glVertex2f(550, 220)
            glVertex2f(700, 220)
            glVertex2f(700, 240)
            glVertex2f(550, 240)

            glVertex2f(618, 180)
            glVertex2f(636, 180)
            glVertex2f(636, 280)
            glVertex2f(618, 280)
            glEnd()
            glPopMatrix()

            for figs in fig:
                figs.dibujar()





            pygame.display.flip()
            pygame.time.wait(int(1000/30)) #30 fps
    pygame.quit()

main()

