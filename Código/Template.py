#flake8:noqa
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import camera
import vector_utils

import sys
import math , random

window_w, window_h = 800, 600
window_wG, window_hG = 640, 480
pontos = []
aux = []
vetores = []
triangles = []
index = 0
point_size = 13.0
rot = 0



ESC = '\x1b'
MODIFIED = -1
IDLE = -2
FPS = 30

def get_vertices():
    global triangles
    data = open("input/calice.txt","r")
    first_line = data.readline()

    num_face = first_line.split(" ")[0]
    num_vert = first_line.split(" ")[1]
    lines = data.readlines()

    for x in range(1,int(num_face)):
        vetor = {'x':0.0,'y':0.0,'z':0.0}
        vetor['x'] = lines[x].replace('\n','').replace('\r','').split(' ')[0]
        vetor['y'] = lines[x].replace('\n','').replace('\r','').split(' ')[1]
        vetor['z'] = lines[x].replace('\n','').replace('\r','').split(' ')[2]
        triangles.append(vetor)

def display():
    global poligonos
    global matrix_camera
    global window_w, window_h
    global rot
    global mult

    glClear(GL_DEPTH_BUFFER_BIT)

    rot = rot + 0.1
    rot = rot%360
    fovy = 45
    aspect = window_w/window_h
    f = 1/math.tan(fovy/2)
    near = 2.5
    far = 1000

    matrix_camera = [f/aspect,0.0,0.0,0.0,
                     0.0,f,0.0,0.0,
                     0.0,0.0,(far+near)/(near-far),(2*far*near)/(near-far),
                     0.0,0.0,-1,0.0]

    glMatrixMode(GL_PROJECTION)
    glLoadMatrixf(matrix_camera)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0)
    #print(len(mult))
    for p in range(0, len(mult)):
        glVertex3f(float(mult[p]['v1']['x']), float(mult[p]['v1']['y']), float(mult[p]['v1']['z']))
        glVertex3f(float(mult[p]['v2']['x']), float(mult[p]['v2']['y']), float(mult[p]['v2']['z']))
        glVertex3f(float(mult[p]['v3']['x']), float(mult[p]['v3']['y']), float(mult[p]['v3']['z']))
    glEnd()

    #glBegin(GL_POLYGON)
    #glColor3f(1, 0, 0)
    #glVertex3f(float(mult[0]['v1']['x']), float(mult[0]['v1']['y']), float(mult[0]['v1']['z']))
    #glVertex3f(float(mult[1]['v2']['x']), float(mult[1]['v2']['y']), float(mult[1]['v2']['z']))
    #glVertex3f(float(mult[2]['v3']['x']), float(mult[2]['v3']['y']), float(mult[2]['v3']['z']))
    #glEnd()

    #glBegin(GL_POLYGON)
    #glColor3f(0, 1, 0);
    #glVertex3f( 1.0, -1.0, -2.0)
    #glVertex3f( 1.0, -1.0, -4.0)
    #glVertex3f( 0.5,  1.0, -3.0)
    #glEnd()


    #glBegin(GL_POLYGON);
    #glColor3f(0, 0, 1);
    #glVertex3f(-1.0, -1.0, -2.0)
    #glVertex3f(-1.0, -1.0, -4.0)
    #glVertex3f( 0.5,  1.0, -3.0)
    #glEnd()

    #glBegin(GL_POLYGON);
    #glColor3f(1, 0, 1);
    #glVertex3f(-1.0, -1.0, -4.0)
    #glVertex3f( 1.0, -1.0, -4.0)
    #glVertex3f( 0.5,  1.0, -3.0)
    #glEnd()


    glutSwapBuffers();
    #glutPostRedisplay();

def hadleKeyboard(*args):
    global castel

    if args[0] == ESC:
        sys.exit()
    elif args[0] == 'c':
        castel = True
        glutPostRedisplay()


vertices = camera.get_vertices()
triangulos = camera.get_triangulos()
poligonos = camera.get_vertice_triangulo(triangulos, vertices)
retorno = camera.get_input()
UVN = camera.set_view()
poligonosMenosC = camera.dif_polygon_C(poligonos, retorno['C_in'])
mult = camera.mult_UVN_tripla(poligonosMenosC, UVN)
#mult = vector_utils.normalizacao_vetor(mult)

for w in range (0, len(mult)):
    mult[w]['v1'] = vector_utils.normalizacao_vetor(mult[w]['v1'])
    mult[w]['v2'] = vector_utils.normalizacao_vetor(mult[w]['v2'])
    mult[w]['v3'] = vector_utils.normalizacao_vetor(mult[w]['v3'])


glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowPosition(112, 84)
glutInitWindowSize(window_w,window_h)

glutInitWindowPosition(112, 84)
glutCreateWindow(b"PG - Project 2")
glutDisplayFunc(display)
glutKeyboardFunc(hadleKeyboard)

glClearDepth(1.0)
glClearColor(0.0, 0.0, 0.0, 0.0)

glutMainLoop()
