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
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -3)

    head_model = ObjModel.from_file("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 5, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        head_model.draw_opengl()

        pygame.display.flip()
        pygame.time.wait(1)


if __name__ == "__main__":
    main()
