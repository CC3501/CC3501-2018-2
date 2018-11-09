# coding=utf-8
"""
Visor de una figura, utiliza tanto cámara ortográfica como en perspectiva.
Modelos:
- cubo
- otros
"""

"""
-------------------------------------------------------------------------------
Importación de librerías
-------------------------------------------------------------------------------
"""
from PyOpenGLtoolbox import *  # Se usará esta librería sólo para manejar la ventana de OpenGL, v2.1.0

"""
-------------------------------------------------------------------------------
Definición de funciones
-------------------------------------------------------------------------------
"""


def reshape_window_perspective(w, h, near, far, fov):
    """
    Crea la ventana con una proyección en perspectiva.
    """
    h = max(h, 1)
    glLoadIdentity()

    # Crea el viewport
    glViewport(0, 0, int(w), int(h))
    glMatrixMode(GL_PROJECTION)

    # Proyección en perspectiva
    gluPerspective(fov, float(w) / float(h), near, far)

    # Setea el modo de la cámara
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def reshape_window_ortho(w, h, left, right, bottom, top, near, far):
    """
    Crea la ventana con una proyección ortográfica.
    """
    h = max(h, 1)
    glLoadIdentity()

    # Crea el viewport
    glViewport(0, 0, int(w), int(h))
    glMatrixMode(GL_PROJECTION)

    # Proyección ortográfica
    glOrtho(left, right, bottom, top, near, far)

    # Setea el modo de la cámara
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


"""
-------------------------------------------------------------------------------
Definición de algunas constantes
-------------------------------------------------------------------------------
"""
FOV = 60
FPS = 60
VENTANA_H = 600
VENTANA_W = 800

"""
-------------------------------------------------------------------------------
Inicio de OpenGL
-------------------------------------------------------------------------------
"""
init_pygame(VENTANA_W, VENTANA_H, 'TPOSE', centered_window=True)
init_gl(transparency=False, materialcolor=False, normalized=True, perspectivecorr=True, antialiasing=True,
        depth=True, smooth=True, verbose=True, version=True)
# reshape_window_perspective(w=VENTANA_W, h=VENTANA_H, near=0.01, far=1000, fov=60)
reshape_window_ortho(w=VENTANA_W, h=VENTANA_H, left=-15, right=15, bottom=-15, top=15, near=1, far=50)
clock = pygame.time.Clock()

"""
-------------------------------------------------------------------------------
Creación de modelos
-------------------------------------------------------------------------------
"""
axis = create_axes(10)  # Retorna una lista con los ejes, parte de la librería

# Generamos un cubo (2x2x2)
cubo = create_cube()
gorro = create_pyramid()

# Creamos a la persona
tpose = glGenLists(1)  # Inicia una lista
glNewList(tpose, GL_COMPILE)

# Gorro
glPushMatrix()
glTranslate(0, 0, 11)
glRotate(180, 1, 0, 1)
glScale(1, 1, 1)
glColor4fv([1, 0, 1, 1])
glCallList(gorro)
glPopMatrix()

# La cabeza
glPushMatrix()
glTranslate(0, 0, 10)
glColor4fv([1, 1, 0, 1])
glCallList(cubo)
glPopMatrix()

# El cuello
glPushMatrix()
glTranslate(0, 0, 9)
glScale(0.25, 0.25, 0.5)
glCallList(cubo)
glPopMatrix()

# El torso
glPushMatrix()
glTranslate(0, 0, 6)
glScale(2, 1, 2.5)
glColor4fv([1, 0, 0, 1])
glCallList(cubo)
glPopMatrix()

# Los brazos
glPushMatrix()
glTranslate(4, 0, 7.5)
glScale(2, 0.5, 0.5)
glColor4fv([1, 1, 0, 1])
glCallList(cubo)
glPopMatrix()
glPushMatrix()
glTranslate(-4, 0, 7.5)
glScale(2, 0.5, 0.5)
glColor4fv([1, 1, 0, 1])
glCallList(cubo)
glPopMatrix()

# Las piernas
glPushMatrix()
glTranslate(1, 0, 1.5)
glScale(0.5, 0.5, 2)
glColor4fv([0, 0, 1, 1])
glCallList(cubo)
glPopMatrix()
glPushMatrix()
glTranslate(-1, 0, 1.5)
glScale(0.5, 0.5, 2)
glColor4fv([0, 0, 1, 1])
glCallList(cubo)
glPopMatrix()

glEndList()  # Cierra la lista

"""
-------------------------------------------------------------------------------
Creación de la cámara
-------------------------------------------------------------------------------
"""
CAMARA_POS = [0, 0, 20]  # Donde estoy (x,y,z)
CAMARA_CENTRO = [0, 0, 0]  # Dónde apunto (x,y,z)
CAMARA_NORMAL = [1, 0, 0]  # La camara está parada normal al eje z

"""
-------------------------------------------------------------------------------
Inicio de OpenGL
-------------------------------------------------------------------------------
"""
ang = 0  # Variable del ángulo de rotación

while True:

    # Tick del reloj
    clock.tick(FPS)

    # Elimina el buffer
    clear_buffer()

    # Ubica la cámara
    glLoadIdentity()
    gluLookAt(CAMARA_POS[0], CAMARA_POS[1], CAMARA_POS[2],
              CAMARA_CENTRO[0], CAMARA_CENTRO[1], CAMARA_CENTRO[2],
              CAMARA_NORMAL[0], CAMARA_NORMAL[1], CAMARA_NORMAL[2])

    # Dibuja los ejes, si sólo lo llamo así no se aplican transformadas
    glCallList(axis)

    # Dibujamos la figura, si queremos transformadas hay que crear una nueva matriz
    glPushMatrix()
    glRotatef(ang, 0, 0, 1)  # Rota en (x,y,z) un determinado ángulo
    glScale(0.25, 0.25, 0.25)
    glCallList(tpose)
    glPopMatrix()

    glPushMatrix()
    glTranslate(10, 0, 10)
    glScale(0.1, 0.25, 1)
    glCallList(tpose)
    glPopMatrix()

    # Chequea eventos
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):  # Cierra la app
            exit()

    # Vuelca el contenido
    pygame.display.flip()

    # Aumentamos el ángulo de rotación
    ang = (ang + 30.0/FPS) % 360
