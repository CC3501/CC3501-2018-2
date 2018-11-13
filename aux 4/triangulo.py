# coding=utf-8
"""
Triangulo
"""

# Carga las librerías
from PyOpenGLtoolbox import *

# Constantes
AXES_LENGTH = 3
CAMERA_PHI = 45
CAMERA_RAD = 5
CAMERA_ROT_VEL = 2.5
CAMERA_THETA = 56
FPS = 60
WINDOW_SIZE = [800, 600]

# Inicia la ventana
init_pygame(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Triangulo', centered_window=True)
init_gl(transparency=False, materialcolor=False, normalized=True, perspectivecorr=True, antialiasing=True,
        depth=True, smooth=True, verbose=True, version=True)
reshape_window_perspective(w=WINDOW_SIZE[0], h=WINDOW_SIZE[1], near=1, far=1000)
clock = pygame.time.Clock()

# Crea objetos
axis = create_axes(AXES_LENGTH)
camera = CameraR(CAMERA_RAD, CAMERA_PHI, CAMERA_THETA)
camera.set_r_vel(0.1)  # Velocidad radial

# Crea el triangulo
triangulo = glGenLists(1)  # Inicia una lista
glNewList(triangulo, GL_COMPILE)
glBegin(GL_POLYGON)  # Inicia una figura
glColor3f(1, 0, 0)
glVertex3f(-0.6, -0.75, 0.5)
glColor3f(0, 1, 0)
glVertex3f(0.6, -0.75, 0)
glColor3f(0, 0, 1)
glVertex3f(0, 0.75, 0)
glEnd()  # Termina la figura
glEndList()  # Cierra la lista

# Muestra ayuda
print('Rota eje X con W/S')
print('Rota eje Y con A/D')
print('Rota eje Z con Q/E')
print('Zoom +/- con N/M')

# Main loop
while True:
    clock.tick(FPS)
    clear_buffer()
    camera.place()

    glCallList(axis)
    glCallList(triangulo)

    # Chequea eventos
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):  # Cierra la app
            exit()

    # Obtiene teclas presionadas
    keys = pygame.key.get_pressed()

    # Rota camara ángulo theta
    if keys[K_w]:
        camera.rotate_theta(CAMERA_ROT_VEL)
    elif keys[K_s]:
        camera.rotate_theta(-CAMERA_ROT_VEL)

    # Rota camara ángulo phi
    if keys[K_a]:
        camera.rotate_phi(-CAMERA_ROT_VEL)
    elif keys[K_d]:
        camera.rotate_phi(CAMERA_ROT_VEL)

    # Acerca / aleja la camara
    if keys[K_n]:
        camera.close()
    elif keys[K_m]:
        camera.far()

    # Vuelca el contenido
    pygame.display.flip()
