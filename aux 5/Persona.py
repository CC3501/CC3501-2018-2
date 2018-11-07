from PautaAux.CC3501Utils import *



class Persona():
    def __init__(self, pos=(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.pos=pos
        self.color = rgb
        self.lista = 0
        self.crear()

    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)

        self.figura()

        glEndList()

    def dibujar(self):
        glPushMatrix()
        glColor3fv(self.color)
        glTranslatef(self.pos[0], self.pos[1], 0.0)
        glCallList(self.lista)

        glPopMatrix()
    def figura(self):

        glScale(0.5, 0.5,1 )
        glTranslate(100,300,1)

        glRotate(900, 0,0,1)

        glBegin(GL_QUADS)
        glColor3f(53 / 255, 51 / 255, 255 / 255)
        # Torso
        glVertex2f(0, 100)
        glVertex2f(50, 100)
        glVertex2f(50, 0)
        glVertex2f(0, 0)

        # Hombros
        glVertex2f(50, 100)
        glVertex2f(70, 100)
        glVertex2f(70, 70)
        glVertex2f(50, 70)

        glVertex2f(-20, 100)
        glVertex2f(0, 100)
        glVertex2f(0, 70)
        glVertex2f(-20, 70)

        # Brazos
        glColor3f(252 / 255, 193 / 255, 156 / 255)

        glVertex2f(50, 70)
        glVertex2f(65, 70)
        glVertex2f(65, 10)
        glVertex2f(50, 10)

        glVertex2f(-15, 70)
        glVertex2f(0, 70)
        glVertex2f(0, 10)
        glVertex2f(-15, 10)
        glEnd()

        # Falda
        glBegin(GL_TRIANGLES)
        glColor3f(53 / 255, 51 / 255, 255 / 255)
        glVertex(25, 80)
        glVertex(150, -100)
        glVertex(-100, -100)

        glColor3f(1, 1, 1)
        glVertex(25, 40)
        glVertex(50, -100)
        glVertex(0, -100)
        glEnd()
        # pelo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(114 / 255, 61 / 255, 27 / 255)
        glVertex2f(25, 135)
        radio = 30
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(25 + cos(ang_i) * radio, 135 + sin(ang_i) * radio)

        glEnd()
        # cabeza
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(252 / 255, 193 / 255, 156 / 255)
        glVertex2f(25, 125)
        radio = 30
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(25 + cos(ang_i) * radio, 125 + sin(ang_i) * radio)

        glEnd()
        # Trencitas

        glBegin(GL_QUADS)
        glColor3f(114 / 255, 61 / 255, 27 / 255)
        # moño derecho
        glVertex2f(-4, 140)
        glVertex2f(-10, 90)
        glVertex2f(0, 90)
        glVertex2f(0, 140)
        # moño izquierdo
        glVertex2f(52, 140)
        glVertex2f(46, 90)
        glVertex2f(56, 90)
        glVertex2f(56, 140)
        glEnd()





