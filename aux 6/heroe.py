import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from curvas import *
from utils import rgb

class Heroe:
    def __init__(self, p):
        self.p = np.array(p) # posicion
        self.vive = True # marca para poder eliminar ...
        self.r = 30

    def mover(self,dt,v):
        self.p = self.p + dt*np.array(v)


    def dibujar(self):
        glPushMatrix()

        glTranslatef(self.p[0], self.p[1], 0.0)

        # Cuerpo
        glColor3fv(rgb(0,255,0))
        glBegin(GL_QUADS)
        glVertex2fv([-10, -10])
        glVertex2fv([10, -10])
        glVertex2fv([10, -40])
        glVertex2fv([-10, -40])
        glEnd()

        # Piernas
        glColor3fv(rgb(56, 32, 3))
        glBegin(GL_QUADS)
        glVertex2fv([-5, -40])
        glVertex2fv([0, -40])
        glVertex2fv([0, -60])
        glVertex2fv([-5, -60])

        glVertex2fv([3, -40])
        glVertex2fv([8, -40])
        glVertex2fv([8, -60])
        glVertex2fv([3, -60])
        glEnd()

        #Cabeza
        glColor3fv(rgb(229, 178, 117))

        glBegin(GL_TRIANGLE_FAN)

        glVertex2f(0,0)
        radio = 20
        ang = 2 * np.pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex2f( np.cos(ang_i) * radio,  np.sin(ang_i) * radio)

        glEnd()

        #Sombrero
        triangulos = [
            [[0,25], [-10,30], [-40,0]],
            [[-10,30], [-25, 25], [-40,0]],
            [[-25,25], [-50,-10], [-40,0]],
            [[0,25], [-40,0], [-20, -10]]
        ]

        glColor3fv(rgb(0,255,0))
        glBegin(GL_TRIANGLES)
        for triangulo in triangulos:
            for vertice in triangulo:
                glVertex2fv(vertice)

        glEnd()



        glPopMatrix()

