from lab01.vectorscope import Vectorscope
import lab01.config as cfg

vectorscope = Vectorscope(cfg.img_path_in)
vectorscope.output_img(cfg.img_path_out)
