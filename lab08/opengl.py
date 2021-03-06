from typing import Tuple, List

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from lab08.models.obj3d import ObjModel


class OpenGLRenderer:
    def __init__(self, resolution: Tuple[int, int] = (600, 600), ):
        self._resolution = resolution
        self._objects: List[ObjModel] = []
        self._callbacks = []
        self._clock = pygame.time.Clock()

        self._init_gl()

    def _init_gl(self):
        pygame.init()
        pygame.display.set_mode(self._resolution, DOUBLEBUF | OPENGL)
        pygame.mouse.set_visible(False)
        gluPerspective(60, (self._resolution[0] / self._resolution[1]), 0.1, 50.0)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)

        glEnable(GL_FOG)
        glFogfv(GL_FOG_COLOR, (1.0, 1.0, 1.0))
        glFogi(GL_FOG_MODE, GL_LINEAR)
        glFogf(GL_FOG_START, 10)
        glFogf(GL_FOG_END, 13)

        glClearColor(1.0, 1.0, 1.0, 1)

        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, (0, 100., 0, 0.))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.15, 0.15, 0.15))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (20., 20.2, 20.2))
        glLightfv(GL_LIGHT0, GL_SPECULAR, (1., 1., 1.))

    def add_model(self, obj: ObjModel):
        self._objects.append(obj)

    def add_models(self, objs: List[ObjModel]):
        for obj in objs:
            self.add_model(obj)

    def start(self):
        self._clock.tick()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self._clock.tick()
            self._fire_event()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
            glPushMatrix()

            for obj in self._objects:
                obj.draw_opengl()

            glPopMatrix()

            pygame.display.flip()
            pygame.time.wait(10)

    def subscribe(self, callback):
        self._callbacks.append(callback)

    def get_fps(self):
        return self._clock.get_fps()

    def _fire_event(self, **attrs):
        e = EventOnRender(self, **attrs)
        for fn in self._callbacks:
            fn(e)


class EventOnRender:
    def __init__(self, source: OpenGLRenderer, **attrs):
        self.source: OpenGLRenderer = source
        self.attrs = attrs
