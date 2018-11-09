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
init_pygame(VENTANA_W, VENTANA_H, 'Visualizador figuritas', centered_window=True)
init_gl(transparency=False, materialcolor=False, normalized=True, perspectivecorr=True, antialiasing=True,
        depth=True, smooth=True, verbose=True, version=True)
reshape_window_perspective(w=VENTANA_W, h=VENTANA_H, near=1, far=1000, fov=FOV)
clock = pygame.time.Clock()

"""
-------------------------------------------------------------------------------
Creación de modelos
-------------------------------------------------------------------------------
"""
axis = create_axes(10)  # Retorna una lista con los ejes, parte de la librería

# Creamos una figura en 3D
figurita = glGenLists(1)  # Inicia una lista
glNewList(figurita, GL_COMPILE)
glBegin(GL_POLYGON)  # Inicia una figura
glColor3f(1, 0, 0)
glVertex3f(-0.6, -0.75, 0.5)
glColor3f(0, 1, 0)
glVertex3f(0.6, -0.75, 0)
glColor3f(0, 0, 1)
glVertex3f(0, 0.75, 0)
glEnd()  # Termina la figura
glEndList()  # Cierra la lista

"""
-------------------------------------------------------------------------------
Creación de la cámara
-------------------------------------------------------------------------------
"""
CAMARA_POS = [10, 10, 10]  # Donde estoy (x,y,z)
CAMARA_CENTRO = [0, 0, 0]  # Dónde apunto (x,y,z)
CAMARA_NORMAL = [0, 0, 1]  # La camara está parada normal al eje z

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
    glRotatef(ang, 1, 1, 0)  # Rota en (x,y,z) un determinado ángulo
    glCallList(figurita)
    glPopMatrix()

    # Chequea eventos
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):  # Cierra la app
            exit()

    # Vuelca el contenido
    pygame.display.flip()

    # Aumentamos el ángulo de rotación
    ang = (ang + 1) % 360
