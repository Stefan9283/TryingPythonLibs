import OpenGL
OpenGL.FORWARD_COMPATIBLE_ONLY = True

import OpenGL.GL as GL
import OpenGL.GLU as GLU
import OpenGL.GLUT as GLUT
from OpenGL.arrays import ArrayDatatype
import sys

import numpy as np
from ctypes import c_float, c_void_p, cast, sizeof

window = 0
width, height = 800, 800


fragment_shader = []
vertex_shader = []

def readLines(filepath):
    f = open(filepath, "r")

    Lines = f.readlines()

    file = []
    for line in Lines:
        file.append(line)
    return file

def compile_shader(type_shader, source):
    id = GL.glCreateShader(type_shader)

    GL.glShaderSource(id, source)
    GL.glCompileShader(id)
    return id

def create_shader():
    program = GL.glCreateProgram();

    vs = compile_shader(GL.GL_VERTEX_SHADER, vertex_shader)
    fs = compile_shader(GL.GL_FRAGMENT_SHADER, fragment_shader)
    GL.glAttachShader(program, vs)
    GL.glAttachShader(program, fs)
    GL.glLinkProgram(program)

    return program

    
GLUT.glutInit()
GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA | GLUT.GLUT_DOUBLE | GLUT.GLUT_ALPHA |
                         GLUT.GLUT_DEPTH)
GLUT.glutInitWindowSize(width, height)
GLUT.glutInitWindowPosition(900, 900)


window = GLUT.glutCreateWindow("cow.exe")

print(GL.glGetString(GL.GL_VERSION))

vertex_shader = readLines("vert.glsl")
fragment_shader = readLines("frag.glsl")
shader_id = create_shader()

GL.glUseProgram(shader_id)

VAO = GL.glGenVertexArrays(1)
GL.glBindVertexArray(VAO)

vertices = np.array([1, 1, 0, 0, 0, 0, 0, 1, 0], dtype=np.float32).flatten()
VBO = GL.glGenBuffers(1)
GL.glBindBuffer(GL.GL_ARRAY_BUFFER, VBO)
GL.glBufferData(GL.GL_ARRAY_BUFFER, vertices, GL.GL_STATIC_DRAW)

indices = np.array([0, 1, 2], dtype=np.uint16)
EBO = GL.glGenBuffers(1)
GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, EBO)
GL.glBufferData(GL.GL_ELEMENT_ARRAY_BUFFER, indices, GL.GL_STATIC_DRAW)



GL.glEnableVertexAttribArray(0)
GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 3 * sizeof(c_float) , cast(3 * sizeof(c_float), c_void_p))

GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, 0)
GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
GL.glBindVertexArray(0)

def draw():
    GL.glClearColor(0.2, 0, 0, 1)
    
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glBindVertexArray(VAO)
    
    GL.glDrawElements(GL.GL_TRIANGLES, len(indices), GL.GL_UNSIGNED_INT, 0)

    GL.glLoadIdentity()
    GLUT.glutSwapBuffers()

GLUT.glutDisplayFunc(draw)
GLUT.glutIdleFunc(draw)
GLUT.glutMainLoop()
