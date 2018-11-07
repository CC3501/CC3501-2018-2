import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from curvas import *
from utils import rgb

class Dragon:
    def __init__(self, p):
        self.p = np.array(p) # posicion
        self.vive = True # marca para poder eliminar ...
        self.r = 80


    def mover(self,dt,v):
        pass


    def dibujar(self):
        glPushMatrix()

        glTranslatef(self.p[0], self.p[1], 0.0)

        #Cuerpo1
        glColor3fv(rgb(181, 18, 7))

        glBegin(GL_TRIANGLE_FAN)

        glVertex2f(0, 0)
        radio_a = 100
        radio_b = 150
        ang = 2 * np.pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex2f(np.cos(ang_i) * radio_a,  np.sin(ang_i) * radio_b)

        glEnd()

        # Cuerpo2
        glColor3fv(rgb(226, 221, 145))

        glBegin(GL_TRIANGLE_FAN)

        glVertex2f(-40, 0)
        radio_a = 70
        radio_b = 100
        ang = 2 * np.pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex2f(-40 + np.cos(ang_i) * radio_a, np.sin(ang_i) * radio_b)

        glEnd()

        #Cabeza1
        glColor3fv(rgb(181, 18, 7))

        glBegin(GL_TRIANGLE_FAN)

        glVertex2f(0, 200)
        radio = 50
        ang = 2 * np.pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex2f(np.cos(ang_i) * radio, 200 + np.sin(ang_i) * radio)

        glEnd()


        #Cabeza2
        cuadrados = [
            [[-100, 150], [-100, 180], [0, 180], [0, 150]],
            [[-100, 190], [-100, 220], [0, 220], [0, 190]]
        ]

        glBegin(GL_QUADS)
        for cuadrado in cuadrados:
            for vertice in cuadrado:
                glVertex2fv(vertice)

        glEnd()

        # Alitas2
        glColor3fv(rgb(181, 18, 7))
        glBegin(GL_TRIANGLES)
        triangulos = [
            [[40, 0], [160, 0], [100, 110]]
        ]
        for triangulo in triangulos:
            for vertice in triangulo:
                glVertex2fv(vertice)
        glEnd()

        # Alitas
        glColor3fv(rgb(226, 221, 145))
        glBegin(GL_TRIANGLES)
        triangulos = [
            [[50, 0], [150, 0], [100, 100]]
        ]
        for triangulo in triangulos:
            for vertice in triangulo:
                glVertex2fv(vertice)
        glEnd()

        glPopMatrix()