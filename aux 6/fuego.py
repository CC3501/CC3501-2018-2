import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from curvas import *
from utils import rgb

class Fuego:
    def __init__(self, p):
        self.p = np.array(p) # posicion
        self.trayectoria = self.calcularTrayectoria([100,0])
        self.scale = [1.0,1.0,1.0]
        self.r = 30

    def calcularTrayectoria(self, objetivo):
        N = 50

        R0 = np.array([[self.p[0], self.p[1], 0]]).T
        R1 = np.array([[self.p[0] - 100, self.p[1], 0]]).T
        R2 = np.array([[500, 200, 0]]).T
        R3 = np.array([[objetivo[0], 100, 0]]).T

        GMb = bezierMatrix(R0, R1, R2, R3)
        bezierCurve = evalCurve(GMb, N)

        return bezierCurve

    def mover(self, instante, maxInstante, objetivo):
        # modifica la posicion de acuerdo a la curva que debe seguir
        self.calcularTrayectoria(objetivo)

        #Tenemos dos animaciones: En la primera mitad del tiempo queremos deplazarnos
        #En la segundo mitad queremos expandir y contraer el tamaño del objeto

        if instante < maxInstante/2:
            self.p = np.array([self.trayectoria[instante][0], self.trayectoria[instante][1]])
            self.scale = [1.0, 1.0, 1.0]

        if 3*maxInstante/4 >= instante >= maxInstante/2:
            self.scale[0] = self.scale[0] * (1 + instante / 2000)
            self.scale[1] = self.scale[1] * (1 + instante / 2000)

        if maxInstante >= instante >= 3 * maxInstante / 4:
            self.scale[0] = self.scale[0] * (1 - instante / 2000)
            self.scale[1] = self.scale[1] * (1 - instante / 2000)

    def dibujar(self):
        glPushMatrix()

        glTranslatef(self.p[0], self.p[1], 0.0)
        glScalef(self.scale[0], self.scale[1], 1.0)
        glColor3f(1,0,0)

        glBegin(GL_TRIANGLE_FAN)

        glVertex2f(0,0)
        radio = 30
        ang = 2 * np.pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex2f( np.cos(ang_i) * radio,  np.sin(ang_i) * radio)

        glEnd()

        # Parte amarilla
        glColor3f(0.8, 0.8, 0)
        glBegin(GL_TRIANGLE_FAN)

        glVertex2f(0, 0)
        radio = 22
        ang = 2 * np.pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex2f(np.cos(ang_i) * radio, np.sin(ang_i) * radio)

        glEnd()
        glPopMatrix()
