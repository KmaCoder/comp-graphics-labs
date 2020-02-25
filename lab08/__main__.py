import pygame
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from lab08.models.obj3d import ObjModel


def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(60, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -4)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 100., 0, 0.))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.15, 0.15, 0.15))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (20., 20.2, 20.2))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1., 1., 1.))

    head_model = ObjModel.from_file("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")
    head_model_2 = ObjModel.from_file("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")
    head_model_3 = ObjModel.from_file("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")

    head_model.translate(2, 0, -2)
    head_model_2.translate(-2, 0, -2)
    head_model_3.translate(0, 0, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        head_model.rotate(5, 5, 5)
        head_model.draw_opengl()

        head_model_2.rotate(-4, 1, 3)
        head_model_2.draw_opengl()

        head_model_3.rotate(1, 1, 1)
        head_model_3.draw_opengl()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
