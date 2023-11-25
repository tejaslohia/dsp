import rawpy
import imageio
from PIL import Image

def read_nikon_raw_image(file_path):
    # Read the raw image
    with rawpy.imread(file_path) as raw:
        # Post-process the raw image
        # rgb = raw.postprocess(four_color_rgb=True,output_color=rawpy.ColorSpace.raw)
        # rgb = raw.postprocess(gamma=(1,1), no_auto_bright=True)
        # rgb = raw.postprocess(no_auto_bright=True,use_auto_wb =False,gamma=None)
        rgb = raw.postprocess(no_auto_bright=True)
    return rgb

# Replace 'your_raw_image.NEF' with the actual path to your Nikon RAW image file
raw_file_path = '/home/ridhima/Desktop/dsp/nikon/DSC_0299.NEF'
# Read the raw image
image_data = read_nikon_raw_image(raw_file_path)
#imageio.imsave("/home/ridhima/Desktop/dsp/nikon/DSC_0299.bmp",image_data)
#imageio.imsave("/home/ridhima/Desktop/dsp/nikon/test.jpg",image_data)
img = Image.fromarray(image_data,"RGB")
img.show()

