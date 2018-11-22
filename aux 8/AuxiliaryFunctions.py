# -*- coding: utf-8 -*-
"""
Daniel Calderon S.

file: AuxiliaryFunctions.py
---------------------------
V1.0 - 08/05/2012
Funciones varias para simplificar el proceso de dibujo
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#####################################################################

def printVersions():
    print("GPU                      = ",glGetString(GL_VENDOR)) 
    print("Renderer                 = ",glGetString(GL_RENDERER)) 
    print("OpenGL                   = ",glGetString(GL_VERSION)) 
    print("Shading Language Version = ",glGetString(GL_SHADING_LANGUAGE_VERSION))

#####################################################################

def draw2Vertexfv(a,b):
    n = len(a)
    if n == 2:
        glVertex2fv(a)
        glVertex2fv(b)
    elif n == 3:
        glVertex3fv(a)
        glVertex3fv(b)
    elif n == 4:
        glVertex4fv(a)
        glVertex4fv(b)
        
def draw2Vertexfvn(a,b,n):
    glNormal3fv(n)    
    draw2Vertexfv(a,b)

def draw2Vertexfvn2(a,b,na,nb):
    n = len(a)
    if n == 2:
        glNormal3fv(na)
        glVertex2fv(a)
        glNormal3fv(nb) 
        glVertex2fv(b)
    elif n == 3:
        glNormal3fv(na)
        glVertex3fv(a)
        glNormal3fv(nb) 
        glVertex3fv(b)
    elif n == 4:
        glNormal3fv(na)
        glVertex4fv(a)
        glNormal3fv(nb) 
        glVertex4fv(b)
        
#####################################################################
    
def draw3Vertexfv(a,b,c):
    n = len(a)
    if n == 2:
        glVertex2fv(a)
        glVertex2fv(b)
        glVertex2fv(c)
    elif n == 3:
        glVertex3fv(a)
        glVertex3fv(b)
        glVertex3fv(c)
    elif n == 4:
        glVertex4fv(a)
        glVertex4fv(b)
        glVertex4fv(c)

def draw3Vertexfvn(a,b,c,n):
    glNormal3fv(n)    
    draw3Vertexfv(a,b,c)

def draw3Vertexfvn3(a,b,c,na,nb,nc):
    n = len(a)
    if n == 2:
        glNormal3fv(na)
        glVertex2fv(a)
        glNormal3fv(nb) 
        glVertex2fv(b)
        glNormal3fv(nc) 
        glVertex2fv(c)
    elif n == 3:
        glNormal3fv(na)
        glVertex3fv(a)
        glNormal3fv(nb) 
        glVertex3fv(b)
        glNormal3fv(nc) 
        glVertex3fv(c)
    elif n == 4:
        glNormal3fv(na)
        glVertex4fv(a)
        glNormal3fv(nb) 
        glVertex4fv(b)
        glNormal3fv(nc) 
        glVertex4fv(c)        

#####################################################################

def tdraw3Vertexfv(a,b,c,ta,tb,tc):
    n = len(a)
    if n == 2:
        glTexCoord2fv(ta)
        glVertex2fv(a)
        glTexCoord2fv(tb)
        glVertex2fv(b)
        glTexCoord2fv(tc)
        glVertex2fv(c)
    elif n == 3:
        glTexCoord2fv(ta)
        glVertex3fv(a)
        glTexCoord2fv(tb)
        glVertex3fv(b)
        glTexCoord2fv(tc)
        glVertex3fv(c)
    elif n == 4:
        glTexCoord2fv(ta)
        glVertex4fv(a)
        glTexCoord2fv(tb)
        glVertex4fv(b)
        glTexCoord2fv(tc)
        glVertex4fv(c)

def tdraw3Vertexfvn(a,b,c,n,ta,tb,tc):
    glNormal3fv(n)
    tdraw3Vertexfv(a,b,c,ta,tb,tc)

def tdraw3Vertexfvn4(a,b,c,na,nb,nc,ta,tb,tc):
    n = len(a)
    if n == 2:
        glTexCoord2fv(ta)
        glNormal3fv(na)
        glVertex2fv(a)
        
        glTexCoord2fv(tb)
        glNormal3fv(nb) 
        glVertex2fv(b)
        
        glTexCoord2fv(tc)
        glNormal3fv(nc) 
        glVertex2fv(c)
    elif n == 3:
        glTexCoord2fv(ta)
        glNormal3fv(na)
        glVertex3fv(a)
        
        glTexCoord2fv(tb)
        glNormal3fv(nb) 
        glVertex3fv(b)
        
        glTexCoord2fv(tc)
        glNormal3fv(nc) 
        glVertex3fv(c)
    elif n == 4:
        glTexCoord2fv(ta)
        glNormal3fv(na)
        glVertex4fv(a)
        
        glTexCoord2fv(tb)
        glNormal3fv(nb) 
        glVertex4fv(b)
        
        glTexCoord2fv(tc)
        glNormal3fv(nc) 
        glVertex4fv(c)

#####################################################################

def draw4Vertexfv(a,b,c,d):
    n = len(a)
    if n == 2:
        glVertex2fv(a)
        glVertex2fv(b)
        glVertex2fv(c)
        glVertex2fv(d)
    elif n == 3:
        glVertex3fv(a)
        glVertex3fv(b)
        glVertex3fv(c)
        glVertex3fv(d)
    elif n == 4:
        glVertex4fv(a)
        glVertex4fv(b)
        glVertex4fv(c)
        glVertex4fv(d)

def draw4Vertexfvn(a,b,c,d,n):
    glNormal3fv(n)    
    draw4Vertexfv(a,b,c,d)

def draw4Vertexfvn4(a,b,c,d,na,nb,nc,nd):
    n = len(a)
    if n == 2:
        glNormal3fv(na)
        glVertex2fv(a)
        glNormal3fv(nb) 
        glVertex2fv(b)
        glNormal3fv(nc) 
        glVertex2fv(c)
        glNormal3fv(nd) 
        glVertex2fv(d)
    elif n == 3:
        glNormal3fv(na)
        glVertex3fv(a)
        glNormal3fv(nb) 
        glVertex3fv(b)
        glNormal3fv(nc) 
        glVertex3fv(c)
        glNormal3fv(nd) 
        glVertex3fv(d)
    elif n == 4:
        glNormal3fv(na)
        glVertex4fv(a)
        glNormal3fv(nb) 
        glVertex4fv(b)
        glNormal3fv(nc) 
        glVertex4fv(c)
        glNormal3fv(nd) 
        glVertex4fv(d)

#####################################################################

def tdraw4Vertexfv(a,b,c,d,ta,tb,tc,td):
    n = len(a)
    if n == 2:
        glTexCoord2fv(ta)
        glVertex2fv(a)
        glTexCoord2fv(tb)
        glVertex2fv(b)
        glTexCoord2fv(tc)
        glVertex2fv(c)
        glTexCoord2fv(td)
        glVertex2fv(d)
    elif n == 3:
        glTexCoord2fv(ta)
        glVertex3fv(a)
        glTexCoord2fv(tb)
        glVertex3fv(b)
        glTexCoord2fv(tc)
        glVertex3fv(c)
        glTexCoord2fv(td)
        glVertex3fv(d)
    elif n == 4:
        glTexCoord2fv(ta)
        glVertex4fv(a)
        glTexCoord2fv(tb)
        glVertex4fv(b)
        glTexCoord2fv(tc)
        glVertex4fv(c)
        glTexCoord2fv(td)
        glVertex4fv(d)

def tdraw4Vertexfvn(a,b,c,d,n,ta,tb,tc,td):
    glNormal3fv(n)
    tdraw4Vertexfv(a,b,c,d,ta,tb,tc,td)

def tdraw4Vertexfvn4(a,b,c,d,na,nb,nc,nd,ta,tb,tc,td):
    n = len(a)
    if n == 2:
        glTexCoord2fv(ta)
        glNormal3fv(na)
        glVertex2fv(a)
        
        glTexCoord2fv(tb)
        glNormal3fv(nb) 
        glVertex2fv(b)
        
        glTexCoord2fv(tc)
        glNormal3fv(nc) 
        glVertex2fv(c)
        
        glTexCoord2fv(td)
        glNormal3fv(nd) 
        glVertex2fv(d)
    elif n == 3:
        glTexCoord2fv(ta)
        glNormal3fv(na)
        glVertex3fv(a)
        
        glTexCoord2fv(tb)
        glNormal3fv(nb) 
        glVertex3fv(b)
        
        glTexCoord2fv(tc)
        glNormal3fv(nc) 
        glVertex3fv(c)
        
        glTexCoord2fv(td)
        glNormal3fv(nd) 
        glVertex3fv(d)
    elif n == 4:
        glTexCoord2fv(ta)
        glNormal3fv(na)
        glVertex4fv(a)
        
        glTexCoord2fv(tb)
        glNormal3fv(nb) 
        glVertex4fv(b)
        
        glTexCoord2fv(tc)
        glNormal3fv(nc) 
        glVertex4fv(c)
        
        glTexCoord2fv(td)
        glNormal3fv(nd) 
        glVertex4fv(d)
        
#####################################################################

def axesList(h):
    # h : lenght of the axes
    # draw axis X in red
    # draw axis Y in green
    # draw axis Z in blue
    
    x = [h,0,0,1]
    y = [0,h,0,1]
    z = [0,0,h,1]
    o = [0,0,0,1]
    
    lista = glGenLists(1)
    glNewList(lista, GL_COMPILE)
    
    glBegin(GL_LINES)
    
    glColor4fv([1,0,0,1])
    draw2Vertexfv(o,x)
    
    glColor4fv([0,1,0,1])
    draw2Vertexfv(o,y)
    
    glColor4fv([0,0,1,1])
    draw2Vertexfv(o,z)
    
    glEnd()
    
    glEndList()
    
    return lista
    
#####################################################################

def drawList(lista,pos = [0.0,0.0,0.0],o = 0.0,rot = None,sz = None,rgb = None):
    glPushMatrix()
    
    glTranslatef(pos[0],pos[1],pos[2])
    
    if (sz != None):
        glScalef(sz[0],sz[1],sz[2])
        
    if (rot != None):
        glRotatef(o,rot[0],rot[1],rot[2])
    
    if (rgb != None):
        glColor4fv(rgb)
    
    glCallList(lista)
    
    glPopMatrix()
    
#####################################################################

def plusList(a,b):
    d = len(a)
    
    c = []
    for i in range(0,d):
        c.append(a[i]+b[i])
    
    return c

def scaleList(s,a):
    d = len(a)
    
    c = []
    for i in range(0,d):
        c.append(a[i]*s)
    
    return c

def meanList(lists):
    n = len(lists)
    d = len(lists[0])
    
    c = []
    for i in range(0,d):
        c.append(0.0)
    
    for l in lists:
        c = plusList(c,l)
        
    return scaleList( 1/float(n) , c)

#####################################################################  
        
def generarTex(filename,repeat = False, alpha = False):
    
    import Image
    import numpy
    
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8) #Se supone que hace mas rapido la lectura y escritura...

    texture = glGenTextures(1)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glBindTexture(GL_TEXTURE_2D, texture)
    
    if (repeat):
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    else:
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    
    if alpha: #Si posee transparencias
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    else:    #No posee transparencias
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
	
    return texture
    
#####################################################################        