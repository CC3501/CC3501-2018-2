import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from curvas import *
from utils import rgb

class Flecha:
    def __init__(self, p):
        self.p = np.array(p) # posicion
        self.vive = True # marca para poder eliminar ...
        self.r = 30

    def mover(self,dt,v):
        self.p = self.p + dt*np.array(v)

    def dibujar(self):
        glPushMatrix()

        glTranslatef(self.p[0], self.p[1], 0.0)

        #Punta flecha
        triangulos = [
            [[0,15], [15, 0], [0, -15]],
        ]

        glColor3fv(rgb(0,0,0))
        glBegin(GL_TRIANGLES)
        for triangulo in triangulos:
            for vertice in triangulo:
                glVertex2fv(vertice)

        glEnd()

        glBegin(GL_QUADS)
        cuadrados = [
            [[-50,-5], [-50, 5], [0, 5], [0, -5]]
        ]

        for cuadrado in cuadrados:
            for vertice in cuadrado:
                glVertex2fv(vertice)
        glEnd()

        glPopMatrix()

