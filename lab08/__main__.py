from lab08.models.obj3d import ObjModel
from lab08.opengl import OpenGLRenderer, EventOnRender


def main():
    head_path = "/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj"
    head_model = ObjModel.from_file(head_path)
    head_model_2 = ObjModel.from_file(head_path)
    head_model_3 = ObjModel.from_file(head_path)

    head_model.translate(0, 0, -3)
    head_model_2.translate(-2, 0, -6)
    head_model_3.translate(2, 0, -6)

    renderer = OpenGLRenderer((600, 600))
    renderer.add_model(head_model)
    renderer.add_model(head_model_2)
    renderer.add_model(head_model_3)

    def on_render(e: EventOnRender):
        print(f"\rFPS: {int(e.source.get_fps())}", end="")
        head_model.rotate(2, 2, 2)

    renderer.subscribe(on_render)
    renderer.start()


if __name__ == "__main__":
    main()
