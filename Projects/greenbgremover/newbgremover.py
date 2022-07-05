import pixellib
from pixellib.tune_bg import alter_bg
change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_if_kernels.h5")
change_bg.color_bg.color_bg("sample.jpg",colors = (0,128,0),output_image_name="colored_bg.jpg")