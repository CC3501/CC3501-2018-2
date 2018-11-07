import numpy as np

def rgb(r,g,b):
    return [r/255.0, g/255.0, b/255.0]


def estanChocando(o1, o2):
    return distancia(o1.p, o2.p) < o2.r

def estanChocandoX(o1,o2):
    return o1.p[0] - o2.p[0] < 0

def distancia(v1,v2):
    return np.sqrt((v2[0]-v1[0])**2 + (v2[1]-v1[1])**2)