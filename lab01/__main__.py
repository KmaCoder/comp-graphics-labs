import os

from lab01.vectorscope import Vectorscope

dirname = os.path.dirname(__file__)

vectorscope = Vectorscope(os.path.join(dirname, 'IO/original.tif'))
vectorscope.output_img(os.path.join(dirname, 'IO/output.tif'))
# vectorscope.show_img()
