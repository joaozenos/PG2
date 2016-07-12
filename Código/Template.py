#flake8:noqa
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import camera
import vector_utils

import sys
import scene
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

def display():
    global matrix_camera
    global window_w, window_h
    global rot

    glClearColor(1.0, 0.0, 0.0, 1.0)
    glClear(GL_DEPTH_BUFFER_BIT)

    # Camera *camera = scene->get_camera();   
    # glDrawPixels(camera->get_resx(), camera->get_resy(), GL_RGB, GL_FLOAT, scene->get_buffer());
    
    glFlush();

def initialize():
    # scene = new Scene();
    # SDLReader::read_sdl("exemplo.sdl", *scene);
    
    m_viewport = [0,0,800,600]
    teste = glGetIntegerv(GL_VIEWPORT, m_viewport)
    print type(teste)
    scene.get_camera().Set_screen_res(m_viewport[2], m_viewport[3])
    scene.set_buffer(m_viewport[2], m_viewport[3])
    scene.set_la(Color(100, 100, 100))
    scene.draw()

def hadleKeyboard(*args):
    global castel

    if args[0] == ESC:
        sys.exit()
    elif args[0] == 'c':
        castel = True
        glutPostRedisplay()

glutInit()
glutInitWindowSize(800, 600)
glutInitWindowPosition(50, 50)
window = glutCreateWindow("OpenGL Setup Test")
glutDisplayFunc(display)
glutKeyboardFunc(hadleKeyboard)
initialize()
glutMainLoop()