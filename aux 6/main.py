# coding=utf-8
"""
Daniel Calderon, CC3501, 2018-2
Transformation examples using PyOpenGL
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from utils import *
from fuego import *
from heroe import *
from dragon import *
from flecha import *



celeste = rgb(34, 201, 226)
rojo = rgb(255, 0, 0)
verde = rgb(0, 255, 0)
azul = rgb(0, 0, 255)

def drawBackground():
    glBegin(GL_QUADS)

    global celeste
    glColor3fv(celeste)

    glVertex2fv([800, 600])
    glVertex2fv([0, 600])
    glVertex2fv([0, 0])
    glVertex2fv([800, 0])

    glColor3f(0.5,0.5, 0)

    glVertex2fv([800, 100])
    glVertex2fv([0, 100])
    glVertex2fv([0, 0])
    glVertex2fv([800, 0])

    glEnd()

def init():
    Width = 800
    Height = 600

    pygame.init()
    pygame.display.set_mode((Width, Height), OPENGL | DOUBLEBUF)
    pygame.display.set_caption("Aux6")
    # inicializar opengl
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, Width, 0.0, Height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # definir variables de opengl
    glClearColor(0.0, 0.0, 0.0, 0.0)  # color del fondo
    glShadeModel(GL_SMOOTH)
    glClearDepth(1.0)


fuego = Fuego([500, 400])
heroe = Heroe([100, 100])
dragon = Dragon([650, 250])
flechas = []
if __name__ == '__main__':

    init()
    #Medimos el tiempo inicial
    t0 = pygame.time.get_ticks()
    instante = 0
    maxInstante = 100
    run = True
    while run:
        if instante == maxInstante:
            instante = 0


        #Control del tiempo
        t1 = pygame.time.get_ticks() #tiempo actual
        dt = (t1 - t0)
        t0 = t1

        for event in pygame.event.get():
            if event.type == QUIT:  # close window
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pass
                if event.key == K_d:
                    heroe.mover(dt, [1, 0])

                if event.key == K_a:
                    heroe.mover(dt, [-1, 0])

                if event.key == K_p:
                    flecha = Flecha(heroe.p)
                    flechas.append(flecha)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clean buffers

        drawBackground()


        fuego.mover(instante, maxInstante, heroe.p)
        for f in flechas:
            f.mover(dt, [1,0])
            if estanChocandoX(f, dragon):
                dragon.vive = False
                flecha.vive = False

        if estanChocando(heroe, fuego):
            heroe.vive = False

        if heroe.vive:
            heroe.dibujar()

        if dragon.vive:
            dragon.dibujar()

        for f in flechas:
            if f.vive:
                f.dibujar()


        fuego.dibujar()
        for f in flechas:
            f.dibujar()

        pygame.display.flip()  # refresh screen
        pygame.time.wait(int(1000 / 30))  # 30 fps

        instante += 1

    pygame.quit()