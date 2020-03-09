from typing import Tuple

from lab08.models.color import Color
from lab08.models.obj3d import ObjModel
from lab08.models.polygon import Polygon
from lab08.models.torus_obj3d import Torus
from lab08.models.vertex import Vertex
from lab08.opengl import OpenGLRenderer, EventOnRender


def gen_quad(width: float, color: Color = None, position: Tuple[float, float, float] = None) -> ObjModel:
    w2 = width / 2
    plain = ObjModel([
        Polygon((Vertex((w2, 0, w2)), Vertex((w2, 0, -w2)), Vertex((-w2, 0, -w2))), color if color else Color.random()),
        Polygon((Vertex((w2, 0, w2)), Vertex((-w2, 0, -w2)), Vertex((-w2, 0, w2))), color if color else Color.random())
    ])
    if position is not None:
        plain.translate(*position)
    return plain


def main():
    # head_path = "/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj"
    # head_model = ObjModel.from_file(head_path)
    # head_model.translate(0, 0.5, -4)
    #
    # head_model_2 = ObjModel.from_file(head_path)
    # head_model_2.translate(-2, 0, -6)
    #
    # head_model_3 = ObjModel.from_file(head_path)
    # head_model_3.translate(2, 0, -6)

    quad = gen_quad(4, Color(0.2, 0.8, 0.2), (0, -1.5, -4))

    tor_models = [Torus(R=1.0, r=0.4, vertices_count=20),
                  Torus(R=0.3, r=0.25, vertices_count=10),
                  Torus(R=0.6, r=0.1, vertices_count=10)]
    tor_models[0].translate(0, 0, -4)
    tor_models[1].translate(-2, 2, -5)
    tor_models[2].translate(2, 2, -5)

    renderer = OpenGLRenderer((600, 600))
    renderer.add_model(quad)
    renderer.add_models(tor_models)

    def on_render(e: EventOnRender):
        print(f"\rFPS: {int(e.source.get_fps())}", end="")
        tor_models[0].rotate(2, 2, 2)
        tor_models[1].rotate(1, -1, 0)
        tor_models[2].rotate(-1, 0, 1)

    renderer.subscribe(on_render)
    renderer.start()


if __name__ == "__main__":
    main()
