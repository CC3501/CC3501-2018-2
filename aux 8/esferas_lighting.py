# -*- coding: utf-8 -*-
"""
Benjamin Mellado

file: esferas_lighting.py
----------------------------
Dibuja esferas rotando con distintos efectos de iluminación.

Control del programa:
1: Visualiza o no los ejes de coordenadas
2: Pinta o no los polígonos
ESC: terminar
"""

import pygame
from pygame.locals import *
from math import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from AuxiliaryFunctions import *


#####################################################################

def init_pygame(w, h, title=""):
    pygame.init()
    pygame.display.set_mode((w, h), OPENGL | DOUBLEBUF)
    pygame.display.set_caption(title)


def init_opengl(w, h):
    reshape(w, h)
    init()


def init():
    # setea el color de fondo
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # se habilitan las transparencias
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    # el color debe incluir la cuarta componente, alpha
    # alpha=1  --> objeto totalmente opaco
    # alpha=0  --> opbjeto totalmente transparente

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    # glDepthFunc(GL_LESS)

    #    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    # normaliza las normales luego del escalamiento.
    glEnable(GL_NORMALIZE)


def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(width) / float(height), 0.1, 20000.0)
    # glOrtho(-2*width,2*width,-2*height,2*height,1,20000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


#####################################################################

def initLight():
    glLightfv(GL_LIGHT0, GL_POSITION, [3000.0, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0)

    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 180.0)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [-1.0, 0.0, 0.0])
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT, 0.0)

    glEnable(GL_LIGHT0)


#####################################################################
def vectorEsfericas(r, phi, theta):
    return [r * sin(theta) * cos(phi), r * sin(theta) * sin(phi) , r * cos(theta)]


def listaEsferaFlat(radio):
    dphi = 2 * pi / 20.0
    dtheta = 2 * pi / 20.0
    theta = 0
    phi = 0

    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    glBegin(GL_QUADS)
    while( theta <= pi - dtheta):
        while(phi <= 2 * pi - dphi):
            p1 = vectorEsfericas(radio, phi, theta)
            p2 = vectorEsfericas(radio, phi + dphi, theta)
            p3 = vectorEsfericas(radio, phi + dphi, theta + dtheta)
            p4 = vectorEsfericas(radio, phi, theta + dtheta)

            #la normal corresponde a r tongo
            n = [sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)]

            draw4Vertexfvn(p1, p2, p3, p4, n)
            phi += dphi
        phi = 0
        theta += dtheta
    glEnd()
    glEndList()
    return lista

def listaEsferaSmooth(radio):
    dphi = 2 * pi / 20.0
    dtheta = 2 * pi / 20.0
    theta = 0
    phi = 0

    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    glBegin(GL_QUADS)
    while( theta <= pi - dtheta):
        while(phi <= 2 * pi - dphi):
            p1 = vectorEsfericas(radio, phi, theta)
            p2 = vectorEsfericas(radio, phi + dphi, theta)
            p3 = vectorEsfericas(radio, phi + dphi, theta + dtheta)
            p4 = vectorEsfericas(radio, phi, theta + dtheta)

            #la normal corresponde a r tongo
            n1 = [sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)]
            n2 = [sin(theta) * cos(phi + dphi), sin(theta) * sin(phi + dphi), cos(theta)]
            n3 = [sin(theta + dtheta) * cos(phi + dphi), sin(theta + dtheta) * sin(phi + dphi), cos(theta + dtheta)]
            n4 = [sin(theta + dtheta) * cos(phi), sin(theta + dtheta) * sin(phi), cos(theta + dtheta)]
            draw4Vertexfvn4(p1, p2, p3, p4, n1, n2, n3, n4)
            phi += dphi
        phi = 0
        theta += dtheta
    glEnd()
    glEndList()
    return lista





#####################################################################

W = 640  # ancho de ventana
H = 480  # alto de ventana

# inicializando ...
init_pygame(W, H, "esferas_lighting")
init_opengl(W, H)

# imprime información sobre el Hardware gráfico y
# la version de OpenGL implementada
printVersions()

# creación de dibujos en listas
esfera = listaEsferaFlat(1)
esferaSmooth = listaEsferaSmooth(1)


axes = axesList(100000)

# variables del programa
o = 30
w = 0.1

show_axes = True
fill_polygons = True

# configuración de camara
glLoadIdentity()
gluLookAt(2000.0, 1000.0, 2000.0, \
          0.0, 0.0, 0.0, \
          0.0, 0.0, 1.0)

# habilita iluminación
glEnable(GL_LIGHTING)

# configura fuentes de luz
initLight()

# medida de tiempo inicial
t0 = pygame.time.get_ticks()
d = 1000
run = True
while run:
    # 0: CONTROL DEL TIEMPO
    t1 = pygame.time.get_ticks()  # tiempo actual
    dt = (t1 - t0)  # diferencial de tiempo asociado a la iteración
    t0 = t1  # actualizar tiempo inicial para siguiente iteración

    # 1: MANEJAMOS EVENTOS DE ENTRADA (TECLADO, MOUSE, ETC.)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_1:
                show_axes = not show_axes
            if event.key == K_2:
                fill_polygons = not fill_polygons
            if event.key == K_LEFT:
                d-= 100
            if event.key == K_RIGHT:
                d+= 100


    # 2: EJECUTAMOS LOGICA DE LA APLICACION
    o += w * dt

    # 3: DIBUJAMOS LOS ELEMENTOS
    # limpia la pantalla (buffer de color y de profundidad)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # posibilidad de pintar o no los polígonos
    if fill_polygons:
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT, GL_LINE)
        glPolygonMode(GL_BACK, GL_LINE)

    # posibilidad de mostrar o no los ejes
    if show_axes:
        glDisable(GL_LIGHTING)
        glCallList(axes)
        glEnable(GL_LIGHTING)


    #PARAMETROS DE LUZ PARA EL MATERIAL SILVER
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0.19225, 0.19225, 0.19225, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.50754, 0.50754, 0.50754, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.508273, 0.508273, 0.508273, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [0.4])
    glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0, 1.0])

    glShadeModel(GL_FLAT)
    drawList(esfera, pos=[0, -1000, 0], o=o, rot=[0, 0, 1], sz=[600, 600, 600])

    glShadeModel(GL_SMOOTH)
    drawList(esferaSmooth, pos=[0, 1000, 0], o=o, rot=[0, 0, 1], sz=[600, 600, 600])

    pygame.display.flip()  # vuelca el dibujo a la pantalla
    pygame.time.wait(int(1000 / 30))  # ajusta para trabajar a 30 fps.

#####################################################################
